# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_darabonba_env.client import Client as EnvClient


class GetSecretValue:
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
    def get_secret_value(
        client: KmsSdkClient,
        fetch_extended_config: bool,
        secret_name: str,
        version_id: str,
        version_stage: str,
    ) -> dedicated_kms_sdk_models.GetSecretValueResponse:
        request = dedicated_kms_sdk_models.GetSecretValueRequest(
            fetch_extended_config=fetch_extended_config,
            secret_name=secret_name,
            version_id=version_id,
            version_stage=version_stage
        )
        return client.get_secret_value(request)

    @staticmethod
    async def get_secret_value_async(
        client: KmsSdkClient,
        fetch_extended_config: bool,
        secret_name: str,
        version_id: str,
        version_stage: str,
    ) -> dedicated_kms_sdk_models.GetSecretValueResponse:
        request = dedicated_kms_sdk_models.GetSecretValueRequest(
            fetch_extended_config=fetch_extended_config,
            secret_name=secret_name,
            version_id=version_id,
            version_stage=version_stage
        )
        return await client.get_secret_value_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = GetSecretValue.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = GetSecretValue.create_client(kms_instance_config)
        fetch_extended_config = False
        secret_name = 'your secretName'
        version_id = 'your versionId'
        version_stage = 'your versionStage'
        response = GetSecretValue.get_secret_value(client, fetch_extended_config, secret_name, version_id, version_stage)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await GetSecretValue.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await GetSecretValue.create_client_async(kms_instance_config)
        fetch_extended_config = False
        secret_name = 'your secretName'
        version_id = 'your versionId'
        version_stage = 'your versionStage'
        response = await GetSecretValue.get_secret_value_async(client, fetch_extended_config, secret_name, version_id, version_stage)
        print(response)


if __name__ == '__main__':
    GetSecretValue.main(sys.argv[1:])
