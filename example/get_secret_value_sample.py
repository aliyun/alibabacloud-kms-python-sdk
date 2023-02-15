# -*- coding: utf-8 -*-
import os

from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_tea_openapi import models as open_api_models

from alibabacloud_kms_kms20160120.client import Client
from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions


# 新接入用户可以参考此方法调用KMS实例网关的服务。
def new_user_get_secret_value_sample():
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
    client = Client(kms_config=kms_config)
    get_secret_value(client)


# 密钥迁移前示例代码
def before_migrate_get_secret_value_sample():
    # 创建kms共享网关config并设置相应参数
    config = open_api_models.Config(
        # 设置地域Id
        region_id='<your-region-id>',
        # 设置访问凭证AccessKeyId
        access_key_id=os.getenv('ACCESS_KEY_ID'),
        # 设置访问凭证AccessKeySecret
        access_key_secret=os.getenv('ACCESS_KEY_SECRET')
    )
    client = Client(config=config)
    get_secret_value(client)


# 密钥迁移后示例代码
def after_migrate_get_secret_value_sample():
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
    client = Client(config=config, kms_config=kms_config)
    get_secret_value(client)


def get_secret_value(client):
    request = kms_20160120_models.GetSecretValueRequest(
        secret_name='<your-secret-name>',
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
        response = client.get_secret_value_with_options(request, runtime)
        print(str(response.body))
    except Exception as e:
        print(str(e))


new_user_get_secret_value_sample()
before_migrate_get_secret_value_sample()
after_migrate_get_secret_value_sample()
