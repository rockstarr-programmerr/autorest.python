# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod
from collections.abc import MutableSequence
from enum import Enum
import logging
from typing import List, Optional, TYPE_CHECKING, Union, Generic, TypeVar, cast
from .request_builder_parameter import RequestBuilderMultipleTypeBodyParameter, RequestBuilderSingleTypeBodyParameter, RequestBuilderParameter
from .parameter import ParameterLocation, SingleTypeBodyParameter, MultipleTypeBodyParameter, Parameter, ParameterMethodLocation, ClientParameter, ConfigParameter

ParameterType = TypeVar("ParameterType", bound=Union[Parameter, RequestBuilderParameter])
BodyParameterType = TypeVar("BodyParameterType", bound=Union[SingleTypeBodyParameter, MultipleTypeBodyParameter, RequestBuilderSingleTypeBodyParameter])


if TYPE_CHECKING:
    from .code_model import CodeModel

class ParameterImplementation(Enum):
    METHOD = "method"
    CLIENT = "client"

_LOGGER = logging.getLogger(__name__)


def method_signature_helper(
    positional: List[str], keyword_only: Optional[List[str]], kwarg_params: List[str]
):
    keyword_only = keyword_only or []
    return positional + keyword_only + kwarg_params

def _sort(params):
    return sorted(
        params, key=lambda x: not (x.client_default_value or x.optional), reverse=True
    )


class _ParameterListBase(MutableSequence, Generic[ParameterType, BodyParameterType]):  # pylint: disable=too-many-public-methods
    def __init__(
        self,
        code_model: "CodeModel",
        parameters: List[ParameterType],
        body_parameter: Optional[BodyParameterType] = None,
    ) -> None:
        self.code_model = code_model
        self.parameters = parameters or []
        self._body_parameter = body_parameter

    # MutableSequence

    def __getitem__(self, index):
        if isinstance(index, str):
            raise TypeError(f"{index} is invalid type")
        return self.parameters[index]

    def __len__(self) -> int:
        return len(self.parameters)

    def __setitem__(self, index, parameter):
        self.parameters[index] = parameter

    def __delitem__(self, index):
        del self.parameters[index]

    def insert(self, index: int, value: ParameterType) -> None:
        self.parameters.insert(index, value)

    # Parameter helpers

    @property
    def body_parameter(self) -> BodyParameterType:
        if not self._body_parameter:
            raise ValueError("There is no body parameter")
        return self._body_parameter

    @property
    def has_body_parameter(self) -> bool:
        return bool(self._body_parameter)

    @property
    def path(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location in (ParameterLocation.PATH, ParameterLocation.ENDPOINT_PATH)]

    @property
    def query(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location == ParameterLocation.QUERY]

    @property
    def headers(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location == ParameterLocation.HEADER]

    @property
    def grouped(self) -> List[ParameterType]:
        raise NotImplementedError("No parameter grouping")

    @property
    def groupers(self) -> List[ParameterType]:
        raise NotImplementedError("No parameter grouping")

    @property
    def constant(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.constant]

    @property
    def positional(self) -> List[Union[ParameterType, BodyParameterType]]:
        return _sort([
            p for p in self.unsorted_method_params if p.method_location == ParameterMethodLocation.POSITIONAL
        ])

    @property
    def keyword_only(self) -> List[Union[ParameterType, BodyParameterType]]:
        return _sort([
            p for p in self.unsorted_method_params if p.method_location == ParameterMethodLocation.KEYWORD_ONLY
        ])

    @property
    def kwarg(self) -> List[Union[ParameterType, BodyParameterType]]:
        return _sort([
            p for p in self.unsorted_method_params if p.method_location == ParameterMethodLocation.KWARG
        ])

    @property
    @abstractmethod
    def implementation(self) -> str:
        ...

    @property
    def unsorted_method_params(self) -> List[Union[ParameterType, BodyParameterType]]:
        method_params: List[Union[ParameterType, BodyParameterType]] = [p for p in self.parameters if p.in_method_signature and p.implementation == self.implementation]
        if self.has_body_parameter:
            method_params.append(self.body_parameter)
        return method_params

    @property
    def method(self) -> List[Union[ParameterType, BodyParameterType]]:
        return self.positional + self.keyword_only + self.kwarg

    def method_signature(self, is_python3_file: bool) -> List[str]:
        return method_signature_helper(
            positional=self.method_signature_positional(is_python3_file),
            keyword_only=self.method_signature_keyword_only(is_python3_file),
            kwarg_params=self.method_signature_kwargs(is_python3_file),
        )

    def method_signature_positional(self, is_python3_file: bool) -> List[str]:
        return [
            parameter.method_signature(is_python3_file) for parameter in self.positional
        ]

    def method_signature_keyword_only(self, is_python3_file: bool) -> List[str]:
        if not (self.keyword_only and is_python3_file):
            return []
        return ["*,"] + [
            parameter.method_signature(is_python3_file)
            for parameter in self.keyword_only
        ]

    @staticmethod
    def method_signature_kwargs(is_python3_file: bool) -> List[str]:
        return ["**kwargs: Any"] if is_python3_file else ["**kwargs  # type: Any"]

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Union[ParameterType, BodyParameterType]]:
        kwargs_to_pop = [p for p in self.method if p.method_location == ParameterMethodLocation.KWARG]
        if not is_python3_file:
            kwargs_to_pop += [p for p in self.method if p.method_location == ParameterMethodLocation.KEYWORD_ONLY]
        return kwargs_to_pop

    @property
    def call(self) -> List[str]:
        retval = [p.client_name for p in self.method if p.method_location == ParameterMethodLocation.POSITIONAL]
        retval.extend(
            [f"{p.client_name}={p.client_name}" for p in self.method if p.method_location == ParameterMethodLocation.KEYWORD_ONLY]
        )
        retval.append("**kwargs")
        return retval

class _ParameterList(_ParameterListBase[Parameter, BodyParameterType]):

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def path(self) -> List[Parameter]:
        return [k for k in super().path if k.location == ParameterLocation.ENDPOINT_PATH]

class ParameterList(_ParameterList[SingleTypeBodyParameter]):
    ...

class OverloadedOperationParameterList(_ParameterList[MultipleTypeBodyParameter]):
    """This parameter list is used if we have overloads for an operation due to multiple types of the body parameter"""
    ...

class _RequestBuilderParameterList(_ParameterListBase[RequestBuilderParameter, BodyParameterType]):

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def unsorted_method_params(self) -> List[Union[RequestBuilderParameter, BodyParameterType]]:
        return [k for k in super().unsorted_method_params if k.location != ParameterLocation.ENDPOINT_PATH]

    @property
    def path(self) -> List[RequestBuilderParameter]:
        return [p for p in super().path if p.location != ParameterLocation.ENDPOINT_PATH]


class RequestBuilderParameterList(_RequestBuilderParameterList[RequestBuilderSingleTypeBodyParameter]):
    ...


class OverloadedRequestBuilderParameterList(_RequestBuilderParameterList[RequestBuilderMultipleTypeBodyParameter]):
    def method_signature(self, is_python3_file: bool) -> List[str]:
        if self.positional:
            return ["*args", "**kwargs"]
        return ["**kwargs"]


class _ClientGlobalParameterList(_ParameterListBase[ParameterType, SingleTypeBodyParameter]):
    @property
    def implementation(self) -> str:
        return "Client"

    @property
    def credential(self) -> Optional[ParameterType]:
        try:
            return next(p for p in self.parameters if p.client_name == "credential")
        except StopIteration:
            return None

class ClientGlobalParameterList(_ClientGlobalParameterList[ClientParameter]):

    @property
    def path(self) -> List[ClientParameter]:
        return [p for p in super().path if not p.is_host]

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Union[ClientParameter, SingleTypeBodyParameter]]:
        return [
            k for k in super().kwargs_to_pop(is_python3_file=is_python3_file)
            if k.location == ParameterLocation.ENDPOINT_PATH
        ]


class ConfigGlobalParameterList(_ClientGlobalParameterList[ConfigParameter]):
    @property
    def implementation(self) -> str:
        return "Client"
