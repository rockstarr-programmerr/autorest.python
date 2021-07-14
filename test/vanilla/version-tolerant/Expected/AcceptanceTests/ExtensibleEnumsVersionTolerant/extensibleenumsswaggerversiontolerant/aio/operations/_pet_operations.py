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
from ...rest import pet as rest_pet

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetOperations:
    """PetOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~extensibleenumsswaggerversiontolerant.models
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
    async def get_by_pet_id(self, pet_id: str, **kwargs: Any) -> Any:
        """get pet by id.

        :param pet_id: Pet id.
        :type pet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON object, or the result of cls(response)
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "DaysOfWeek": "str (optional). Default value is \"Friday\"",
                    "IntEnum": "str",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_pet.build_get_by_pet_id_request(
            pet_id=pet_id,
            template_url=self.get_by_pet_id.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_pet_id.metadata = {"url": "/extensibleenums/pet/{petId}"}  # type: ignore

    @distributed_trace_async
    async def add_pet(self, pet_param: Any = None, **kwargs: Any) -> Any:
        """add pet.

        :param pet_param: pet param.
        :type pet_param: Any
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON object, or the result of cls(response)
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your `json` input.
                pet_param = {
                    "DaysOfWeek": "str (optional). Default value is \"Friday\"",
                    "IntEnum": "str",
                    "name": "str (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "DaysOfWeek": "str (optional). Default value is \"Friday\"",
                    "IntEnum": "str",
                    "name": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if pet_param is not None:
            json = self._serialize.body(pet_param, "object")
        else:
            json = None

        request = rest_pet.build_add_pet_request(
            content_type=content_type,
            json=json,
            template_url=self.add_pet.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add_pet.metadata = {"url": "/extensibleenums/pet/addPet"}  # type: ignore
