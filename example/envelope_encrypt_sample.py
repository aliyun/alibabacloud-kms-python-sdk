# -*- coding: utf-8 -*-
import base64
import os
import random
import string

from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_tea_openapi import models as open_api_models
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from alibabacloud_kms_kms20160120.client import Client
from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions


# 新接入用户可以参考此方法调用KMS实例网关的服务。
def new_user_envelope_encrypt_sample():
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
    envelope_encrypt(client)


# 密钥迁移前示例代码
def before_migrate_envelope_encrypt_sample():
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
    envelope_encrypt(client)


# 密钥迁移后示例代码
def after_migrate_envelope_encrypt_sample():
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
    envelope_encrypt(client)


def envelope_encrypt(client):
    try:
        plaintext = b'<your-plaintext-data>'
        associated_data = b'<your-associated-data>'

        # 获取数据密钥，下面以<your-key-id>密钥为例进行说明，数据密钥长度32字节
        request = kms_20160120_models.GenerateDataKeyRequest(
            key_id='<your-key-id>',
            number_of_bytes=32
        )

        # 如果验证服务器证书，可以在RuntimeOptions设置ca证书路径
        runtime = KmsRuntimeOptions(
            ca='<your-ca-certificate-file-path>'
        )
        # 或者，忽略ssl验证，可以在RuntimeOptions设置ignore_ssl=True
        # runtime = KmsRuntimeOptions(
        #    ignore_ssl=True
        # )

        # 调用生成数据密钥接口
        response = client.generate_data_key_with_options(request, runtime)
        # KMS返回的数据密钥明文, 加密本地数据使用
        data_key = base64.b64decode(response.body.plaintext)
        data_key_blob = response.body.ciphertext_blob

        # 计算本地加密初始向量，解密时需要传入
        gcm_iv_length = 12
        iv = bytes(''.join(random.sample(string.ascii_letters + string.digits, gcm_iv_length)), encoding='utf-8')

        encryptor = Cipher(algorithms.AES(data_key), modes.GCM(iv)).encryptor()
        encryptor.authenticate_additional_data(associated_data)
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        # 输出密文，密文输出或持久化由用户根据需要进行处理，下面示例仅展示将密文输出到一个对象的情况
        # 假如envelope_cipher_text是需要输出的密文对象，至少需要包括以下三个内容:
        # (1) encrypted_data_key: KMS返回的数据密钥密文
        # (2) iv: 加密初始向量
        # (3) cipher_text: 密文数据
        envelope_cipher_text = EnvelopeCipherPersistObject()
        envelope_cipher_text.encrypted_data_key = data_key_blob
        envelope_cipher_text.iv = base64.b64encode(iv)
        envelope_cipher_text.cipher_text = base64.b64encode(ciphertext)
        envelope_cipher_text.tag = base64.b64encode(encryptor.tag)
        print(str(envelope_cipher_text))

    except Exception as e:
        print(str(e))


class EnvelopeCipherPersistObject(object):
    def __init__(self):
        self.encrypted_data_key = None
        self.iv = None
        self.cipher_text = None
        self.tag = None


new_user_envelope_encrypt_sample()
before_migrate_envelope_encrypt_sample()
after_migrate_envelope_encrypt_sample()
