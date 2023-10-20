# -*- coding: utf-8 -*-
import argparse
import datetime
import hashlib
import logging
import multiprocessing
import os.path
import signal
import sys
import threading
import time
from logging import handlers
import warnings

from multiprocessing.managers import BaseManager
from openapi.models import Config as DKmsConfig
from openapi_util.models import RuntimeOptions
from sdk.client import Client
from sdk.models import EncryptRequest, DecryptRequest, SignRequest, VerifyRequest, GetSecretValueRequest

warnings.filterwarnings("ignore")
processes_wait_event = multiprocessing.Event()


def get_now_milliseconds():
    return int(time.time() * 1000)


class MyManager(BaseManager):
    pass


class Config:
    def __init__(
            self,
            case_name=None,
            endpoint=None,
            key_id=None,
            client_key_path=None,
            client_key_password=None,
            data_size=None,
            concurrence_nums=None,
            duration=None,
            period=None,
            log_path=None,
            enable_debug_log=None,
            ca_file_path=None,
            secret_name=None
    ):
        self.case_name = case_name
        self.endpoint = endpoint
        self.key_id = key_id
        self.client_key_path = client_key_path
        self.client_key_password = client_key_password
        self.data_size = data_size
        self.concurrence_nums = concurrence_nums
        self.duration = duration
        self.period = period
        self.log_path = log_path
        self.enable_debug_log = enable_debug_log
        self.ca_file_path = ca_file_path
        self.secret_name = secret_name

        self.algorithm = None
        self.plaintext = None
        self.aad = None
        self.digest = None
        self.ca = None

    def apply_flag(self):
        self.check_params()
        if self.plaintext is None or len(self.plaintext) != self.data_size:
            self.plaintext = (''.join(['1' for _ in range(self.data_size)])).encode('utf8')
        self.digest = hashlib.sha256(self.plaintext).digest()
        if self.ca_file_path is not None and self.ca_file_path != '':
            with open(self.ca_file_path, 'r') as f:
                self.ca = f.read()
        self.aad = 'this is encryption context'.encode()

    def check_params(self):
        if self.key_id is None or self.key_id == '':
            if self.case_name != 'get_secret_value':
                raise Exception('--key_id can not be empty')
        if self.secret_name is None or self.secret_name == '':
            if self.case_name == 'get_secret_value':
                raise Exception('--secret_name can not be empty')


class CountRecorder:
    def __init__(self, count):
        self.count = count
        self.lock = multiprocessing.Lock()

    def get(self):
        with self.lock:
            return self.count

    def set(self, count):
        with self.lock:
            self.count = count

    def add(self):
        with self.lock:
            self.count += 1

    def get_and_reset(self):
        with self.lock:
            count = self.count
            self.count = 0
            return count


class CountCollect:
    def __init__(self, concurrence_nums):
        self.concurrence_nums = concurrence_nums
        self.request_count_list = [0] * concurrence_nums
        self.response_count_list = [0] * concurrence_nums
        self.response_limit_count = [0] * concurrence_nums
        self.timeout_error_count = [0] * concurrence_nums
        self.client_error_count = [0] * concurrence_nums
        self.time_cost_sum_per_thread_list = [0] * concurrence_nums
        self.count_per_thread_list = [0] * concurrence_nums
        self.run_bench_time_cost = 0
        self.min_once_time_cost_list = [0] * concurrence_nums
        self.max_once_time_cost_list = [0] * concurrence_nums
        self.period_tps_list = [CountRecorder(0)] * concurrence_nums
        self.analysis_last_time = 0

    def add_request_count_list(self, index, v):
        self.request_count_list[index] += v

    def get_run_bench_time_cost(self):
        return self.run_bench_time_cost

    def set_run_bench_time_cost(self, v):
        self.run_bench_time_cost = v

    def get_analysis_last_time(self):
        return self.analysis_last_time

    def set_analysis_last_time(self, v):
        self.analysis_last_time = v

    def analysis(self, duration, is_period):
        if self.run_bench_time_cost < 1000 or duration < 1000:
            return
        all_thread_count = 0
        all_thread_time_cost = 0
        all_request_count = 0
        all_response_count = 0
        all_period_tps = 0
        all_client_error_count = 0
        all_limit_error_count = 0
        all_timeout_error_count = 0
        for i in range(self.concurrence_nums):
            all_thread_count += self.count_per_thread_list[i]
            all_thread_time_cost += self.time_cost_sum_per_thread_list[i]
            all_request_count += self.request_count_list[i]
            all_response_count += self.response_count_list[i]
            all_period_tps += self.period_tps_list[i].get_and_reset()
            all_client_error_count += self.client_error_count[i]
            all_limit_error_count += self.response_limit_count[i]
            all_timeout_error_count += self.timeout_error_count[i]
        max_once_cost = 0
        min_once_cost = sys.maxsize
        for cost in self.min_once_time_cost_list:
            if cost < min_once_cost:
                min_once_cost = cost
        for cost in self.max_once_time_cost_list:
            if max_once_cost < cost:
                max_once_cost = cost
        if all_thread_count == 0:
            return
        period_tps = ''
        if is_period:
            period_tps = 'TPS: {}\t'.format(int(all_period_tps / (duration / 1000)))
        record = "[Benchmark-Detail]\tRequestCount: {}\tResponseCount: {}\t{}AvgTPS: {}\n" \
                 "MaxOnceTimeCost: {} ms\tMinOnceTimeCost: {} ms\tAvgOnceTimeCost: {} ms\n" \
                 "ClientErrorCount: {}\tLimitExceededErrorCount: {}\t" \
                 "TimeoutErrorCount: {}".format(all_request_count,
                                                all_response_count,
                                                period_tps,
                                                int(all_response_count / (self.run_bench_time_cost / 1000)),
                                                max_once_cost,
                                                min_once_cost,
                                                int(all_thread_time_cost / all_thread_count),
                                                all_client_error_count,
                                                all_limit_error_count,
                                                all_timeout_error_count
                                                )
        return record

    def update_count_and_cost(self, index, once_time_cost, e):
        if e is None:
            # 单线程响应总次数
            self.response_count_list[index] += 1
            # 单线程请求总耗时
            self.time_cost_sum_per_thread_list[index] += once_time_cost
            # 单线程请求总数
            self.count_per_thread_list[index] += 1
            # 单次请求最大耗时
            if self.max_once_time_cost_list[index] < once_time_cost:
                self.max_once_time_cost_list[index] = once_time_cost
            # 单次请求最小耗时
            if self.min_once_time_cost_list[index] > once_time_cost:
                self.min_once_time_cost_list[index] = once_time_cost
            # 每个输出周期Tps
            self.period_tps_list[index].add()
        else:
            err_msg = str(e)
            if 'timed out' in err_msg or 'timeout' in err_msg:
                self.timeout_error_count[index] += 1
            elif 'Limit Exceeded' in err_msg:
                self.response_limit_count[index] += 1
            else:
                self.client_error_count[index] += 1


class EncryptWorker:
    def __init__(self, client, key_id, plaintext, aad, ca):
        self.client = client
        self.key_id = key_id
        self.plaintext = plaintext
        self.aad = aad
        self.ca = ca

    def do_action(self):
        return self.encrypt().request_id

    def encrypt(self):
        request = EncryptRequest()
        request.plaintext = self.plaintext
        request.key_id = self.key_id
        request.aad = self.aad
        runtime = RuntimeOptions()
        runtime.max_attempts = 0
        if self.ca is not None and self.ca != '':
            runtime.verify = self.ca
        else:
            runtime.ignore_ssl = True
        return self.client.encrypt_with_options(request, runtime)


class DecryptWorker:
    def __init__(self, client, key_id, cipher, iv, aad, ca):
        self.client = client
        self.key_id = key_id
        self.cipher = cipher
        self.iv = iv
        self.aad = aad
        self.ca = ca

    def do_action(self):
        return self.decrypt().request_id

    def decrypt(self):
        request = DecryptRequest()
        request.key_id = self.key_id
        request.ciphertext_blob = self.cipher
        request.iv = self.iv
        request.aad = self.aad
        runtime = RuntimeOptions()
        runtime.max_attempts = 0
        if self.ca is not None and self.ca != '':
            runtime.verify = self.ca
        else:
            runtime.ignore_ssl = True
        return self.client.decrypt_with_options(request, runtime)


class SignWorker:
    def __init__(self, client, key_id, message, message_type, ca):
        self.client = client
        self.key_id = key_id
        self.message = message
        self.message_type = message_type
        self.ca = ca

    def do_action(self):
        return self.sign().request_id

    def sign(self):
        request = SignRequest()
        request.key_id = self.key_id
        request.message = self.message
        request.message_type = self.message_type
        runtime = RuntimeOptions()
        runtime.max_attempts = 0
        if self.ca is not None and self.ca != '':
            runtime.verify = self.ca
        else:
            runtime.ignore_ssl = True
        return self.client.sign_with_options()


class VerifyWorker:
    def __init__(self, client, key_id, message, message_type, signature, ca):
        self.client = client
        self.key_id = key_id
        self.message = message
        self.message_type = message_type
        self.signature = signature
        self.ca = ca

    def do_action(self):
        return self.verify().request_id

    def verify(self):
        request = VerifyRequest()
        request.key_id = self.key_id
        request.message = self.message
        request.message_type = self.message_type
        request.signature = self.signature
        runtime = RuntimeOptions()
        runtime.max_attempts = 0
        if self.ca is not None and self.ca != '':
            runtime.verify = self.ca
        else:
            runtime.ignore_ssl = True
        return self.client.verify_with_options(request, runtime)


class GetSecretValueWorker:
    def __init__(self, client, secret_name, ca):
        self.client = client
        self.secret_name = secret_name
        self.ca = ca

    def do_action(self):
        return self.get_secret_value().request_id

    def get_secret_value(self):
        request = GetSecretValueRequest()
        request.secret_name = self.secret_name
        runtime = RuntimeOptions()
        runtime.max_attempts = 0
        if self.ca is not None and self.ca != '':
            runtime.verify = self.ca
        else:
            runtime.ignore_ssl = True
        return self.client.get_secret_value_with_options(request, runtime)


class CountDownLatch:
    def __init__(self, count):
        self.count = count
        self.lock = threading.Condition()

    def count_down(self):
        with self.lock:
            self.count -= 1
            if self.count <= 0:
                self.lock.notifyAll()

    def wait(self):
        with self.lock:
            while self.count > 0:
                self.lock.wait()


def sigterm_handler(signum, frame):
    ProcessesWaitEvent.notify()


class ProcessesWaitEvent:
    def __init__(self):
        self.processes = []
        signal.signal(signal.SIGTERM, sigterm_handler)

    def add_process(self, p):
        self.processes.append(p)

    @staticmethod
    def is_set():
        return processes_wait_event.is_set()

    @staticmethod
    def notify():
        processes_wait_event.set()

    def wait(self):
        for p in self.processes:
            p.join()


class MyMultiProcess(multiprocessing.Process):
    def __init__(self, worker, thread_num, wait_process_start, duration_millis, index, count_collect,
                 debug_logger):
        super(MyMultiProcess, self).__init__()
        self.worker = worker
        self.thread_num = thread_num
        self.wait_process_start = wait_process_start
        self.duration_millis = duration_millis
        self.index = index
        self.count_collect = count_collect
        self.debug_logger = debug_logger

    def run(self):
        self.wait_process_start.wait()
        if self.thread_num == 0:
            self.execute_worker_task(None, None, self.index)
        else:
            wait_threads_start = CountDownLatch(self.thread_num)
            wait_threads_end = CountDownLatch(self.thread_num)
            threads = []
            for i in range(self.thread_num):
                t = threading.Thread(
                    target=self.execute_worker_task,
                    args=(wait_threads_start, wait_threads_end, self.index + i))
                threads.append(t)
                t.start()
                wait_threads_start.count_down()
            # 等待压测完成
            try:
                wait_threads_end.wait()
            except KeyboardInterrupt:
                pass
            # 等待所有线程退出
            for t in threads:
                t.join()

    def execute_worker_task(self, wait_threads_start, wait_threads_end, index):
        if wait_threads_start is not None:
            wait_threads_start.wait()
        count = 0
        start = get_now_milliseconds()
        while not ProcessesWaitEvent.is_set():
            try:
                self.count_collect.add_request_count_list(index, 1)
            except Exception:
                break
            err = None
            request_id = ''
            once_time_cost = 0
            try:
                once_time_start = get_now_milliseconds()
                request_id = self.worker.do_action()
                once_time_cost = get_now_milliseconds() - once_time_start
            except KeyboardInterrupt:
                break
            except Exception as e:
                err = e
                if self.debug_logger is not None:
                    self.debug_logger.info('[BenchError_{0}] Exception:{1}'.format(count, e))
            finally:
                try:
                    self.count_collect.update_count_and_cost(index, once_time_cost, err)
                except Exception:
                    break
                if self.debug_logger is not None:
                    msg = '[BenchDebug_{0}] Success onceTimeCost:{1}ms RequestId:{2}'.format(count, once_time_cost,
                                                                                             request_id)
                    if err is not None:
                        msg = '[BenchError_{0}] Error:{1}'.format(count, err)
                    self.debug_logger.info(msg)
            if self.duration_millis != -1 and get_now_milliseconds() - start > self.duration_millis:
                break
        if wait_threads_end is not None:
            wait_threads_end.count_down()


class Benchmark:
    def __init__(
            self,
            config,
            report_logger=None,
            debug_logger=None,
            count_collect=None
    ):
        self.config = config
        self.report_logger = report_logger
        self.debug_logger = debug_logger
        self.count_collect = count_collect
        self.worker = None
        self.init_worker()

    def init_worker(self):
        dkms_config = DKmsConfig()
        dkms_config.protocol = "https"
        dkms_config.client_key_file = self.config.client_key_path
        dkms_config.password = self.config.client_key_password
        dkms_config.endpoint = self.config.endpoint
        dkms_config.max_idle_conns = self.config.concurrence_nums
        client = Client(dkms_config)

        if self.config.case_name == 'encrypt':
            self.worker = EncryptWorker(client, self.config.key_id, self.config.plaintext,
                                        self.config.aad, self.config.ca)
        elif self.config.case_name == 'decrypt':
            encrypt_worker = EncryptWorker(client, self.config.key_id, self.config.plaintext,
                                           self.config.aad, self.config.ca)
            enc_resp = encrypt_worker.encrypt()
            self.worker = DecryptWorker(client, self.config.key_id, enc_resp.ciphertext_blob, enc_resp.iv,
                                        self.config.aad, self.config.ca)
        elif self.config.case_name == 'sign':
            self.worker = SignWorker(client, self.config.key_id, self.config.digest, 'DIGEST', self.config.ca)
        elif self.config.case_name == 'verify':
            sign_worker = SignWorker(client, self.config.key_id, self.config.digest, 'DIGEST', self.config.ca)
            sign_resp = sign_worker.sign()
            self.worker = VerifyWorker(client, self.config.key_id, self.config.digest, 'DIGEST', sign_resp.signature,
                                       self.config.ca)
        elif self.config.case_name == 'get_secret_value':
            self.worker = GetSecretValueWorker(client, self.config.secret_name, self.config.ca)
        else:
            raise Exception('invalid benchmark case name:{}'.format(self.config.case_name))

    def run(self):
        threads = []
        wait_process_start = multiprocessing.Event()
        wait_processes = ProcessesWaitEvent()
        finished_chan = threading.Event()
        cpu_count = multiprocessing.cpu_count()
        # 启动压测
        if self.config.concurrence_nums <= cpu_count:
            for i in range(self.config.concurrence_nums):
                proc = MyMultiProcess(self.worker,
                                      0,
                                      wait_process_start,
                                      self.config.duration * 1000,
                                      i,
                                      self.count_collect,
                                      self.debug_logger
                                      )
                proc.daemon = True
                wait_processes.add_process(proc)
                proc.start()
        else:
            every_thread_num = int(self.config.concurrence_nums / cpu_count)
            over_thread_num = int(self.config.concurrence_nums % cpu_count)
            for i in range(cpu_count):
                thread_num = every_thread_num
                if over_thread_num != 0 and i < over_thread_num:
                    thread_num = thread_num + 1
                proc = MyMultiProcess(self.worker,
                                      thread_num,
                                      wait_process_start,
                                      self.config.duration * 1000,
                                      i,
                                      self.count_collect,
                                      self.debug_logger
                                      )
                proc.daemon = True
                wait_processes.add_process(proc)
                proc.start()

        wait_process_start.set()

        begin_time = get_now_milliseconds()
        self.count_collect.set_analysis_last_time(begin_time)
        # 创建定时输出统计日志线程
        t = threading.Thread(target=Benchmark.print_period_analysis,
                             args=(self, self.config.period, begin_time, finished_chan,))
        t.setDaemon(True)
        threads.append(t)
        t.start()
        # 等待压测完成
        try:
            wait_processes.wait()
        except KeyboardInterrupt:
            pass
        # 关闭定时输出线程
        if not finished_chan.is_set():
            finished_chan.set()
        # 最终输出
        self.print_statistics(begin_time)
        # 等待所有线程退出
        for t in threads:
            t.join()

    def print_analysis(self, title, begin_time, is_period):
        try:
            now_millis = get_now_milliseconds()
            self.count_collect.set_run_bench_time_cost(now_millis - begin_time)
            if is_period:
                duration = now_millis - self.count_collect.get_analysis_last_time()
            else:
                duration = self.count_collect.get_run_bench_time_cost()
            self.count_collect.set_analysis_last_time(now_millis)
            record = self.count_collect.analysis(duration, is_period)
            if record is not None and record != '':
                self.report_logger.info(title)
                self.report_logger.info(record)
        except Exception:
            pass

    def print_period_analysis(self, period, begin_time, finished_chan):
        count = 0
        while not finished_chan.is_set():
            time.sleep(period)
            count += 1
            self.print_analysis('----------------- Time_{0}: [{1}]--------------'.format(
                count, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), begin_time, True)

    def print_statistics(self, begin_time):
        self.print_analysis('----------------- Statistics: [{0}]--------------'.format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), begin_time, False)


def exit_print(section, err):
    print('Section[{0}] Error:{1}'.format(section, err))
    sys.exit(1)


def get_logs(config):
    debug_log = None
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if config.log_path is not None and config.log_path != '':
        report_log = logging.getLogger('report_log')
        report_log.setLevel(level=logging.INFO)
        report_log_file = os.path.join(config.log_path, 'statistics.log')
        report_log_handler = handlers.RotatingFileHandler(
            filename=report_log_file,
            maxBytes=2000000000,
            encoding='utf-8'
        )
        report_log_handler.setLevel(logging.INFO)
        report_log_handler.setFormatter(formatter)
        report_log.addHandler(report_log_handler)

        if config.enable_debug_log:
            debug_log = logging.getLogger('debug_log')
            debug_log.setLevel(level=logging.INFO)
            debug_log_file = os.path.join(config.log_path, 'debug.log')
            debug_log_handler = handlers.RotatingFileHandler(
                filename=debug_log_file,
                maxBytes=2000000000,
                encoding='utf-8'
            )
            debug_log_handler.setLevel(logging.INFO)
            debug_log_handler.setFormatter(formatter)
            debug_log.addHandler(debug_log_handler)
    else:
        report_log = logging.getLogger('report_log')
        report_log.setLevel(level=logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)
        report_log.addHandler(handler)

        if config.enable_debug_log:
            debug_log = logging.getLogger('debug_log')
            debug_log.setLevel(level=logging.INFO)
            debug_log.addHandler(handler)

    return report_log, debug_log


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case')
    parser.add_argument('--endpoint')
    parser.add_argument('--client_key_path')
    parser.add_argument('--client_key_password')
    parser.add_argument('--concurrence_nums', nargs='?', default=32)
    parser.add_argument('--duration', nargs='?', default=600)
    parser.add_argument('--period', nargs='?', default=1)
    parser.add_argument('--log_path', nargs='?', default='')
    parser.add_argument('--key_id', nargs='?', default='')
    parser.add_argument('--data_size', nargs='?', default=32)
    parser.add_argument('--secret_name', nargs='?', default='')
    parser.add_argument('--ca_path', nargs='?', default='')
    parser.add_argument('--enable_debug_log', nargs='?', default=False)
    args = parser.parse_args()
    enable_debug_log = args.enable_debug_log
    if not isinstance(enable_debug_log, bool):
        enable_debug_log = True if enable_debug_log.lower() == 'true' else False
    config = Config(
        args.case,
        args.endpoint,
        args.key_id,
        args.client_key_path,
        args.client_key_password,
        int(args.data_size),
        int(args.concurrence_nums),
        int(args.duration),
        int(args.period),
        args.log_path,
        enable_debug_log,
        args.ca_path,
        args.secret_name
    )
    try:
        config.apply_flag()
    except Exception as e:
        exit_print('apply_flag', e)

    report_log, debug_log = get_logs(config)

    print('Start [{}] Case'.format(args.case))

    try:
        MyManager.register('CountCollect', CountCollect)
        manager = MyManager()
        manager.start()
        count_collect = manager.CountCollect(config.concurrence_nums)
        bench = Benchmark(config=config, report_logger=report_log, debug_logger=debug_log, count_collect=count_collect)
        bench.run()
    except Exception as e:
        exit_print('Benchmark', e)

    print('[{}] Case complete!'.format(args.case))


if __name__ == '__main__':
    main()
