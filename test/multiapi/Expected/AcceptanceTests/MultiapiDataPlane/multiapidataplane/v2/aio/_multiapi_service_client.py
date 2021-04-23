# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest, _AsyncStreamContextManager
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import MultiapiServiceClientConfiguration
from .operations import MultiapiServiceClientOperationsMixin
from .operations import OperationGroupOneOperations
from .operations import OperationGroupTwoOperations
from .. import models


class MultiapiServiceClient(MultiapiServiceClientOperationsMixin):
    """Service client for multiapi client testing.

    :ivar operation_group_one: OperationGroupOneOperations operations
    :vartype operation_group_one: multiapidataplane.v2.aio.operations.OperationGroupOneOperations
    :ivar operation_group_two: OperationGroupTwoOperations operations
    :vartype operation_group_two: multiapidataplane.v2.aio.operations.OperationGroupTwoOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param base_url: Service URL
    :type base_url: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self.operation_group_one = OperationGroupOneOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_group_two = OperationGroupTwoOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `multiapidataplane.v2.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from multiapidataplane.v2.rest import build_test_one_request
        >>> request = build_test_one_request(id, message)
        <HttpRequest [PUT], url: '/multiapi/testOneEndpoint'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """
        request_copy = deepcopy(http_request)
        request_copy.url = self._client.format_url(request_copy.url)
        if kwargs.pop("stream_response", False):
            return _AsyncStreamContextManager(
                client=self._client._pipeline,
                request=request_copy,
            )
        pipeline_response = await self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = AsyncHttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response
        )
        await response.read()
        return response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MultiapiServiceClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
