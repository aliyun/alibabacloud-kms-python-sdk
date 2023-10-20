# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_env.client import Client as EnvClient


class Decrypt:
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
    def decrypt(
        client: KmsSdkClient,
        padding_mode: str,
        aad: bytes,
        ciphertext_blob: bytes,
        key_id: str,
        iv: bytes,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.DecryptResponse:
        request = dedicated_kms_sdk_models.DecryptRequest(
            padding_mode=padding_mode,
            aad=aad,
            ciphertext_blob=ciphertext_blob,
            key_id=key_id,
            iv=iv,
            algorithm=algorithm
        )
        return client.decrypt(request)

    @staticmethod
    async def decrypt_async(
        client: KmsSdkClient,
        padding_mode: str,
        aad: bytes,
        ciphertext_blob: bytes,
        key_id: str,
        iv: bytes,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.DecryptResponse:
        request = dedicated_kms_sdk_models.DecryptRequest(
            padding_mode=padding_mode,
            aad=aad,
            ciphertext_blob=ciphertext_blob,
            key_id=key_id,
            iv=iv,
            algorithm=algorithm
        )
        return await client.decrypt_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = Decrypt.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = Decrypt.create_client(kms_instance_config)
        padding_mode = 'your paddingMode'
        aad = UtilClient.to_bytes('your aad')
        ciphertext_blob = UtilClient.to_bytes('your ciphertextBlob')
        key_id = 'your keyId'
        iv = UtilClient.to_bytes('your iv')
        algorithm = 'your algorithm'
        response = Decrypt.decrypt(client, padding_mode, aad, ciphertext_blob, key_id, iv, algorithm)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await Decrypt.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await Decrypt.create_client_async(kms_instance_config)
        padding_mode = 'your paddingMode'
        aad = UtilClient.to_bytes('your aad')
        ciphertext_blob = UtilClient.to_bytes('your ciphertextBlob')
        key_id = 'your keyId'
        iv = UtilClient.to_bytes('your iv')
        algorithm = 'your algorithm'
        response = await Decrypt.decrypt_async(client, padding_mode, aad, ciphertext_blob, key_id, iv, algorithm)
        print(response)


if __name__ == '__main__':
    Decrypt.main(sys.argv[1:])
