# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, Union, Type, TYPE_CHECKING, cast
from .base_schema import BaseSchema
from .dictionary_schema import DictionarySchema
from .property import Property
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


class ObjectSchema(BaseSchema):  # pylint: disable=too-many-instance-attributes
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """

    def __init__(
        self, yaml_data: Dict[str, Any], code_model: "CodeModel", name: str, description: str = "", **kwargs
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = name
        self.description = description
        self.max_properties: Optional[int] = kwargs.pop("max_properties", None)
        self.min_properties: Optional[int] = kwargs.pop("min_properties", None)
        self.properties: List[Property] = kwargs.pop("properties", [])
        self.is_exception: bool = kwargs.pop("is_exception", False)
        self.base_models: List["ObjectSchema"] = []
        self.subtype_map: Optional[Dict[str, str]] = kwargs.pop("subtype_map", None)
        self.discriminator_name: Optional[str] = kwargs.pop("discriminator_name", None)
        self.discriminator_value: Optional[str] = kwargs.pop("discriminator_value", None)
        self._created_json_template_representation = False

    @property
    def serialization_type(self) -> str:
        return self.name

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        retval = f"_models.{self.name}"
        return retval if is_operation_file else f'"{retval}"'

    @property
    def docstring_type(self) -> str:
        return f"~{self.code_model.namespace}.models.{self.name}"

    @property
    def docstring_text(self) -> str:
        return self.name

    def get_declaration(self, value: Any) -> str:
        return f"{self.name}()"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    @property
    def has_xml_serialization_ctxt(self) -> bool:
        return False

    def xml_serialization_ctxt(self) -> Optional[str]:
        # object schema contains _xml_map, they don't need serialization context
        return ""

    def xml_map_content(self) -> Optional[str]:
        if not self.xml_metadata:
            raise ValueError("This object does not contain XML metadata")
        # This is NOT an error on the super call, we use the serialization context for "xml_map",
        # but we don't want to write a serialization context for an object.
        return super().xml_serialization_ctxt()

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        if self._created_json_template_representation:
            return "..."  # do this to avoid loop
        self._created_json_template_representation = True
        # don't add additional properties, because there's not really a concept of
        # additional properties in the template
        representation = {
            f'"{prop.rest_api_name}"': prop.get_json_template_representation(**kwargs)
            for prop in [
                p for p in self.properties
                if not (p.is_discriminator or p.name == "additional_properties")
            ]
        }
        try:
            # add discriminator prop if there is one
            discriminator = next(p for p in self.properties if p.is_discriminator)
            representation[
                discriminator.rest_api_name
            ] = self.discriminator_value or discriminator.rest_api_name
        except StopIteration:
            pass

        # once we've finished, we want to reset created_json_template_representation to false
        # so we can call it again
        self._created_json_template_representation = False
        return representation

    def get_files_and_data_template_representation(self, **kwargs: Any) -> Any:
        object_schema_names = kwargs.get("object_schema_names", [])
        object_schema_names.append(self.name)  # do tis to avoid circular
        kwargs["object_schema_names"] = object_schema_names
        return {
            "{}".format(
                prop.rest_api_name
            ): prop.get_files_and_data_template_representation(**kwargs)
            for prop in self.properties
        }


    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "ObjectSchema":
        """Returns a ClassType from the dict object constructed from a yaml file.

        WARNING: This guy might create an infinite loop.

        :param str name: The name of the class type.
        :param yaml_data: A representation of the schema of a class type from a yaml file.
        :type yaml_data: dict(str, str)
        :returns: A ClassType.
        :rtype: ~autorest.models.schema.ClassType
        """
        obj = cls(yaml_data, code_model, "", description="")
        obj.fill_instance_from_yaml(yaml_data, code_model)
        return obj

    def fill_instance_from_yaml(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        self.description = yaml_data.get("description", "")
        self.name = yaml_data["name"]
        extends = yaml_data.get("extends")
        if extends:
            try:
                parent = code_model.lookup_schema(id(extends))
            except KeyError:
                from . import build_type
                # Not created yet, let's create it and add it to the index
                parent = build_type(extends, code_model)
            self.base_models.append(cast(ObjectSchema, parent))
        discriminator = yaml_data.get("discriminator")
        if discriminator:
            # do discriminator stuff
            raise NotImplementedError("Don't have discriminator set up yet")
        for property in yaml_data["properties"]:
            self.properties.append(Property.from_yaml(property, code_model))

        if yaml_data.get("properties"):
            self.properties.extend([
                Property.from_yaml(p, code_model=code_model)
                for p in yaml_data["properties"]
            ])
        is_exception = False
        exceptions_set = None # FIXME: mark model as an error model in emitter
        if exceptions_set:
            if id(yaml_data) in exceptions_set:
                is_exception = True

        self.yaml_data = yaml_data
        self.is_exception = is_exception

    @property
    def has_readonly_or_constant_property(self) -> bool:
        return any(x.readonly or x.constant for x in self.properties)

    @property
    def property_with_discriminator(self) -> Any:
        try:
            return next(p for p in self.properties if getattr(p.type, "discriminator_name", None))
        except StopIteration:
            return None

    def imports(self) -> FileImport:
        file_import = FileImport()
        if self.is_exception:
            file_import.add_submodule_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)
        return file_import

    def model_file_imports(self) -> FileImport:
        file_import = self.imports()
        file_import.add_import("__init__", ImportType.LOCAL, typing_section=TypingSection.TYPING, alias="_models")
        return file_import

class HiddenModelObjectSchema(ObjectSchema):

    @property
    def serialization_type(self) -> str:
        return "object"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        if self.xml_metadata:
            return "ET.Element"
        return "JSONType"

    @property
    def docstring_type(self) -> str:
        if self.xml_metadata:
            return "ET.Element"
        return "JSONType"

    @property
    def docstring_text(self) -> str:
        if self.xml_metadata:
            return "XML Element"
        return "JSON object"

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        if self.xml_metadata:
            file_import.add_submodule_import("xml.etree", "ElementTree", ImportType.STDLIB, alias="ET")
        return file_import

def get_object_schema(code_model) -> Type[ObjectSchema]:
    if code_model.options["models_mode"]:
        return ObjectSchema
    return HiddenModelObjectSchema
