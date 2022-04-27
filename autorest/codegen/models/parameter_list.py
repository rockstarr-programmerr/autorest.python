# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from collections.abc import MutableSequence
import logging
from typing import cast, List, Callable, Optional, TypeVar, Dict, TYPE_CHECKING

from .parameter import Parameter, ParameterLocation, ParameterMethodLocation
from .base_schema import BaseSchema
from .primitive_schemas import StringSchema
from .utils import JSON_REGEXP

if TYPE_CHECKING:
    from .schema_request import SchemaRequest
    from .code_model import CodeModel

T = TypeVar("T")
OrderedSet = Dict[T, None]

_LOGGER = logging.getLogger(__name__)


def _method_signature_helper(
    positional: List[str], keyword_only: Optional[List[str]], kwarg_params: List[str]
):
    keyword_only = keyword_only or []
    return positional + keyword_only + kwarg_params


class ParameterList(MutableSequence):  # pylint: disable=too-many-public-methods
    def __init__(
        self,
        code_model: "CodeModel",
        parameters: Optional[List[Parameter]] = None,
        schema_requests: Optional[List["SchemaRequest"]] = None,
    ) -> None:
        self.code_model = code_model
        self.schema_requests = schema_requests or []
        self.parameters = parameters or []
        self._json_body: Optional[BaseSchema] = None

    # MutableSequence

    def __getitem__(self, index):
        if isinstance(index, str):
            raise TypeError(f"{index} is invalid type")
        return self.parameters[index]

    def __len__(self) -> int:
        return len(self.parameters)

    def __setitem__(self, index, parameter):
        self.parameters[index] = parameter

    def __delitem__(self, index):
        del self.parameters[index]

    def insert(self, index: int, value: Parameter) -> None:
        self.parameters.insert(index, value)

    # Parameter helpers

    def has_any_location(self, location: ParameterLocation) -> bool:
        return bool(
            [
                parameter
                for parameter in self.parameters
                if parameter.location == location
            ]
        )

    def get_from_predicate(
        self, predicate: Callable[[Parameter], bool]
    ) -> List[Parameter]:
        return [parameter for parameter in self.parameters if predicate(parameter)]

    def get_from_location(self, location: ParameterLocation) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: parameter.location == location)

    @property
    def content_types(self) -> List[str]:
        ordered_set = {
            m: None for request in self.schema_requests for m in request.content_types
        }
        return list(ordered_set.keys())

    @property
    def default_content_type(self) -> str:
        json_content_types = [c for c in self.content_types if JSON_REGEXP.match(c)]
        if json_content_types:
            if "application/json" in json_content_types:
                return "application/json"
            return json_content_types[0]

        xml_content_types = [c for c in self.content_types if "xml" in c]
        if xml_content_types:
            if "application/xml" in xml_content_types:
                return "application/xml"
            return xml_content_types[0]
        return self.content_types[0]

    @property
    def json_body(self) -> BaseSchema:
        if not self._json_body:
            self._json_body = self.body[0].schema
        return self._json_body

    @property
    def has_body(self) -> bool:
        return self.has_any_location(ParameterLocation.Body)

    @property
    def body(self) -> List[Parameter]:
        if not self.has_body:
            raise ValueError(f"Can't get body parameter")
        # Should we check if there is two body? Modeler role right?
        body_params = self.get_from_location(ParameterLocation.Body)
        return body_params

    @staticmethod
    def _wanted_path_parameter(parameter: Parameter):
        # TODO add 'and parameter.location == "Method"' as requirement to this check once
        # I can use send_request on operations.
        # Don't want to duplicate code from send_request.
        return (
            parameter.location == ParameterLocation.Uri
            and parameter.rest_api_name != "$host"
        )

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def path(self) -> List[Parameter]:
        return [
            parameter
            for parameter in self.parameters
            if self._wanted_path_parameter(parameter)
        ]

    @property
    def query(self) -> List[Parameter]:
        return self.get_from_location(ParameterLocation.Query)

    @property
    def headers(self) -> List[Parameter]:
        headers = self.get_from_location(ParameterLocation.Header)
        if not headers:
            return headers
        return list({header.serialized_name: header for header in headers}.values())

    @property
    def grouped(self) -> List[Parameter]:
        return self.get_from_predicate(
            lambda parameter: cast(bool, parameter.grouped_by)
        )

    @property
    def groupers(self) -> List[Parameter]:
        groupers: List[Parameter] = []
        for parameter in self.parameters:
            if any(
                [
                    p
                    for p in self.grouped
                    if p.grouped_by
                    and id(p.grouped_by.yaml_data) == id(parameter.yaml_data)
                ]
            ):
                groupers.append(parameter)
        return groupers

    @property
    def constant(self) -> List[Parameter]:
        """Return the constants of this parameter list.

        This excludes the constant from flatening on purpose, since technically they are not
        constant from this set of parameters, they are constants on the models and hence they do
        not have impact on any generation at this level
        """
        return self.get_from_predicate(lambda parameter: parameter.constant)

    @property
    def multipart(self) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: parameter.is_multipart)

    @property
    def data_inputs(self) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: parameter.is_data_input)

    def _filter_out_multiple_content_type(self, kwarg_params):
        """We don't want multiple content type kwargs in the method signature"""
        content_type_params = [
            k for k in kwarg_params if k.rest_api_name == "Content-Type"
        ]
        if len(content_type_params) > 1:
            # we don't want multiple content type params in the method, just one
            # we'll pick the one with the default content type
            seen_content_type = False
            new_kwarg_params = []
            for k in kwarg_params:
                if k.rest_api_name == "Content-Type":
                    if (
                        not seen_content_type
                        and k.default_value_declaration
                        == f'"{self.default_content_type}"'
                    ):
                        new_kwarg_params.append(k)
                        seen_content_type = True
                    else:
                        continue
                else:
                    new_kwarg_params.append(k)
            kwarg_params = new_kwarg_params
        return kwarg_params

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature."""
        # Client level should not be on Method, etc.
        parameters_of_this_implementation = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation
            and parameter.in_method_signature
        )
        positional = [
            p
            for p in parameters_of_this_implementation
            if p.method_location == ParameterMethodLocation.POSITIONAL
        ]
        keyword_only = self._filter_out_multiple_content_type(
            [
                p
                for p in parameters_of_this_implementation
                if p.method_location == ParameterMethodLocation.KEYWORD_ONLY
            ]
        )
        kwargs = self._filter_out_multiple_content_type(
            [
                p
                for p in parameters_of_this_implementation
                if p.method_location
                in (ParameterMethodLocation.KWARG, ParameterMethodLocation.HIDDEN_KWARG)
            ]
        )

        def _sort(params):
            return sorted(
                params, key=lambda x: not x.default_value and x.required, reverse=True
            )

        signature_parameters = _sort(positional) + _sort(keyword_only) + _sort(kwargs)
        return signature_parameters

    def method_signature(self, is_python3_file: bool) -> List[str]:
        return _method_signature_helper(
            positional=self.method_signature_positional(is_python3_file),
            keyword_only=self.method_signature_keyword_only(is_python3_file),
            kwarg_params=self.method_signature_kwargs(is_python3_file),
        )

    def method_signature_positional(self, is_python3_file: bool) -> List[str]:
        return [
            parameter.method_signature(is_python3_file) for parameter in self.positional
        ]

    def method_signature_keyword_only(self, is_python3_file: bool) -> List[str]:
        if not (self.keyword_only and is_python3_file):
            return []
        return ["*,"] + [
            parameter.method_signature(is_python3_file)
            for parameter in self.keyword_only
        ]

    @staticmethod
    def method_signature_kwargs(is_python3_file: bool) -> List[str]:
        return ["**kwargs: Any"] if is_python3_file else ["**kwargs  # type: Any"]

    @property
    def positional(self) -> List[Parameter]:
        return [
            p
            for p in self.method
            if p.method_location == ParameterMethodLocation.POSITIONAL
        ]

    @property
    def keyword_only(self) -> List[Parameter]:
        return [
            p
            for p in self.method
            if p.method_location == ParameterMethodLocation.KEYWORD_ONLY
        ]

    @property
    def kwargs(self) -> List[Parameter]:
        return [
            p
            for p in self.method
            if p.method_location
            in (ParameterMethodLocation.KWARG, ParameterMethodLocation.HIDDEN_KWARG)
        ]

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Parameter]:
        kwargs_to_pop = self.kwargs
        if not is_python3_file:
            kwargs_to_pop += self.keyword_only
        return kwargs_to_pop

    def call(self, is_python3_file: bool) -> List[str]:
        retval = [p.serialized_name for p in self.positional]
        if is_python3_file:
            retval.extend(
                [f"{p.serialized_name}={p.serialized_name}" for p in self.keyword_only]
            )
        retval.append("**kwargs")
        return retval

    @property
    def is_flattened(self) -> bool:
        return cast(
            bool, self.get_from_predicate(lambda parameter: parameter.flattened)
        )


class GlobalParameterList(ParameterList):
    @property
    def implementation(self) -> str:
        return "Client"

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature."""
        # Client level should not be on Method, etc.
        positional = [
            p
            for p in self.parameters
            if p.method_location == ParameterMethodLocation.POSITIONAL
        ]
        keyword_only = self._filter_out_multiple_content_type(
            [
                p
                for p in self.parameters
                if p.method_location == ParameterMethodLocation.KEYWORD_ONLY
            ]
        )
        kwargs = self._filter_out_multiple_content_type(
            [
                p
                for p in self.parameters
                if p.method_location
                in (ParameterMethodLocation.KWARG, ParameterMethodLocation.HIDDEN_KWARG)
            ]
        )

        def _sort(params):
            return sorted(
                params, key=lambda x: not x.default_value and x.required, reverse=True
            )

        signature_parameters = _sort(positional) + _sort(keyword_only) + _sort(kwargs)
        return signature_parameters

    @property
    def host_variable_name(self) -> str:
        return (
            "base_url"
            if self.code_model.is_legacy
            else "endpoint"
        )

    @staticmethod
    def _wanted_path_parameter(parameter: Parameter) -> bool:
        return (
            parameter.location == ParameterLocation.Uri
            and parameter.implementation == "Client"
            and parameter.rest_api_name != "$host"
        )

    def add_host(self, host_value: Optional[str]) -> None:
        # only adds if we don't have a parameterized host
        host_param = Parameter(
            yaml_data={},
            code_model=self.code_model,
            schema=StringSchema(yaml_data={"type": "str"}, code_model=self.code_model),
            rest_api_name=self.host_variable_name,
            serialized_name=self.host_variable_name,
            description=f"Service URL.",
            implementation="Client",
            required=True,
            location=ParameterLocation.Other,
            skip_url_encoding=False,
            constraints=[],
            client_default_value=host_value,
        )
        if not self.code_model.is_legacy:
            host_param.method_location = ParameterMethodLocation.KEYWORD_ONLY
        self.parameters.append(host_param)

    def add_credential_global_parameter(self) -> None:
        credential_parameter = Parameter(
            yaml_data={},
            code_model=self.code_model,
            schema=self.code_model.credential_model.credential_schema_policy.credential,
            serialized_name="credential",
            rest_api_name="credential",
            implementation="Client",
            description="Credential needed for the client to connect to Azure.",
            required=True,
            location=ParameterLocation.Other,
            skip_url_encoding=True,
            constraints=[],
        )
        if self.code_model.is_legacy:
            self.parameters.insert(0, credential_parameter)
        else:
            self.parameters.append(credential_parameter)

    @property
    def host(self) -> Optional[Parameter]:
        try:
            return next(
                p
                for p in self.parameters
                if p.serialized_name == self.host_variable_name
            )
        except StopIteration:
            return None

    @property
    def host_value(self) -> Optional[str]:
        if self.code_model.service_client.has_parameterized_host:
            return None
        return next(
            p for p in self.parameters if p.serialized_name == self.host_variable_name
        ).default_value_declaration

    @property
    def client_method(self) -> List[Parameter]:
        return self.method

    def _param_is_in_config_method(self, serialized_name):
        if self.code_model.service_client.has_parameterized_host:
            return True
        return serialized_name != self.host_variable_name

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Parameter]:
        return [
            k
            for k in super().kwargs_to_pop(is_python3_file)
            if not self._param_is_in_config_method(k.serialized_name)
        ]

    def config_kwargs_to_pop(self, is_python3_file: bool) -> List[Parameter]:
        current_kwargs_to_pop = super().kwargs_to_pop(is_python3_file)
        return [
            k
            for k in current_kwargs_to_pop
            if self._param_is_in_config_method(k.serialized_name)
        ]

    @property
    def config_method(self) -> List[Parameter]:
        return [
            p for p in self.method if self._param_is_in_config_method(p.serialized_name)
        ]

    def client_method_signature(self, is_python3_file: bool) -> List[str]:
        return self.method_signature(is_python3_file)

    def config_method_signature(self, is_python3_file: bool) -> List[str]:

        positional = [
            p.method_signature(is_python3_file)
            for p in self.positional
            if self._param_is_in_config_method(p.serialized_name)
        ]
        keyword_only_params = [
            p
            for p in self.keyword_only
            if self._param_is_in_config_method(p.serialized_name)
        ]
        keyword_only_method_signature = []
        if is_python3_file:
            keyword_only_method_signature = (
                (
                    ["*,"]
                    + [p.method_signature(is_python3_file) for p in keyword_only_params]
                )
                if keyword_only_params
                else []
            )
        return _method_signature_helper(
            positional=positional,
            keyword_only=keyword_only_method_signature,
            kwarg_params=self.method_signature_kwargs(is_python3_file),
        )
