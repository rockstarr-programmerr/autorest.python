# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, List, Optional

_SERIALIZER = Serializer()


def build_put_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as an Array.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as an Array to put.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as an Array to put.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = [
                {
                    "id": "str (optional)",
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
            ]
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/array")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get External Resource as an Array.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == [
                {
                    "id": "str (optional)",
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "p.name": "str (optional)",
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)",
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
            ]
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/array")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_wrapped_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as an Array to put.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as an Array to put.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = [
                {
                    "value": "str (optional)"
                }
            ]
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/wrappedarray")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_wrapped_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == [
                {
                    "value": "str (optional)"
                }
            ]
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/wrappedarray")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_dictionary_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a Dictionary.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as a Dictionary to put.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as a Dictionary to put.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "str": {
                    "id": "str (optional)",
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "p.name": "str (optional)",
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)",
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/dictionary")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_dictionary_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get External Resource as a Dictionary.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "str": {
                    "id": "str (optional)",
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "p.name": "str (optional)",
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)",
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
            }
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/dictionary")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_resource_collection_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a ResourceCollection.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as a ResourceCollection to put.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as a ResourceCollection to put.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "arrayofresources": [
                    {
                        "id": "str (optional)",
                        "location": "str (optional)",
                        "name": "str (optional)",
                        "p.name": "str (optional)",
                        "provisioningState": "str (optional)",
                        "provisioningStateValues": "str (optional)",
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                ],
                "dictionaryofresources": {
                    "str": {
                        "id": "str (optional)",
                        "location": "str (optional)",
                        "name": "str (optional)",
                        "p.name": "str (optional)",
                        "provisioningState": "str (optional)",
                        "provisioningStateValues": "str (optional)",
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                },
                "productresource": {
                    "id": "str (optional)",
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "p.name": "str (optional)",
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)",
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/resourcecollection")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_resource_collection_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get External Resource as a ResourceCollection.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "arrayofresources": [
                    {
                        "id": "str (optional)",
                        "location": "str (optional)",
                        "name": "str (optional)",
                        "p.name": "str (optional)",
                        "provisioningState": "str (optional)",
                        "provisioningStateValues": "str (optional)",
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                ],
                "dictionaryofresources": {
                    "str": {
                        "id": "str (optional)",
                        "location": "str (optional)",
                        "name": "str (optional)",
                        "p.name": "str (optional)",
                        "provisioningState": "str (optional)",
                        "provisioningStateValues": "str (optional)",
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                },
                "productresource": {
                    "id": "str (optional)",
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "p.name": "str (optional)",
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)",
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
            }
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/resourcecollection")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_simple_product_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple body product to put.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple body product to put.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "@odata.value": "str (optional)",
                "base_product_description": "str (optional)",
                "base_product_id": "str",
                "generic_value": "str (optional)",
                "max_product_capacity": "str (optional)",
                "max_product_display_name": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "@odata.value": "str (optional)",
                "base_product_description": "str (optional)",
                "base_product_id": "str",
                "generic_value": "str (optional)",
                "max_product_capacity": "str (optional)",
                "max_product_display_name": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/customFlattening")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_post_flattened_simple_product_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Flattened Simple Product with client flattening true on the parameter.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple body product to post.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple body product to post.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "@odata.value": "str (optional)",
                "base_product_description": "str (optional)",
                "base_product_id": "str",
                "generic_value": "str (optional)",
                "max_product_capacity": "str (optional)",
                "max_product_display_name": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "@odata.value": "str (optional)",
                "base_product_description": "str (optional)",
                "base_product_id": "str",
                "generic_value": "str (optional)",
                "max_product_capacity": "str (optional)",
                "max_product_display_name": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/customFlattening")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)


def build_put_simple_product_with_grouping_request(
    name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param name: Product name with value 'groupproduct'.
    :type name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple body product to put.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple body product to put.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "@odata.value": "str (optional)",
                "base_product_description": "str (optional)",
                "base_product_id": "str",
                "generic_value": "str (optional)",
                "max_product_capacity": "str (optional)",
                "max_product_display_name": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "@odata.value": "str (optional)",
                "base_product_description": "str (optional)",
                "base_product_id": "str",
                "generic_value": "str (optional)",
                "max_product_capacity": "str (optional)",
                "max_product_display_name": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/customFlattening/parametergrouping/{name}/")
    path_format_arguments = {
        "name": _SERIALIZER.url("name", name, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)
