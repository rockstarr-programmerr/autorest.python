# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, TypeVar, Dict
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter

T = TypeVar('T')
OrderedSet = Dict[T, None]

class RequestBuilderParameterList(ParameterList):

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Parameter]:
        # we don't want to pop the body kwargs in py2.7. We send them straight to HttpRequest
        kwargs_to_pop = self.kwargs
        if not is_python3_file:
            kwargs_to_pop += [k for k in self.keyword_only if not (k.is_body and not k.constant)]
        return kwargs_to_pop

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature. Includes both positional and kwargs
        """
        signature_parameters_no_default_value = []
        signature_parameters_default_value = []

        # Want all method parameters.
        # Also allow client parameters if they're going to be used in the request body.
        # i.e., path parameter, query parameter, header.
        parameters = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation or parameter.in_method_code
        )
        for parameter in parameters:
            if parameter.in_method_signature:
                if not parameter.default_value and parameter.optional:
                    signature_parameters_default_value.append(parameter)
                else:
                    signature_parameters_no_default_value.append(parameter)
        if self.request_body:
            signature_parameters_no_default_value.append(self.request_body)
        signature_parameters = signature_parameters_no_default_value + signature_parameters_default_value
        signature_parameters.sort(key=lambda item: item.is_keyword_only)
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
