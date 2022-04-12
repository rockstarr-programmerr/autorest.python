# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, Any, Optional, TYPE_CHECKING
from .base_schema import BaseSchema
from .imports import FileImport

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)


class ConstantSchema(BaseSchema):
    """Schema for constants that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param str value: The actual value of this constant.
    :param schema: The schema for the value of this constant.
    :type schema: ~autorest.models.PrimitiveSchema
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        value_type: BaseSchema,
        value: Optional[str],
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.value_type = value_type
        self.value = value

    def get_declaration(self, value: Any):
        if value != self.value:
            _LOGGER.warning(
                "Passed in value of %s differs from constant value of %s. Choosing constant value",
                str(value),
                str(self.value),
            )
        if self.value is None:
            return "None"
        return self.value_type.get_declaration(self.value)

    def description(self, *, is_operation_file: bool) -> str:
        constant_description = f'Constant value of "{self.value}"'
        if is_operation_file:
            return constant_description
        return self.yaml_data["description"] + ". " + constant_description

    @property
    def serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return self.value_type.serialization_type

    @property
    def docstring_text(self) -> str:
        return "constant"

    @property
    def docstring_type(self) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace: Optional. The namespace for the models.
        """
        return self.value_type.docstring_type

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        return self.value_type.type_annotation(is_operation_file=is_operation_file)

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "ConstantSchema":
        """Constructs a ConstantSchema from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created ConstantSchema
        :rtype: ~autorest.models.ConstantSchema
        """
        from . import build_schema

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            value_type=build_schema(yaml_data["valueType"], code_model),
            value=yaml_data["value"],
        )

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        kwargs["default_value_declaration"] = self.value_type.get_declaration(self.value)
        return self.value_type.get_json_template_representation(**kwargs)

    def imports(self, *, is_operation_file: bool) -> FileImport:
        file_import = FileImport()
        file_import.merge(self.value_type.imports(is_operation_file=is_operation_file))
        return file_import
