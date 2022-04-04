# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import cast, Dict, List, Any, Optional, Union, Set, TYPE_CHECKING

from .base_builder import BaseBuilder, create_parameters
from .imports import FileImport, ImportType, TypingSection
from .response import Response
from .parameter import Parameter, get_parameter, ParameterLocation, RequestBody
from .parameter_list import ParameterList, get_parameter_list
from .base_schema import BaseSchema
from .object_schema import ObjectSchema
from .request_builder import RequestBuilder
from .schema_request import SchemaRequest
from .primitive_schemas import IOSchema

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)

class Operation(BaseBuilder):  # pylint: disable=too-many-public-methods, too-many-instance-attributes
    """Represent an self.
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        parameters,
    ) -> None:
        super().__init__(
            yaml_data=yaml_data,
            code_model=code_model,
            name=name,
            parameters=parameters,
        )
        self._request_builder: Optional[RequestBuilder] = None
        self.want_tracing = True

    @property
    def python_name(self) -> str:
        return self.name

    @property
    def request_builder(self) -> RequestBuilder:
        if not self._request_builder:
            raise ValueError(
                "You're calling request_builder when you haven't linked up operation to its "
                "request builder through the code model"
            )
        return self._request_builder

    @request_builder.setter
    def request_builder(self, r: RequestBuilder) -> None:
        self._request_builder = r

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return any(response.is_stream_response for response in self.responses)

    @property
    def body_kwargs_to_pass_to_request_builder(self) -> List[str]:
        return [p.serialized_name for p in self.request_builder.body_kwargs_to_get]

    @property
    def has_optional_return_type(self) -> bool:
        """Has optional return type if there are multiple successful response types where some have
        bodies and some are None
        """
        return False
        # successful status codes of responses that have bodies
        status_codes_for_responses_with_bodies = [
            code for code in self.successful_status_codes
            if isinstance(code, int) and self.get_response_from_status(code).has_body
        ]

        successful_responses = [
            response for response in self.responses
            if any(code in self.successful_status_codes for code in response.status_codes)
        ]

        return (
            self.has_response_body and
            len(successful_responses) > 1 and
            len(self.successful_status_codes) != len(status_codes_for_responses_with_bodies)
        )

    @property
    def serialization_context(self) -> str:
        # FIXME Do the serialization context (XML)
        return ""


    def _imports_shared(self, async_mode: bool) -> FileImport: # pylint: disable=unused-argument
        file_import = FileImport()
        file_import.add_submodule_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        for param in self.parameters.method:
            file_import.merge(param.imports())

        # for param in self.multiple_content_type_parameters:
        #     file_import.merge(param.imports())

        for response in self.responses:
            file_import.merge(response.imports(self.code_model))
            if response.type:
                file_import.merge(cast(BaseSchema, response.type).imports())

        response_types = [r.type_annotation(is_operation_file=True) for r in self.responses if r.type]
        if len(set(response_types)) > 1:
            file_import.add_submodule_import("typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL)

        if self.is_stream_response:
            file_import.add_submodule_import("typing", "IO", ImportType.STDLIB, TypingSection.CONDITIONAL)
        return file_import


    def imports_for_multiapi(self, async_mode: bool) -> FileImport:  # pylint: disable=unused-argument
        return self._imports_shared(async_mode)

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_base(async_mode, is_python3_file)
        if any(r for r in self.responses if r.type) and not self.has_optional_return_type and not self.code_model.options["models_mode"]:
            file_import.add_submodule_import("typing", "cast", ImportType.STDLIB)
        return file_import

    @staticmethod
    def has_kwargs_to_pop_with_default(kwargs_to_pop: List[Parameter], location: ParameterLocation) -> bool:
        return any(kwarg.has_default_value and kwarg.location == location for kwarg in kwargs_to_pop)

    def _imports_base(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)

        # Exceptions
        file_import.add_submodule_import("azure.core.exceptions", "map_error", ImportType.AZURECORE)
        if self.code_model.options["azure_arm"]:
            file_import.add_submodule_import("azure.mgmt.core.exceptions", "ARMErrorFormat", ImportType.AZURECORE)
        file_import.add_submodule_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)

        file_import.add_submodule_import("typing", "Callable", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("azure.core.pipeline", "PipelineResponse", ImportType.AZURECORE)
        file_import.add_submodule_import("azure.core.rest", "HttpRequest", ImportType.AZURECORE)
        kwargs_to_pop = self.parameters.kwargs_to_pop(is_python3_file)
        if (self.has_kwargs_to_pop_with_default(kwargs_to_pop, ParameterLocation.Header) or
            self.has_kwargs_to_pop_with_default(kwargs_to_pop, ParameterLocation.Query)):
            file_import.add_submodule_import("azure.core.utils", "case_insensitive_dict", ImportType.AZURECORE)
        if async_mode:
            file_import.add_submodule_import("azure.core.pipeline.transport", "AsyncHttpResponse", ImportType.AZURECORE)
        else:
            file_import.add_submodule_import("azure.core.pipeline.transport", "HttpResponse", ImportType.AZURECORE)

        if self.code_model.options["builders_visibility"] != "embedded":
            builder_group_name = self.request_builder.builder_group_name
            rest_import_path = "..." if async_mode else ".."
            if builder_group_name:
                file_import.add_submodule_import(
                    f"{rest_import_path}{self.code_model.rest_layer_name}",
                    builder_group_name,
                    import_type=ImportType.LOCAL,
                    alias=f"rest_{builder_group_name}"
                )
            else:
                file_import.add_submodule_import(
                    rest_import_path,
                    self.code_model.rest_layer_name,
                    import_type=ImportType.LOCAL,
                    alias="rest"
                )
        if self.code_model.options["builders_visibility"] == "embedded" and not async_mode:
            file_import.merge(self.request_builder.imports())
        if self.code_model.need_request_converter:
            relative_path = "..." if async_mode else ".."
            file_import.add_submodule_import(
                f"{relative_path}_vendor", "_convert_request", ImportType.LOCAL
            )

        if self.code_model.options["version_tolerant"] and (
            self.parameters.request_body or
            any(r for r in self.responses if r.type)
        ):
            file_import.define_mypy_type("JSONType", "Any")
        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator{'_async' if async_mode else ''}",
                f"distributed_trace{'_async' if async_mode else ''}",
                ImportType.AZURECORE,
            )
        return file_import

    def _get_body_param_from_body_kwarg(self, body_kwarg: Parameter) -> Parameter:
        # determine which of the body parameters returned from m4 corresponds to this body_kwarg
        if not self.multiple_content_type_parameters.has_body:
            return self.parameters.body[0]
        if body_kwarg.serialized_name == "data":
            return next(p for p in self.multiple_content_type_parameters.body if p.is_data_input)
        if body_kwarg.serialized_name == "files":
            return next(p for p in self.multiple_content_type_parameters.body if p.is_multipart)
        if body_kwarg.serialized_name == "json":
            # first check if there's any non-binary. In the case of multiple content types, there's
            # usually one binary (for content), and one schema parameter (for json)
            try:
                return next(
                    p for p in self.multiple_content_type_parameters.body
                    if not isinstance(p.schema, IOSchema)
                )
            except StopIteration:
                return next(p for p in self.multiple_content_type_parameters.body if p.is_json_parameter)
        return self.multiple_content_type_parameters.body[0]

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model) -> "Operation":
        name = yaml_data["name"]
        _LOGGER.debug("Parsing %s operation", name)

        parameter_creator = get_parameter(code_model).from_yaml
        parameter_list_creator = get_parameter_list(code_model)
        parameters = [parameter_creator(p, code_model) for p in yaml_data["parameters"]]
        if yaml_data.get("requestBody"):
            request_body = RequestBody.from_yaml(yaml_data["requestBody"], code_model)
        else:
            request_body = None
        parameter_list = parameter_list_creator(code_model, parameters, request_body=request_body)

        return cls(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            parameters=parameter_list,
        )
