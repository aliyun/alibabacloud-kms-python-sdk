# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_darabonba_env.client import Client as EnvClient


class GetPublicKey:
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
    def get_public_key(
        client: KmsSdkClient,
        key_id: str,
    ) -> dedicated_kms_sdk_models.GetPublicKeyResponse:
        request = dedicated_kms_sdk_models.GetPublicKeyRequest(
            key_id=key_id
        )
        return client.get_public_key(request)

    @staticmethod
    async def get_public_key_async(
        client: KmsSdkClient,
        key_id: str,
    ) -> dedicated_kms_sdk_models.GetPublicKeyResponse:
        request = dedicated_kms_sdk_models.GetPublicKeyRequest(
            key_id=key_id
        )
        return await client.get_public_key_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = GetPublicKey.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = GetPublicKey.create_client(kms_instance_config)
        key_id = 'your keyId'
        response = GetPublicKey.get_public_key(client, key_id)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await GetPublicKey.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await GetPublicKey.create_client_async(kms_instance_config)
        key_id = 'your keyId'
        response = await GetPublicKey.get_public_key_async(client, key_id)
        print(response)


if __name__ == '__main__':
    GetPublicKey.main(sys.argv[1:])
