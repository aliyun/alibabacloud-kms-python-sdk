# -*- coding: utf-8 -*-
import hashlib
import json


def get_sha256(context):
    hash_object = hashlib.sha256()
    hash_object.update(context)
    return hash_object.hexdigest()


def sort_and_encode(encryption_context, encoding):
    if encryption_context is None:
        return None
    encryption_context_json = json.loads(encryption_context)
    sorted_keys = sorted(encryption_context_json.keys())
    context = ""
    for key in sorted_keys:
        context = context + key + "=" + encryption_context_json.get(key) + "&"
    if context.index("&") > 0:
        context = context[:len(context) - 1]
    return get_sha256(context.encode(encoding)).encode(encoding)
