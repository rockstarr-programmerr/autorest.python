# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, TYPE_CHECKING

from .base_model import BaseModel
from .constant_schema import ConstantSchema
from .imports import FileImport, ImportType, TypingSection
from .base_schema import BaseSchema

if TYPE_CHECKING:
    from .code_model import CodeModel

class Property(BaseModel):  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseSchema,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.rest_api_name = yaml_data["restApiName"]
        self.serialized_name = yaml_data["serializedName"]
        self.type = type
        self.optional = yaml_data["optional"]
        self.description = yaml_data.get("description", "")

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Property":
        from . import build_type  # pylint: disable=import-outside-toplevel
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=build_type(yaml_data=yaml_data["type"], code_model=code_model),
        )

    @property
    def constant_declaration(self) -> str:
        if self.type:
            if isinstance(self.type, ConstantSchema):
                return self.type.get_declaration(self.type.value)
            raise ValueError(
                "Trying to get constant declaration for a schema that is not ConstantSchema"
                )
        raise ValueError("Trying to get a declaration for a schema that doesn't exist")

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    @property
    def xml_metadata(self) -> str:
        if self.type.has_xml_serialization_ctxt:
            return f", 'xml': {{{self.type.xml_serialization_ctxt()}}}"
        return ""

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if not self.optional:
            return self.type.type_annotation(is_operation_file=is_operation_file)
        return f"Optional[{self.type.type_annotation(is_operation_file=is_operation_file)}]"

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        if self.description:
            kwargs["description"] = self.description
        return self.type.get_json_template_representation(optional=self.optional, **kwargs)

    def get_files_and_data_template_representation(self, **kwargs: Any) -> Any:
        return self.type.get_files_and_data_template_representation(optional=self.optional, **kwargs)

    def model_file_imports(self) -> FileImport:
        file_import = self.type.model_file_imports()
        if self.optional:
            file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.merge(self.type.model_file_imports())
        return file_import
