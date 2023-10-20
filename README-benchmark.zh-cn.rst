压力测试工具
============

压力测试工具可用来测试KMS实例性能。

工具编译
--------

登录Linux ECS实例中， ECS需要处在可以访问KMS实例的VPC中

-  1.安装依赖包

.. code:: shell

   $ pip install alibabacloud-kms-python-sdk

-  2.下载工具代码

.. code:: shell

   $ git clone https://github.com/aliyun/alibabacloud-kms-python-sdk.git

使用方法
--------

-  1.首先切换到工具代码文件所在目录benchmarks下。

.. code:: shell

   $ cd alibabacloud-kms-python2-sdk/benchmarks

-  2.执行下面示例命令进行测试，，命令行参数参考下面\ `可配置参数 <#可配置参数>`__\ 项。

运行环境：KMS实例计算性能选项2000，客户端机器配置8核*2台。

示例：使用密钥规格Aliyun_AES_256，进行加密操作(encrypt)压测，数据大小32字节，线程数32，压测时间600秒，命令如下:

.. code:: shell

   python benchmark.py --case=encrypt --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600 --log_path=./log

可配置参数
----------

+------+---------------------------------------------------------------+
| 参数 | 参数说明                                                      |
| 名称 |                                                               |
+======+===============================================================+
| case | 测试case名称，当前支持的测试case名称如下： encrypt：          |
|      | 加密操作，调用Encrypt接口 decrypt： 解密操作，调用Decrypt接口 |
|      | sign： 签名操作，调用Sign接口 verify：                        |
|      | 验签操作，调用Verify接口 get_secret_value：                   |
|      | 获取凭据值操作，调用GetSecretValue接口                        |
+------+---------------------------------------------------------------+
| endp | KMS实例地址                                                   |
| oint |                                                               |
+------+---------------------------------------------------------------+
| cli  | Client Key文件路径                                            |
| ent_ |                                                               |
| key_ |                                                               |
| path |                                                               |
+------+---------------------------------------------------------------+
| cli  | Client Key口令                                                |
| ent_ |                                                               |
| key_ |                                                               |
| pass |                                                               |
| word |                                                               |
+------+---------------------------------------------------------------+
| conc | 并发线程数，默认32                                            |
| urre |                                                               |
| nce_ |                                                               |
| nums |                                                               |
+------+---------------------------------------------------------------+
| dura | 测试时间, 默认600秒                                           |
| tion |                                                               |
+------+---------------------------------------------------------------+
| pe   | 结果输出周期，默认1秒输出一次结果                             |
| riod |                                                               |
+------+---------------------------------------------------------------+
| log_ | 日志输出路径，不配置输出到控制台                              |
| path |                                                               |
+------+---------------------------------------------------------------+
| ke   | 测试密钥的Id，加解密测试需要设置此项，获取凭据测试忽略此项    |
| y_id |                                                               |
+------+---------------------------------------------------------------+
| d    | 测试数据大小，单位字节，默认32，测试数据越大性能越低          |
| ata_ |                                                               |
| size |                                                               |
+------+---------------------------------------------------------------+
| sec  | 测试的凭据名称，获取凭据测试需要设置此项，加解密测试忽略此项  |
| ret_ |                                                               |
| name |                                                               |
+------+---------------------------------------------------------------+
| ca_  | CA证书路径，默认为空表示忽略验证服务端证书                    |
| path |                                                               |
+------+---------------------------------------------------------------+

测试case使用说明： - encrypt：测试加密接口性能。

示例：数据大小32字节，线程数32，压测时间600秒，输出到控制台。

.. code:: shell

   $ python benchmark.py --case=encrypt --client_key_path=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  decrypt：测试解密接口性能。

示例：数据大小32字节，线程数32，压测时间600秒，输出到控制台。

.. code:: shell

   $ python benchmark.py --case=decrypt --client_key_path=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  sign：测试签名接口性能。

示例：数据大小32字节，线程数32，压测时间600秒，输出到控制台。

.. code:: shell

   $ python benchmark.py --case=sgin --client_key_path=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  verify：测试验签接口性能。

示例：数据大小32字节，线程数32，压测时间600秒，输出到控制台。

.. code:: shell

   $ python benchmark.py --case=verify --client_key_path=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  get_secret_value：测试获取凭据接口性能。

示例：数据大小32字节，线程数32，压测时间600秒，输出到控制台。

.. code:: shell

   $ python benchmark.py --case=get_secret_value --client_key_path=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --secret_name=**** --data_size=32 --concurrence_nums=32 --duration=600

KMS实例不同性能的参考配置参数
-----------------------------

+-----+------+-----------+------------+------+--------------+--------+
| 计  | 客   | 客户      | 密钥规格   | case | conc         | dat    |
| 算  | 户端 | 端机器负  |            |      | urrence_nums | a_size |
| 性  | 机器 | 载(%CPU)  |            |      |              |        |
| 能  | 配置 |           |            |      |              |        |
| 选  |      |           |            |      |              |        |
| 项  |      |           |            |      |              |        |
+=====+======+===========+============+======+==============+========+
| 2   | 8核  | 85        | Aliy       | enc  | 32           | 32     |
| 000 | *2台 |           | un_AES_256 | rypt |              |        |
+-----+------+-----------+------------+------+--------------+--------+
| 3   | 8核  | 85        | Aliy       | enc  | 32(单台)     | 32     |
| 000 | *4台 |           | un_AES_256 | rypt |              |        |
+-----+------+-----------+------------+------+--------------+--------+
| 4   | 16核 | 85        | Aliy       | enc  | 64           | 32     |
| 000 | *2台 |           | un_AES_256 | rypt |              |        |
+-----+------+-----------+------------+------+--------------+--------+
| 6   | 16核 | 85        | Aliy       | enc  | 64(单台)     | 32     |
| 000 | *4台 |           | un_AES_256 | rypt |              |        |
+-----+------+-----------+------------+------+--------------+--------+
| 8   | 16核 | 85        | Aliy       | enc  | 64(单台)     | 32     |
| 000 | *8台 |           | un_AES_256 | rypt |              |        |
+-----+------+-----------+------------+------+--------------+--------+

配置选择说明：

-  客户端机器负载：客户端机器CPU使用率推荐85%。如果在此负载下压测性能不能符合预期，可以适当增加客户端机器配置。

-  并发数量：客户端为8核机器推荐并发数32。如果在此并发数下压测性能不能符合预期，可以适当增加客户端机器配置，然后提高并发数。

-  数据大小: 数据大小推荐为32。数据越大的压测性能降低。

-  如果业务侧自己通过调用SDK进行压测，出现连接数持续增加，可以将MaxIdleConns设置为与并发数相同。

结果输出
--------

.. code:: text

   2023-10-20 15:18:32,321 - report_log - INFO - ----------------- Time_49: [2023-10-20 15:18:32]--------------
   2023-10-20 15:18:32,321 - report_log - INFO - [Benchmark-Detail]        RequestCount: 76205     ResponseCount: 76192    TPS: 1528       AvgTPS: 1532
   MaxOnceTimeCost: 130 ms MinOnceTimeCost: 0 ms   AvgOnceTimeCost: 13 ms
   ClientErrorCount: 0     LimitExceededErrorCount: 0      TimeoutErrorCount: 0
   2023-10-20 15:18:32,599 - report_log - INFO - ----------------- Statistics: [2023-10-20 15:18:32]--------------
   2023-10-20 15:18:32,599 - report_log - INFO - [Benchmark-Detail]        RequestCount: 76586     ResponseCount: 76586    AvgTPS: 1531
   MaxOnceTimeCost: 130 ms MinOnceTimeCost: 0 ms   AvgOnceTimeCost: 13 ms
   ClientErrorCount: 0     LimitExceededErrorCount: 0      TimeoutErrorCount: 0

输出参数解释：

RequestCount：总请求数

ResponseCount：总响应数

TPS：每秒处理的事务数

AvgTPS：每秒处理的事务数均值

MaxOnceTimeCost：单次请求最大耗时

MinOnceTimeCost：单次请求最小耗时

AvgOnceTimeCost：单次请求平均耗时

ClientErrorCount：客户端错误次数

LimitExceededErrorCount：限流错误次数

TimeoutErrorCount：超时错误次数
