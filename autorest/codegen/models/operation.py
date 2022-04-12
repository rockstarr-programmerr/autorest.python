# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import Dict, List, Any, Optional, Union, TYPE_CHECKING, cast

from .base_builder import BaseBuilder, create_parameters_and_overloads
from .imports import FileImport, ImportType, TypingSection
from .response import Response
from .parameter import MultipartBodyParameter, OverloadBodyParameter, Parameter, BodyParameter, UrlEncodedBodyParameter, ParameterLocation
from .parameter_list import OverloadBaseParameterList, ParameterList
from .object_schema import ObjectSchema
from .request_builder import RequestBuilder

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)

def _get_operation_class(operation_type):
    if operation_type == "paging":
        from .paging_operation import PagingOperation
        return PagingOperation
    if operation_type == "lro":
        from .lro_operation import LROOperation
        return LROOperation
    if operation_type == "lropaging":
        from .lro_paging_operation import LROPagingOperation
        return LROPagingOperation
    return Operation

def _get_overloads(
    overload_body_parameters: List[OverloadBodyParameter],
    yaml_data: Dict[str, Any],
    code_model: "CodeModel",
    request_builder: RequestBuilder,
    parameters: List[Parameter],
    responses: List[Response],
):
    overloads: List[Operation] = []
    if overload_body_parameters:
        # we have overloads now, one for each type
        for obp in overload_body_parameters:
            overloads.append(Operation(
                yaml_data=yaml_data,
                code_model=code_model,
                name=yaml_data["name"],
                request_builder=request_builder,
                parameters=ParameterList(
                    code_model=code_model,
                    parameters=parameters,
                    body_parameter=obp
                ),
                responses=responses,
                overloads=[],
                want_tracing=False,
            ))
    return overloads


class Operation(BaseBuilder):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        request_builder: RequestBuilder,
        parameters: ParameterList,
        responses: List[Response],
        overloads: List["Operation"],
        *,
        want_description_docstring: bool = True,
        want_tracing: bool = True,
        abstract: bool = False,
    ) -> None:
        super().__init__(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            parameters=parameters,
            overloads=overloads,
            abstract=abstract,
            want_tracing=want_tracing,
        )
        self.overloads = overloads or []
        self.responses = responses
        self.want_description_docstring = want_description_docstring
        self.request_builder = request_builder
        self.deprecated = False
        self.operation_type = "operation"

    @property
    def has_optional_return_type(self) -> bool:
        """Has optional return type if there are multiple successful response types where some have
        bodies and some are None
        """
        # means if we have at least one successful response with a body and one without
        successful_responses = [r for r in self.responses if not r.is_error]
        successful_response_with_body = any(
            r for r in successful_responses if r.types
        )
        successful_response_without_body = any(
            r for r in successful_responses if not r.types
        )
        return successful_response_with_body and successful_response_without_body

    @property
    def has_response_body(self) -> bool:
        """Tell if at least one response has a body."""
        return any(
            response.types or response.is_stream_response
            for response in self.responses
        )

    @property
    def any_response_has_headers(self) -> bool:
        return any(response.headers for response in self.responses)

    @property
    def default_error_deserialization(self) -> Optional[str]:
        retval = [
            r for r in self.responses
            if r.is_error and "*" in r.status_codes
        ]
        if not retval:
            return None
        excep_schema = retval[0].types[0]
        if isinstance(excep_schema, ObjectSchema):
            return f"_models.{excep_schema.name}"
        # in this case, it's just an AnySchema
        return "'object'"


    @property
    def non_default_errors(self) -> List[Response]:
        return [
            r for r in self.responses if r.is_error and "*" not in r.status_codes
        ]

    @property
    def non_default_error_status_codes(self) -> List[Union[str, int]]:
        """Actually returns all of the status codes from exceptions (besides default)"""
        return list(
            chain.from_iterable(
                [error.status_codes for error in self.non_default_errors]
            )
        )

    def _imports_shared(
        self, async_mode: bool  # pylint: disable=unused-argument
    ) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        for param in self.parameters.method:
            if self.abstract and isinstance(param, (MultipartBodyParameter, UrlEncodedBodyParameter)):
                continue
            file_import.merge(param.imports())

        for response in self.responses:
            file_import.merge(response.imports(self.code_model))

        response_types = [
            r.type_annotation()
            for r in self.responses
            if r.types
        ]
        if len(set(response_types)) > 1:
            file_import.add_submodule_import(
                "typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        return file_import

    def imports_for_multiapi(
        self, async_mode: bool
    ) -> FileImport:  # pylint: disable=unused-argument
        return self._imports_shared(async_mode)

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_base(async_mode, is_python3_file)
        if self.abstract:
            return file_import
        if (
            self.has_response_body
            and not self.has_optional_return_type
            and not self.code_model.options["models_mode"]
        ):
            file_import.add_submodule_import("typing", "cast", ImportType.STDLIB)
        return file_import

    @staticmethod
    def has_kwargs_to_pop_with_default(
        kwargs_to_pop: List[Parameter], location: ParameterLocation
    ) -> bool:
        return any(
            kwarg.has_default_value and kwarg.location == location
            for kwarg in kwargs_to_pop
        )

    def _imports_base(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)

        # Exceptions
        if self.abstract:
            file_import.add_import("abc", ImportType.STDLIB)
        else:
            file_import.add_submodule_import(
                "azure.core.exceptions", "map_error", ImportType.AZURECORE
            )
            if self.code_model.options["azure_arm"]:
                file_import.add_submodule_import(
                    "azure.mgmt.core.exceptions", "ARMErrorFormat", ImportType.AZURECORE
                )
            file_import.add_submodule_import(
                "azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE
            )
            file_import.add_submodule_import(
                "azure.core.exceptions",
                "ClientAuthenticationError",
                ImportType.AZURECORE,
            )
            file_import.add_submodule_import(
                "azure.core.exceptions", "ResourceNotFoundError", ImportType.AZURECORE
            )
            file_import.add_submodule_import(
                "azure.core.exceptions", "ResourceExistsError", ImportType.AZURECORE
            )

            kwargs_to_pop = self.parameters.kwargs_to_pop(is_python3_file)
            if self.has_kwargs_to_pop_with_default(
                kwargs_to_pop, ParameterLocation.HEADER
            ) or self.has_kwargs_to_pop_with_default(
                kwargs_to_pop, ParameterLocation.QUERY
            ):
                file_import.add_submodule_import(
                    "azure.core.utils", "case_insensitive_dict", ImportType.AZURECORE
                )
            if self.deprecated:
                file_import.add_import("warnings", ImportType.STDLIB)
            if self.code_model.options["builders_visibility"] != "embedded":
                builder_group_name = self.request_builder.builder_group_name
                rest_import_path = "..." if async_mode else ".."
                if builder_group_name:
                    file_import.add_submodule_import(
                        f"{rest_import_path}{self.code_model.rest_layer_name}",
                        builder_group_name,
                        import_type=ImportType.LOCAL,
                        alias=f"rest_{builder_group_name}",
                    )
                else:
                    file_import.add_submodule_import(
                        rest_import_path,
                        self.code_model.rest_layer_name,
                        import_type=ImportType.LOCAL,
                        alias="rest",
                    )
            if self.code_model.need_request_converter:
                relative_path = "..." if async_mode else ".."
                file_import.add_submodule_import(
                    f"{relative_path}_vendor", "_convert_request", ImportType.LOCAL
                )
        if async_mode:
            file_import.add_submodule_import(
                "azure.core.pipeline.transport",
                "AsyncHttpResponse",
                ImportType.AZURECORE,
            )
        else:
            file_import.add_submodule_import(
                "azure.core.pipeline.transport", "HttpResponse", ImportType.AZURECORE
            )
        if (
            self.code_model.options["builders_visibility"] == "embedded"
            and not async_mode
        ):
            file_import.merge(self.request_builder.imports())
        file_import.add_submodule_import(
            "azure.core.pipeline", "PipelineResponse", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "azure.core.rest", "HttpRequest", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "typing", "Callable", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import(
            "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import(
            "typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import(
            "typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator{'_async' if async_mode else ''}",
                f"distributed_trace{'_async' if async_mode else ''}",
                ImportType.AZURECORE,
            )

        return file_import

    def get_response_from_status(
        self, status_code: Optional[Union[str, int]]
    ) -> Response:
        try:
            return next(r for r in self.responses if status_code in r.status_codes)
        except StopIteration:
            raise ValueError(f"Incorrect status code {status_code}, operation {self.name}")

    @property
    def success_status_codes(self) -> List[Union[str, int]]:
        """The list of all successfull status code."""
        return [
            code
            for response in self.responses
            for code in response.status_codes
            if not response.is_error
        ]

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "Operation":
        name = yaml_data["name"]
        parameters = [Parameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        abstract = False
        request_builder = code_model.lookup_request_builder(id(yaml_data))
        responses = [Response.from_yaml(r, code_model) for r in yaml_data["responses"]]
        parameter_list, overload_body_parameters = create_parameters_and_overloads(
            yaml_data, code_model, is_operation=True
        )
        overloads = _get_overloads(
            cast(List[OverloadBodyParameter], overload_body_parameters),
            yaml_data,
            code_model,
            request_builder,
            parameters,
            responses,
        )
        if code_model.options["version_tolerant"] and any(p for p in parameter_list if p.is_multipart or p.is_data_input):
            _LOGGER.warning(
                'Not going to generate operation "%s" because it has multipart / urlencoded body parameters. '
                "Multipart / urlencoded body parameters are not supported for version tolerant generation right now. "
                'Please write your own custom operation in the "_patch.py" file '
                "following https://aka.ms/azsdk/python/dpcodegen/python/customize",
                name,
            )
            abstract = True

        op_cls = _get_operation_class(yaml_data["operationType"])
        return op_cls(
            yaml_data=yaml_data,
            code_model=code_model,
            request_builder=request_builder,
            overloads=overloads,
            name=name,
            parameters=parameter_list,
            responses=responses,
            abstract=abstract,
        )
