# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, Optional, TYPE_CHECKING, Union, overload

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_by_pet_id_request(
    pet_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/extensibleenums/pet/{petId}")
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_add_pet_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/extensibleenums/pet/addPet")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )

# fmt: on
class PetOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~extensibleenumsswagger.PetStoreInc`'s
        :attr:`pet` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_by_pet_id(
        self,
        pet_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.Pet
        """get pet by id.

        :param pet_id: Pet id. Required.
        :type pet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Pet]

        request = build_get_by_pet_id_request(
            pet_id=pet_id,
            template_url=self.get_by_pet_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Pet", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_pet_id.metadata = {"url": "/extensibleenums/pet/{petId}"}  # type: ignore

    @overload
    def add_pet(
        self,
        pet_param=None,  # type: Optional[_models.Pet]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.Pet
        """add pet.

        :param pet_param: pet param. Default value is None.
        :type pet_param: ~extensibleenumsswagger.models.Pet
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises: ~azure.core.exceptions.HttpResponseError
        """

    @overload
    def add_pet(
        self,
        pet_param=None,  # type: Optional[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.Pet
        """add pet.

        :param pet_param: pet param. Default value is None.
        :type pet_param: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises: ~azure.core.exceptions.HttpResponseError
        """

    @distributed_trace
    def add_pet(
        self,
        pet_param=None,  # type: Optional[Union[_models.Pet, IO]]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.Pet
        """add pet.

        :param pet_param: pet param. Is either a model type or a IO type. Default value is None.
        :type pet_param: ~extensibleenumsswagger.models.Pet or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Pet]

        _json = None
        _content = None
        if isinstance(pet_param, (IO, bytes)):
            _content = pet_param
        else:
            if pet_param is not None:
                _json = self._serialize.body(pet_param, "Pet")
            else:
                _json = None
            content_type = content_type or "application/json"

        request = build_add_pet_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.add_pet.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Pet", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add_pet.metadata = {"url": "/extensibleenums/pet/addPet"}  # type: ignore
