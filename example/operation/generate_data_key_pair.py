# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_env.client import Client as EnvClient


class GenerateDataKeyPair:
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
    def generate_data_key_pair(
        client: KmsSdkClient,
        key_format: str,
        aad: bytes,
        key_id: str,
        key_pair_spec: str,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.GenerateDataKeyPairResponse:
        request = dedicated_kms_sdk_models.GenerateDataKeyPairRequest(
            key_format=key_format,
            aad=aad,
            key_id=key_id,
            key_pair_spec=key_pair_spec,
            algorithm=algorithm
        )
        return client.generate_data_key_pair(request)

    @staticmethod
    async def generate_data_key_pair_async(
        client: KmsSdkClient,
        key_format: str,
        aad: bytes,
        key_id: str,
        key_pair_spec: str,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.GenerateDataKeyPairResponse:
        request = dedicated_kms_sdk_models.GenerateDataKeyPairRequest(
            key_format=key_format,
            aad=aad,
            key_id=key_id,
            key_pair_spec=key_pair_spec,
            algorithm=algorithm
        )
        return await client.generate_data_key_pair_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = GenerateDataKeyPair.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = GenerateDataKeyPair.create_client(kms_instance_config)
        key_format = 'your keyFormat'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        key_pair_spec = 'your keyPairSpec'
        algorithm = 'your algorithm'
        response = GenerateDataKeyPair.generate_data_key_pair(client, key_format, aad, key_id, key_pair_spec, algorithm)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await GenerateDataKeyPair.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await GenerateDataKeyPair.create_client_async(kms_instance_config)
        key_format = 'your keyFormat'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        key_pair_spec = 'your keyPairSpec'
        algorithm = 'your algorithm'
        response = await GenerateDataKeyPair.generate_data_key_pair_async(client, key_format, aad, key_id, key_pair_spec, algorithm)
        print(response)


if __name__ == '__main__':
    GenerateDataKeyPair.main(sys.argv[1:])
