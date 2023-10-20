# -*- coding: utf-8 -*-
import base64
import os

from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_tea_openapi import models as open_api_models
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from alibabacloud_kms_kms20160120.transfer_client import TransferClient
from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions


# 新接入用户可以参考此方法调用KMS实例网关的服务。
def new_user_envelope_decrypt_sample():
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
    client = TransferClient(kms_config=kms_config)
    envelope_decrypt(client)


# 密钥迁移前示例代码
def before_migrate_envelope_decrypt_sample():
    # 创建kms共享网关config并设置相应参数
    config = open_api_models.Config(
        # 设置地域Id
        region_id='<your-region-id>',
        # 设置访问凭证AccessKeyId
        access_key_id=os.getenv('ACCESS_KEY_ID'),
        # 设置访问凭证AccessKeySecret
        access_key_secret=os.getenv('ACCESS_KEY_SECRET')
    )
    client = TransferClient(config=config)
    envelope_decrypt(client)


# 密钥迁移后示例代码
def after_migrate_envelope_decrypt_sample():
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
    client = TransferClient(config=config, kms_config=kms_config)
    envelope_decrypt(client)


def envelope_decrypt(client):
    try:
        # 读取封信加密持久化对象
        envelope_cipher_text = get_envelope_cipher_persist_object()
        # 数据密钥密文
        encrypted_data_key = envelope_cipher_text.encrypted_data_key
        # 密文数据
        cipher_text = base64.b64decode(envelope_cipher_text.cipher_text)
        # 加密初始向量
        iv = base64.b64decode(envelope_cipher_text.iv)
        tag = base64.b64decode(envelope_cipher_text.tag)
        associated_data = b'<your-associated-data>'

        # 从封信加密持久化对象获取数据密钥密文，调用KMS在线解密
        request = kms_20160120_models.DecryptRequest(
            ciphertext_blob=encrypted_data_key
        )

        # 如果验证服务器证书，可以在RuntimeOptions设置ca证书路径
        runtime = KmsRuntimeOptions(
            ca='<your-ca-certificate-file-path>'
        )
        # 或者，忽略ssl验证，可以在RuntimeOptions设置ignore_ssl=True
        # runtime = KmsRuntimeOptions(
        #    ignore_ssl=True
        # )

        # 调用解密接口
        response = client.decrypt_with_options(request, runtime)

        # 数据密钥明文
        plain_data_key = base64.b64decode(response.body.plaintext)

        # 使用数据密钥明文在本地进行解密, 下面是以AES-256 GCM模式为例
        decryptor = Cipher(algorithms.AES(plain_data_key), modes.GCM(iv, tag)).decryptor()
        decryptor.authenticate_additional_data(associated_data)
        decrypted_text = decryptor.update(cipher_text) + decryptor.finalize()
        print(str(decrypted_text))
    except Exception as e:
        print(str(e))


class EnvelopeCipherPersistObject(object):
    def __init__(self):
        self.encrypted_data_key = None
        self.iv = None
        self.cipher_text = None
        self.tag = None


def get_envelope_cipher_persist_object() -> EnvelopeCipherPersistObject:
    # TODO 用户需要在此处代码进行替换，从存储中读取封信加密持久化对象
    return EnvelopeCipherPersistObject()


new_user_envelope_decrypt_sample()
before_migrate_envelope_decrypt_sample()
after_migrate_envelope_decrypt_sample()
