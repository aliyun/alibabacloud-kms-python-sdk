# -*- coding: utf-8 -*-
from Tea.exceptions import TeaException
from alibabacloud_tea_openapi import models as open_api_models
from openapi_util import models as dkms_util_models
from requests import codes
from sdk.client import Client as DKmsClient
from sdk.models import GetPublicKeyRequest

from alibabacloud_kms_kms20160120.handlers.kms_transfer_handler import KmsTransferHandler
from alibabacloud_kms_kms20160120.models import KmsRuntimeOptions, KmsConfig
from alibabacloud_kms_kms20160120.utils import consts


class GetPublicKeyTransferHandler(KmsTransferHandler):

    def __init__(self, client: DKmsClient, action: str, kms_config: KmsConfig):
        self.client = client
        self.action = action
        self.response_headers = [consts.MIGRATION_KEY_VERSION_ID_KEY]
        self.encoding = 'utf-8'
        if kms_config is not None and kms_config.encoding is not None:
            self.encoding = kms_config.encoding

    def get_client(self):
        return self.client

    def get_action(self):
        return self.action

    def build_kms_request(self, request: open_api_models.OpenApiRequest, runtime_options: KmsRuntimeOptions):
        kms_request = GetPublicKeyRequest()
        kms_request.key_id = request.query.get('KeyId')
        return kms_request

    def call_kms(self, request, runtime_options: KmsRuntimeOptions):
        dkms_runtime_options = dkms_util_models.RuntimeOptions().from_map(runtime_options.to_map())
        dkms_runtime_options.verify = runtime_options.ca
        dkms_runtime_options.response_headers = self.response_headers
        return self.client.get_public_key_with_options(request, dkms_runtime_options)

    def transfer_response(self, response, runtime_options: KmsRuntimeOptions) -> dict:
        response_headers = response.response_headers
        if not response_headers:
            raise TeaException({
                'message': 'Can not found response headers'
            })
        key_version_id = response_headers.get(consts.MIGRATION_KEY_VERSION_ID_KEY)
        body = {
            'KeyId': response.key_id,
            'PublicKey': response.public_key,
            'RequestId': response.request_id,
            'KeyVersionId': key_version_id
        }
        return {
            'body': body,
            'headers': response_headers,
            'statusCode': codes.ok
        }
