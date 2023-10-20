# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_darabonba_env.client import Client as EnvClient


class SetDeletionProtection:
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
    def set_deletion_protection(
        client: KmsSdkClient,
        protected_resource_arn: str,
        enable_deletion_protection: bool,
        deletion_protection_description: str,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        request = kms_20160120_models.SetDeletionProtectionRequest(
            protected_resource_arn=protected_resource_arn,
            enable_deletion_protection=enable_deletion_protection,
            deletion_protection_description=deletion_protection_description
        )
        return client.set_deletion_protection(request)

    @staticmethod
    async def set_deletion_protection_async(
        client: KmsSdkClient,
        protected_resource_arn: str,
        enable_deletion_protection: bool,
        deletion_protection_description: str,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        request = kms_20160120_models.SetDeletionProtectionRequest(
            protected_resource_arn=protected_resource_arn,
            enable_deletion_protection=enable_deletion_protection,
            deletion_protection_description=deletion_protection_description
        )
        return client.set_deletion_protection(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = SetDeletionProtection.create_open_api_config(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = SetDeletionProtection.create_client(open_api_config)
        protected_resource_arn = 'your protectedResourceArn'
        enable_deletion_protection = False
        deletion_protection_description = 'your deletionProtectionDescription'
        response = SetDeletionProtection.set_deletion_protection(client, protected_resource_arn, enable_deletion_protection, deletion_protection_description)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = await SetDeletionProtection.create_open_api_config_async(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = await SetDeletionProtection.create_client_async(open_api_config)
        protected_resource_arn = 'your protectedResourceArn'
        enable_deletion_protection = False
        deletion_protection_description = 'your deletionProtectionDescription'
        response = await SetDeletionProtection.set_deletion_protection_async(client, protected_resource_arn, enable_deletion_protection, deletion_protection_description)
        print(response)


if __name__ == '__main__':
    SetDeletionProtection.main(sys.argv[1:])
