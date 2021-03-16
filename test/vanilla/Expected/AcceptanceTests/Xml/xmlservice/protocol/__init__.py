# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import _prepare_xml_get_complex_type_ref_no_meta_request
    from ._preparers_py3 import _prepare_xml_put_complex_type_ref_no_meta_request
    from ._preparers_py3 import _prepare_xml_get_complex_type_ref_with_meta_request
    from ._preparers_py3 import _prepare_xml_put_complex_type_ref_with_meta_request
    from ._preparers_py3 import _prepare_xml_get_simple_request
    from ._preparers_py3 import _prepare_xml_put_simple_request
    from ._preparers_py3 import _prepare_xml_get_wrapped_lists_request
    from ._preparers_py3 import _prepare_xml_put_wrapped_lists_request
    from ._preparers_py3 import _prepare_xml_get_headers_request
    from ._preparers_py3 import _prepare_xml_get_empty_list_request
    from ._preparers_py3 import _prepare_xml_put_empty_list_request
    from ._preparers_py3 import _prepare_xml_get_empty_wrapped_lists_request
    from ._preparers_py3 import _prepare_xml_put_empty_wrapped_lists_request
    from ._preparers_py3 import _prepare_xml_get_root_list_request
    from ._preparers_py3 import _prepare_xml_put_root_list_request
    from ._preparers_py3 import _prepare_xml_get_root_list_single_item_request
    from ._preparers_py3 import _prepare_xml_put_root_list_single_item_request
    from ._preparers_py3 import _prepare_xml_get_empty_root_list_request
    from ._preparers_py3 import _prepare_xml_put_empty_root_list_request
    from ._preparers_py3 import _prepare_xml_get_empty_child_element_request
    from ._preparers_py3 import _prepare_xml_put_empty_child_element_request
    from ._preparers_py3 import _prepare_xml_list_containers_request
    from ._preparers_py3 import _prepare_xml_get_service_properties_request
    from ._preparers_py3 import _prepare_xml_put_service_properties_request
    from ._preparers_py3 import _prepare_xml_get_acls_request
    from ._preparers_py3 import _prepare_xml_put_acls_request
    from ._preparers_py3 import _prepare_xml_list_blobs_request
    from ._preparers_py3 import _prepare_xml_json_input_request
    from ._preparers_py3 import _prepare_xml_json_output_request
    from ._preparers_py3 import _prepare_xml_get_xms_text_request
    from ._preparers_py3 import _prepare_xml_get_bytes_request
    from ._preparers_py3 import _prepare_xml_put_binary_request
    from ._preparers_py3 import _prepare_xml_get_uri_request
    from ._preparers_py3 import _prepare_xml_put_uri_request
except (SyntaxError, ImportError):
    from ._preparers import _prepare_xml_get_complex_type_ref_no_meta_request  # type: ignore
    from ._preparers import _prepare_xml_put_complex_type_ref_no_meta_request  # type: ignore
    from ._preparers import _prepare_xml_get_complex_type_ref_with_meta_request  # type: ignore
    from ._preparers import _prepare_xml_put_complex_type_ref_with_meta_request  # type: ignore
    from ._preparers import _prepare_xml_get_simple_request  # type: ignore
    from ._preparers import _prepare_xml_put_simple_request  # type: ignore
    from ._preparers import _prepare_xml_get_wrapped_lists_request  # type: ignore
    from ._preparers import _prepare_xml_put_wrapped_lists_request  # type: ignore
    from ._preparers import _prepare_xml_get_headers_request  # type: ignore
    from ._preparers import _prepare_xml_get_empty_list_request  # type: ignore
    from ._preparers import _prepare_xml_put_empty_list_request  # type: ignore
    from ._preparers import _prepare_xml_get_empty_wrapped_lists_request  # type: ignore
    from ._preparers import _prepare_xml_put_empty_wrapped_lists_request  # type: ignore
    from ._preparers import _prepare_xml_get_root_list_request  # type: ignore
    from ._preparers import _prepare_xml_put_root_list_request  # type: ignore
    from ._preparers import _prepare_xml_get_root_list_single_item_request  # type: ignore
    from ._preparers import _prepare_xml_put_root_list_single_item_request  # type: ignore
    from ._preparers import _prepare_xml_get_empty_root_list_request  # type: ignore
    from ._preparers import _prepare_xml_put_empty_root_list_request  # type: ignore
    from ._preparers import _prepare_xml_get_empty_child_element_request  # type: ignore
    from ._preparers import _prepare_xml_put_empty_child_element_request  # type: ignore
    from ._preparers import _prepare_xml_list_containers_request  # type: ignore
    from ._preparers import _prepare_xml_get_service_properties_request  # type: ignore
    from ._preparers import _prepare_xml_put_service_properties_request  # type: ignore
    from ._preparers import _prepare_xml_get_acls_request  # type: ignore
    from ._preparers import _prepare_xml_put_acls_request  # type: ignore
    from ._preparers import _prepare_xml_list_blobs_request  # type: ignore
    from ._preparers import _prepare_xml_json_input_request  # type: ignore
    from ._preparers import _prepare_xml_json_output_request  # type: ignore
    from ._preparers import _prepare_xml_get_xms_text_request  # type: ignore
    from ._preparers import _prepare_xml_get_bytes_request  # type: ignore
    from ._preparers import _prepare_xml_put_binary_request  # type: ignore
    from ._preparers import _prepare_xml_get_uri_request  # type: ignore
    from ._preparers import _prepare_xml_put_uri_request  # type: ignore

__all__ = [
    "_prepare_xml_get_complex_type_ref_no_meta_request",
    "_prepare_xml_put_complex_type_ref_no_meta_request",
    "_prepare_xml_get_complex_type_ref_with_meta_request",
    "_prepare_xml_put_complex_type_ref_with_meta_request",
    "_prepare_xml_get_simple_request",
    "_prepare_xml_put_simple_request",
    "_prepare_xml_get_wrapped_lists_request",
    "_prepare_xml_put_wrapped_lists_request",
    "_prepare_xml_get_headers_request",
    "_prepare_xml_get_empty_list_request",
    "_prepare_xml_put_empty_list_request",
    "_prepare_xml_get_empty_wrapped_lists_request",
    "_prepare_xml_put_empty_wrapped_lists_request",
    "_prepare_xml_get_root_list_request",
    "_prepare_xml_put_root_list_request",
    "_prepare_xml_get_root_list_single_item_request",
    "_prepare_xml_put_root_list_single_item_request",
    "_prepare_xml_get_empty_root_list_request",
    "_prepare_xml_put_empty_root_list_request",
    "_prepare_xml_get_empty_child_element_request",
    "_prepare_xml_put_empty_child_element_request",
    "_prepare_xml_list_containers_request",
    "_prepare_xml_get_service_properties_request",
    "_prepare_xml_put_service_properties_request",
    "_prepare_xml_get_acls_request",
    "_prepare_xml_put_acls_request",
    "_prepare_xml_list_blobs_request",
    "_prepare_xml_json_input_request",
    "_prepare_xml_json_output_request",
    "_prepare_xml_get_xms_text_request",
    "_prepare_xml_get_bytes_request",
    "_prepare_xml_put_binary_request",
    "_prepare_xml_get_uri_request",
    "_prepare_xml_put_uri_request",
]