# -*- coding: utf-8 -*-
from Tea.exceptions import TeaException
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_kms20160120.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
from openapi import models as dkms_models
from sdk.client import Client as DKmsClient

from alibabacloud_kms_kms20160120.handlers.advance_decrypt_transfer_handler import AdvanceDecryptTransferHandler
from alibabacloud_kms_kms20160120.handlers.advance_encrypt_transfer_handler import AdvanceEncryptTransferHandler
from alibabacloud_kms_kms20160120.handlers.advance_generate_data_key_transfer_handler import \
    AdvanceGenerateDataKeyTransferHandler
from alibabacloud_kms_kms20160120.handlers.advance_generate_data_key_without_plaintext_transfer_handler import \
    AdvanceGenerateDataKeyWithoutPlaintextTransferHandler
from alibabacloud_kms_kms20160120.handlers.asymmetic_decrypt_transfer_handler import AsymmetricDecryptTransferHandler
from alibabacloud_kms_kms20160120.handlers.asymmetic_encrypt_transfer_handler import AsymmetricEncryptTransferHandler
from alibabacloud_kms_kms20160120.handlers.asymmetic_sign_transfer_handler import AsymmetricSignTransferHandler
from alibabacloud_kms_kms20160120.handlers.asymmetic_verify_transfer_handler import AsymmetricVerifyTransferHandler
from alibabacloud_kms_kms20160120.handlers.decrypt_transfer_handler import DecryptTransferHandler
from alibabacloud_kms_kms20160120.handlers.encrypt_transfer_handler import EncryptTransferHandler
from alibabacloud_kms_kms20160120.handlers.generate_data_key_transfer_handler import GenerateDataKeyTransferHandler
from alibabacloud_kms_kms20160120.handlers.generate_data_key_without_plaintext_transfer_handler import \
    GenerateDataKeyWithoutPlaintextTransferHandler
from alibabacloud_kms_kms20160120.handlers.get_public_key_transfer_handler import GetPublicKeyTransferHandler
from alibabacloud_kms_kms20160120.handlers.get_secret_value_transfer_handler import GetSecretValueTransferHandler
from alibabacloud_kms_kms20160120.models import KmsConfig, KmsRuntimeOptions
from alibabacloud_kms_kms20160120.utils.consts import *


class TransferClient(OpenApiClient):

    def __init__(
            self,
            config: open_api_models.Config = None,
            kms_config: dkms_models.Config = None,
            is_use_kms_share_gateway: bool = False
    ):
        self.handlers = dict()
        self.client = None
        self.kms_config = None
        if config is None and kms_config is None:
            raise TeaException({
                'message': 'The parameter config and kms_config can not be both None'
            })
        elif config is not None and kms_config is not None:
            super(TransferClient, self).__init__(config)
            if isinstance(kms_config, KmsConfig):
                self.kms_config = kms_config
            self.client = DKmsClient(kms_config)
            self.is_use_kms_share_gateway = is_use_kms_share_gateway
            self.init_kms_transfer_handlers()
        elif config is not None and kms_config is None:
            super(TransferClient, self).__init__(config)
            self.is_use_kms_share_gateway = True
        else:
            super(TransferClient, self).__init__(open_api_models.Config(endpoint=kms_config.endpoint))
            self.client = DKmsClient(kms_config)
            self.init_kms_transfer_handlers()
            self.is_use_kms_share_gateway = False

    def init_kms_transfer_handlers(self):
        self.handlers[ASYMMETRIC_ENCRYPT_API_NAME] = \
            AsymmetricEncryptTransferHandler(self.client, ASYMMETRIC_ENCRYPT_API_NAME, self.kms_config)
        self.handlers[ASYMMETRIC_DECRYPT_API_NAME] = \
            AsymmetricDecryptTransferHandler(self.client, ASYMMETRIC_DECRYPT_API_NAME, self.kms_config)
        self.handlers[ASYMMETRIC_SIGN_API_NAME] = \
            AsymmetricSignTransferHandler(self.client, ASYMMETRIC_SIGN_API_NAME, self.kms_config)
        self.handlers[ASYMMETRIC_VERIFY_API_NAME] = \
            AsymmetricVerifyTransferHandler(self.client, ASYMMETRIC_VERIFY_API_NAME, self.kms_config)
        self.handlers[GET_PUBLIC_KEY_API_NAME] = \
            GetPublicKeyTransferHandler(self.client, GET_PUBLIC_KEY_API_NAME, self.kms_config)
        self.handlers[GET_SECRET_VALUE_API_NAME] = \
            GetSecretValueTransferHandler(self.client, GET_SECRET_VALUE_API_NAME, self.kms_config)
        if self.kms_config and self.kms_config.force_low_version_crypto_transfer:
            self.handlers[ENCRYPT_API_NAME] = EncryptTransferHandler(self.client, ENCRYPT_API_NAME, self.kms_config)
            self.handlers[DECRYPT_API_NAME] = DecryptTransferHandler(self.client, DECRYPT_API_NAME, self.kms_config)
            self.handlers[GENERATE_DATA_KEY_API_NAME] = \
                GenerateDataKeyTransferHandler(self.client, GENERATE_DATA_KEY_API_NAME, self.kms_config)
            self.handlers[GENERATE_DATA_KEY_WITHOUT_PLAINTEXT_API_NAME] = \
                GenerateDataKeyWithoutPlaintextTransferHandler(self.client,
                                                               GENERATE_DATA_KEY_WITHOUT_PLAINTEXT_API_NAME,
                                                               self.kms_config)
        else:
            self.handlers[ENCRYPT_API_NAME] = AdvanceEncryptTransferHandler(self.client, ENCRYPT_API_NAME,
                                                                            self.kms_config)
            self.handlers[DECRYPT_API_NAME] = AdvanceDecryptTransferHandler(self.client, DECRYPT_API_NAME,
                                                                            self.kms_config)
            self.handlers[GENERATE_DATA_KEY_API_NAME] = \
                AdvanceGenerateDataKeyTransferHandler(self.client, GENERATE_DATA_KEY_API_NAME, self.kms_config)
            self.handlers[GENERATE_DATA_KEY_WITHOUT_PLAINTEXT_API_NAME] = \
                AdvanceGenerateDataKeyWithoutPlaintextTransferHandler(self.client,
                                                                      GENERATE_DATA_KEY_WITHOUT_PLAINTEXT_API_NAME,
                                                                      self.kms_config)

    def judge_call_default_kms(self, runtime: KmsRuntimeOptions, action: str):
        if runtime.is_use_kms_share_gateway is not None:
            return runtime.is_use_kms_share_gateway
        if self.kms_config is not None and self.kms_config.default_kms_api_names is not None and \
                action in self.kms_config.default_kms_api_names:
            return True
        return self.is_use_kms_share_gateway

    def call_api(
            self,
            params: open_api_models.Params,
            request: open_api_models.OpenApiRequest,
            runtime: util_models.RuntimeOptions,
    ) -> dict:
        if not isinstance(runtime, KmsRuntimeOptions):
            kms_runtime = KmsRuntimeOptions().from_map(runtime.to_map())
        else:
            kms_runtime = runtime
        if self.judge_call_default_kms(kms_runtime, params.action):
            return super(TransferClient, self).call_api(params, request, kms_runtime)
        if self.handlers.__contains__(params.action):
            return self.handlers.get(params.action).handler_kms_request_with_options(request, kms_runtime)
        else:
            return super(TransferClient, self).call_api(params, request, kms_runtime)

    def asymmetric_decrypt_with_options(
            self,
            request: kms_20160120_models.AsymmetricDecryptRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        return super(TransferClient, self).asymmetric_decrypt_with_options(request, runtime)

    def asymmetric_decrypt(
            self,
            request: kms_20160120_models.AsymmetricDecryptRequest
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_decrypt_with_options(request, runtime)

    def asymmetric_encrypt_with_options(
            self,
            request: kms_20160120_models.AsymmetricEncryptRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        return super(TransferClient, self).asymmetric_encrypt_with_options(request, runtime)

    def asymmetric_encrypt(
            self,
            request: kms_20160120_models.AsymmetricEncryptRequest
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_encrypt_with_options(request, runtime)

    def asymmetric_sign_with_options(
            self,
            request: kms_20160120_models.AsymmetricSignRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.AsymmetricSignResponse:
        return super(TransferClient, self).asymmetric_sign_with_options(request, runtime)

    def asymmetric_sign(
            self,
            request: kms_20160120_models.AsymmetricSignRequest
    ) -> kms_20160120_models.AsymmetricSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_sign_with_options(request, runtime)

    def asymmetric_verify_with_options(
            self,
            request: kms_20160120_models.AsymmetricVerifyRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        return super(TransferClient, self).asymmetric_verify_with_options(request, runtime)

    def asymmetric_verify(
            self,
            request: kms_20160120_models.AsymmetricVerifyRequest
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_verify_with_options(request, runtime)

    def decrypt_with_options(
            self,
            request: kms_20160120_models.DecryptRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.DecryptResponse:
        return super(TransferClient, self).decrypt_with_options(request, runtime)

    def decrypt(
            self,
            request: kms_20160120_models.DecryptRequest
    ) -> kms_20160120_models.DecryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    def encrypt_with_options(
            self,
            request: kms_20160120_models.EncryptRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.EncryptResponse:
        return super(TransferClient, self).encrypt_with_options(request, runtime)

    def encrypt(
            self,
            request: kms_20160120_models.EncryptRequest
    ) -> kms_20160120_models.EncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    def generate_data_key_with_options(
            self,
            request: kms_20160120_models.GenerateDataKeyRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        return super(TransferClient, self).generate_data_key_with_options(request, runtime)

    def generate_data_key(
            self,
            request: kms_20160120_models.GenerateDataKeyRequest
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_with_options(request, runtime)

    def get_public_key_with_options(
            self,
            request: kms_20160120_models.GetPublicKeyRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.GetPublicKeyResponse:
        return super(TransferClient, self).get_public_key_with_options(request, runtime)

    def get_public_key(
            self,
            request: kms_20160120_models.GetPublicKeyRequest
    ) -> kms_20160120_models.GetPublicKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_public_key_with_options(request, runtime)

    def get_secret_value_with_options(
            self,
            request: kms_20160120_models.GetSecretValueRequest,
            runtime: util_models.RuntimeOptions
    ) -> kms_20160120_models.GetSecretValueResponse:
        return super(TransferClient, self).get_secret_value_with_options(request, runtime)

    def get_secret_value(
            self,
            request: kms_20160120_models.GetSecretValueRequest
    ) -> kms_20160120_models.GetSecretValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)
