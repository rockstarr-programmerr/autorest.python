# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

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
    build_parameter_grouping_post_multi_param_groups_request,
    build_parameter_grouping_post_optional_request,
    build_parameter_grouping_post_required_request,
    build_parameter_grouping_post_reserved_words_request,
    build_parameter_grouping_post_shared_parameter_group_object_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ParameterGroupingOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azureparametergroupingversiontolerant.aio.AutoRestParameterGroupingTestService`'s
        :attr:`parameter_grouping` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def post_required(  # pylint: disable=inconsistent-return-statements
        self, path: str, body: int, *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs: Any
    ) -> None:
        """Post a bunch of required parameters grouped.

        :param path: Path parameter.
        :type path: str
        :param body:
        :type body: int
        :keyword custom_header:  Default value is None.
        :paramtype custom_header: str
        :keyword query: Query parameter with default. Default value is 30.
        :paramtype query: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = body

        request = build_parameter_grouping_post_required_request(
            path=path,
            content_type=content_type,
            json=_json,
            custom_header=custom_header,
            query=query,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def post_optional(  # pylint: disable=inconsistent-return-statements
        self, *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs: Any
    ) -> None:
        """Post a bunch of optional parameters grouped.

        :keyword custom_header:  Default value is None.
        :paramtype custom_header: str
        :keyword query: Query parameter with default. Default value is 30.
        :paramtype query: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_optional_request(
            custom_header=custom_header,
            query=query,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def post_reserved_words(  # pylint: disable=inconsistent-return-statements
        self, *, from_parameter: Optional[str] = None, accept_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Post a grouped parameters with reserved words.

        :keyword from_parameter: 'from' is a reserved word. Pass in 'bob' to pass. Default value is
         None.
        :paramtype from_parameter: str
        :keyword accept_parameter: 'accept' is a reserved word. Pass in 'yes' to pass. Default value is
         None.
        :paramtype accept_parameter: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_reserved_words_request(
            from_parameter=from_parameter,
            accept_parameter=accept_parameter,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def post_multi_param_groups(  # pylint: disable=inconsistent-return-statements
        self,
        *,
        header_one: Optional[str] = None,
        query_one: Optional[int] = 30,
        header_two: Optional[str] = None,
        query_two: Optional[int] = 30,
        **kwargs: Any
    ) -> None:
        """Post parameters from multiple different parameter groups.

        :keyword header_one:  Default value is None.
        :paramtype header_one: str
        :keyword query_one: Query parameter with default. Default value is 30.
        :paramtype query_one: int
        :keyword header_two:  Default value is None.
        :paramtype header_two: str
        :keyword query_two: Query parameter with default. Default value is 30.
        :paramtype query_two: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_multi_param_groups_request(
            header_one=header_one,
            query_one=query_one,
            header_two=header_two,
            query_two=query_two,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def post_shared_parameter_group_object(  # pylint: disable=inconsistent-return-statements
        self, *, header_one: Optional[str] = None, query_one: Optional[int] = 30, **kwargs: Any
    ) -> None:
        """Post parameters with a shared parameter group object.

        :keyword header_one:  Default value is None.
        :paramtype header_one: str
        :keyword query_one: Query parameter with default. Default value is 30.
        :paramtype query_one: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_shared_parameter_group_object_request(
            header_one=header_one,
            query_one=query_one,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
