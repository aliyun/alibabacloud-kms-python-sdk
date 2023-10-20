# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_env.client import Client as EnvClient
from alibabacloud_darabonba_number.client import Client as NumberClient


class GenerateDataKey:
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
    def generate_data_key(
        client: KmsSdkClient,
        aad: bytes,
        key_id: str,
        number_of_bytes: int,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.GenerateDataKeyResponse:
        request = dedicated_kms_sdk_models.GenerateDataKeyRequest(
            aad=aad,
            key_id=key_id,
            number_of_bytes=number_of_bytes,
            algorithm=algorithm
        )
        return client.generate_data_key(request)

    @staticmethod
    async def generate_data_key_async(
        client: KmsSdkClient,
        aad: bytes,
        key_id: str,
        number_of_bytes: int,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.GenerateDataKeyResponse:
        request = dedicated_kms_sdk_models.GenerateDataKeyRequest(
            aad=aad,
            key_id=key_id,
            number_of_bytes=number_of_bytes,
            algorithm=algorithm
        )
        return await client.generate_data_key_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = GenerateDataKey.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = GenerateDataKey.create_client(kms_instance_config)
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        number_of_bytes = NumberClient.parse_int(UtilClient.assert_as_string('your numberOfBytes'))
        algorithm = 'your algorithm'
        response = GenerateDataKey.generate_data_key(client, aad, key_id, number_of_bytes, algorithm)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await GenerateDataKey.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await GenerateDataKey.create_client_async(kms_instance_config)
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        number_of_bytes = NumberClient.parse_int(UtilClient.assert_as_string('your numberOfBytes'))
        algorithm = 'your algorithm'
        response = await GenerateDataKey.generate_data_key_async(client, aad, key_id, number_of_bytes, algorithm)
        print(response)


if __name__ == '__main__':
    GenerateDataKey.main(sys.argv[1:])
