# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, IO, Optional, Union, overload

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from .._vendor import _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_model_request(
    mode: str,
    **kwargs: Any
) -> HttpRequest:
    """Get models that you will either return to end users as a raw body, or with a model added during
    grow up.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users. Required.
    :type mode: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/customization/model/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_post_model_request(
    mode: str,
    *,
    json: JSON,
    content_type: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
    take a model instead, and put in 'model' as mode.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users. Required.
    :type mode: str
    :keyword json: Please put {'hello': 'world!'}. Required.
    :paramtype json: JSON
    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "hello": "str"  # Required.
            }
    """

    ...

@overload
def build_post_model_request(
    mode: str,
    *,
    content: IO,
    content_type: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
    take a model instead, and put in 'model' as mode.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users. Required.
    :type mode: str
    :keyword content: Please put {'hello': 'world!'}. Required.
    :paramtype content: IO
    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    ...

def build_post_model_request(
    mode: str,
    **kwargs
) -> HttpRequest:
    """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
    take a model instead, and put in 'model' as mode.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users. Required.
    :type mode: str
    :keyword json: Please put {'hello': 'world!'}. Is either a model type or a IO type. Required.
    :paramtype json: JSON or IO
    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/customization/model/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_pages_request(
    mode: str,
    **kwargs: Any
) -> HttpRequest:
    """Get pages that you will either return to users in pages of raw bodies, or pages of models
    following growup.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users. Required.
    :type mode: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/customization/paging/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_lro_request(
    mode: str,
    **kwargs: Any
) -> HttpRequest:
    """Long running put request that will either return to end users a final payload of a raw body, or
    a final payload of a model after the SDK has grown up.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users. Required.
    :type mode: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/customization/lro/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )
