# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

_SERIALIZER = Serializer()

# fmt: off

def build_test_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Should be a mixin operation. Put in 1 for the required parameter and have the correct api
    version of 1.0.0 to pass.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword id: An int parameter. Put in 1 to pass.
    :paramtype id: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    id = kwargs.pop('id')  # type: int

    api_version = "1.0.0"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/test')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

