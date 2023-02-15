# -*- coding: utf-8 -*-
from alibabacloud_tea_openapi import models as open_api_models
from openapi_util import models as dkms_util_models
from requests import codes
from sdk.client import Client as DKmsClient
from sdk.models import GetSecretValueRequest

from alibabacloud_kms_kms20160120.handlers.kms_transfer_handler import KmsTransferHandler
from alibabacloud_kms_kms20160120.models import KmsRuntimeOptions, KmsConfig


class GetSecretValueTransferHandler(KmsTransferHandler):

    def __init__(self, client: DKmsClient, action: str, kms_config: KmsConfig):
        self.client = client
        self.action = action
        self.response_headers = []
        self.encoding = 'utf-8'
        if kms_config is not None and kms_config.encoding is not None:
            self.encoding = kms_config.encoding

    def get_client(self):
        return self.client

    def get_action(self):
        return self.action

    def build_kms_request(self, request: open_api_models.OpenApiRequest, runtime_options: KmsRuntimeOptions):
        kms_request = GetSecretValueRequest()
        kms_request.secret_name = request.query.get('SecretName')
        kms_request.version_id = request.query.get('VersionId')
        kms_request.version_stage = request.query.get('VersionStage')
        kms_request.fetch_extended_config = request.query.get('FetchExtendedConfig')
        return kms_request

    def call_kms(self, request, runtime_options: KmsRuntimeOptions):
        dkms_runtime_options = dkms_util_models.RuntimeOptions().from_map(runtime_options.to_map())
        dkms_runtime_options.verify = runtime_options.ca
        dkms_runtime_options.response_headers = self.response_headers
        return self.client.get_secret_value_with_options(request, dkms_runtime_options)

    def transfer_response(self, response, runtime_options: KmsRuntimeOptions) -> dict:
        body = {
            'SecretName': response.secret_name,
            'SecretType': response.secret_type,
            'SecretData': response.secret_data,
            'SecretDataType': response.secret_data_type,
            'VersionStages': {'VersionStage': response.version_stages},
            'VersionId': response.version_id,
            'CreateTime': response.create_time,
            'RequestId': response.request_id,
            'LastRotationDate': response.last_rotation_date,
            'NextRotationDate': response.next_rotation_date,
            'ExtendedConfig': response.extended_config,
            'AutomaticRotation': response.automatic_rotation,
            'RotationInterval': response.rotation_interval,
        }
        return {
            'body': body,
            'headers': response.response_headers,
            'statusCode': codes.ok
        }
