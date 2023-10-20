# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_darabonba_env.client import Client as EnvClient


class GetPublicKeyBySharedEndpoint:
    def __init__(self):
        pass

    @staticmethod
    def create_open_api_config(
        access_key_id: str,
        access_key_secret: str,
        region_id: str,
    ) -> open_api_models.Config:
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            region_id=region_id
        )
        return config

    @staticmethod
    async def create_open_api_config_async(
        access_key_id: str,
        access_key_secret: str,
        region_id: str,
    ) -> open_api_models.Config:
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            region_id=region_id
        )
        return config

    @staticmethod
    def create_client(
        open_api_config: open_api_models.Config,
    ) -> KmsSdkClient:
        return KmsSdkClient(open_api_config=open_api_config)

    @staticmethod
    async def create_client_async(
        open_api_config: open_api_models.Config,
    ) -> KmsSdkClient:
        return KmsSdkClient(open_api_config=open_api_config)

    @staticmethod
    def get_public_key_by_shared_endpoint(
        client: KmsSdkClient,
        key_version_id: str,
        key_id: str,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        request = kms_20160120_models.GetPublicKeyRequest(
            key_version_id=key_version_id,
            key_id=key_id
        )
        return client.get_public_key_by_shared_endpoint(request)

    @staticmethod
    async def get_public_key_by_shared_endpoint_async(
        client: KmsSdkClient,
        key_version_id: str,
        key_id: str,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        request = kms_20160120_models.GetPublicKeyRequest(
            key_version_id=key_version_id,
            key_id=key_id
        )
        return client.get_public_key_by_shared_endpoint(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = GetPublicKeyBySharedEndpoint.create_open_api_config(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = GetPublicKeyBySharedEndpoint.create_client(open_api_config)
        key_version_id = 'your keyVersionId'
        key_id = 'your keyId'
        response = GetPublicKeyBySharedEndpoint.get_public_key_by_shared_endpoint(client, key_version_id, key_id)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = await GetPublicKeyBySharedEndpoint.create_open_api_config_async(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = await GetPublicKeyBySharedEndpoint.create_client_async(open_api_config)
        key_version_id = 'your keyVersionId'
        key_id = 'your keyId'
        response = await GetPublicKeyBySharedEndpoint.get_public_key_by_shared_endpoint_async(client, key_version_id, key_id)
        print(response)


if __name__ == '__main__':
    GetPublicKeyBySharedEndpoint.main(sys.argv[1:])
