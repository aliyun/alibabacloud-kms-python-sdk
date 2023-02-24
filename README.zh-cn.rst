阿里云KMS Python SDK
====================

|image0|

阿里云KMS Python SDK可以帮助Python开发者快速使用KMS。

*其他语言版本:*\ `English <README.rst>`__\ *,*\ `简体中文 <README.zh-cn.rst>`__

-  `阿里云KMS主页 <https://help.aliyun.com/document_detail/311016.html>`__
-  `代码示例 </examples>`__
-  `Issues <https://github.com/aliyun/alibabacloud-kms-python-sdk/issues>`__
-  `Release <https://github.com/aliyun/alibabacloud-kms-python-sdk/releases>`__

许可证
------

`Apache License
2.0 <https://www.apache.org/licenses/LICENSE-2.0.html>`__

软件要求
--------

-  Python 3.6 or later

安装
------

::

   pip install alibabacloud-kms-python-sdk

客户端机制
----------

阿里云KMS Python SDK默认情况下会将以下方法的请求转发到KMS实例网关.

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

您可以使用阿里云KMS Python SDK将以上的转发到KMS实例网关的方法转发到KMS共享网关。

- 参考如下代码将上述所有接口的调用转发到KMS共享网关。以GetSecretValue为例。

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_tea_util import models as util_models

   from alibabacloud_kms_kms20160120.client import Client
   from alibabacloud_kms_kms20160120.models import KmsConfig


   def get_secret_value_sample():
       # 创建kms共享网关config并设置相应参数
       openapi_config = open_api_models.Config(
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

       # 创建KmsClient, 并设置参数is_use_kms_share_gateway=True, 将所有接口转发到KMS共享网关
       client = Client(config=openapi_config, kms_config=kms_config, is_use_kms_share_gateway=True)

       request = kms_20160120_models.GetSecretValueRequest(
           secret_name='<your-secret-name>',
       )

       # 如果您要忽略SSL认证，您可以设定ignore_ssl为True
       runtime = util_models.RuntimeOptions(
           # ignore_ssl=True
       )

       try:
           response = client.get_secret_value_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   get_secret_value_sample()

- 参考如下代码将指定方法调用转发到KMS共享网关。以GetSecretValue为例。

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_tea_util import models as util_models
   from openapi import models as dkms_models

   from alibabacloud_kms_kms20160120.client import Client
   from alibabacloud_kms_kms20160120.models import KmsConfig


   def get_secret_value_sample():
       # 创建kms共享网关config并设置相应参数
       openapi_config = open_api_models.Config(
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
           endpoint='<your-kms-instance-endpoint>',
           # 设置指定的API接口转发到KMS共享网关
           default_kms_api_names=['GetSecretValue']
       )
       # 创建KmsClient
       client = Client(config=openapi_config, kms_config=kms_config)

       request = kms_20160120_models.GetSecretValueRequest(
           secret_name='<your-secret-name>',
       )

       # 如果您要忽略SSL认证，您可以设定ignore_ssl为True
       runtime = util_models.RuntimeOptions(
           # ignore_ssl=True
       )

       try:
           response = client.get_secret_value_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   get_secret_value_sample()

- 参考如下的代码将单独一次调用转发到KMS共享网关。以GetSecretValue为例。

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_tea_openapi import models as open_api_models
   from openapi import models as dkms_models

   from alibabacloud_kms_kms20160120.client import Client
   from alibabacloud_kms_kms20160120.models import KmsRuntimeOptions


   def get_secret_value_sample():
       # 创建kms共享网关config并设置相应参数
       openapi_config = open_api_models.Config(
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
       # 创建KmsClient
       client = Client(config=openapi_config, kms_config=kms_config)

       request = kms_20160120_models.GetSecretValueRequest(
           secret_name='<your-secret-name>',
       )

       # 如果您要忽略SSL认证，您可以设定ignore_ssl为True
       runtime = KmsRuntimeOptions(
           # ignore_ssl=True,
           # 如果您设定is_use_kms_share_gateway为True，那么这次调用将被转发到共享kms网关
           is_use_kms_share_gateway=True
       )

       try:
           response = client.get_secret_value_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   get_secret_value_sample()


示例代码(以Encrypt接口为例)
---------------------------
用户可根据不同的场景选择参考示例调用KMS服务
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
场景一 新接入用户可以参考下面的代码调用KMS实例网关的服务。
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   from alibabacloud_kms20160120 import models as kms_20160120_models
   from alibabacloud_kms_kms20160120.client import Client as KmsClient
   from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions


   def encrypt_sample():
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
       # 创建KmsClient
       client = KmsClient(kms_config=kms_config)

       request = kms_20160120_models.EncryptRequest(
           # 设置您在KMS控制台创建的主密钥ID
           key_id='<your-key-id>',
           # 设置待加密明文数据
           plaintext='<your-plaintext>'
       )

       # 如果验证服务器证书，可以在KmsRuntimeOptions设置ca证书路径
       runtime = KmsRuntimeOptions(
           ca='<your-ca-certificate-file-path>'
       )
       # 或者，忽略ssl验证，可以在KmsRuntimeOptions设置ignore_ssl=True
       # runtime = KmsRuntimeOptions(
       #    ignore_ssl=True
       # )

       try:
           response = client.encrypt_with_options(request, runtime)
           print(str(response.body))
       except Exception as e:
           print(str(e))


   encrypt_sample()

场景二 老用户可参考以下两种不同方案的示例代码调用KMS服务。
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- 方案一 在密钥迁移前，先将旧的sdk(kms20160120)替换成本sdk，然后依然使用KMS共享网关访问KMS服务，示例代码参考密钥迁移前。
        在密钥迁移后，再将KMS共享网关替换成KMS实例网关访问KMS服务，示例代码参考密钥迁移后。
- 方案二 在密钥迁移后，直接将旧的sdk(kms20160120)替换成本sdk，使用KMS实例网关访问KMS服务，示例代码参考密钥迁移后。

密钥迁移前示例代码如下：
''''''''''''''''''''''''

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_tea_util import models as util_models


    def encrypt_sample():
        # 创建kms共享网关config并设置相应参数
        config = open_api_models.Config(
            # 设置地域Id
           region_id='<your-region-id>',
           # 设置访问凭证AccessKeyId
           access_key_id=os.getenv('ACCESS_KEY_ID'),
           # 设置访问凭证AccessKeySecret
           access_key_secret=os.getenv('ACCESS_KEY_SECRET')
        )
        # 创建KmsClient
        client = KmsClient(config=config)

        request = kms_20160120_models.EncryptRequest(
            # 设置您在KMS控制台创建的主密钥ID
            key_id='<your-key-id>',
            # 设置待加密明文数据
            plaintext='<your-plaintext>'
        )

        # 如果需要忽略ssl验证，可以在RuntimeOptions设置ignore_ssl=True
        runtime = util_models.RuntimeOptions(
            # ignore_ssl=True
        )

        try:
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))

密钥迁移后示例代码如下:
''''''''''''''''''''''''

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions

    def encrypt_sample():
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
        # 创建KmsClient
        client = KmsClient(config=config, kms_config=kms_config)

        request = kms_20160120_models.EncryptRequest(
            # 设置您在KMS控制台创建的主密钥ID
            key_id='<your-key-id>',
            # 设置待加密明文数据
            plaintext='<your-plaintext>'
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
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))


字符编码设置说明(默认为UTF-8)
-----------------------------
- 您可以参考以下代码示例，设置全局的字符集编码。

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions

    def encrypt_sample():
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
           endpoint='<your-kms-instance-endpoint>',
           # 设置字符集编码为UTF-8
           encoding='utf-8'
        )
        # 创建KmsClient
        client = KmsClient(config=config, kms_config=kms_config)

        request = kms_20160120_models.EncryptRequest(
            # 设置您在KMS控制台创建的主密钥ID
            key_id='<your-key-id>',
            # 设置待加密明文数据
            plaintext='<your-plaintext>'
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
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))

- 您可以参考以下代码示例，设置单独一次请求的字符集编码。

.. code:: python

    from alibabacloud_kms20160120 import models as kms_20160120_models
    from alibabacloud_kms_kms20160120.client import Client as KmsClient
    from alibabacloud_tea_openapi import models as open_api_models
    from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions

    def encrypt_sample():
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
        # 创建KmsClient
        client = KmsClient(config=config, kms_config=kms_config)

        request = kms_20160120_models.EncryptRequest(
            # 设置您在KMS控制台创建的主密钥ID
            key_id='<your-key-id>',
            # 设置待加密明文数据
            plaintext='<your-plaintext>'
        )

        # 如果验证服务器证书，可以在RuntimeOptions设置ca证书路径
        runtime = KmsRuntimeOptions(
            ca='<your-ca-certificate-file-path>',
            # 设置字符集编码为UTF-8
            encoding='utf-8'
        )
        # 或者，忽略ssl验证，可以在RuntimeOptions设置ignore_ssl=True
        # runtime = KmsRuntimeOptions(
        #    ignore_ssl=True,
        #    # 设置字符集编码为UTF-8
        #    encoding='utf-8'
        # )

        try:
            response = client.encrypt_with_options(request, runtime)
            print(str(response.body))
        except Exception as e:
            print(str(e))


.. _许可证-1:

许可证
------

`Apache-2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__

版权所有 2009-present, 阿里巴巴集团.

.. |image0| image:: https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg
