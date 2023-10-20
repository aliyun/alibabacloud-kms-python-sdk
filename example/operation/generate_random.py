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


class GenerateRandom:
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
    def generate_random(
        client: KmsSdkClient,
        length: int,
    ) -> dedicated_kms_sdk_models.GenerateRandomResponse:
        request = dedicated_kms_sdk_models.GenerateRandomRequest(
            length=length
        )
        return client.generate_random(request)

    @staticmethod
    async def generate_random_async(
        client: KmsSdkClient,
        length: int,
    ) -> dedicated_kms_sdk_models.GenerateRandomResponse:
        request = dedicated_kms_sdk_models.GenerateRandomRequest(
            length=length
        )
        return await client.generate_random_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = GenerateRandom.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = GenerateRandom.create_client(kms_instance_config)
        length = NumberClient.parse_int(UtilClient.assert_as_string('your length'))
        response = GenerateRandom.generate_random(client, length)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await GenerateRandom.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await GenerateRandom.create_client_async(kms_instance_config)
        length = NumberClient.parse_int(UtilClient.assert_as_string('your length'))
        response = await GenerateRandom.generate_random_async(client, length)
        print(response)


if __name__ == '__main__':
    GenerateRandom.main(sys.argv[1:])
