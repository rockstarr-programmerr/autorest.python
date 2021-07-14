# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_get_complex_type_ref_no_meta_request
    from ._request_builders_py3 import build_put_complex_type_ref_no_meta_request
    from ._request_builders_py3 import build_get_complex_type_ref_with_meta_request
    from ._request_builders_py3 import build_put_complex_type_ref_with_meta_request
    from ._request_builders_py3 import build_get_simple_request
    from ._request_builders_py3 import build_put_simple_request
    from ._request_builders_py3 import build_get_wrapped_lists_request
    from ._request_builders_py3 import build_put_wrapped_lists_request
    from ._request_builders_py3 import build_get_headers_request
    from ._request_builders_py3 import build_get_empty_list_request
    from ._request_builders_py3 import build_put_empty_list_request
    from ._request_builders_py3 import build_get_empty_wrapped_lists_request
    from ._request_builders_py3 import build_put_empty_wrapped_lists_request
    from ._request_builders_py3 import build_get_root_list_request
    from ._request_builders_py3 import build_put_root_list_request
    from ._request_builders_py3 import build_get_root_list_single_item_request
    from ._request_builders_py3 import build_put_root_list_single_item_request
    from ._request_builders_py3 import build_get_empty_root_list_request
    from ._request_builders_py3 import build_put_empty_root_list_request
    from ._request_builders_py3 import build_get_empty_child_element_request
    from ._request_builders_py3 import build_put_empty_child_element_request
    from ._request_builders_py3 import build_list_containers_request
    from ._request_builders_py3 import build_get_service_properties_request
    from ._request_builders_py3 import build_put_service_properties_request
    from ._request_builders_py3 import build_get_acls_request
    from ._request_builders_py3 import build_put_acls_request
    from ._request_builders_py3 import build_list_blobs_request
    from ._request_builders_py3 import build_json_input_request
    from ._request_builders_py3 import build_json_output_request
    from ._request_builders_py3 import build_get_xms_text_request
    from ._request_builders_py3 import build_get_bytes_request
    from ._request_builders_py3 import build_put_binary_request
    from ._request_builders_py3 import build_get_uri_request
    from ._request_builders_py3 import build_put_uri_request
except (SyntaxError, ImportError):
    from ._request_builders import build_get_complex_type_ref_no_meta_request  # type: ignore
    from ._request_builders import build_put_complex_type_ref_no_meta_request  # type: ignore
    from ._request_builders import build_get_complex_type_ref_with_meta_request  # type: ignore
    from ._request_builders import build_put_complex_type_ref_with_meta_request  # type: ignore
    from ._request_builders import build_get_simple_request  # type: ignore
    from ._request_builders import build_put_simple_request  # type: ignore
    from ._request_builders import build_get_wrapped_lists_request  # type: ignore
    from ._request_builders import build_put_wrapped_lists_request  # type: ignore
    from ._request_builders import build_get_headers_request  # type: ignore
    from ._request_builders import build_get_empty_list_request  # type: ignore
    from ._request_builders import build_put_empty_list_request  # type: ignore
    from ._request_builders import build_get_empty_wrapped_lists_request  # type: ignore
    from ._request_builders import build_put_empty_wrapped_lists_request  # type: ignore
    from ._request_builders import build_get_root_list_request  # type: ignore
    from ._request_builders import build_put_root_list_request  # type: ignore
    from ._request_builders import build_get_root_list_single_item_request  # type: ignore
    from ._request_builders import build_put_root_list_single_item_request  # type: ignore
    from ._request_builders import build_get_empty_root_list_request  # type: ignore
    from ._request_builders import build_put_empty_root_list_request  # type: ignore
    from ._request_builders import build_get_empty_child_element_request  # type: ignore
    from ._request_builders import build_put_empty_child_element_request  # type: ignore
    from ._request_builders import build_list_containers_request  # type: ignore
    from ._request_builders import build_get_service_properties_request  # type: ignore
    from ._request_builders import build_put_service_properties_request  # type: ignore
    from ._request_builders import build_get_acls_request  # type: ignore
    from ._request_builders import build_put_acls_request  # type: ignore
    from ._request_builders import build_list_blobs_request  # type: ignore
    from ._request_builders import build_json_input_request  # type: ignore
    from ._request_builders import build_json_output_request  # type: ignore
    from ._request_builders import build_get_xms_text_request  # type: ignore
    from ._request_builders import build_get_bytes_request  # type: ignore
    from ._request_builders import build_put_binary_request  # type: ignore
    from ._request_builders import build_get_uri_request  # type: ignore
    from ._request_builders import build_put_uri_request  # type: ignore

__all__ = [
    "build_get_complex_type_ref_no_meta_request",
    "build_put_complex_type_ref_no_meta_request",
    "build_get_complex_type_ref_with_meta_request",
    "build_put_complex_type_ref_with_meta_request",
    "build_get_simple_request",
    "build_put_simple_request",
    "build_get_wrapped_lists_request",
    "build_put_wrapped_lists_request",
    "build_get_headers_request",
    "build_get_empty_list_request",
    "build_put_empty_list_request",
    "build_get_empty_wrapped_lists_request",
    "build_put_empty_wrapped_lists_request",
    "build_get_root_list_request",
    "build_put_root_list_request",
    "build_get_root_list_single_item_request",
    "build_put_root_list_single_item_request",
    "build_get_empty_root_list_request",
    "build_put_empty_root_list_request",
    "build_get_empty_child_element_request",
    "build_put_empty_child_element_request",
    "build_list_containers_request",
    "build_get_service_properties_request",
    "build_put_service_properties_request",
    "build_get_acls_request",
    "build_put_acls_request",
    "build_list_blobs_request",
    "build_json_input_request",
    "build_json_output_request",
    "build_get_xms_text_request",
    "build_get_bytes_request",
    "build_put_binary_request",
    "build_get_uri_request",
    "build_put_uri_request",
]