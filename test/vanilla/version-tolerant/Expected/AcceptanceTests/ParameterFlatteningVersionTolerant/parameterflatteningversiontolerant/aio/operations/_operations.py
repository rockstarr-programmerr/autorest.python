# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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

from ...operations._operations import build_availability_sets_update_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AvailabilitySetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~parameterflatteningversiontolerant.aio.AutoRestParameterFlattening`'s
        :attr:`availability_sets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def update(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, avset: str, tags: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Updates the tags for an availability set.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param avset: The name of the storage availability set. Required.
        :type avset: str
        :param tags: The tags. Required.
        :type tags: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                tags = {
                    "tags": {
                        "str": "str"  # A description about the set of tags. Required.
                    }
                }
        """

        ...

    @overload
    async def update(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, avset: str, tags: IO, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Updates the tags for an availability set.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param avset: The name of the storage availability set. Required.
        :type avset: str
        :param tags: The tags. Required.
        :type tags: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def update(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, avset: str, tags: Union[JSON, IO], **kwargs: Any
    ) -> None:
        """Updates the tags for an availability set.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param avset: The name of the storage availability set. Required.
        :type avset: str
        :param tags: The tags. Is either a model type or a IO type. Required.
        :type tags: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = None
        _content = None
        if isinstance(tags, (IO, bytes)):
            _content = tags
        else:
            _json = tags
            content_type = content_type or "application/json"

        request = build_availability_sets_update_request(
            resource_group_name=resource_group_name,
            avset=avset,
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

        if cls:
            return cls(pipeline_response, None, {})
