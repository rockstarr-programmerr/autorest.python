# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_upload_file_request(*args, **kwargs) -> HttpRequest:
    """You need to write a custom operation for "build_upload_file_request". Please refer to
    https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    """

    raise NotImplementedError(
        "You need to write a custom operation for 'build_upload_file_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )


def build_upload_file_via_body_request(*, content: Any, **kwargs: Any) -> HttpRequest:
    """Upload file.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). File to upload. Required. Required.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/octet-stream, application/json")

    # Construct URL
    _url = "/formdata/stream/uploadfile"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, content=content, **kwargs)


def build_upload_files_request(*args, **kwargs) -> HttpRequest:
    """You need to write a custom operation for "build_upload_files_request". Please refer to
    https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    """

    raise NotImplementedError(
        "You need to write a custom operation for 'build_upload_files_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )
