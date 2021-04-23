# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest, _AsyncStreamContextManager
from msrest import Deserializer, Serializer

from ._configuration import AutoRestValidationTestConfiguration
from .operations import AutoRestValidationTestOperationsMixin
from .. import models


class AutoRestValidationTest(AutoRestValidationTestOperationsMixin):
    """Test Infrastructure for AutoRest. No server backend exists for these tests.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param base_url: Service URL
    :type base_url: str
    """

    def __init__(self, subscription_id: str, base_url: Optional[str] = None, **kwargs: Any) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestValidationTestConfiguration(subscription_id, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize = Serializer(client_models)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `validation.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from validation.rest import build_validation_of_method_parameters_request
        >>> request = build_validation_of_method_parameters_request(subscription_id, resource_group_name, id)
        <HttpRequest [GET], url: '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'>
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
            _internal_response=pipeline_response.http_response,
        )
        await response.read()
        return response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestValidationTest":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
