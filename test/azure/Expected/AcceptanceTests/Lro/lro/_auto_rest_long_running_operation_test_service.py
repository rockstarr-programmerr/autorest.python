# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core.rest import HttpResponse, _StreamContextManager
from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest

from ._configuration import AutoRestLongRunningOperationTestServiceConfiguration
from .operations import LROsOperations
from .operations import LRORetrysOperations
from .operations import LROSADsOperations
from .operations import LROsCustomHeaderOperations
from . import models


class AutoRestLongRunningOperationTestService(object):
    """Long-running Operation for AutoRest.

    :ivar lros: LROsOperations operations
    :vartype lros: lro.operations.LROsOperations
    :ivar lro_retrys: LRORetrysOperations operations
    :vartype lro_retrys: lro.operations.LRORetrysOperations
    :ivar lrosads: LROSADsOperations operations
    :vartype lrosads: lro.operations.LROSADsOperations
    :ivar lr_os_custom_header: LROsCustomHeaderOperations operations
    :vartype lr_os_custom_header: lro.operations.LROsCustomHeaderOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param base_url: Service URL
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestLongRunningOperationTestServiceConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self.lros = LROsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.lro_retrys = LRORetrysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.lrosads = LROSADsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.lr_os_custom_header = LROsCustomHeaderOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `lro.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from lro.rest import build_put200_succeeded_request_initial
        >>> request = build_put200_succeeded_request_initial(json, content)
        <HttpRequest [PUT], url: '/lro/put/200/succeeded'>
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
        request_copy.url = self._client.format_url(request_copy.url)
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
        # type: () -> AutoRestLongRunningOperationTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
