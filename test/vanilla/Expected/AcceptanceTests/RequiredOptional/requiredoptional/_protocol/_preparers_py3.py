# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, List, Optional

from azure.core.pipeline.transport import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section
from msrest import Serializer

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


def prepare_implicit_get_required_path_request(path_parameter: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/required/path/{pathParameter}")
    path_format_arguments = {
        "pathParameter": _SERIALIZER.url("path_parameter", path_parameter, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_implicit_put_optional_query_request(query_parameter: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query_parameter is not None:
        query_parameters["queryParameter"] = _SERIALIZER.query("query_parameter", query_parameter, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("PUT", url, query_parameters, header_parameters)


def prepare_implicit_put_optional_header_request(query_parameter: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if query_parameter is not None:
        header_parameters["queryParameter"] = _SERIALIZER.header("query_parameter", query_parameter, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("PUT", url, query_parameters, header_parameters)


def prepare_implicit_put_optional_body_request(body: Optional[str] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("PUT", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_implicit_put_optional_binary_body_request(body: Optional[IO] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/binary-body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["stream_content"] = body

    return _request("PUT", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_implicit_get_required_global_path_request(required_global_path: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/required/path/{required-global-path}")
    path_format_arguments = {
        "required-global-path": _SERIALIZER.url("required_global_path", required_global_path, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_implicit_get_required_global_query_request(required_global_query: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/required/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["required-global-query"] = _SERIALIZER.query("required_global_query", required_global_query, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_implicit_get_optional_global_query_request(
    optional_global_query: Optional[int] = None, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/optional/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if optional_global_query is not None:
        query_parameters["optional-global-query"] = _SERIALIZER.query(
            "optional_global_query", optional_global_query, "int"
        )

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_explicit_put_optional_binary_body_request(body: Optional[IO] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/explicit/optional/binary-body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["stream_content"] = body

    return _request("PUT", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_put_required_binary_body_request(body: IO, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/explicit/required/binary-body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["stream_content"] = body

    return _request("PUT", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_integer_parameter_request(body: int, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/integer/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_integer_parameter_request(body: Optional[int] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/integer/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_integer_property_request(body: "_models.IntWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/integer/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_integer_property_request(
    body: Optional["_models.IntOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/integer/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_integer_header_request(header_parameter: int, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/integer/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_explicit_post_optional_integer_header_request(
    header_parameter: Optional[int] = None, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/integer/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_parameter is not None:
        header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_explicit_post_required_string_parameter_request(body: str, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/string/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_string_parameter_request(body: Optional[str] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/string/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_string_property_request(body: "_models.StringWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/string/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_string_property_request(
    body: Optional["_models.StringOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/string/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_string_header_request(header_parameter: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/string/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_explicit_post_optional_string_header_request(body_parameter: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/string/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if body_parameter is not None:
        header_parameters["bodyParameter"] = _SERIALIZER.header("body_parameter", body_parameter, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_explicit_post_required_class_parameter_request(body: "_models.Product", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/class/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_class_parameter_request(
    body: Optional["_models.Product"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/class/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_class_property_request(body: "_models.ClassWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/class/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_class_property_request(
    body: Optional["_models.ClassOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/class/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_array_parameter_request(body: List[str], **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/array/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_array_parameter_request(body: Optional[List[str]] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/array/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_array_property_request(body: "_models.ArrayWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/array/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_optional_array_property_request(
    body: Optional["_models.ArrayOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/array/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_explicit_post_required_array_header_request(header_parameter: List[str], **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/array/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "[str]", div=",")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_explicit_post_optional_array_header_request(
    header_parameter: Optional[List[str]] = None, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/array/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_parameter is not None:
        header_parameters["headerParameter"] = _SERIALIZER.header(
            "header_parameter", header_parameter, "[str]", div=","
        )
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)