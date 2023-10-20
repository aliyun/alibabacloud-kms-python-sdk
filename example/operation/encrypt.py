# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_env.client import Client as EnvClient


class Encrypt:
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
    async def create_kms_instance_config_async(
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
    async def create_client_async(
        kms_instance_config: dedicated_kms_openapi_models.Config,
    ) -> KmsSdkClient:
        return KmsSdkClient(kms_instance_config=kms_instance_config)

    @staticmethod
    def encrypt(
        client: KmsSdkClient,
        padding_mode: str,
        aad: bytes,
        key_id: str,
        plaintext: bytes,
        iv: bytes,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.EncryptResponse:
        request = dedicated_kms_sdk_models.EncryptRequest(
            padding_mode=padding_mode,
            aad=aad,
            key_id=key_id,
            plaintext=plaintext,
            iv=iv,
            algorithm=algorithm
        )
        return client.encrypt(request)

    @staticmethod
    async def encrypt_async(
        client: KmsSdkClient,
        padding_mode: str,
        aad: bytes,
        key_id: str,
        plaintext: bytes,
        iv: bytes,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.EncryptResponse:
        request = dedicated_kms_sdk_models.EncryptRequest(
            padding_mode=padding_mode,
            aad=aad,
            key_id=key_id,
            plaintext=plaintext,
            iv=iv,
            algorithm=algorithm
        )
        return await client.encrypt_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = Encrypt.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = Encrypt.create_client(kms_instance_config)
        padding_mode = 'your paddingMode'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        plaintext = UtilClient.to_bytes('your plaintext')
        iv = UtilClient.to_bytes('your iv')
        algorithm = 'your algorithm'
        response = Encrypt.encrypt(client, padding_mode, aad, key_id, plaintext, iv, algorithm)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await Encrypt.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await Encrypt.create_client_async(kms_instance_config)
        padding_mode = 'your paddingMode'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        plaintext = UtilClient.to_bytes('your plaintext')
        iv = UtilClient.to_bytes('your iv')
        algorithm = 'your algorithm'
        response = await Encrypt.encrypt_async(client, padding_mode, aad, key_id, plaintext, iv, algorithm)
        print(response)


if __name__ == '__main__':
    Encrypt.main(sys.argv[1:])
