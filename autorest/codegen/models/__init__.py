# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from .base_model import BaseModel
from .code_model import CodeModel
from .credential_schema import AzureKeyCredentialSchema, TokenCredentialSchema
from .object_schema import ObjectSchema, get_object_schema, HiddenModelObjectSchema
from .dictionary_schema import DictionarySchema
from .list_schema import ListSchema
from .primitive_schemas import StringSchema, get_primitive_schema, AnySchema, PrimitiveSchema, IOSchema, NumberSchema
from .enum_schema import EnumSchema, HiddenModelEnumSchema, get_enum_schema
from .base_schema import BaseSchema
from .constant_schema import ConstantSchema
from .imports import FileImport, ImportType, TypingSection
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .parameter import Parameter, ParameterStyle, ParameterLocation, RequestBody
from .operation import Operation
from .property import Property
from .operation_group import OperationGroup
from .response import Response
from .parameter_list import ParameterList, GlobalParameterList
from .request_builder import RequestBuilder
from .base_builder import BaseBuilder
from .lro_paging_operation import LROPagingOperation
from .request_builder_parameter import RequestBuilderParameter
from .schema_request import SchemaRequest

__all__ = [
    "AzureKeyCredentialSchema",
    "AnySchema",
    "BaseModel",
    "BaseSchema",
    "CodeModel",
    "ConstantSchema",
    "ObjectSchema",
    "DictionarySchema",
    "ListSchema",
    "EnumSchema",
    "HiddenModelEnumSchema",
    "FileImport",
    "ImportType",
    "TypingSection",
    "PrimitiveSchema",
    "LROOperation",
    "Operation",
    "PagingOperation",
    "Parameter",
    "ParameterList",
    "ParameterLocation",
    "OperationGroup",
    "Property",
    "RequestBuilder",
    "Response",
    "TokenCredentialSchema",
    "LROPagingOperation",
    "BaseBuilder",
    "SchemaRequest",
    "RequestBuilderParameter",
    "HiddenModelObjectSchema",
    "ParameterStyle",
    "IOSchema",
    "GlobalParameterList",
    "RequestBody",
]

def _generate_as_object_schema(yaml_data: Dict[str, Any]) -> bool:
    if (
        yaml_data.get('properties') or
        yaml_data.get('discriminator') or
        yaml_data.get('parents') and yaml_data['parents'].get('immediate')
    ):
        return True
    return False


def build_type(yaml_data: Dict[str, Any], code_model: CodeModel) -> BaseSchema:
    yaml_id = id(yaml_data)
    try:
        return code_model.lookup_schema(yaml_id)
    except KeyError:
        # Not created yet, let's create it and add it to the index
        pass
    type_to_object = {
        "integer": NumberSchema,
        "string": StringSchema,
        "model": ObjectSchema,
        "array": ListSchema,
    }[yaml_data["type"]]
    response = type_to_object.from_yaml(yaml_data, code_model=code_model)
    code_model.types_map[yaml_id] = response
    return response
