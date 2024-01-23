# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

"""
setup module for alibabacloud-kms-python-sdk.

Created on 12/06/2022

@author: Alibaba Cloud SDK
"""

packages = find_packages()
NAME = "alibabacloud-kms-python-sdk"
DESCRIPTION = "Alibaba Cloud KMS Python SDK"
AUTHOR = "Alibaba Cloud SDK"
AUTHOR_EMAIL = "sdk-team@alibabacloud.com"
URL = "https://github.com/aliyun/alibabacloud-kms-python-sdk"
VERSION = "1.1.3"
REQUIRES = [
    'alibabacloud_dkms_gcs==1.0.2',
    'alibabacloud_kms20160120>=2.0.2,<3.0.0',
    'protobuf>=3.12.0,<3.20.0'
]

LONG_DESCRIPTION = ''
if os.path.exists('./README.rst'):
    with open("./README.rst", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License 2.0",
    url=URL,
    keywords=["alibabacloud", "kms", "python", "sdk"],
    packages=find_packages(exclude=["example*"]),
    include_package_data=True,
    platforms="any",
    install_requires=REQUIRES,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development"
    ],
)
