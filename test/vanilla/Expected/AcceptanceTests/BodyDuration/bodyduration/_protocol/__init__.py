# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_duration_get_null_request
    from ._preparers_py3 import prepare_duration_put_positive_duration_request
    from ._preparers_py3 import prepare_duration_get_positive_duration_request
    from ._preparers_py3 import prepare_duration_get_invalid_request
except (SyntaxError, ImportError):
    from ._preparers import prepare_duration_get_null_request  # type: ignore
    from ._preparers import prepare_duration_put_positive_duration_request  # type: ignore
    from ._preparers import prepare_duration_get_positive_duration_request  # type: ignore
    from ._preparers import prepare_duration_get_invalid_request  # type: ignore

__all__ = [
    "prepare_duration_get_null_request",
    "prepare_duration_put_positive_duration_request",
    "prepare_duration_get_positive_duration_request",
    "prepare_duration_get_invalid_request",
]