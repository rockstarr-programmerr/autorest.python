# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class ImplicitOperations(object):
    """ImplicitOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_required_path(
            self, path_parameter, custom_headers=None, raw=False, **operation_config):
        """Test implicitly required path parameter.

        :param path_parameter:
        :type path_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_path.metadata['url']
        path_format_arguments = {
            'pathParameter': self._serialize.url("path_parameter", path_parameter, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_required_path.metadata = {'url': '/reqopt/implicit/required/path/{pathParameter}'}

    def put_optional_query(
            self, query_parameter=None, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional query parameter.

        :param query_parameter:
        :type query_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_parameter is not None:
            query_parameters['queryParameter'] = self._serialize.query("query_parameter", query_parameter, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_optional_query.metadata = {'url': '/reqopt/implicit/optional/query'}

    def put_optional_header(
            self, query_parameter=None, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional header parameter.

        :param query_parameter:
        :type query_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)
        if query_parameter is not None:
            header_parameters['queryParameter'] = self._serialize.header("query_parameter", query_parameter, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_optional_header.metadata = {'url': '/reqopt/implicit/optional/header'}

    def put_optional_body(
            self, body_parameter=None, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional body parameter.

        :param body_parameter:
        :type body_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_body.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'str')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_optional_body.metadata = {'url': '/reqopt/implicit/optional/body'}

    def get_required_global_path(
            self, custom_headers=None, raw=False, **operation_config):
        """Test implicitly required path parameter.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_global_path.metadata['url']
        path_format_arguments = {
            'required-global-path': self._serialize.url("self.config.required_global_path", self.config.required_global_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_required_global_path.metadata = {'url': '/reqopt/global/required/path/{required-global-path}'}

    def get_required_global_query(
            self, custom_headers=None, raw=False, **operation_config):
        """Test implicitly required query parameter.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_global_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['required-global-query'] = self._serialize.query("self.config.required_global_query", self.config.required_global_query, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_required_global_query.metadata = {'url': '/reqopt/global/required/query'}

    def get_optional_global_query(
            self, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional query parameter.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_optional_global_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        if self.config.optional_global_query is not None:
            query_parameters['optional-global-query'] = self._serialize.query("self.config.optional_global_query", self.config.optional_global_query, 'int')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_optional_global_query.metadata = {'url': '/reqopt/global/optional/query'}