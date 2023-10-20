# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_env.client import Client as EnvClient


class Verify:
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
    def verify(
        client: KmsSdkClient,
        message_type: str,
        signature: bytes,
        key_id: str,
        message: bytes,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.VerifyResponse:
        request = dedicated_kms_sdk_models.VerifyRequest(
            message_type=message_type,
            signature=signature,
            key_id=key_id,
            message=message,
            algorithm=algorithm
        )
        return client.verify(request)

    @staticmethod
    async def verify_async(
        client: KmsSdkClient,
        message_type: str,
        signature: bytes,
        key_id: str,
        message: bytes,
        algorithm: str,
    ) -> dedicated_kms_sdk_models.VerifyResponse:
        request = dedicated_kms_sdk_models.VerifyRequest(
            message_type=message_type,
            signature=signature,
            key_id=key_id,
            message=message,
            algorithm=algorithm
        )
        return await client.verify_async(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        kms_instance_config = Verify.create_kms_instance_config(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = Verify.create_client(kms_instance_config)
        message_type = 'your messageType'
        signature = UtilClient.to_bytes('your signature')
        key_id = 'your keyId'
        message = UtilClient.to_bytes('your message')
        algorithm = 'your algorithm'
        response = Verify.verify(client, message_type, signature, key_id, message, algorithm)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        kms_instance_config = await Verify.create_kms_instance_config_async(EnvClient.get_env('your client key file path env'), EnvClient.get_env('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = await Verify.create_client_async(kms_instance_config)
        message_type = 'your messageType'
        signature = UtilClient.to_bytes('your signature')
        key_id = 'your keyId'
        message = UtilClient.to_bytes('your message')
        algorithm = 'your algorithm'
        response = await Verify.verify_async(client, message_type, signature, key_id, message, algorithm)
        print(response)


if __name__ == '__main__':
    Verify.main(sys.argv[1:])
