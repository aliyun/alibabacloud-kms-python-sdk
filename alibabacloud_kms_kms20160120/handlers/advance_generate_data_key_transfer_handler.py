# -*- coding: utf-8 -*-
import base64

from Tea.exceptions import TeaException
from alibabacloud_tea_openapi import models as open_api_models
from openapi_util import models as dkms_util_models
from requests import codes
from sdk.client import Client as DKmsClient
from sdk.models import AdvanceEncryptRequest, AdvanceGenerateDataKeyRequest

from alibabacloud_kms_kms20160120.handlers.kms_transfer_handler import KmsTransferHandler, INVALID_PARAM_ERROR_CODE, \
    INVALID_PARAMETER_KEY_SPEC_ERROR_MESSAGE
from alibabacloud_kms_kms20160120.models import KmsRuntimeOptions, KmsConfig
from alibabacloud_kms_kms20160120.utils import consts, encryption_context_utils
from alibabacloud_kms_kms20160120.utils.consts import *


class AdvanceGenerateDataKeyTransferHandler(KmsTransferHandler):

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
        kms_request = AdvanceGenerateDataKeyRequest()
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
            kms_request.aad = encryption_context_utils.sort_and_encode(request.query.get('EncryptionContext'), encoding)
        return kms_request

    def call_kms(self, request, runtime_options: KmsRuntimeOptions):
        dkms_runtime_options = dkms_util_models.RuntimeOptions().from_map(runtime_options.to_map())
        dkms_runtime_options.verify = runtime_options.ca
        dkms_runtime_options.response_headers = self.response_headers
        advance_generate_data_key_response = self.client.advance_generate_data_key_with_options(request, dkms_runtime_options)

        advance_encrypt_request = AdvanceEncryptRequest()
        advance_encrypt_request.key_id = request.key_id
        advance_encrypt_request.plaintext = base64.b64encode(advance_generate_data_key_response.plaintext)
        advance_encrypt_request.aad = request.aad
        encrypt_response = self.client.advance_encrypt_with_options(advance_encrypt_request, dkms_runtime_options)

        advance_generate_data_key_response.response_headers = encrypt_response.response_headers
        advance_generate_data_key_response.ciphertext_blob = encrypt_response.ciphertext_blob
        advance_generate_data_key_response.iv = encrypt_response.iv
        return advance_generate_data_key_response

    def transfer_response(self, response, runtime_options: KmsRuntimeOptions) -> dict:
        response_headers = response.response_headers
        if runtime_options is not None and runtime_options.encoding is not None:
            encoding = runtime_options.encoding
        else:
            encoding = self.encoding
        start = MAGIC_NUM_LENGTH + CIPHER_VER_AND_PADDING_MODE_LENGTH + ALGORITHM_LENGTH
        ciphertext_blob = response.ciphertext_blob[start: len(response.ciphertext_blob)]
        body = {
            'KeyId': response.key_id,
            'CiphertextBlob': base64.b64encode(ciphertext_blob).decode(encoding),
            'Plaintext': base64.b64encode(response.plaintext).decode(encoding),
            'RequestId': response.request_id,
            'KeyVersionId': response.key_version_id
        }
        return {
            'body': body,
            'headers': response_headers,
            'statusCode': codes.ok
        }
