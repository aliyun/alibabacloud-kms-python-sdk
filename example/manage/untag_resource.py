# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_darabonba_env.client import Client as EnvClient


class UntagResource:
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
    def untag_resource(
        client: KmsSdkClient,
        secret_name: str,
        tag_keys: str,
        certificate_id: str,
        key_id: str,
    ) -> kms_20160120_models.UntagResourceResponse:
        request = kms_20160120_models.UntagResourceRequest(
            secret_name=secret_name,
            tag_keys=tag_keys,
            certificate_id=certificate_id,
            key_id=key_id
        )
        return client.untag_resource(request)

    @staticmethod
    async def untag_resource_async(
        client: KmsSdkClient,
        secret_name: str,
        tag_keys: str,
        certificate_id: str,
        key_id: str,
    ) -> kms_20160120_models.UntagResourceResponse:
        request = kms_20160120_models.UntagResourceRequest(
            secret_name=secret_name,
            tag_keys=tag_keys,
            certificate_id=certificate_id,
            key_id=key_id
        )
        return client.untag_resource(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = UntagResource.create_open_api_config(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = UntagResource.create_client(open_api_config)
        secret_name = 'your secretName'
        tag_keys = 'your tagKeys'
        certificate_id = 'your certificateId'
        key_id = 'your keyId'
        response = UntagResource.untag_resource(client, secret_name, tag_keys, certificate_id, key_id)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = await UntagResource.create_open_api_config_async(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = await UntagResource.create_client_async(open_api_config)
        secret_name = 'your secretName'
        tag_keys = 'your tagKeys'
        certificate_id = 'your certificateId'
        key_id = 'your keyId'
        response = await UntagResource.untag_resource_async(client, secret_name, tag_keys, certificate_id, key_id)
        print(response)


if __name__ == '__main__':
    UntagResource.main(sys.argv[1:])
