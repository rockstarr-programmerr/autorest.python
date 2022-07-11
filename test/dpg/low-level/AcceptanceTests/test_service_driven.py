
# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import pytest
from azure.core.rest import HttpRequest

from dpgservicedriveninitiallowlevel import DPGClient as DPGClientInitial
from dpgservicedrivenupdateonelowlevel import DPGClient as DPGClientUpdateOne

from dpgservicedriveninitiallowlevel.rest import params as params_initial
from dpgservicedrivenupdateonelowlevel.rest import params as params_update_one


@pytest.fixture
def initial_client():
    with DPGClientInitial() as client:
        yield client

@pytest.fixture
def update_one_client():
    with DPGClientUpdateOne() as client:
        yield client

@pytest.fixture
def initial_send_request(initial_client, base_send_request):
    def _send_request(request):
        return base_send_request(initial_client, request)
    return _send_request

@pytest.fixture
def update_one_send_request(update_one_client, base_send_request):
    def _send_request(request):
        return base_send_request(update_one_client, request)
    return _send_request


def test_required_to_optional(initial_send_request, update_one_send_request):
    request = params_initial.build_get_required_request(parameter="foo")
    initial_send_request(request)

    request = params_update_one.build_get_required_request(parameter="foo", new_parameter="bar")
    update_one_send_request(request)

def test_add_optional_parameter_to_none(initial_send_request, update_one_send_request):
    request = params_initial.build_head_no_params_request()
    initial_send_request(request)

    request = params_update_one.build_head_no_params_request(new_parameter="bar")
    update_one_send_request(request)

def test_add_optional_parameter_to_required_optional(initial_send_request, update_one_send_request):
    request = params_initial.build_put_required_optional_request(required_param="foo", optional_param="bar")
    initial_send_request(request)

    request = params_update_one.build_put_required_optional_request(required_param="foo", optional_param="bar", new_parameter="baz")
    update_one_send_request(request)

def test_add_optional_parameter_to_optional(initial_send_request, update_one_send_request):
    request = params_initial.build_get_optional_request(optional_param="foo")
    initial_send_request(request)

    request = params_update_one.build_get_optional_request(optional_param="foo", new_parameter="bar")
    update_one_send_request(request)

def test_add_new_content_type(initial_send_request, update_one_send_request):
    request = params_initial.build_post_parameters_request(json={ "url": "http://example.org/myimage.jpeg" })
    initial_send_request(request)

    request = params_update_one.build_post_parameters_request(json={ "url": "http://example.org/myimage.jpeg" })
    update_one_send_request(request)
    request = params_update_one.build_post_parameters_request(content=b"hello", content_type="image/jpeg")
    update_one_send_request(request)

def test_add_new_operation(update_one_send_request):
    with pytest.raises(AttributeError):
        params_initial.build_delete_parameters_request()
    
    request = params_update_one.build_delete_parameters_request()
    update_one_send_request(request)

def test_add_new_path(update_one_send_request):
    with pytest.raises(AttributeError):
        params_initial.build_get_new_operation_request()
    
    request = params_update_one.build_get_new_operation_request()
    assert update_one_send_request(request).json() == {'message': 'An object was successfully returned'}

def test_glass_breaker(update_one_send_request):
    request = HttpRequest(method="GET", url="/servicedriven/glassbreaker", params=[], headers={"Accept": "application/json"})
    response = update_one_send_request(request)
    assert response.status_code == 200
    assert response.json() == {'message': 'An object was successfully returned'}