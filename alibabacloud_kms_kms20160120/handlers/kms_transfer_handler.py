# -*- coding: utf-8 -*-
import abc

from Tea.exceptions import UnretryableException, RetryError
from alibabacloud_tea_openapi import models as open_api_models

from alibabacloud_kms_kms20160120.models import KmsRuntimeOptions
from alibabacloud_kms_kms20160120.utils.kms_error_code_transfer_utils import *


def get_missing_parameter_client_exception(param_name):
    return TeaException({
        'code': MISSING_PARAMETER_ERROR_CODE,
        'message': f"The parameter {param_name} needed but no provided."
    })


def get_invalid_parameter_client_exception(param_name):
    return TeaException({
        'code': INVALID_PARAMETER_ERROR_CODE,
        'message': "The parameter  %s  is invalid." % param_name
    })


def transfer_kms_exception(e: TeaException):
    if e.code == INVALID_PARAM_ERROR_CODE:
        if e.message == INVALID_PARAM_DATE_ERROR_MESSAGE:
            return transfer_invalid_date_exception(e.data)
        elif e.message == INVALID_PARAM_AUTHORIZATION_ERROR_MESSAGE:
            return transfer_incomplete_signature_exception(e.data)
    elif e.code == UNAUTHORIZED_ERROR_CODE:
        return transfer_invalid_access_key_id_exception(e.data)
    else:
        error_message = transfer_error_message(e.code)
        error_message = error_message if error_message else e.message
        return TeaException({
            'code': e.code,
            'message': error_message,
            'data': e.data
        })


def transfer_unretryable_exception(e):
    if isinstance(e, UnretryableException):
        if 'Read timed out' in e.message or 'timeout' in e.message or isinstance(e.inner_exception, RetryError):
            return TeaException({
                'code': 'SDK.ReadTimeout',
                'message': str(e)
            })
        elif "Name or service not known" in e.message:
            return TeaException({
                'code': 'SDK.ServerUnreachable',
                'message': str(e)
            })
    return e


class KmsTransferHandler(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_client(self):
        pass

    @abc.abstractmethod
    def get_action(self):
        pass

    def handler_kms_request_with_options(
            self,
            request: open_api_models.OpenApiRequest,
            runtime: KmsRuntimeOptions
    ) -> dict:
        try:
            kms_request = self.build_kms_request(request, runtime)
            return self.transfer_response(self.call_kms(kms_request, runtime), runtime)
        except UnretryableException as e:
            if isinstance(e.inner_exception, TeaException):
                raise transfer_kms_exception(e.inner_exception)
            raise transfer_unretryable_exception(e)
        except TeaException as e:
            raise transfer_kms_exception(e)

    @abc.abstractmethod
    def build_kms_request(self, request: open_api_models.OpenApiRequest, runtime_options: KmsRuntimeOptions):
        pass

    @abc.abstractmethod
    def transfer_response(self, response, runtime_options: KmsRuntimeOptions) -> dict:
        pass

    @abc.abstractmethod
    def call_kms(self, request, runtime_options: KmsRuntimeOptions):
        pass
