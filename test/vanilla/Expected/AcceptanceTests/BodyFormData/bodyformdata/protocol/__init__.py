# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import _prepare_formdata_upload_file_request
    from ._preparers_py3 import _prepare_formdata_upload_file_via_body_request
    from ._preparers_py3 import _prepare_formdata_upload_files_request
except (SyntaxError, ImportError):
    from ._preparers import _prepare_formdata_upload_file_request  # type: ignore
    from ._preparers import _prepare_formdata_upload_file_via_body_request  # type: ignore
    from ._preparers import _prepare_formdata_upload_files_request  # type: ignore

__all__ = [
    "_prepare_formdata_upload_file_request",
    "_prepare_formdata_upload_file_via_body_request",
    "_prepare_formdata_upload_files_request",
]