Alibaba Cloud KMS SDK for Python
================================

.. figure:: https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg
   :alt: image0

   image0

Alibaba Cloud KMS SDK for Python can help Python developers to use the
KMS.

*Read this in other
languages:*\ `English <README.rst>`__\ *,*\ `简体中文 <README.zh-cn.rst>`__

-  `Alibaba Cloud KMS
   Homepage <https://www.alibabacloud.com/help/zh/doc-detail/311016.htm>`__
-  `Sample Code </example>`__
-  `Issues <https://github.com/aliyun/alibabacloud-kms-python-sdk/issues>`__
-  `Release <https://github.com/aliyun/alibabacloud-kms-python-sdk/releases>`__

Advantage
---------

Alibaba Cloud KMS SDK helps Python developers quickly use all APIs of
Alibaba Cloud KMS products: - KMS resource management and key operations
can be performed through KMS public gateway access - You can perform key
operations through KMS instance gateway

Requirements
------------

-  Python 3.6 or later

Install
-------

::

   pip install alibabacloud-kms-python-sdk

Introduction to KMS Client

+--------------------------+---------------------+---------------------+
| KMS client classes       | Introduction        | Usage scenarios     |
+==========================+=====================+=====================+
| alibabacloud_kms_k       | KMS resource        | 1. Scenarios where  |
| ms20160120.client.Client | management and key  | key operations are  |
|                          | operations for KMS  | performed only      |
|                          | instance gateways   | through VPC         |
|                          | are supported       | gateways. 2. KMS    |
|                          |                     | resource management |
|                          |                     | scenarios that only |
|                          |                     | use public          |
|                          |                     | gateways. 3.        |
|                          |                     | Scenarios where you |
|                          |                     | want to perform key |
|                          |                     | operations through  |
|                          |                     | VPC gateways and    |
|                          |                     | manage KMS          |
|                          |                     | resources through   |
|                          |                     | public gateways.    |
+--------------------------+---------------------+---------------------+
| al                       | Users can migrate   | Users who use       |
| ibabacloud_kms_kms201601 | from KMS 1.0 key    | Alibaba Cloud SDK   |
| 20.client.TransferClient | operations to KMS   | to access KMS 1.0   |
|                          | 3.0 key operations  | key operations need |
|                          |                     | to migrate to KMS   |
|                          |                     | 3.0                 |
+--------------------------+---------------------+---------------------+

Sample code
-----------

1. Scenarios where key operations are performed only through VPC gateways.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the following sample code to call the KMS AdvanceEncrypt API. For more API examples, see\ `operation samples <./example/operation>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

2. KMS resources are managed only through public gateways.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the following sample code to call the KMS CreateKey API. For more API examples, see\ `manage samples <./example/manage>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
           #Make sure that the environment in which the code runs has environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET set.
           #Project code leakage may cause AccessKey to be leaked and threaten the security of all resources under the account. The following code example uses an environment variable to obtain the AccessKey for reference only, it is recommended to use the more secure STS mode, for more authentication access methods, see https://help.aliyun.com/document_detail/378657.html
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

3. You must not only perform key operations through a VPC gateway, but also manage KMS resources through a public gateway.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the following sample code to call the KMS CreateKey API and the AdvanceEncrypt API. For more API examples, see `operation samples <./example/operation>`__ 和 `manage samples <./example/manage>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
           #Make sure that the environment in which the code runs has environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET set.
           #Project code leakage may cause AccessKey to be leaked and threaten the security of all resources under the account. The following code example uses an environment variable to obtain the AccessKey for reference only, it is recommended to use the more secure STS mode, for more authentication access methods, see https://help.aliyun.com/document_detail/378657.html
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

Users who uses Alibaba Cloud SDK to access KMS 1.0 keys need to migrate to access KMS 3.0 keys.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the following sample code to call the KMS API. For more API examples, see `kms transfer samples <./example/transfer>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   import os
   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions
   from alibabacloud_kms_kms20160120.transfer_client import TransferClient


   def create_client():
          # set config
          openapi_config = open_api_models.Config(
              # set region id
              region_id='<your-region-id>',
              # set access key id
              access_key_id=os.getenv('ACCESS_KEY_ID'),
              # set access key secret
              access_key_secret=os.getenv('ACCESS_KEY_SECRET')
          )
          # set kms config
          kms_config = KmsConfig(
              # set the request protocol to https
              protocol='https',
              # set client key file path
              client_key_file='<your-client-key-file-path>',
              # set client key password
              password='<your-password>',
              # set kms instance endpoint
              endpoint='<your-kms-instance-endpoint>'
          )
       # create transfer client
       return TransferClient(config=config, kms_config=kms_config)


   def create_key(client):
       request = kms_20160120_models.CreateKeyRequest(
           key_spec='<your-key-spec>',
           key_usage='<your-key-usage>'
       )

       # If verify server CA certificate,you can set CA certificate file path with RuntimeOptions
       runtime = KmsRuntimeOptions(
           ca='<your-ca-certificate-file-path>'
       )
       # If you ignore ssl verification，you can set ignore_ssl with True related to the RuntimeOptions parameter
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

       # If verify server CA certificate,you can set CA certificate file path with RuntimeOptions
       runtime = KmsRuntimeOptions(
           ca='<your-ca-certificate-file-path>'
       )
       # If you ignore ssl verification，you can set ignore_ssl with True related to the RuntimeOptions parameter
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

KMS instance performance testing
--------------------------------

If you need to use the KMS instance SDK for KMS instance performance
testing, please refer to the sample code of the pressure measurement
tools in the directory named benchmarks , compile it into an executable
program and run it with the following command:

.. code:: shell

   $ python benchmark.py --case=encrypt --client_key_file=./ClientKey_****.json --client_key_password=**** --endpoint=kst-****.cryptoservice.kms.aliyuncs.com --key_id=key-**** --data_size=32 --concurrence_nums=32 --duration=600

How to compile and use the stress test tool, please refer to `the
document <README-benchmark.rst>`__.

License
-------

`Apache License
2.0 <https://www.apache.org/licenses/LICENSE-2.0.html>`__

Copyright (c) 2009-present, Alibaba Cloud All rights reserved.
