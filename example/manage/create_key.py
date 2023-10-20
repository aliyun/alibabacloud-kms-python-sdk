# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_darabonba_env.client import Client as EnvClient


class CreateKey:
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
    def create_key(
        client: KmsSdkClient,
        enable_automatic_rotation: bool,
        rotation_interval: str,
        key_usage: str,
        origin: str,
        description: str,
        dkmsinstance_id: str,
        protection_level: str,
        key_spec: str,
    ) -> kms_20160120_models.CreateKeyResponse:
        request = kms_20160120_models.CreateKeyRequest(
            enable_automatic_rotation=enable_automatic_rotation,
            rotation_interval=rotation_interval,
            key_usage=key_usage,
            origin=origin,
            description=description,
            dkmsinstance_id=dkmsinstance_id,
            protection_level=protection_level,
            key_spec=key_spec
        )
        return client.create_key(request)

    @staticmethod
    async def create_key_async(
        client: KmsSdkClient,
        enable_automatic_rotation: bool,
        rotation_interval: str,
        key_usage: str,
        origin: str,
        description: str,
        dkmsinstance_id: str,
        protection_level: str,
        key_spec: str,
    ) -> kms_20160120_models.CreateKeyResponse:
        request = kms_20160120_models.CreateKeyRequest(
            enable_automatic_rotation=enable_automatic_rotation,
            rotation_interval=rotation_interval,
            key_usage=key_usage,
            origin=origin,
            description=description,
            dkmsinstance_id=dkmsinstance_id,
            protection_level=protection_level,
            key_spec=key_spec
        )
        return client.create_key(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = CreateKey.create_open_api_config(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = CreateKey.create_client(open_api_config)
        enable_automatic_rotation = False
        rotation_interval = 'your rotationInterval'
        key_usage = 'your keyUsage'
        origin = 'your origin'
        description = 'your description'
        d_kmsinstance_id = 'your dKMSInstanceId'
        protection_level = 'your protectionLevel'
        key_spec = 'your keySpec'
        response = CreateKey.create_key(client, enable_automatic_rotation, rotation_interval, key_usage, origin, description, d_kmsinstance_id, protection_level, key_spec)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = await CreateKey.create_open_api_config_async(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = await CreateKey.create_client_async(open_api_config)
        enable_automatic_rotation = False
        rotation_interval = 'your rotationInterval'
        key_usage = 'your keyUsage'
        origin = 'your origin'
        description = 'your description'
        d_kmsinstance_id = 'your dKMSInstanceId'
        protection_level = 'your protectionLevel'
        key_spec = 'your keySpec'
        response = await CreateKey.create_key_async(client, enable_automatic_rotation, rotation_interval, key_usage, origin, description, d_kmsinstance_id, protection_level, key_spec)
        print(response)


if __name__ == '__main__':
    CreateKey.main(sys.argv[1:])
