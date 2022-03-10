# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.rest import HttpRequest

from .._vendor import _format_url_section

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_put_array_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put External Resource as an Array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as an Array to put. Default value is
     None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as an Array to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = [
                {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "tags": {
                        "str": "str"  # Optional. A set of tags. Dictionary of
                          :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            ]
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/array"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_get_array_request(**kwargs: Any) -> HttpRequest:
    """Get External Resource as an Array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == [
                {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "properties": {
                        "p.name": "str",  # Optional.
                        "provisioningState": "str",  # Optional.
                        "provisioningStateValues": "str",  # Optional. Possible
                          values include: "Succeeded", "Failed", "canceled", "Accepted",
                          "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
                          "OK".
                        "type": "str"  # Optional.
                    },
                    "tags": {
                        "str": "str"  # Optional. A set of tags. Dictionary of
                          :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            ]
    """

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/array"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_put_wrapped_array_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as an Array to put. Default value is
     None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as an Array to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = [
                {
                    "value": "str"  # Optional. the product value.
                }
            ]
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/wrappedarray"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_get_wrapped_array_request(**kwargs: Any) -> HttpRequest:
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == [
                {
                    "property": {
                        "value": "str"  # Optional. the product value.
                    }
                }
            ]
    """

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/wrappedarray"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_put_dictionary_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put External Resource as a Dictionary.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as a Dictionary to put. Default value is
     None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as a Dictionary to put. Default value is
     None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "str": {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "properties": {
                        "p.name": "str",  # Optional.
                        "provisioningState": "str",  # Optional.
                        "provisioningStateValues": "str",  # Optional. Possible
                          values include: "Succeeded", "Failed", "canceled", "Accepted",
                          "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
                          "OK".
                        "type": "str"  # Optional.
                    },
                    "tags": {
                        "str": "str"  # Optional. A set of tags. Dictionary of
                          :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/dictionary"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_get_dictionary_request(**kwargs: Any) -> HttpRequest:
    """Get External Resource as a Dictionary.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "str": {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "properties": {
                        "p.name": "str",  # Optional.
                        "provisioningState": "str",  # Optional.
                        "provisioningStateValues": "str",  # Optional. Possible
                          values include: "Succeeded", "Failed", "canceled", "Accepted",
                          "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
                          "OK".
                        "type": "str"  # Optional.
                    },
                    "tags": {
                        "str": "str"  # Optional. A set of tags. Dictionary of
                          :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/dictionary"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_put_resource_collection_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put External Resource as a ResourceCollection.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. External Resource as a ResourceCollection to put. Default
     value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). External Resource as a ResourceCollection to put. Default
     value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "arrayofresources": [
                    {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional.
                            "provisioningState": "str",  # Optional.
                            "provisioningStateValues": "str",  # Optional.
                              Possible values include: "Succeeded", "Failed", "canceled",
                              "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting",
                              "Deleted", "OK".
                            "type": "str"  # Optional.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary
                              of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                ],
                "dictionaryofresources": {
                    "str": {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional. Dictionary of
                              :code:`<FlattenedProduct>`.
                            "provisioningState": "str",  # Optional. Dictionary
                              of :code:`<FlattenedProduct>`.
                            "provisioningStateValues": "str",  # Optional.
                              Possible values include: "Succeeded", "Failed", "canceled",
                              "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting",
                              "Deleted", "OK".
                            "type": "str"  # Optional. Dictionary of
                              :code:`<FlattenedProduct>`.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary
                              of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                },
                "productresource": {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "properties": {
                        "p.name": "str",  # Optional. Flattened product.
                        "provisioningState": "str",  # Optional. Flattened product.
                        "provisioningStateValues": "str",  # Optional. Possible
                          values include: "Succeeded", "Failed", "canceled", "Accepted",
                          "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
                          "OK".
                        "type": "str"  # Optional. Flattened product.
                    },
                    "tags": {
                        "str": "str"  # Optional. A set of tags. Dictionary of
                          :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/resourcecollection"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_get_resource_collection_request(**kwargs: Any) -> HttpRequest:
    """Get External Resource as a ResourceCollection.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

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
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional.
                            "provisioningState": "str",  # Optional.
                            "provisioningStateValues": "str",  # Optional.
                              Possible values include: "Succeeded", "Failed", "canceled",
                              "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting",
                              "Deleted", "OK".
                            "type": "str"  # Optional.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary
                              of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                ],
                "dictionaryofresources": {
                    "str": {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional. Dictionary of
                              :code:`<FlattenedProduct>`.
                            "provisioningState": "str",  # Optional. Dictionary
                              of :code:`<FlattenedProduct>`.
                            "provisioningStateValues": "str",  # Optional.
                              Possible values include: "Succeeded", "Failed", "canceled",
                              "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting",
                              "Deleted", "OK".
                            "type": "str"  # Optional. Dictionary of
                              :code:`<FlattenedProduct>`.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary
                              of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                },
                "productresource": {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "properties": {
                        "p.name": "str",  # Optional. Flattened product.
                        "provisioningState": "str",  # Optional. Flattened product.
                        "provisioningStateValues": "str",  # Optional. Possible
                          values include: "Succeeded", "Failed", "canceled", "Accepted",
                          "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
                          "OK".
                        "type": "str"  # Optional. Flattened product.
                    },
                    "tags": {
                        "str": "str"  # Optional. A set of tags. Dictionary of
                          :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/resourcecollection"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_put_simple_product_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple body product to put. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple body product to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Required. Unique identifier representing a
                  specific product for a given latitude & longitude. For example, uberX in San
                  Francisco will have a different product_id than uberX in Los Angeles.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Has constant value: "Large".
                    "max_product_display_name": "str",  # Required. Display name of
                      product.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }

            # response body for status code(s): 200
            response.json() == {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Required. Unique identifier representing a
                  specific product for a given latitude & longitude. For example, uberX in San
                  Francisco will have a different product_id than uberX in Los Angeles.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Has constant value: "Large".
                    "max_product_display_name": "str",  # Required. Display name of
                      product.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/customFlattening"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_post_flattened_simple_product_request(
    *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Put Flattened Simple Product with client flattening true on the parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple body product to post. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple body product to post. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Required. Unique identifier representing a
                  specific product for a given latitude & longitude. For example, uberX in San
                  Francisco will have a different product_id than uberX in Los Angeles.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Has constant value: "Large".
                    "max_product_display_name": "str",  # Required. Display name of
                      product.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }

            # response body for status code(s): 200
            response.json() == {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Required. Unique identifier representing a
                  specific product for a given latitude & longitude. For example, uberX in San
                  Francisco will have a different product_id than uberX in Los Angeles.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Has constant value: "Large".
                    "max_product_display_name": "str",  # Required. Display name of
                      product.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/customFlattening"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_put_simple_product_with_grouping_request(
    name: str, *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param name: Product name with value 'groupproduct'.
    :type name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple body product to put. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple body product to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Required. Unique identifier representing a
                  specific product for a given latitude & longitude. For example, uberX in San
                  Francisco will have a different product_id than uberX in Los Angeles.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Has constant value: "Large".
                    "max_product_display_name": "str",  # Required. Display name of
                      product.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }

            # response body for status code(s): 200
            response.json() == {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Required. Unique identifier representing a
                  specific product for a given latitude & longitude. For example, uberX in San
                  Francisco will have a different product_id than uberX in Los Angeles.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Has constant value: "Large".
                    "max_product_display_name": "str",  # Required. Display name of
                      product.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/model-flatten/customFlattening/parametergrouping/{name}/"
    path_format_arguments = {
        "name": _SERIALIZER.url("name", name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)
