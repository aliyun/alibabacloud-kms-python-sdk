阿里云KMS Python SDK
====================

.. figure:: https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg
   :alt: image0

   image0

阿里云KMS Python SDK可以帮助Python开发者快速使用KMS。

*其他语言版本:*\ `English <README.rst>`__\ *,*\ `简体中文 <README.zh-cn.rst>`__

-  `阿里云KMS主页 <https://help.aliyun.com/document_detail/311016.html>`__
-  `代码示例 </example>`__
-  `Issues <https://github.com/aliyun/alibabacloud-kms-python-sdk/issues>`__
-  `Release <https://github.com/aliyun/alibabacloud-kms-python-sdk/releases>`__

优势
----

帮助Python开发者通过本SDK快速使用阿里云KMS产品的所有API： -
支持通过KMS公共网关访问进行KMS资源管理和密钥运算 -
支持通过KMS实例网关进行密钥运算

软件要求
--------

-  Python 3.6 or later

安装
----

::

   pip install alibabacloud-kms-python-sdk

KMS Client介绍
--------------

+--------------------------+---------------------+---------------------+
| KMS 客户端类             | 简介                | 使用场景            |
+==========================+=====================+=====================+
| alibabacloud_kms_k       | 支持KMS资源管理和KM | 1.                  |
| ms20160120.client.Client | S实例网关的密钥运算 | 仅通过VPC网关进行密 |
|                          |                     | 钥运算操作的场景。  |
|                          |                     | 2.仅通过公共网关对  |
|                          |                     | KMS资源管理的场景。 |
|                          |                     | 3.既要通过VPC网     |
|                          |                     | 关进行密钥运算操作  |
|                          |                     | 又要通过公共网关对  |
|                          |                     | KMS资源管理的场景。 |
+--------------------------+---------------------+---------------------+
| al                       | 支                  | 使用阿里云          |
| ibabacloud_kms_kms201601 | 持用户应用简单修改  | SDK访问KMS          |
| 20.client.TransferClient | 的情况下就可以从KMS | 1.0密钥运算的       |
|                          | 1.0密钥运算迁移到   | 用户，需要迁移到KMS |
|                          | KMS 3.0密钥运算     | 3.0的场景。         |
+--------------------------+---------------------+---------------------+

示例代码
--------

1. 仅通过VPC网关进行密钥运算操作的场景。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

参考以下示例代码调用KMS AdvanceEncrypt API。更多API示例参考 `密钥运算示例代码 <./example/operation>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   import sys
   from typing import List
   from openapi import models as dedicated_kms_openapi_models
   from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
   from sdk import models as dedicated_kms_sdk_models
   from alibabacloud_tea_util.client import Client as UtilClient
   from alibabacloud_darabonba_env.client import Client as EnvClient


   class AdvanceEncrypt:
       def __init__(self):
           pass

       @staticmethod
       def create_kms_instance_config(
           client_key_file: str,
           password: str,
           endpoint: str,
           ca_file_path: str,
       ) -> dedicated_kms_openapi_models.Config:
           config = dedicated_kms_openapi_models.Config(
               client_key_file=client_key_file,
               password=password,
               endpoint=endpoint,
               ca_file_path=ca_file_path
           )
           return config

       @staticmethod
       def create_client(
           kms_instance_config: dedicated_kms_openapi_models.Config,
       ) -> KmsSdkClient:
           return KmsSdkClient(kms_instance_config=kms_instance_config)

       @staticmethod
       def advance_encrypt(
           client: KmsSdkClient,
           key_id: str,
           plaintext: bytes,
       ) -> dedicated_kms_sdk_models.AdvanceEncryptResponse:
           request = dedicated_kms_sdk_models.AdvanceEncryptRequest(
               key_id=key_id,
               plaintext=plaintext
           )
           return client.advance_encrypt(request)

       @staticmethod
       def main(
           args: List[str],
       ) -> None:
           kms_instance_config = AdvanceEncrypt.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
           client = AdvanceEncrypt.create_client(kms_instance_config)
           key_id = 'your keyId'
           plaintext = UtilClient.to_bytes('your plaintext')
           response = AdvanceEncrypt.advance_encrypt(client, key_id, plaintext)
           print(response)

   if __name__ == '__main__':
       AdvanceEncrypt.main(sys.argv[1:])

2. 仅通过公共网关对KMS资源管理的场景。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

参考以下示例代码调用KMS CreateKey API。更多API示例参考 `密钥管理代码示例 <./example/manage>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   import sys

   from typing import List

   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_darabonba_env.client import Client as EnvClient


   class CreateKey:
       def __init__(self):
           pass

       @staticmethod
       def create_open_api_config(
           access_key_id: str,
           access_key_secret: str,
           region_id: str,
       ) -> open_api_models.Config:
           config = open_api_models.Config(
               access_key_id=access_key_id,
               access_key_secret=access_key_secret,
               region_id=region_id
           )
           return config

       @staticmethod
       def create_client(
           open_api_config: open_api_models.Config,
       ) -> KmsSdkClient:
           return KmsSdkClient(open_api_config=open_api_config)

       @staticmethod
       def create_key(
           client: KmsSdkClient,
           enable_automatic_rotation: bool,
           rotation_interval: str,
           key_usage: str,
           origin: str,
           description: str,
           dkmsinstance_id: str,
           protection_level: str,
           key_spec: str,
       ) -> kms_20160120_models.CreateKeyResponse:
           request = kms_20160120_models.CreateKeyRequest(
               enable_automatic_rotation=enable_automatic_rotation,
               rotation_interval=rotation_interval,
               key_usage=key_usage,
               origin=origin,
               description=description,
               dkmsinstance_id=dkmsinstance_id,
               protection_level=protection_level,
               key_spec=key_spec
           )
           return client.create_key(request)

       @staticmethod
       def main(
           args: List[str],
       ) -> None:
           # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
           # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
           open_api_config = CreateKey.create_open_api_config(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
           client = CreateKey.create_client(open_api_config)
           enable_automatic_rotation = False
           rotation_interval = 'your rotationInterval'
           key_usage = 'your keyUsage'
           origin = 'your origin'
           description = 'your description'
           d_kmsinstance_id = 'your dKMSInstanceId'
           protection_level = 'your protectionLevel'
           key_spec = 'your keySpec'
           response = CreateKey.create_key(client, enable_automatic_rotation, rotation_interval, key_usage, origin, description, d_kmsinstance_id, protection_level, key_spec)
           print(response)


   if __name__ == '__main__':
       CreateKey.main(sys.argv[1:])

3. 既要通过VPC网关进行密钥运算操作又要通过公共网关对KMS资源管理的场景。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

参考以下示例代码调用KMS CreateKey API 和 AdvanceEncrypt API。更多API示例参考 `密钥运算示例代码 <./example/operation>`__ 和 `密钥管理示例代码 <./example/manage>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   import sys
   from typing import List
   from openapi import models as dedicated_kms_openapi_models
   from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
   from sdk import models as dedicated_kms_sdk_models
   from alibabacloud_tea_util.client import Client as UtilClient
   from alibabacloud_darabonba_env.client import Client as EnvClient
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_kms20160120 import models as kms_20160120_models

   class Sample:
       def __init__(self):
           pass

       @staticmethod
       def create_kms_instance_config(
           client_key_file: str,
           password: str,
           endpoint: str,
           ca_file_path: str,
       ) -> dedicated_kms_openapi_models.Config:
           config = dedicated_kms_openapi_models.Config(
               client_key_file=client_key_file,
               password=password,
               endpoint=endpoint,
               ca_file_path=ca_file_path
           )
           return config

       @staticmethod
       def create_open_api_config(
           access_key_id: str,
           access_key_secret: str,
           region_id: str,
       ) -> open_api_models.Config:
           config = open_api_models.Config(
               access_key_id=access_key_id,
               access_key_secret=access_key_secret,
               region_id=region_id
           )
           return config

       @staticmethod
       def create_client(kms_instance_config: dedicated_kms_openapi_models.Config,
                         open_api_config: open_api_models.Config
       ) -> KmsSdkClient:
           return KmsSdkClient(kms_instance_config=kms_instance_config, open_api_config=open_api_config)

       @staticmethod
       def create_key(
           client: KmsSdkClient,
           enable_automatic_rotation: bool,
           rotation_interval: str,
           key_usage: str,
           origin: str,
           description: str,
           dkmsinstance_id: str,
           protection_level: str,
           key_spec: str,
       ) -> kms_20160120_models.CreateKeyResponse:
           request = kms_20160120_models.CreateKeyRequest(
               enable_automatic_rotation=enable_automatic_rotation,
               rotation_interval=rotation_interval,
               key_usage=key_usage,
               origin=origin,
               description=description,
               dkmsinstance_id=dkmsinstance_id,
               protection_level=protection_level,
               key_spec=key_spec
           )
           return client.create_key(request)
       @staticmethod
       def advance_encrypt(
           client: KmsSdkClient,
           key_id: str,
           plaintext: bytes,
       ) -> dedicated_kms_sdk_models.AdvanceEncryptResponse:
           request = dedicated_kms_sdk_models.AdvanceEncryptRequest(
               key_id=key_id,
               plaintext=plaintext
           )
           return client.advance_encrypt(request)

       @staticmethod
       def main(
           args: List[str],
       ) -> None:
           kms_instance_config = Sample.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
           open_api_config = Sample.create_open_api_config(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
           client = Sample.create_client(kms_instance_config, open_api_config)
           #CreateKey
           enable_automatic_rotation = False
           rotation_interval = 'your rotationInterval'
           key_usage = 'your keyUsage'
           origin = 'your origin'
           description = 'your description'
           d_kmsinstance_id = 'your dKMSInstanceId'
           protection_level = 'your protectionLevel'
           key_spec = 'your keySpec'
           create_key_resp = Sample.create_key(client, enable_automatic_rotation, rotation_interval, key_usage, origin, description, d_kmsinstance_id, protection_level, key_spec)
           print(create_key_resp)
           #Advance Encrypt
           key_id = 'your keyId'
           plaintext = UtilClient.to_bytes('your plaintext')
           encrypt_resp = Sample.advance_encrypt(client, key_id, plaintext)
           print(encrypt_resp)

   if __name__ == '__main__':
       Sample.main(sys.argv[1:])

使用阿里云 SDK访问KMS 1.0密钥运算的用户，需要迁移到KMS 3.0的场景。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

参考以下示例代码调用KMS API。更多API示例参考 `KMS迁移代码示例 <./example/transfer>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   import os
   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions
   from alibabacloud_kms_kms20160120.transfer_client import TransferClient


   def create_client():
       # 创建kms共享网关config并设置相应参数
       config = open_api_models.Config(
           # 设置地域Id
           region_id='<your-region-id>',
           # 设置访问凭证AccessKeyId
           access_key_id=os.getenv('ACCESS_KEY_ID'),
           # 设置访问凭证AccessKeySecret
           access_key_secret=os.getenv('ACCESS_KEY_SECRET')
       )
       # 创建kms实例网关config并设置相应参数
       kms_config = KmsConfig(
           # 设置请求协议为https
           protocol='https',
           # 设置client key文件地址
           client_key_file='<your-client-key-file-path>',
           # 设置client key密码
           password='<your-password>',
           # 设置kms实例服务地址
           endpoint='<your-kms-instance-endpoint>'
       )
       # 创建TransferClient
       return TransferClient(config=config, kms_config=kms_config)


   def create_key(client):
       request = kms_20160120_models.CreateKeyRequest(
           key_spec='<your-key-spec>',
           key_usage='<your-key-usage>'
       )

       # 如果验证服务器证书，可以在RuntimeOptions设置ca证书路径
       runtime = KmsRuntimeOptions(
           ca='<your-ca-certificate-file-path>'
       )
       # 或者，忽略ssl验证，可以在RuntimeOptions设置ignore_ssl=True
       # runtime = KmsRuntimeOptions(
       #    ignore_ssl=True
       # )

       try:
           response = client.create_key_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   def generate_data_key(client):
       request = kms_20160120_models.GenerateDataKeyRequest(
           key_id='<your-key-id>',
       )

       # 如果验证服务器证书，可以在RuntimeOptions设置ca证书路径
       runtime = KmsRuntimeOptions(
           ca='<your-ca-certificate-file-path>'
       )
       # 或者，忽略ssl验证，可以在RuntimeOptions设置ignore_ssl=True
       # runtime = KmsRuntimeOptions(
       #    ignore_ssl=True
       # )

       try:
           response = client.generate_data_key_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   client = create_client()
   create_key(client)
   generate_data_key(client)

KMS实例性能测试
---------------

如果需要使用KMS实例SDK进行KMS实例性能测试，请参考benchmarks目录下的压力测试工具示例代码，编译成可执行程序以后使用如下命令运行:

.. code:: shell

      $ python benchmark.py --case=encrypt --client_key_path=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

压力测试工具如何编译以及使用请参考\ `文档 <README-benchmark.zh-cn.rst>`__\ 。

许可证
------

`Apache License
2.0 <https://www.apache.org/licenses/LICENSE-2.0.html>`__

版权所有 2009-present, 阿里巴巴集团.
