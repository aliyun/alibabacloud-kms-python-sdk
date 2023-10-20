# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict, Any

from alibabacloud_kms20160120.client import Client as Kms20160120Client
from sdk.client import Client as DedicatedKmsSdkClient
from openapi import models as dedicated_kms_openapi_models
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_kms20160120 import models as kms_20160120_models


class Client(DedicatedKmsSdkClient):
    _kms_client: Kms20160120Client = None

    def __init__(
            self,
            kms_instance_config: dedicated_kms_openapi_models.Config = None,
            open_api_config: open_api_models.Config = None,
    ):
        if kms_instance_config is None:
            kms_instance_config = dedicated_kms_openapi_models.Config(endpoint="mock endpoint")
        super().__init__(kms_instance_config)
        if open_api_config is None:
            open_api_config = open_api_models.Config(region_id="mock region_id")
        self._kms_client = Kms20160120Client(open_api_config)

    def do_action(
            self,
            query: Dict[str, Any],
            action: str,
            runtime: util_models.RuntimeOptions,
    ) -> Dict[str, Any]:
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action=action,
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return self._kms_client.call_api(params, req, runtime)

    def cancel_key_deletion(
            self,
            request: kms_20160120_models.CancelKeyDeletionRequest,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        """
        调用CancelKeyDeletion接口撤销密钥删除
        @param request:
        @return: CancelKeyDeletionResponse
        """
        return self._kms_client.cancel_key_deletion(request)

    def cancel_key_deletion_with_options(
            self,
            request: kms_20160120_models.CancelKeyDeletionRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        """
        带运行参数调用CancelKeyDeletion接口撤销密钥删除
        @param request:
        @param runtime:
        @return: CancelKeyDeletionResponse
        """
        return self._kms_client.cancel_key_deletion_with_options(request, runtime)

    def create_alias(
            self,
            request: kms_20160120_models.CreateAliasRequest,
    ) -> kms_20160120_models.CreateAliasResponse:
        """
        调用CreateAlias接口为主密钥（CMK）创建一个别名
        @param request:
        @return: CreateAliasResponse
        """
        return self._kms_client.create_alias(request)

    def create_alias_with_options(
            self,
            request: kms_20160120_models.CreateAliasRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateAliasResponse:
        """
        带运行参数调用CreateAlias接口为主密钥（CMK）创建一个别名
        @param request:
        @param runtime:
        @return: CreateAliasResponse
        """
        return self._kms_client.create_alias_with_options(request, runtime)

    def create_key(
            self,
            request: kms_20160120_models.CreateKeyRequest,
    ) -> kms_20160120_models.CreateKeyResponse:
        """
        调用CreateKey接口创建一个主密钥
        @param request:
        @return: CreateKeyResponse
        """
        return self._kms_client.create_key(request)

    def create_key_with_options(
            self,
            request: kms_20160120_models.CreateKeyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyResponse:
        """
        带运行参数调用CreateKey接口创建一个主密钥
        @param request:
        @param runtime:
        @return: CreateKeyResponse
        """
        return self._kms_client.create_key_with_options(request, runtime)

    def create_key_version(
            self,
            request: kms_20160120_models.CreateKeyVersionRequest,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        """
        调用CreateKeyVersion接口为用户主密钥（CMK）创建密钥版本
        @param request:
        @return: CreateKeyVersionResponse
        """
        return self._kms_client.create_key_version(request)

    def create_key_version_with_options(
            self,
            request: kms_20160120_models.CreateKeyVersionRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        """
        带运行参数调用CreateKeyVersion接口为用户主密钥（CMK）创建密钥版本
        @param request:
        @param runtime:
        @return: CreateKeyVersionResponse
        """
        return self._kms_client.create_key_version_with_options(request, runtime)

    def create_secret(
            self,
            request: kms_20160120_models.CreateSecretRequest,
    ) -> kms_20160120_models.CreateSecretResponse:
        """
        创建凭据并存入凭据的初始版本
        @param request:
        @return: CreateSecretResponse
        """
        return self._kms_client.create_secret(request)

    def create_secret_with_options(
            self,
            request: kms_20160120_models.CreateSecretRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateSecretResponse:
        """
        带运行参数创建凭据并存入凭据的初始版本
        @param request:
        @param runtime:
        @return: CreateSecretResponse
        """
        return self._kms_client.create_secret_with_options(request, runtime)

    def delete_alias(
            self,
            request: kms_20160120_models.DeleteAliasRequest,
    ) -> kms_20160120_models.DeleteAliasResponse:
        """
        调用DeleteAlias接口删除别名
        @param request:
        @return: DeleteAliasResponse
        """
        return self._kms_client.delete_alias(request)

    def delete_alias_with_options(
            self,
            request: kms_20160120_models.DeleteAliasRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteAliasResponse:
        """
        带运行参数调用DeleteAlias接口删除别名
        @param request:
        @param runtime:
        @return: DeleteAliasResponse
        """
        return self._kms_client.delete_alias_with_options(request, runtime)

    def delete_key_material(
            self,
            request: kms_20160120_models.DeleteKeyMaterialRequest,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        """
        调用DeleteKeyMaterial接口删除已导入的密钥材料
        @param request:
        @return: DeleteKeyMaterialResponse
        """
        return self._kms_client.delete_key_material(request)

    def delete_key_material_with_options(
            self,
            request: kms_20160120_models.DeleteKeyMaterialRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        """
        带运行参数调用DeleteKeyMaterial接口删除已导入的密钥材料
        @param request:
        @param runtime:
        @return: DeleteKeyMaterialResponse
        """
        return self._kms_client.delete_key_material_with_options(request, runtime)

    def delete_secret(
            self,
            request: kms_20160120_models.DeleteSecretRequest,
    ) -> kms_20160120_models.DeleteSecretResponse:
        """
        调用DeleteSecret接口删除凭据对象
        @param request:
        @return: DeleteSecretResponse
        """
        return self._kms_client.delete_secret(request)

    def delete_secret_with_options(
            self,
            request: kms_20160120_models.DeleteSecretRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteSecretResponse:
        """
        带运行参数调用DeleteSecret接口删除凭据对象
        @param request:
        @param runtime:
        @return: DeleteSecretResponse
        """
        return self._kms_client.delete_secret_with_options(request, runtime)

    def describe_key(
            self,
            request: kms_20160120_models.DescribeKeyRequest,
    ) -> kms_20160120_models.DescribeKeyResponse:
        """
        调用DescribeKey接口查询用户主密钥（CMK）详情
        @param request:
        @return: DescribeKeyResponse
        """
        return self._kms_client.describe_key(request)

    def describe_key_with_options(
            self,
            request: kms_20160120_models.DescribeKeyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyResponse:
        """
        带运行参数调用DescribeKey接口查询用户主密钥（CMK）详情
        @param request:
        @param runtime:
        @return: DescribeKeyResponse
        """
        return self._kms_client.describe_key_with_options(request, runtime)

    def describe_key_version(
            self,
            request: kms_20160120_models.DescribeKeyVersionRequest,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        """
        调用DescribeKeyVersion接口查询指定密钥版本信息
        @param request:
        @return: DescribeKeyVersionResponse
        """
        return self._kms_client.describe_key_version(request)

    def describe_key_version_with_options(
            self,
            request: kms_20160120_models.DescribeKeyVersionRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        """
        带运行参数调用DescribeKeyVersion接口查询指定密钥版本信息
        @param request:
        @param runtime:
        @return: DescribeKeyVersionResponse
        """
        return self._kms_client.describe_key_version_with_options(request, runtime)

    def describe_secret(
            self,
            request: kms_20160120_models.DescribeSecretRequest,
    ) -> kms_20160120_models.DescribeSecretResponse:
        """
        调用DescribeSecret接口查询凭据的元数据信息
        @param request:
        @return: DescribeSecretResponse
        """
        return self._kms_client.describe_secret(request)

    def describe_secret_with_options(
            self,
            request: kms_20160120_models.DescribeSecretRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeSecretResponse:
        """
        带运行参数调用DescribeSecret接口查询凭据的元数据信息
        @param request:
        @param runtime:
        @return: DescribeSecretResponse
        """
        return self._kms_client.describe_secret_with_options(request, runtime)

    def disable_key(
            self,
            request: kms_20160120_models.DisableKeyRequest,
    ) -> kms_20160120_models.DisableKeyResponse:
        """
        调用DisableKey接口禁用指定的主密钥（CMK）进行加解密
        @param request:
        @return: DisableKeyResponse
        """
        return self._kms_client.disable_key(request)

    def disable_key_with_options(
            self,
            request: kms_20160120_models.DisableKeyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DisableKeyResponse:
        """
        带运行参数调用DisableKey接口禁用指定的主密钥（CMK）进行加解密
        @param request:
        @param runtime:
        @return: DisableKeyResponse
        """
        return self._kms_client.disable_key_with_options(request, runtime)

    def enable_key(
            self,
            request: kms_20160120_models.EnableKeyRequest,
    ) -> kms_20160120_models.EnableKeyResponse:
        """
        调用EnableKey接口启用指定的主密钥进行加解密
        @param request:
        @return: EnableKeyResponse
        """
        return self._kms_client.enable_key(request)

    def enable_key_with_options(
            self,
            request: kms_20160120_models.EnableKeyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EnableKeyResponse:
        """
        带运行参数调用EnableKey接口启用指定的主密钥进行加解密
        @param request:
        @param runtime:
        @return: EnableKeyResponse
        """
        return self._kms_client.enable_key_with_options(request, runtime)

    def export_data_key(
            self,
            request: kms_20160120_models.ExportDataKeyRequest,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        """
        调用ExportDataKey接口使用传入的公钥加密导出数据密钥
        @param request:
        @return: ExportDataKeyResponse
        """
        return self._kms_client.export_data_key(request)

    def export_data_key_with_options(
            self,
            request: kms_20160120_models.ExportDataKeyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        """
        带运行参数调用ExportDataKey接口使用传入的公钥加密导出数据密钥
        @param request:
        @param runtime:
        @return: ExportDataKeyResponse
        """
        return self._kms_client.export_data_key_with_options(request, runtime)

    def generate_and_export_data_key(
            self,
            request: kms_20160120_models.GenerateAndExportDataKeyRequest,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        """
        调用GenerateAndExportDataKey接口随机生成一个数据密钥
        @param request:
        @return: GenerateAndExportDataKeyResponse
        """
        return self._kms_client.generate_and_export_data_key(request)

    def generate_and_export_data_key_with_options(
            self,
            request: kms_20160120_models.GenerateAndExportDataKeyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        """
        带运行参数调用GenerateAndExportDataKey接口随机生成一个数据密钥
        @param request:
        @param runtime:
        @return: GenerateAndExportDataKeyResponse
        """
        return self._kms_client.generate_and_export_data_key_with_options(request, runtime)

    def get_parameters_for_import(
            self,
            request: kms_20160120_models.GetParametersForImportRequest,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        """
        调用GetParametersForImport接口获取导入主密钥材料的参数
        @param request:
        @return: GetParametersForImportResponse
        """
        return self._kms_client.get_parameters_for_import(request)

    def get_parameters_for_import_with_options(
            self,
            request: kms_20160120_models.GetParametersForImportRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        """
        带运行参数调用GetParametersForImport接口获取导入主密钥材料的参数
        @param request:
        @param runtime:
        @return: GetParametersForImportResponse
        """
        return self._kms_client.get_parameters_for_import_with_options(request, runtime)

    def get_random_password(
            self,
            request: kms_20160120_models.GetRandomPasswordRequest,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        """
        调用GetRandomPassword接口获得一个随机口令字符串
        @param request:
        @return: GetRandomPasswordResponse
        """
        return self._kms_client.get_random_password(request)

    def get_random_password_with_options(
            self,
            request: kms_20160120_models.GetRandomPasswordRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        """
        带运行参数调用GetRandomPassword接口获得一个随机口令字符串
        @param request:
        @param runtime:
        @return: GetRandomPasswordResponse
        """
        return self._kms_client.get_random_password_with_options(request, runtime)

    def import_key_material(
            self,
            request: kms_20160120_models.ImportKeyMaterialRequest,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        """
        调用ImportKeyMaterial接口导入密钥材料
        @param request:
        @return: ImportKeyMaterialResponse
        """
        return self._kms_client.import_key_material(request)

    def import_key_material_with_options(
            self,
            request: kms_20160120_models.ImportKeyMaterialRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        """
        带运行参数调用ImportKeyMaterial接口导入密钥材料
        @param request:
        @param runtime:
        @return: ImportKeyMaterialResponse
        """
        return self._kms_client.import_key_material_with_options(request, runtime)

    def list_aliases(
            self,
            request: kms_20160120_models.ListAliasesRequest,
    ) -> kms_20160120_models.ListAliasesResponse:
        """
        调用ListAliases接口查询当前用户在当前地域的所有别名
        @param request:
        @return: ListAliasesResponse
        """
        return self._kms_client.list_aliases(request)

    def list_aliases_with_options(
            self,
            request: kms_20160120_models.ListAliasesRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesResponse:
        """
        带运行参数调用ListAliases接口查询当前用户在当前地域的所有别名
        @param request:
        @param runtime:
        @return: ListAliasesResponse
        """
        return self._kms_client.list_aliases_with_options(request, runtime)

    def list_keys(
            self,
            request: kms_20160120_models.ListKeysRequest,
    ) -> kms_20160120_models.ListKeysResponse:
        """
        调用ListKeys查询调用者在调用地域的所有主密钥ID
        @param request:
        @return: ListKeysResponse
        """
        return self._kms_client.list_keys(request)

    def list_keys_with_options(
            self,
            request: kms_20160120_models.ListKeysRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeysResponse:
        """
        带运行参数调用ListKeys查询调用者在调用地域的所有主密钥ID
        @param request:
        @param runtime:
        @return: ListKeysResponse
        """
        return self._kms_client.list_keys_with_options(request, runtime)

    def list_key_versions(
            self,
            request: kms_20160120_models.ListKeyVersionsRequest,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        """
        调用ListKeyVersions接口列出主密钥的所有密钥版本
        @param request:
        @return: ListKeyVersionsResponse
        """
        return self._kms_client.list_key_versions(request)

    def list_key_versions_with_options(
            self,
            request: kms_20160120_models.ListKeyVersionsRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        """
        带运行参数调用ListKeyVersions接口列出主密钥的所有密钥版本
        @param request:
        @param runtime:
        @return: ListKeyVersionsResponse
        """
        return self._kms_client.list_key_versions_with_options(request, runtime)

    def list_resource_tags(
            self,
            request: kms_20160120_models.ListResourceTagsRequest,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        """
        调用ListResourceTags获取用户主密钥的标签
        @param request:
        @return: ListResourceTagsResponse
        """
        return self._kms_client.list_resource_tags(request)

    def list_resource_tags_with_options(
            self,
            request: kms_20160120_models.ListResourceTagsRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        """
        带运行参数调用ListResourceTags获取用户主密钥的标签
        @param request:
        @param runtime:
        @return: ListResourceTagsResponse
        """
        return self._kms_client.list_resource_tags_with_options(request, runtime)

    def list_secrets(
            self,
            request: kms_20160120_models.ListSecretsRequest,
    ) -> kms_20160120_models.ListSecretsResponse:
        """
        调用ListSecrets接口查询当前用户在当前地域创建的所有凭据
        @param request:
        @return: ListSecretsResponse
        """
        return self._kms_client.list_secrets(request)

    def list_secrets_with_options(
            self,
            request: kms_20160120_models.ListSecretsRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretsResponse:
        """
        带运行参数调用ListSecrets接口查询当前用户在当前地域创建的所有凭据
        @param request:
        @param runtime:
        @return: ListSecretsResponse
        """
        return self._kms_client.list_secrets_with_options(request, runtime)

    def list_secret_version_ids(
            self,
            request: kms_20160120_models.ListSecretVersionIdsRequest,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        """
        调用ListSecretVersionIds接口查询凭据的所有版本信息
        @param request:
        @return: ListSecretVersionIdsResponse
        """
        return self._kms_client.list_secret_version_ids(request)

    def list_secret_version_ids_with_options(
            self,
            request: kms_20160120_models.ListSecretVersionIdsRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        """
        带运行参数调用ListSecretVersionIds接口查询凭据的所有版本信息
        @param request:
        @param runtime:
        @return: ListSecretVersionIdsResponse
        """
        return self._kms_client.list_secret_version_ids_with_options(request, runtime)

    def put_secret_value(
            self,
            request: kms_20160120_models.PutSecretValueRequest,
    ) -> kms_20160120_models.PutSecretValueResponse:
        """
        调用PutSecretValue接口为凭据存入一个新版本的凭据值
        @param request:
        @return: PutSecretValueResponse
        """
        return self._kms_client.put_secret_value(request)

    def put_secret_value_with_options(
            self,
            request: kms_20160120_models.PutSecretValueRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.PutSecretValueResponse:
        """
        带运行参数调用PutSecretValue接口为凭据存入一个新版本的凭据值
        @param request:
        @param runtime:
        @return: PutSecretValueResponse
        """
        return self._kms_client.put_secret_value_with_options(request, runtime)

    def restore_secret(
            self,
            request: kms_20160120_models.RestoreSecretRequest,
    ) -> kms_20160120_models.RestoreSecretResponse:
        """
        调用RestoreSecret接口恢复被删除的凭据
        @param request:
        @return: RestoreSecretResponse
        """
        return self._kms_client.restore_secret(request)

    def restore_secret_with_options(
            self,
            request: kms_20160120_models.RestoreSecretRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RestoreSecretResponse:
        """
        带运行参数调用RestoreSecret接口恢复被删除的凭据
        @param request:
        @param runtime:
        @return: RestoreSecretResponse
        """
        return self._kms_client.restore_secret_with_options(request, runtime)

    def rotate_secret(
            self,
            request: kms_20160120_models.RotateSecretRequest,
    ) -> kms_20160120_models.RotateSecretResponse:
        """
        调用RotateSecret接口手动轮转凭据
        @param request:
        @return: RotateSecretResponse
        """
        return self._kms_client.rotate_secret(request)

    def rotate_secret_with_options(
            self,
            request: kms_20160120_models.RotateSecretRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RotateSecretResponse:
        """
        带运行参数调用RotateSecret接口手动轮转凭据
        @param request:
        @param runtime:
        @return: RotateSecretResponse
        """
        return self._kms_client.rotate_secret_with_options(request, runtime)

    def schedule_key_deletion(
            self,
            request: kms_20160120_models.ScheduleKeyDeletionRequest,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        """
        调用ScheduleKeyDeletion接口申请删除一个指定的主密钥（CMK)
        @param request:
        @return: ScheduleKeyDeletionResponse
        """
        return self._kms_client.schedule_key_deletion(request)

    def schedule_key_deletion_with_options(
            self,
            request: kms_20160120_models.ScheduleKeyDeletionRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        """
        带运行参数调用ScheduleKeyDeletion接口申请删除一个指定的主密钥（CMK)
        @param request:
        @param runtime:
        @return: ScheduleKeyDeletionResponse
        """
        return self._kms_client.schedule_key_deletion_with_options(request, runtime)

    def set_deletion_protection(
            self,
            request: kms_20160120_models.SetDeletionProtectionRequest,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        """
        调用SetDeletionProtection接口为用户主密钥（CMK）开启或关闭删除保护
        @param request:
        @return: SetDeletionProtectionResponse
        """
        return self._kms_client.set_deletion_protection(request)

    def set_deletion_protection_with_options(
            self,
            request: kms_20160120_models.SetDeletionProtectionRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        """
        带运行参数调用SetDeletionProtection接口为用户主密钥（CMK）开启或关闭删除保护
        @param request:
        @param runtime:
        @return: SetDeletionProtectionResponse
        """
        return self._kms_client.set_deletion_protection_with_options(request, runtime)

    def tag_resource(
            self,
            request: kms_20160120_models.TagResourceRequest,
    ) -> kms_20160120_models.TagResourceResponse:
        """
        调用TagResource接口为主密钥、凭据或证书绑定标签
        @param request:
        @return: TagResourceResponse
        """
        return self._kms_client.tag_resource(request)

    def tag_resource_with_options(
            self,
            request: kms_20160120_models.TagResourceRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourceResponse:
        """
        带运行参数调用TagResource接口为主密钥、凭据或证书绑定标签
        @param request:
        @param runtime:
        @return: TagResourceResponse
        """
        return self._kms_client.tag_resource_with_options(request, runtime)

    def untag_resource(
            self,
            request: kms_20160120_models.UntagResourceRequest,
    ) -> kms_20160120_models.UntagResourceResponse:
        """
        调用UntagResource接口为主密钥、凭据或证书解绑标签
        @param request:
        @return: UntagResourceResponse
        """
        return self._kms_client.untag_resource(request)

    def untag_resource_with_options(
            self,
            request: kms_20160120_models.UntagResourceRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UntagResourceResponse:
        """
        带运行参数调用UntagResource接口为主密钥、凭据或证书解绑标签
        @param request:
        @param runtime:
        @return: UntagResourceResponse
        """
        return self._kms_client.untag_resource_with_options(request, runtime)

    def update_alias(
            self,
            request: kms_20160120_models.UpdateAliasRequest,
    ) -> kms_20160120_models.UpdateAliasResponse:
        """
        调用UpdateAlias接口更新已存在的别名所代表的主密钥（CMK）ID
        @param request:
        @return: UpdateAliasResponse
        """
        return self._kms_client.update_alias(request)

    def update_alias_with_options(
            self,
            request: kms_20160120_models.UpdateAliasRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateAliasResponse:
        """
        带运行参数调用UpdateAlias接口更新已存在的别名所代表的主密钥（CMK）ID
        @param request:
        @param runtime:
        @return: UpdateAliasResponse
        """
        return self._kms_client.update_alias_with_options(request, runtime)

    def update_key_description(
            self,
            request: kms_20160120_models.UpdateKeyDescriptionRequest,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        """
        调用UpdateKeyDescription接口更新主密钥的描述信息
        @param request:
        @return: UpdateKeyDescriptionResponse
        """
        return self._kms_client.update_key_description(request)

    def update_key_description_with_options(
            self,
            request: kms_20160120_models.UpdateKeyDescriptionRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        """
        带运行参数调用UpdateKeyDescription接口更新主密钥的描述信息
        @param request:
        @param runtime:
        @return: UpdateKeyDescriptionResponse
        """
        return self._kms_client.update_key_description_with_options(request, runtime)

    def update_rotation_policy(
            self,
            request: kms_20160120_models.UpdateRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        """
        调用UpdateRotationPolicy接口更新密钥轮转策略
        @param request:
        @return: UpdateRotationPolicyResponse
        """
        return self._kms_client.update_rotation_policy(request)

    def update_rotation_policy_with_options(
            self,
            request: kms_20160120_models.UpdateRotationPolicyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        """
        带运行参数调用UpdateRotationPolicy接口更新密钥轮转策略
        @param request:
        @param runtime:
        @return: UpdateRotationPolicyResponse
        """
        return self._kms_client.update_rotation_policy_with_options(request, runtime)

    def update_secret(
            self,
            request: kms_20160120_models.UpdateSecretRequest,
    ) -> kms_20160120_models.UpdateSecretResponse:
        """
        调用UpdateSecret接口更新凭据的元数据
        @param request:
        @return: UpdateSecretResponse
        """
        return self._kms_client.update_secret(request)

    def update_secret_with_options(
            self,
            request: kms_20160120_models.UpdateSecretRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretResponse:
        """
        带运行参数调用UpdateSecret接口更新凭据的元数据
        @param request:
        @param runtime:
        @return: UpdateSecretResponse
        """
        return self._kms_client.update_secret_with_options(request, runtime)

    def update_secret_rotation_policy(
            self,
            request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        """
        调用UpdateSecretRotationPolicy接口更新凭据轮转策略
        @param request:
        @return: UpdateSecretRotationPolicyResponse
        """
        return self._kms_client.update_secret_rotation_policy(request)

    def update_secret_rotation_policy_with_options(
            self,
            request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        """
        带运行参数调用UpdateSecretRotationPolicy接口更新凭据轮转策略
        @param request:
        @param runtime:
        @return: UpdateSecretRotationPolicyResponse
        """
        return self._kms_client.update_secret_rotation_policy_with_options(request, runtime)

    def update_secret_version_stage(
            self,
            request: kms_20160120_models.UpdateSecretVersionStageRequest,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        """
        调用UpdateSecretVersionStage接口更新凭据的版本状态
        @param request:
        @return: UpdateSecretVersionStageResponse
        """
        return self._kms_client.update_secret_version_stage(request)

    def update_secret_version_stage_with_options(
            self,
            request: kms_20160120_models.UpdateSecretVersionStageRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        """
        带运行参数调用UpdateSecretVersionStage接口更新凭据的版本状态
        @param request:
        @param runtime:
        @return: UpdateSecretVersionStageResponse
        """
        return self._kms_client.update_secret_version_stage_with_options(request, runtime)

    def open_kms_service(self) -> kms_20160120_models.OpenKmsServiceResponse:
        """
        调用OpenKmsService接口为当前阿里云账号开通密钥管理服务
        @return: OpenKmsServiceResponse
        """
        return self._kms_client.open_kms_service()

    def open_kms_service_with_options(
            self,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.OpenKmsServiceResponse:
        """
        带运行参数调用OpenKmsService接口为当前阿里云账号开通密钥管理服务
        @param runtime:
        @return: OpenKmsServiceResponse
        """
        return self._kms_client.open_kms_service_with_options(runtime)

    def describe_regions(self) -> kms_20160120_models.DescribeRegionsResponse:
        """
        调用DescribeRegions接口查询当前账号的可用地域列表
        @return: DescribeRegionsResponse
        """
        return self._kms_client.describe_regions()

    def describe_regions_with_options(
            self,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeRegionsResponse:
        """
        带运行参数调用DescribeRegions接口查询当前账号的可用地域列表
        @param runtime:
        @return: DescribeRegionsResponse
        """
        return self._kms_client.describe_regions_with_options(runtime)

    def describe_account_kms_status(self) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        """
        调用DescribeAccountKmsStatus接口查询当前阿里云账号的密钥管理服务状态
        @return: DescribeAccountKmsStatusResponse
        """
        return self._kms_client.describe_account_kms_status()

    def describe_account_kms_status_with_options(
            self,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        """
        带运行参数调用DescribeAccountKmsStatus接口查询当前阿里云账号的密钥管理服务状态
        @param runtime:
        @return: DescribeAccountKmsStatusResponse
        """
        return self._kms_client.describe_account_kms_status_with_options(runtime)

    def get_secret_value_by_shared_endpoint(
            self,
            request: kms_20160120_models.GetSecretValueRequest,
    ) -> kms_20160120_models.GetSecretValueResponse:
        """
        调用GetSecretValue接口获取共享网关凭据值
        @param request:
        @return: GetSecretValueResponse
        """
        return self._kms_client.get_secret_value(request)

    def get_secret_value_with_options_by_shared_endpoint(
            self,
            request: kms_20160120_models.GetSecretValueRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetSecretValueResponse:
        """
        带运行参数调用GetSecretValue接口获取共享网关凭据值
        @param request:
        @param runtime:
        @return: GetSecretValueResponse
        """
        return self._kms_client.get_secret_value_with_options(request, runtime)

    def get_public_key_by_shared_endpoint(
            self,
            request: kms_20160120_models.GetPublicKeyRequest,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        """
        调用GetPublicKey接口获取共享网关非对称密钥的公钥
        @param request:
        @return: GetPublicKeyResponse
        """
        return self._kms_client.get_public_key(request)

    def get_public_key_with_options_by_shared_endpoint(
            self,
            request: kms_20160120_models.GetPublicKeyRequest,
            runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        """
        带运行参数调用GetPublicKey接口获取共享网关非对称密钥的公钥
        @param request:
        @param runtime:
        @return: GetPublicKeyResponse
        """
        return self._kms_client.get_public_key_with_options(request, runtime)
