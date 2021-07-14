# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
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

from ... import models as _models
from ...rest import basic as rest_basic

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class BasicOperations:
    """BasicOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplexversiontolerant.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_valid(self, **kwargs: Any) -> Any:
        """Get complex type {id: 2, name: 'abc', color: 'YELLOW'}.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON object, or the result of cls(response)
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "color": "str (optional)",
                    "id": "int (optional)",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_basic.build_get_valid_request(
            template_url=self.get_valid.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/basic/valid"}  # type: ignore

    @distributed_trace_async
    async def put_valid(self, complex_body: Any, **kwargs: Any) -> None:
        """Please put {id: 2, name: 'abc', color: 'Magenta'}.

        :param complex_body: Please put {id: 2, name: 'abc', color: 'Magenta'}.
        :type complex_body: Any
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your `json` input.
                complex_body = {
                    "color": "str (optional)",
                    "id": "int (optional)",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(complex_body, "object")

        request = rest_basic.build_put_valid_request(
            content_type=content_type,
            json=json,
            template_url=self.put_valid.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/basic/valid"}  # type: ignore

    @distributed_trace_async
    async def get_invalid(self, **kwargs: Any) -> Any:
        """Get a basic complex type that is invalid for the local strong type.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON object, or the result of cls(response)
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "color": "str (optional)",
                    "id": "int (optional)",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_basic.build_get_invalid_request(
            template_url=self.get_invalid.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid.metadata = {"url": "/complex/basic/invalid"}  # type: ignore

    @distributed_trace_async
    async def get_empty(self, **kwargs: Any) -> Any:
        """Get a basic complex type that is empty.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON object, or the result of cls(response)
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "color": "str (optional)",
                    "id": "int (optional)",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_basic.build_get_empty_request(
            template_url=self.get_empty.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_empty.metadata = {"url": "/complex/basic/empty"}  # type: ignore

    @distributed_trace_async
    async def get_null(self, **kwargs: Any) -> Any:
        """Get a basic complex type whose properties are null.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON object, or the result of cls(response)
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "color": "str (optional)",
                    "id": "int (optional)",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_basic.build_get_null_request(
            template_url=self.get_null.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/complex/basic/null"}  # type: ignore

    @distributed_trace_async
    async def get_not_provided(self, **kwargs: Any) -> Any:
        """Get a basic complex type while the server doesn't provide a response payload.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON object, or the result of cls(response)
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "color": "str (optional)",
                    "id": "int (optional)",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_basic.build_get_not_provided_request(
            template_url=self.get_not_provided.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_not_provided.metadata = {"url": "/complex/basic/notprovided"}  # type: ignore
