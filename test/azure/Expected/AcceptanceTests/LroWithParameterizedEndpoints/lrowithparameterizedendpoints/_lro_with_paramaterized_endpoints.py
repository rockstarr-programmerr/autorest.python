# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpResponse, _StreamContextManager
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.rest import HttpRequest

from ._configuration import LROWithParamaterizedEndpointsConfiguration
from .operations import LROWithParamaterizedEndpointsOperationsMixin
from . import models


class LROWithParamaterizedEndpoints(LROWithParamaterizedEndpointsOperationsMixin):
    """Test Infrastructure for AutoRest.

    :param host: A string value that is used as a global part of the parameterized host. Pass in 'host:3000' to pass test.
    :type host: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        host="host",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = "http://{accountName}{host}"
        self._config = LROWithParamaterizedEndpointsConfiguration(host, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `lrowithparameterizedendpoints.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from lrowithparameterizedendpoints.rest import build_poll_with_parameterized_endpoints_request_initial
        >>> request = build_poll_with_parameterized_endpoints_request_initial()
        <HttpRequest [POST], url: '/lroParameterizedEndpoints'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """
        request_copy = deepcopy(http_request)
        path_format_arguments = {
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        if kwargs.pop("stream_response", False):
            return _StreamContextManager(
                client=self._client._pipeline,
                request=request_copy,
            )
        pipeline_response = self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = HttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response,
        )
        response.read()
        return response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> LROWithParamaterizedEndpoints
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
