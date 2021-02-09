# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class LROWithParamaterizedEndpointsOperationsMixin(object):
    def _poll_with_parameterized_endpoints_initial_request(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._poll_with_parameterized_endpoints_initial_request.metadata["url"])  # type: ignore
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.post(url, query_parameters, header_parameters)

    _poll_with_parameterized_endpoints_initial_request.metadata = {"url": "/lroParameterizedEndpoints"}  # type: ignore

    def _poll_with_parameterized_endpoints_initial(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[str]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._poll_with_parameterized_endpoints_initial_request(account_name=account_name, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("str", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _poll_with_parameterized_endpoints_initial.metadata = {"url": "/lroParameterizedEndpoints"}  # type: ignore

    @distributed_trace
    def begin_poll_with_parameterized_endpoints(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[str]
        """Poll with method and client level parameters in endpoint.

        :param account_name: Account Name. Pass in 'local' to pass test.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the LROBasePolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either str or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[str]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop("polling", False)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._poll_with_parameterized_endpoints_initial(
                account_name=account_name, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("str", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = LROBasePolling(
                lro_delay,
                lro_options={"final-state-via": "location"},
                path_format_arguments=path_format_arguments,
                **kwargs
            )
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_poll_with_parameterized_endpoints.metadata = {"url": "/lroParameterizedEndpoints"}  # type: ignore
