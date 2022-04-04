# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Optional, List, Union, Any, cast, TYPE_CHECKING

from .base_model import BaseModel
from .base_schema import BaseSchema
from .object_schema import ObjectSchema
from .imports import FileImport, ImportType
from .utils import get_schema
from .primitive_schemas import IOSchema

if TYPE_CHECKING:
    from .code_model import CodeModel


class ResponseHeader(BaseModel):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", type: BaseModel) -> None:
        super().__init__(yaml_data, code_model)
        self.name = yaml_data["name"]
        self.type = type

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "ResponseHeader":
        return cls(
            yaml_data,
            code_model,
            code_model.lookup_schema(id(yaml_data["type"]))
        )

class Response(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: Optional[BaseSchema] = None,
        headers: List[ResponseHeader] = [],
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.content_types: List[str] = yaml_data.get("contentTypes", [])
        self.type = type
        self.headers = headers
        self.binary = False  # TODO: binary responses?


    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if not self.type:
            return "None"
        return self.type.type_annotation(is_operation_file=is_operation_file)

    @property
    def docstring_text(self) -> str:
        if not self.type:
            return "None"
        return self.type.docstring_text

    @property
    def docstring_type(self) -> str:
        if not self.type:
            return "None"
        return self.type.docstring_type

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return self.binary

    @property
    def is_exception(self) -> bool:
        if self.type:
            return cast(ObjectSchema, self.type).is_exception
        return False

    @property
    def is_xml(self) -> bool:
        return any(["xml" in ct for ct in self.content_types])

    def imports(self, code_model) -> FileImport:
        file_import = FileImport()
        if not code_model.options["models_mode"] and self.is_xml:
            file_import.add_submodule_import("xml.etree", "ElementTree", ImportType.STDLIB, alias="ET")
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Response":
        type = code_model.lookup_schema(id(yaml_data["type"])) if yaml_data.get("type") else None
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=type,
            headers=[ResponseHeader(header, code_model, code_model.lookup_schema(header["type"])) for header in yaml_data["headers"]]
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.status_codes}>"
