# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, Optional, TypeVar, Union, cast, overload

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
from azure.core.utils import case_insensitive_dict

from ..._operations._operations import (
    build_analyze_body_no_accept_header_request,
    build_analyze_body_request,
    build_binary_body_with_three_content_types_request,
    build_binary_body_with_two_content_types_request,
    build_content_type_with_encoding_request,
    build_put_text_and_json_body_request,
)
from .._vendor import MixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MediaTypesClientOperationsMixin(MixinABC):
    @overload
    async def analyze_body(
        self, input: Optional[JSON] = None, *, content_type: Optional[str] = "application/json", **kwargs: Any
    ) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Optional. Default value is None.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Optional. Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "source": "str"  # Optional. File source path.
                }
        """

        ...

    @overload
    async def analyze_body(
        self, input: Optional[IO] = None, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Optional. Default value is None.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Optional. Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def analyze_body(
        self, input: Optional[Union[JSON, IO]] = None, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Is either a model type or a IO type. Optional. Default value is
         None.
        :type input: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'. Optional. Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _json = input
            content_type = content_type or "application/json"

        request = build_analyze_body_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @overload
    async def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[JSON] = None, *, content_type: Optional[str] = "application/json", **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Optional. Default value is None.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Optional. Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "source": "str"  # Optional. File source path.
                }
        """

        ...

    @overload
    async def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[IO] = None, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Optional. Default value is None.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Optional. Default value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[Union[JSON, IO]] = None, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Is either a model type or a IO type. Optional. Default value is
         None.
        :type input: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'. Optional. Default value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = None
        _content = None
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _json = input
            content_type = content_type or "application/json"

        request = build_analyze_body_no_accept_header_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def content_type_with_encoding(self, input: Optional[str] = None, **kwargs: Any) -> str:
        """Pass in contentType 'text/plain; charset=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter. Optional. Default value is None.
        :type input: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _content = input

        request = build_content_type_with_encoding_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def binary_body_with_two_content_types(
        self, message: IO, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> str:
        """Binary body with two content types. Pass in of {'hello': 'world'} for the application/json
        content type, and a byte stream of 'hello, world!' for application/octet-stream.

        :param message: The payload body.
        :type message: IO
        :keyword content_type: Upload file type. Known values are: 'application/json',
         'application/octet-stream'. Optional. Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _content = message

        request = build_binary_body_with_two_content_types_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def binary_body_with_three_content_types(
        self, message: IO, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> str:
        """Binary body with three content types. Pass in string 'hello, world' with content type
        'text/plain', {'hello': world'} with content type 'application/json' and a byte string for
        'application/octet-stream'.

        :param message: The payload body.
        :type message: IO
        :keyword content_type: Upload file type. Known values are: 'application/json',
         'application/octet-stream', 'text/plain'. Optional. Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _content = message

        request = build_binary_body_with_three_content_types_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def put_text_and_json_body(self, message: str, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Body that's either text/plain or application/json.

        :param message: The payload body.
        :type message: str
        :keyword content_type: Upload file type. Known values are: 'application/json', 'text/plain'.
         Optional. Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _content = message

        request = build_put_text_and_json_body_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)
