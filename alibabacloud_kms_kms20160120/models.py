from alibabacloud_tea_util import models as util_models
from openapi import models as dkms_models


class KmsConfig(dkms_models.Config):
    def __init__(
            self,
            client_key_id=None,
            private_key=None,
            endpoint=None,
            protocol=None,
            region_id=None,
            read_timeout=None,
            connect_timeout=None,
            http_proxy=None,
            https_proxy=None,
            socks_5proxy=None,
            socks_5net_work=None,
            no_proxy=None,
            max_idle_conns=None,
            user_agent=None,
            type=None,
            credential=None,
            client_key_file=None,
            client_key_content=None,
            password=None,
            default_kms_api_names=None,
            encoding=None, advance_switch=True
    ):
        super(KmsConfig, self).__init__(
            access_key_id=client_key_id,
            private_key=private_key,
            endpoint=endpoint,
            protocol=protocol,
            region_id=region_id,
            read_timeout=read_timeout,
            connect_timeout=connect_timeout,
            http_proxy=http_proxy,
            https_proxy=https_proxy,
            socks_5proxy=socks_5proxy,
            socks_5net_work=socks_5net_work,
            no_proxy=no_proxy,
            max_idle_conns=max_idle_conns,
            user_agent=user_agent,
            type=type,
            credential=credential,
            client_key_file=client_key_file,
            client_key_content=client_key_content,
            password=password
        )
        self.default_kms_api_names = default_kms_api_names
        self.encoding = encoding
        self.advance_switch = advance_switch

    def validate(self):
        pass

    def to_map(self):
        result = super(KmsConfig, self).to_map()
        if self.default_kms_api_names is not None:
            result['default_kms_api_names'] = self.default_kms_api_names
        if self.encoding is not None:
            result['encoding'] = self.encoding
        return result

    def from_map(self, m=None):
        super(KmsConfig, self).from_map(m)
        m = m or dict()
        if m.get('default_kms_api_names') is not None:
            self.default_kms_api_names = m.get('default_kms_api_names')
        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')
        return self


class KmsRuntimeOptions(util_models.RuntimeOptions):
    def __init__(
            self,
            autoretry=None,
            ignore_ssl=None,
            max_attempts=None,
            backoff_policy=None,
            backoff_period=None,
            read_timeout=None,
            connect_timeout=None,
            http_proxy=None,
            https_proxy=None,
            no_proxy=None,
            max_idle_conns=None,
            local_addr=None,
            socks_5proxy=None,
            socks_5net_work=None,
            keep_alive=None,
            key=None,
            cert=None,
            ca=None,
            is_use_kms_share_gateway=None,
            encoding=None
    ):
        super(KmsRuntimeOptions, self).__init__(
            autoretry=autoretry,
            ignore_ssl=ignore_ssl,
            max_attempts=max_attempts,
            backoff_policy=backoff_policy,
            backoff_period=backoff_period,
            read_timeout=read_timeout,
            connect_timeout=connect_timeout,
            http_proxy=http_proxy,
            https_proxy=https_proxy,
            no_proxy=no_proxy,
            max_idle_conns=max_idle_conns,
            local_addr=local_addr,
            socks_5proxy=socks_5proxy,
            socks_5net_work=socks_5net_work,
            keep_alive=keep_alive,
            key=key,
            cert=cert,
            ca=ca
        )
        self.is_use_kms_share_gateway = is_use_kms_share_gateway
        self.encoding = encoding

    def validate(self):
        pass

    def to_map(self):
        result = super(KmsRuntimeOptions, self).to_map()
        if self.is_use_kms_share_gateway is not None:
            result['is_use_kms_share_gateway'] = self.is_use_kms_share_gateway
        if self.encoding is not None:
            result['encoding'] = self.encoding
        return result

    def from_map(self, m=None):
        super(KmsRuntimeOptions, self).from_map(m)
        m = m or dict()
        if m.get('is_use_kms_share_gateway') is not None:
            self.is_use_kms_share_gateway = m.get('is_use_kms_share_gateway')
        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')
        return self
