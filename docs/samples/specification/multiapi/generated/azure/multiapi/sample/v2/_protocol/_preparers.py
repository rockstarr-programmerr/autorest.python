# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Optional

_SERIALIZER = Serializer()

import xml.etree.ElementTree as ET
def _request(
    method,
    url,
    params=None,
    headers=None,
    content=None,
    form_content=None,
    stream_content=None,
):
    request = HttpRequest(method, url, headers=headers)

    if params:
        request.format_parameters(params)

    if content is not None:
        content_type = request.headers.get("Content-Type")
        if isinstance(content, ET.Element):
            request.set_xml_body(content)
        # https://github.com/Azure/azure-sdk-for-python/issues/12137
        # A string is valid JSON, make the difference between text
        # and a plain JSON string.
        # Content-Type is a good indicator of intent from user
        elif content_type and content_type.startswith("text/"):
            request.set_text_body(content)
        else:
            try:
                request.set_json_body(content)
            except TypeError:
                request.data = content

    if form_content:
        request.set_formdata_body(form_content)
    elif stream_content:
        request.set_streamed_data_body(stream_content)

    return request


def prepare_test_one_request(
    id,  # type: int
    message=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testOneEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    if message is not None:
        query_parameters['message'] = _SERIALIZER.query("message", message, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return _request("PUT", url, query_parameters, header_parameters)


def prepare_test_different_calls_request(
    greeting_in_english,  # type: str
    greeting_in_chinese=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    if greeting_in_chinese is not None:
        header_parameters['greetingInChinese'] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return _request("GET", url, query_parameters, header_parameters)


def prepare_operationgroupone_test_two_request(
    body=None,  # type: Optional["_models.ModelTwo"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0.0"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/one/testTwoEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs['content'] = body

    return _request("GET", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_operationgroupone_test_three_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/one/testThreeEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return _request("PUT", url, query_parameters, header_parameters)


def prepare_operationgrouptwo_test_four_request(
    parameter_one,  # type: bool
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/two/testFourEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['parameterOne'] = _SERIALIZER.query("parameter_one", parameter_one, 'bool')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return _request("POST", url, query_parameters, header_parameters)
