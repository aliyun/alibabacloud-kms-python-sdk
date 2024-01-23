# -*- coding: utf-8 -*-

GCM_IV_LENGTH = 12
EKT_ID_LENGTH = 36
ENCRYPT_API_NAME = "Encrypt"
ASYMMETRIC_ENCRYPT_API_NAME = "AsymmetricEncrypt"
DECRYPT_API_NAME = "Decrypt"
ASYMMETRIC_DECRYPT_API_NAME = "AsymmetricDecrypt"
ASYMMETRIC_SIGN_API_NAME = "AsymmetricSign"
ASYMMETRIC_VERIFY_API_NAME = "AsymmetricVerify"
GENERATE_DATA_KEY_API_NAME = "GenerateDataKey"
GENERATE_DATA_KEY_WITHOUT_PLAINTEXT_API_NAME = "GenerateDataKeyWithoutPlaintext"
GET_PUBLIC_KEY_API_NAME = "GetPublicKey"
GET_SECRET_VALUE_API_NAME = "GetSecretValue"
DIGEST_MESSAGE_TYPE = "DIGEST"
KMS_KEY_PAIR_AES_256 = "AES_256"
KMS_KEY_PAIR_AES_128 = "AES_128"
REQUEST_ID_KEY_NAME = "requestId"
HTTP_CODE_KEY_NAME = "httpCode"
MIGRATION_KEY_VERSION_ID_KEY = "x-kms-migrationkeyversionid"
NUMBER_OF_BYTES_AES_256 = 32
NUMBER_OF_BYTES_AES_128 = 16
MAGIC_NUM = b'$'
MAGIC_NUM_LENGTH = 1
CIPHER_VER_AND_PADDING_MODE_LENGTH = 1
ALGORITHM_LENGTH = 1
CIPHER_VER = 0
ALG_AES_GCM = b'\x02'
SDK_NAME = "alibabacloud-kms-python-sdk"
SDK_VERSION = "1.1.3"
CLIENT_USER_AGENT = SDK_NAME + "-client/" + SDK_VERSION
TRANSFER_CLIENT_USER_AGENT = SDK_NAME + "-transfer-client/" + SDK_VERSION
