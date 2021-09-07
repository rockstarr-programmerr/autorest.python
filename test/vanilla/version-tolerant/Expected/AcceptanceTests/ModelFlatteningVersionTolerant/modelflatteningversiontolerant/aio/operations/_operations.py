# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._operations import (
    build_get_array_request,
    build_get_dictionary_request,
    build_get_resource_collection_request,
    build_get_wrapped_array_request,
    build_post_flattened_simple_product_request,
    build_put_array_request,
    build_put_dictionary_request,
    build_put_resource_collection_request,
    build_put_simple_product_request,
    build_put_simple_product_with_grouping_request,
    build_put_wrapped_array_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestResourceFlatteningTestServiceOperationsMixin:
    @distributed_trace_async
    async def put_array(self, resource_array: Optional[List[Any]] = None, **kwargs: Any) -> None:
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[Any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_array = [
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
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_array is not None:
            json = resource_array
        else:
            json = None

        request = build_put_array_request(
            content_type=content_type,
            json=json,
            template_url=self.put_array.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace_async
    async def get_array(self, **kwargs: Any) -> List[Any]:
        """Get External Resource as an Array.

        :return: list of JSON object
        :rtype: list[Any]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == [
                    {
                        "id": "str (optional)",
                        "location": "str (optional)",
                        "name": "str (optional)",
                        "properties": {
                            "p.name": "str (optional)",
                            "provisioningState": "str (optional)",
                            "provisioningStateValues": "str (optional)",
                            "type": "str (optional)"
                        },
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                ]
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List[Any]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_array_request(
            template_url=self.get_array.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace_async
    async def put_wrapped_array(self, resource_array: Optional[List[Any]] = None, **kwargs: Any) -> None:
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[Any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_array = [
                    {
                        "value": "str (optional)"
                    }
                ]
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_array is not None:
            json = resource_array
        else:
            json = None

        request = build_put_wrapped_array_request(
            content_type=content_type,
            json=json,
            template_url=self.put_wrapped_array.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace_async
    async def get_wrapped_array(self, **kwargs: Any) -> List[Any]:
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :return: list of JSON object
        :rtype: list[Any]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == [
                    {
                        "property": {
                            "value": "str (optional)"
                        }
                    }
                ]
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List[Any]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_wrapped_array_request(
            template_url=self.get_wrapped_array.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace_async
    async def put_dictionary(self, resource_dictionary: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put.
        :type resource_dictionary: dict[str, Any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_dictionary = {
                    "str": {
                        "id": "str (optional)",
                        "location": "str (optional)",
                        "name": "str (optional)",
                        "properties": {
                            "p.name": "str (optional)",
                            "provisioningState": "str (optional)",
                            "provisioningStateValues": "str (optional)",
                            "type": "str (optional)"
                        },
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_dictionary is not None:
            json = resource_dictionary
        else:
            json = None

        request = build_put_dictionary_request(
            content_type=content_type,
            json=json,
            template_url=self.put_dictionary.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace_async
    async def get_dictionary(self, **kwargs: Any) -> Dict[str, Any]:
        """Get External Resource as a Dictionary.

        :return: dict mapping str to JSON object
        :rtype: dict[str, Any]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "str": {
                        "id": "str (optional)",
                        "location": "str (optional)",
                        "name": "str (optional)",
                        "properties": {
                            "p.name": "str (optional)",
                            "provisioningState": "str (optional)",
                            "provisioningStateValues": "str (optional)",
                            "type": "str (optional)"
                        },
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, Any]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_dictionary_request(
            template_url=self.get_dictionary.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace_async
    async def put_resource_collection(self, resource_complex_object: Any = None, **kwargs: Any) -> None:
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a ResourceCollection to put.
        :type resource_complex_object: Any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_complex_object = {
                    "arrayofresources": [
                        {
                            "id": "str (optional)",
                            "location": "str (optional)",
                            "name": "str (optional)",
                            "properties": {
                                "p.name": "str (optional)",
                                "provisioningState": "str (optional)",
                                "provisioningStateValues": "str (optional)",
                                "type": "str (optional)"
                            },
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
                            "properties": {
                                "p.name": "str (optional)",
                                "provisioningState": "str (optional)",
                                "provisioningStateValues": "str (optional)",
                                "type": "str (optional)"
                            },
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
                        "properties": {
                            "p.name": "str (optional)",
                            "provisioningState": "str (optional)",
                            "provisioningStateValues": "str (optional)",
                            "type": "str (optional)"
                        },
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_complex_object is not None:
            json = resource_complex_object
        else:
            json = None

        request = build_put_resource_collection_request(
            content_type=content_type,
            json=json,
            template_url=self.put_resource_collection.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace_async
    async def get_resource_collection(self, **kwargs: Any) -> Any:
        """Get External Resource as a ResourceCollection.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "arrayofresources": [
                        {
                            "id": "str (optional)",
                            "location": "str (optional)",
                            "name": "str (optional)",
                            "properties": {
                                "p.name": "str (optional)",
                                "provisioningState": "str (optional)",
                                "provisioningStateValues": "str (optional)",
                                "type": "str (optional)"
                            },
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
                            "properties": {
                                "p.name": "str (optional)",
                                "provisioningState": "str (optional)",
                                "provisioningStateValues": "str (optional)",
                                "type": "str (optional)"
                            },
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
                        "properties": {
                            "p.name": "str (optional)",
                            "provisioningState": "str (optional)",
                            "provisioningStateValues": "str (optional)",
                            "type": "str (optional)"
                        },
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_resource_collection_request(
            template_url=self.get_resource_collection.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace_async
    async def put_simple_product(self, simple_body_product: Any = None, **kwargs: Any) -> Any:
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put.
        :type simple_body_product: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                simple_body_product = {
                    "base_product_description": "str (optional)",
                    "base_product_id": "str",
                    "details": {
                        "max_product_capacity": "str",
                        "max_product_display_name": "str",
                        "max_product_image": {
                            "@odata.value": "str (optional)",
                            "generic_value": "str (optional)"
                        }
                    }
                }

                # response body for status code(s): 200
                response.json() == {
                    "base_product_description": "str (optional)",
                    "base_product_id": "str",
                    "details": {
                        "max_product_capacity": "str",
                        "max_product_display_name": "str",
                        "max_product_image": {
                            "@odata.value": "str (optional)",
                            "generic_value": "str (optional)"
                        }
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if simple_body_product is not None:
            json = simple_body_product
        else:
            json = None

        request = build_put_simple_product_request(
            content_type=content_type,
            json=json,
            template_url=self.put_simple_product.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace_async
    async def post_flattened_simple_product(self, simple_body_product: Any = None, **kwargs: Any) -> Any:
        """Put Flattened Simple Product with client flattening true on the parameter.

        :param simple_body_product: Simple body product to post.
        :type simple_body_product: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                simple_body_product = {
                    "base_product_description": "str (optional)",
                    "base_product_id": "str",
                    "details": {
                        "max_product_capacity": "str",
                        "max_product_display_name": "str",
                        "max_product_image": {
                            "@odata.value": "str (optional)",
                            "generic_value": "str (optional)"
                        }
                    }
                }

                # response body for status code(s): 200
                response.json() == {
                    "base_product_description": "str (optional)",
                    "base_product_id": "str",
                    "details": {
                        "max_product_capacity": "str",
                        "max_product_display_name": "str",
                        "max_product_image": {
                            "@odata.value": "str (optional)",
                            "generic_value": "str (optional)"
                        }
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if simple_body_product is not None:
            json = simple_body_product
        else:
            json = None

        request = build_post_flattened_simple_product_request(
            content_type=content_type,
            json=json,
            template_url=self.post_flattened_simple_product.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_flattened_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace_async
    async def put_simple_product_with_grouping(self, name: str, simple_body_product: Any = None, **kwargs: Any) -> Any:
        """Put Simple Product with client flattening true on the model.

        :param name: Product name with value 'groupproduct'.
        :type name: str
        :param simple_body_product: Simple body product to put.
        :type simple_body_product: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                simple_body_product = {
                    "base_product_description": "str (optional)",
                    "base_product_id": "str",
                    "details": {
                        "max_product_capacity": "str",
                        "max_product_display_name": "str",
                        "max_product_image": {
                            "@odata.value": "str (optional)",
                            "generic_value": "str (optional)"
                        }
                    }
                }

                # response body for status code(s): 200
                response.json() == {
                    "base_product_description": "str (optional)",
                    "base_product_id": "str",
                    "details": {
                        "max_product_capacity": "str",
                        "max_product_display_name": "str",
                        "max_product_image": {
                            "@odata.value": "str (optional)",
                            "generic_value": "str (optional)"
                        }
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if simple_body_product is not None:
            json = simple_body_product
        else:
            json = None

        request = build_put_simple_product_with_grouping_request(
            name=name,
            content_type=content_type,
            json=json,
            template_url=self.put_simple_product_with_grouping.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product_with_grouping.metadata = {"url": "/model-flatten/customFlattening/parametergrouping/{name}/"}  # type: ignore