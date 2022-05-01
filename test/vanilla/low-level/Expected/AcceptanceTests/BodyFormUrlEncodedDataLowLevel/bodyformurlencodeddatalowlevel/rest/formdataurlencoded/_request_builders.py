# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._vendor import _format_url_section

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_update_pet_with_form_request(
    pet_id,  # type: int
    data=None,  # type: Optional[Dict[str, Any]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Updates a pet in the store with form data.

    Updates a pet in the store with form data.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param pet_id: ID of pet that needs to be updated. Required.
    :type pet_id: int
    :param data: Multipart input for form encoded data. Default value is None.
    :type data: dict[str, any]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            data = {
                "str": {}  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    # Construct URL
    _url = "/formsdataurlencoded/pet/add/{petId}"
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'int'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        data=data,
        **kwargs
    )


def build_partial_constant_body_request(
    data=None,  # type: Optional[Dict[str, Any]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
    'foo', service: 'bar' } to pass the test.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param data: Multipart input for form encoded data. Default value is None.
    :type data: dict[str, any]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            data = {
                "str": {}  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    # Construct URL
    _url = "/formsdataurlencoded/partialConstantBody"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        data=data,
        **kwargs
    )
