# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_env.client import Client as EnvClient


class AdvanceGenerateDataKeyPairWithoutPlaintext:
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
    def advance_generate_data_key_pair_without_plaintext(
        client: KmsSdkClient,
        key_format: str,
        aad: bytes,
        key_id: str,
        key_pair_spec: str,
    ) -> dedicated_kms_sdk_models.AdvanceGenerateDataKeyPairWithoutPlaintextResponse:
        request = dedicated_kms_sdk_models.AdvanceGenerateDataKeyPairWithoutPlaintextRequest(
            key_format=key_format,
            aad=aad,
            key_id=key_id,
            key_pair_spec=key_pair_spec
        )
        return client.advance_generate_data_key_pair_without_plaintext(request)

    @staticmethod
    async def advance_generate_data_key_pair_without_plaintext_async(
        client: KmsSdkClient,
        key_format: str,
        aad: bytes,
        key_id: str,
        key_pair_spec: str,
    ) -> dedicated_kms_sdk_models.AdvanceGenerateDataKeyPairWithoutPlaintextResponse:
        request = dedicated_kms_sdk_models.AdvanceGenerateDataKeyPairWithoutPlaintextRequest(
            key_format=key_format,
            aad=aad,
            key_id=key_id,
            key_pair_spec=key_pair_spec
        )
        return await client.advance_generate_data_key_pair_without_plaintext_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = AdvanceGenerateDataKeyPairWithoutPlaintext.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = AdvanceGenerateDataKeyPairWithoutPlaintext.create_client(kms_instance_config)
        key_format = 'your keyFormat'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        key_pair_spec = 'your keyPairSpec'
        response = AdvanceGenerateDataKeyPairWithoutPlaintext.advance_generate_data_key_pair_without_plaintext(client, key_format, aad, key_id, key_pair_spec)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await AdvanceGenerateDataKeyPairWithoutPlaintext.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await AdvanceGenerateDataKeyPairWithoutPlaintext.create_client_async(kms_instance_config)
        key_format = 'your keyFormat'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        key_pair_spec = 'your keyPairSpec'
        response = await AdvanceGenerateDataKeyPairWithoutPlaintext.advance_generate_data_key_pair_without_plaintext_async(client, key_format, aad, key_id, key_pair_spec)
        print(response)


if __name__ == '__main__':
    AdvanceGenerateDataKeyPairWithoutPlaintext.main(sys.argv[1:])
