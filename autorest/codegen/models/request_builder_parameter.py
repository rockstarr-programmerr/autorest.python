# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, TYPE_CHECKING
from .parameter import ParameterOnlyPathAndBodyPositional, ParameterLocation, ParameterStyle, get_target_property_name
from .utils import get_schema

if TYPE_CHECKING:
    from .code_model import CodeModel

def _make_public(name):
    if name[0] == "_":
        return name[1:]
    return name

class RequestBuilderParameter(ParameterOnlyPathAndBodyPositional):

    @property
    def in_method_signature(self) -> bool:
        return not(
            # if not inputtable, don't put in signature
            not self.inputtable_by_user
            # If i'm not in the method code, no point in being in signature
            or not self.in_method_code
            # If I'm a flattened property of a body, don't want me, want the body param
            # or self.target_property_name
            or not self.in_method_code
        )

    @property
    def name_in_high_level_operation(self) -> str:
        # template = "{}" if self.code_model.options["version_tolerant"] else "_{}"
        # if self.is_multipart:
        #     return template.format("files")
        # if self.is_data_input:
        #     return template.format("data")
        # if self.is_body and not self.constant:
        #     return f"_{self.serialized_name}"
        # name = self.yaml_data["language"]["python"]["name"]
        # if self.implementation == "Client" and self.in_method_code:
        #     # for these, we're passing the client params to the request builder.
        #     # Need the self._config prefix
        #     name = f"self._config.{name}"
        # return name
        return self.serialized_name

    @property
    def in_method_code(self) -> bool:
        if self.location == ParameterLocation.Uri:
            # don't want any base url path formatting arguments
            return False
        return super(RequestBuilderParameter, self).in_method_code

    @property
    def default_value_declaration(self) -> Optional[str]:
        if self.serialized_name == "content_type":
            # in request builders we're in a weird scenario
            # we need to know what the types of content_type are
            # but we want to serialize content_type with no default.
            # So, we just return None in default_value_declaration for now
            return "None"
        return super().default_value_declaration

    @property
    def is_keyword_only(self) -> bool:
        return not self.location == ParameterLocation.Path and not self.is_kwarg

    @is_keyword_only.setter
    def is_keyword_only(self, val: bool) -> None:
        self._keyword_only = val
        self.is_kwarg = False

    @property
    def full_serialized_name(self) -> str:
        return self.serialized_name
