# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_darabonba_env.client import Client as EnvClient


class UpdateSecretVersionStage:
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
    def update_secret_version_stage(
        client: KmsSdkClient,
        remove_from_version: str,
        secret_name: str,
        move_to_version: str,
        version_stage: str,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        request = kms_20160120_models.UpdateSecretVersionStageRequest(
            remove_from_version=remove_from_version,
            secret_name=secret_name,
            move_to_version=move_to_version,
            version_stage=version_stage
        )
        return client.update_secret_version_stage(request)

    @staticmethod
    async def update_secret_version_stage_async(
        client: KmsSdkClient,
        remove_from_version: str,
        secret_name: str,
        move_to_version: str,
        version_stage: str,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        request = kms_20160120_models.UpdateSecretVersionStageRequest(
            remove_from_version=remove_from_version,
            secret_name=secret_name,
            move_to_version=move_to_version,
            version_stage=version_stage
        )
        return client.update_secret_version_stage(request)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = UpdateSecretVersionStage.create_open_api_config(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = UpdateSecretVersionStage.create_client(open_api_config)
        remove_from_version = 'your removeFromVersion'
        secret_name = 'your secretName'
        move_to_version = 'your moveToVersion'
        version_stage = 'your versionStage'
        response = UpdateSecretVersionStage.update_secret_version_stage(client, remove_from_version, secret_name, move_to_version, version_stage)
        print(response)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = await UpdateSecretVersionStage.create_open_api_config_async(EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_ID'), EnvClient.get_env('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = await UpdateSecretVersionStage.create_client_async(open_api_config)
        remove_from_version = 'your removeFromVersion'
        secret_name = 'your secretName'
        move_to_version = 'your moveToVersion'
        version_stage = 'your versionStage'
        response = await UpdateSecretVersionStage.update_secret_version_stage_async(client, remove_from_version, secret_name, move_to_version, version_stage)
        print(response)


if __name__ == '__main__':
    UpdateSecretVersionStage.main(sys.argv[1:])
