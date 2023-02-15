# -*- coding: utf-8 -*-
import base64

from Tea.exceptions import TeaException
from alibabacloud_tea_openapi import models as open_api_models
from openapi_util import models as dkms_util_models
from requests import codes
from sdk.client import Client as DKmsClient
from sdk.models import GenerateDataKeyRequest, EncryptRequest

from alibabacloud_kms_kms20160120.handlers.kms_transfer_handler import KmsTransferHandler, INVALID_PARAM_ERROR_CODE, \
    INVALID_PARAMETER_KEY_SPEC_ERROR_MESSAGE
from alibabacloud_kms_kms20160120.models import KmsRuntimeOptions, KmsConfig
from alibabacloud_kms_kms20160120.utils import consts


class GenerateDataKeyWithoutPlaintextTransferHandler(KmsTransferHandler):

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
        kms_request = GenerateDataKeyRequest()
        kms_request.key_id = request.query.get('KeyId')
        key_spec = request.query.get('KeySpec')
        number_of_bytes = request.query.get('NumberOfBytes')
        if not number_of_bytes:
            if not key_spec or key_spec == consts.KMS_KEY_PAIR_AES_256:
                number_of_bytes = consts.NUMBER_OF_BYTES_AES_256
            elif key_spec == consts.KMS_KEY_PAIR_AES_128:
                number_of_bytes = consts.NUMBER_OF_BYTES_AES_128
            else:
                raise TeaException({
                    'code': INVALID_PARAM_ERROR_CODE,
                    'message': INVALID_PARAMETER_KEY_SPEC_ERROR_MESSAGE
                })
        kms_request.number_of_bytes = int(number_of_bytes)
        if runtime_options is not None and runtime_options.encoding is not None:
            encoding = runtime_options.encoding
        else:
            encoding = self.encoding
        if request.query.get('EncryptionContext'):
            kms_request.aad = request.query.get('EncryptionContext').encode(encoding)
        return kms_request

    def call_kms(self, request, runtime_options: KmsRuntimeOptions):
        dkms_runtime_options = dkms_util_models.RuntimeOptions().from_map(runtime_options.to_map())
        dkms_runtime_options.verify = runtime_options.ca
        dkms_runtime_options.response_headers = self.response_headers
        generate_data_key_response = self.client.generate_data_key_with_options(request, dkms_runtime_options)

        encrypt_request = EncryptRequest()
        encrypt_request.key_id = request.key_id
        encrypt_request.plaintext = base64.b64encode(generate_data_key_response.plaintext)
        encrypt_request.aad = request.aad
        encrypt_response = self.client.encrypt_with_options(encrypt_request, dkms_runtime_options)

        generate_data_key_response.response_headers = encrypt_response.response_headers
        generate_data_key_response.ciphertext_blob = encrypt_response.ciphertext_blob
        generate_data_key_response.iv = encrypt_response.iv
        return generate_data_key_response

    def transfer_response(self, response, runtime_options: KmsRuntimeOptions) -> dict:
        response_headers = response.response_headers
        if not response_headers:
            raise TeaException({
                'message': 'Can not found response headers'
            })
        key_version_id = response_headers.get(consts.MIGRATION_KEY_VERSION_ID_KEY)
        if not key_version_id:
            raise TeaException({
                'message': f"Can not found response headers parameter[{consts.MIGRATION_KEY_VERSION_ID_KEY}]"
            })
        if runtime_options is not None and runtime_options.encoding is not None:
            encoding = runtime_options.encoding
        else:
            encoding = self.encoding
        ciphertext_blob = key_version_id.encode(encoding) + response.iv + response.ciphertext_blob
        body = {
            'KeyId': response.key_id,
            'CiphertextBlob': base64.b64encode(ciphertext_blob).decode(encoding),
            'RequestId': response.request_id,
            'KeyVersionId': key_version_id
        }
        return {
            'body': body,
            'headers': response_headers,
            'statusCode': codes.ok
        }
