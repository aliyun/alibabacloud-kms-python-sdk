Alibaba Cloud KMS SDK for Python
================================

|image0|

Alibaba Cloud KMS SDK for Python can help Python developers to use the KMS.

*Read this in other
languages:*\ `English <README.rst>`__\ *,*\ `简体中文 <README.zh-cn.rst>`__

-  `Alibaba Cloud KMS Homepage <https://www.alibabacloud.com/help/zh/doc-detail/311016.htm>`__
-  `Sample Code </example>`__
-  `Issues <https://github.com/aliyun/alibabacloud-kms-python-sdk/issues>`__
-  `Release <https://github.com/aliyun/alibabacloud-kms-python-sdk/releases>`__

License
-------

`Apache License
2.0 <https://www.apache.org/licenses/LICENSE-2.0.html>`__

Requirements
------------

-  Python 3.6 or later

Install
-------

::

   pip install alibabacloud-kms-python-sdk

Client Mechanism
----------------
Alibaba Cloud KMS SDK for Python transfers the the following methods of request to KMS instance vpc gateway by default.

-  Encrypt
-  Decrypt
-  GenerateDataKey
-  GenerateDataKeyWithoutPlaintext
-  GetPublicKey
-  AsymmetricEncrypt
-  AsymmetricDecrypt
-  AsymmetricSign
-  AsymmetricVerify
-  GetSecretValue


You could use Alibaba Cloud KMS SDK for Python with the given parameter to send the request related to the given methods to the KMS shared gateway.

- Refer to the following code to forward calls from all of these interfaces to the KMS shared gateway. Take GetSecretValue as an example.

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_tea_util import models as util_models

   from alibabacloud_kms_kms20160120.client import Client
   from alibabacloud_kms_kms20160120.models import KmsConfig


   def get_secret_value_sample():
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

       # create KMS client, set parameter is_use_kms_share_gateway=True, and forward all interfaces to the KMS shared gateway
       client = Client(config=openapi_config, kms_config=kms_config, is_use_kms_share_gateway=True)

       request = kms_20160120_models.GetSecretValueRequest(
           secret_name='<your-secret-name>',
       )

       # If you ignore ssl verification，you can set ignore_ssl with True related to the RuntimeOptions parameter
       runtime = util_models.RuntimeOptions(
           # ignore_ssl=True
       )

       try:
           response = client.get_secret_value_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   get_secret_value_sample()

- Refer to the following code to transfer the GetSecretValue request to the KMS shared gateway.

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_tea_util import models as util_models

   from alibabacloud_kms_kms20160120.client import Client
   from alibabacloud_kms_kms20160120.models import KmsConfig


   def get_secret_value_sample():
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
           endpoint='<your-kms-instance-endpoint>',
           # set the specified API interface to forward to KMS shared gateway
           default_kms_api_names=['GetSecretValue']
       )

       # create KMS client
       client = Client(config=openapi_config, kms_config=kms_config)

       request = kms_20160120_models.GetSecretValueRequest(
           secret_name='<your-secret-name>',
       )

       # If you ignore ssl verification，you can set ignore_ssl with True related to the RuntimeOptions parameter
       runtime = util_models.RuntimeOptions(
           # ignore_ssl=True
       )

       try:
           response = client.get_secret_value_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   get_secret_value_sample()

- Refer to the following code to transfer a single request to the KMS shared gateway.

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models

   from alibabacloud_kms_kms20160120.client import Client
   from alibabacloud_kms_kms20160120.models import KmsRuntimeOptions, KmsConfig


   def get_secret_value_sample():
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

       # create KMS client
       client = Client(config=openapi_config, kms_config=kms_config)

       request = kms_20160120_models.GetSecretValueRequest(
           secret_name='<your-secret-name>',
       )

       # If you ignore ssl verification，you can set ignore_ssl with True related to the RuntimeOptions parameter
       runtime = KmsRuntimeOptions(
           # ignore_ssl=True,
           # If you set is_use_kms_share_gateway with True,the request must be sent to the shared KMS gateway
           is_use_kms_share_gateway=True
       )

       try:
           response = client.get_secret_value_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   get_secret_value_sample()


Sample Code (take the Encrypt interface as an example)
-------------------------------------------------------
You can select reference examples to call KMS services according to different scenarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scenario 1 The new user can refer to the following code to call the service of the KMS instance vpc gateway.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_kms_kms20160120.client import Client as KmsClient
   from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions


   def encrypt_sample():
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

       # create KMS client
       client = KmsClient(config=openapi_config, kms_config=kms_config)

       request = kms_20160120_models.EncryptRequest(
           # set the CMK ID created on the KMS console
           key_id='<your-key-id>',
           # set the plaintext
           plaintext='<your-plaintext>'
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
           response = client.encrypt_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   encrypt_sample()

Scenario 2 Veteran users can refer to the following sample code of two different scenarios to call KMS services.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Solution 1 Before key migration, replace the old SDK (KMS20160120) with the cost SDK, and then use the KMS shared gateway to access KMS services.
             After the key is migrated, replace the KMS shared gateway with a KMS instance vpc gateway to access KMS services.
- Solution 2 After key migration, replace the old SDK (KMS20160120) with the cost SDK and use the KMS instance vpc gateway to access KMS services.

The sample code before key migration is as follows:
'''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_tea_util import models as util_models


    def encrypt_sample():
        # set config
        openapi_config = open_api_models.Config(
           # set region id
           region_id='<your-region-id>',
           # set access key id
           access_key_id=os.getenv('ACCESS_KEY_ID'),
           # set access key secret
           access_key_secret=os.getenv('ACCESS_KEY_SECRET')
        )

        # create KMS client
        client = KmsClient(config=openapi_config)

        request = kms_20160120_models.EncryptRequest(
            # set the CMK ID created on the KMS console
            key_id='<your-key-id>',
            # set the plaintext
            plaintext='<your-plaintext>'
        )

        # If you ignore ssl verification，you can set ignore_ssl with True related to the RuntimeOptions parameter
        runtime = util_models.RuntimeOptions(
            # ignore_ssl=True
        )

        try:
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))

The sample code after key migration is as follows:
''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions

    def encrypt_sample():
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
        # create KMS client
        client = KmsClient(config=config, kms_config=kms_config)

        request = kms_20160120_models.EncryptRequest(
            # set the CMK ID created on the KMS console
            key_id='<your-key-id>',
            # set the plaintext
            plaintext='<your-plaintext>'
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
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))


Character encoding setting instructions (default UTF-8)
--------------------------------------------------------

- You can refer to the following code example to set the global character set encoding.

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions

    def encrypt_sample():
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
           endpoint='<your-kms-instance-endpoint>',
           # set charset encoding to UTF-8
           encoding='utf-8'
        )

        # create KMS client
        client = KmsClient(config=config, kms_config=kms_config)

        request = kms_20160120_models.EncryptRequest(
            # set the CMK ID created on the KMS console
            key_id='<your-key-id>',
            # set the plaintext
            plaintext='<your-plaintext>'
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
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))

- You can refer to the following code example to set the character set encoding for a single request.

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions

    def encrypt_sample():
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

        # create KMS client
        client = KmsClient(config=config, kms_config=kms_config)

        request = kms_20160120_models.EncryptRequest(
            # set the CMK ID created on the KMS console
            key_id='<your-key-id>',
            # set the plaintext
            plaintext='<your-plaintext>'
        )

        # If verify server CA certificate,you can set CA certificate file path with RuntimeOptions
        runtime = KmsRuntimeOptions(
            ca='<your-ca-certificate-file-path>',
            # set charset encoding to UTF-8
            encoding='utf-8'
        )
        # If you ignore ssl verification，you can set ignore_ssl with True related to the RuntimeOptions parameter
        # runtime = KmsRuntimeOptions(
        #    ignore_ssl=True,
        #    # set charset encoding to UTF-8
        #    encoding='utf-8'
        # )

        try:
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))


.. _license-1:

License
-------

`Apache-2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__

Copyright (c) 2009-present, Alibaba Cloud All rights reserved.

.. |image0| image:: https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg
