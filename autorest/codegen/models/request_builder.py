# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, TypeVar, Optional, TYPE_CHECKING

from .base_builder import BaseBuilder, create_parameters
from .request_builder_parameter import RequestBuilderParameter
from .request_builder_parameter_list import RequestBuilderParameterList
from .schema_request import SchemaRequest
from .response import Response
from .imports import FileImport, ImportType, TypingSection
from .parameter import RequestBody, Parameter

if TYPE_CHECKING:
    from .code_model import CodeModel

T = TypeVar('T')
OrderedSet = Dict[T, None]

class RequestBuilder(BaseBuilder):

    @property
    def is_stream(self) -> bool:
        """Is the request we're preparing a stream, like an upload."""
        return any(request.is_stream_request for request in self.schema_requests)

    @property
    def body_kwargs_to_get(self) -> List[Parameter]:
        return self.parameters.body_kwargs_to_get

    @property
    def operation_group_name(self) -> str:
        return self.yaml_data["operationGroupName"]

    @property
    def builder_group_name(self) -> str:
        return self.yaml_data["language"]["python"]["builderGroupName"]

    def imports(self) -> FileImport:
        file_import = FileImport()
        for parameter in self.parameters:
            if parameter.need_import:
                file_import.merge(parameter.imports())

        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
        )
        if self.parameters.path:
            relative_path = ".."
            if not self.code_model.options["builders_visibility"] == "embedded" and self.operation_group_name:
                relative_path = "..." if self.operation_group_name else ".."
            file_import.add_submodule_import(
                f"{relative_path}_vendor", "_format_url_section", ImportType.LOCAL
            )
        if self.parameters.headers or self.parameters.query:
            file_import.add_submodule_import("azure.core.utils", "case_insensitive_dict", ImportType.AZURECORE)
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, typing_section=TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import("msrest", "Serializer", ImportType.THIRDPARTY)
        if self.parameters.request_body and (
            self.code_model.options["builders_visibility"] != "embedded" or
            self.code_model.options["add_python3_operation_files"]
        ):
            file_import.define_mypy_type("JSONType", "Any")
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "RequestBuilder":

        # when combine embeded builders into one operation file, we need to avoid duplicated build function name.
        # So add operation group name is effective method
        additional_mark = ""
        if code_model.options["combine_operation_files"] and code_model.options["builders_visibility"] == "embedded":
            additional_mark = yaml_data["operationGroupName"]
        names = [
            "build",
            additional_mark,
            yaml_data["name"],
            "request"
        ]
        name = "_".join([n for n in names if n])
        parameters = [RequestBuilderParameter.from_yaml(param, code_model) for param in yaml_data["parameters"]]
        if yaml_data.get("requestBody"):
            request_body = RequestBody.from_yaml(yaml_data["requestBody"], code_model)
        else:
            request_body = None
        parameter_list = RequestBuilderParameterList(
            code_model, parameters, request_body=request_body
        )
        request_builder_class = cls(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            parameters=parameter_list,
        )
        code_model.request_builder_ids[id(yaml_data)] = request_builder_class
        return request_builder_class
