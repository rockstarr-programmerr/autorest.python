# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, Set, Union, TYPE_CHECKING
from .base_model import BaseModel
from .response import Response
from .schema_request import SchemaRequest

if TYPE_CHECKING:
    from .code_model import CodeModel


_M4_HEADER_PARAMETERS = ["content_type", "accept"]

def create_parameters(
    yaml_data: Dict[str, Any], code_model, parameter_creator: Callable
):
    multiple_requests = len(yaml_data["requests"]) > 1

    multiple_content_type_parameters = []
    parameters = [
        parameter_creator(yaml, code_model=code_model)
        for yaml in yaml_data.get("parameters", [])
    ]

    for request in yaml_data["requests"]:
        for yaml in request.get("parameters", []):
            parameter = parameter_creator(yaml, code_model=code_model)
            name = yaml["language"]["python"]["name"]
            if name in _M4_HEADER_PARAMETERS:
                parameters.append(parameter)
            elif multiple_requests:
                parameter.has_multiple_content_types = True
                multiple_content_type_parameters.append(parameter)
            else:
                parameters.append(parameter)

    if multiple_content_type_parameters:
        body_parameters_name_set = set(
            p.serialized_name for p in multiple_content_type_parameters
        )
        if len(body_parameters_name_set) > 1:
            raise ValueError(
            f"The body parameter with multiple media types has different names: {body_parameters_name_set}"
        )


    parameters_index = {id(parameter.yaml_data): parameter for parameter in parameters}

    # Need to connect the groupBy and originalParameter
    for parameter in parameters:
        parameter_grouped_by_id = id(parameter.grouped_by)
        if parameter_grouped_by_id in parameters_index:
            parameter.grouped_by = parameters_index[parameter_grouped_by_id]

        parameter_original_id = id(parameter.original_parameter)
        if parameter_original_id in parameters_index:
            parameter.original_parameter = parameters_index[parameter_original_id]

    return parameters, multiple_content_type_parameters

class BaseBuilder(BaseModel):
    """Base class for Operations and Request Builders"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        parameters,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = name
        self.parameters = parameters
        self.summary = yaml_data.get("summary", "")
        self.path = yaml_data["path"]
        self.verb = yaml_data["verb"]
        self.description = yaml_data.get("description", "")
        self.status_code_to_responses = {
            sc: [Response.from_yaml(r, code_model) for r in responses]
            for sc, responses in yaml_data["responses"].items()
        }

    @property
    def has_response_body(self) -> bool:
        return any(r.type for r in self.responses)

    @property
    def successful_status_codes(self) -> List[str]:
        return [sc for sc in self.status_code_to_responses if sc != "*"]

    @property
    def responses(self) -> List[Response]:
        retval: List[Response] = []
        seen_responses: Set[int] = set()
        for responses in self.status_code_to_responses.values():
            for response in responses:
                if id(response.yaml_data) not in seen_responses:
                    retval.append(response)
                seen_responses.add(id(response.yaml_data))
        return retval
