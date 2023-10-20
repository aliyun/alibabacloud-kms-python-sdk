Pressure Measurement Tools
==========================

The pressure measurement tools could be used to test KMS instance
performance.

Compile
-------

Login to a Linux ECS instance, the ECS can access the KMS instance.

-  1.Install requirement packages

.. code:: shell

   $ pip install alibabacloud-kms-python-sdk

-  2.Download tools code

.. code:: shell

   $ git clone https://github.com/aliyun/alibabacloud-kms-python-sdk.git

Usage
-----

-  1.Go to the project directory named benchmarks.

.. code:: shell

   $ cd alibabacloud-kms-python2-sdk/benchmarks

-  2.Execute the following command to test, command line parameters
   refer to the following `configurable
   parameters <#configurable%20parameters>`__.

Runtime environment: KMS instance computing performance option is 2000,
and the configuration of the pressure measurement clients may be 8
cores*2.

Example: Use the key specification Aliyun_AES_256 to perform encryption
operation (encrypt) pressure test, the data size is 32 bytes, the number
of threads is 32, and the pressure test duration is 600 seconds. The
command is as follows:

.. code:: shell

   $ python benchmark.py --case=encrypt --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600 --log_path=./log

Configurable parameters
-----------------------

+---+-------------------------------------------------------------------+
| N | Description                                                       |
| a |                                                                   |
| m |                                                                   |
| e |                                                                   |
+===+===================================================================+
| c | Test case name, currently supported test case names are as        |
| a | follows: encrypt: encryption operation, call the Encrypt decrypt: |
| s | decryption operation, call the Decrypt sign: signature operation, |
| e | call the Sign verify: verification operation, call the Verify     |
|   | get_secret_value: to obtain the secret value operation, call the  |
|   | GetSecretValue                                                    |
+---+-------------------------------------------------------------------+
| e | KMS instance endpoint                                             |
| n |                                                                   |
| d |                                                                   |
| p |                                                                   |
| o |                                                                   |
| i |                                                                   |
| n |                                                                   |
| t |                                                                   |
+---+-------------------------------------------------------------------+
| c | the file path of Client Key                                       |
| l |                                                                   |
| i |                                                                   |
| e |                                                                   |
| n |                                                                   |
| t |                                                                   |
| _ |                                                                   |
| k |                                                                   |
| e |                                                                   |
| y |                                                                   |
| _ |                                                                   |
| p |                                                                   |
| a |                                                                   |
| t |                                                                   |
| h |                                                                   |
+---+-------------------------------------------------------------------+
| c | the password of Client Key                                        |
| l |                                                                   |
| i |                                                                   |
| e |                                                                   |
| n |                                                                   |
| t |                                                                   |
| _ |                                                                   |
| k |                                                                   |
| e |                                                                   |
| y |                                                                   |
| _ |                                                                   |
| p |                                                                   |
| a |                                                                   |
| s |                                                                   |
| s |                                                                   |
| w |                                                                   |
| o |                                                                   |
| r |                                                                   |
| d |                                                                   |
+---+-------------------------------------------------------------------+
| c | concurrence goroutines number, default 32                         |
| o |                                                                   |
| n |                                                                   |
| c |                                                                   |
| u |                                                                   |
| r |                                                                   |
| r |                                                                   |
| e |                                                                   |
| n |                                                                   |
| c |                                                                   |
| e |                                                                   |
| _ |                                                                   |
| n |                                                                   |
| u |                                                                   |
| m |                                                                   |
| s |                                                                   |
+---+-------------------------------------------------------------------+
| d | testing duration,default 600s                                     |
| u |                                                                   |
| r |                                                                   |
| a |                                                                   |
| t |                                                                   |
| i |                                                                   |
| o |                                                                   |
| n |                                                                   |
+---+-------------------------------------------------------------------+
| p | The result output period, default 1 per second                    |
| e |                                                                   |
| r |                                                                   |
| i |                                                                   |
| o |                                                                   |
| d |                                                                   |
+---+-------------------------------------------------------------------+
| l | Log output path, if this parameter is not configured, output to   |
| o | the console                                                       |
| g |                                                                   |
| _ |                                                                   |
| p |                                                                   |
| a |                                                                   |
| t |                                                                   |
| h |                                                                   |
+---+-------------------------------------------------------------------+
| k | The kms cmk id, which needs to be set for the encrypt and decrypt |
| e | test, and ignored for the get secret value test                   |
| y |                                                                   |
| _ |                                                                   |
| i |                                                                   |
| d |                                                                   |
+---+-------------------------------------------------------------------+
| d | Test data size, unit byte, default 32                             |
| a |                                                                   |
| t |                                                                   |
| a |                                                                   |
| _ |                                                                   |
| s |                                                                   |
| i |                                                                   |
| z |                                                                   |
| e |                                                                   |
+---+-------------------------------------------------------------------+
| s | Secret name, which needs to be set for get secret value test, and |
| e | ignored for the encrypt and decrypt test                          |
| c |                                                                   |
| r |                                                                   |
| e |                                                                   |
| t |                                                                   |
| _ |                                                                   |
| n |                                                                   |
| a |                                                                   |
| m |                                                                   |
| e |                                                                   |
+---+-------------------------------------------------------------------+
| c | the path of CA certificate , Ignore verifying the server          |
| a | certificate by default                                            |
| _ |                                                                   |
| p |                                                                   |
| a |                                                                   |
| t |                                                                   |
| h |                                                                   |
+---+-------------------------------------------------------------------+

Test case instructions:

-  encrypt: test Encrypt api performance.

Example: The data size is 32 bytes, the number of threads is 32, the
pressure test time is 600 seconds, and the output is output to the
console.

.. code:: shell

   $ python benchmark.py --case=encrypt --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  decrypt: test Decrypt api performance.

Example: The data size is 32 bytes, the number of threads is 32, the
pressure test time is 600 seconds, and the output is output to the
console.

.. code:: shell

   $ python benchmark.py --case=decrypt --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  sign：test Sign api performance.

Example: The data size is 32 bytes, the number of threads is 32, the
pressure test time is 600 seconds, and the output is output to the
console.

.. code:: shell

   $ python benchmark.py --case=sgin --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  verify：test Verify api performance.

Example: The data size is 32 bytes, the number of threads is 32, the
pressure test time is 600 seconds, and the output is output to the
console.

.. code:: shell

   $ python benchmark.py --case=verify --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

-  get_secret_value：test GetSecretValue api performance.

Example: The data size is 32 bytes, the number of threads is 32, the
pressure test time is 600 seconds, and the output is output to the
console.

.. code:: shell

   $ python benchmark.py --case=get_secret_value --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --secret_name=**** --data_size=32 --concurrence_nums=32 --duration=600

Reference configuration parameters for different performances of KMS instances
------------------------------------------------------------------------------

+--------------+-------------+------------+--------+---+-------+----+
| Computing    | Client      | Client     | Key    | c | c     | d  |
| Performance  | Machine     | Machine    | S      | a | oncur | at |
| Options      | Co          | Load(%CPU) | pecifi | s | rence | a_ |
|              | nfiguration |            | cation | e | _nums | si |
|              |             |            |        |   |       | ze |
+==============+=============+============+========+===+=======+====+
| 2000         | 8 cores \*  | 85         | Al     | e | 32    | 32 |
|              | 2           |            | iyun_A | n |       |    |
|              |             |            | ES_256 | c |       |    |
|              |             |            |        | r |       |    |
|              |             |            |        | y |       |    |
|              |             |            |        | p |       |    |
|              |             |            |        | t |       |    |
+--------------+-------------+------------+--------+---+-------+----+
| 3000         | 8 cores \*  | 85         | Al     | e | 32(Si | 32 |
|              | 2           |            | iyun_A | n | ngle) |    |
|              |             |            | ES_256 | c |       |    |
|              |             |            |        | r |       |    |
|              |             |            |        | y |       |    |
|              |             |            |        | p |       |    |
|              |             |            |        | t |       |    |
+--------------+-------------+------------+--------+---+-------+----+
| 4000         | 16 cores \* | 85         | Al     | e | 64    | 32 |
|              | 2           |            | iyun_A | n |       |    |
|              |             |            | ES_256 | c |       |    |
|              |             |            |        | r |       |    |
|              |             |            |        | y |       |    |
|              |             |            |        | p |       |    |
|              |             |            |        | t |       |    |
+--------------+-------------+------------+--------+---+-------+----+
| 6000         | 16 cores \* | 85         | Al     | e | 64(Si | 32 |
|              | 2           |            | iyun_A | n | ngle) |    |
|              |             |            | ES_256 | c |       |    |
|              |             |            |        | r |       |    |
|              |             |            |        | y |       |    |
|              |             |            |        | p |       |    |
|              |             |            |        | t |       |    |
+--------------+-------------+------------+--------+---+-------+----+
| 8000         | 16 cores \* | 85         | Al     | e | 64(Si | 32 |
|              | 4           |            | iyun_A | n | ngle) |    |
|              |             |            | ES_256 | c |       |    |
|              |             |            |        | r |       |    |
|              |             |            |        | y |       |    |
|              |             |            |        | p |       |    |
|              |             |            |        | t |       |    |
+--------------+-------------+------------+--------+---+-------+----+

Description of configuration options:

-  Client machine load: The CPU usage of the client machine is
   recommended to be 85%.

-  Concurrency nums: The recommended 32 for 8-core machines. If the
   performance of the pressure test cannot meet expectations under this
   concurrency, you can appropriately increase the client machine
   configuration, and then increase the concurrency.

-  Data size: The recommended data size is 32. The larger the data, the
   lower the pressure measurement performance.

-  If the business side calls the SDK for stress testing and the number
   of connections continues to increase, you can set MaxIdleConns to be
   the same as the number of concurrent connections.

Result output
-------------

.. code:: text

   2023-10-20 15:18:32,321 - report_log - INFO - ----------------- Time_49: [2023-10-20 15:18:32]--------------
   2023-10-20 15:18:32,321 - report_log - INFO - [Benchmark-Detail]        RequestCount: 76205     ResponseCount: 76192    TPS: 1528       AvgTPS: 1532
   MaxOnceTimeCost: 130 ms MinOnceTimeCost: 0 ms   AvgOnceTimeCost: 13 ms
   ClientErrorCount: 0     LimitExceededErrorCount: 0      TimeoutErrorCount: 0
   2023-10-20 15:18:32,599 - report_log - INFO - ----------------- Statistics: [2023-10-20 15:18:32]--------------
   2023-10-20 15:18:32,599 - report_log - INFO - [Benchmark-Detail]        RequestCount: 76586     ResponseCount: 76586    AvgTPS: 1531
   MaxOnceTimeCost: 130 ms MinOnceTimeCost: 0 ms   AvgOnceTimeCost: 13 ms
   ClientErrorCount: 0     LimitExceededErrorCount: 0      TimeoutErrorCount: 0

Explanation of output parameters:

RequestCount: total number of requests

ResponseCount: total number of responses

TPS：transactions per second

AvgTPS：average transactions per second

MaxOnceTimeCost：maximum time spent on a single request

MinOnceTimeCost：minimum time spent on a single request

AvgOnceTimeCost：average time spent on a single request

ClientErrorCount：client error count

LimitExceededErrorCount：limit exceeded error count

TimeoutErrorCount：timeout error count
