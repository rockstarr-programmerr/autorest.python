# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_get_null_request
    from ._request_builders_py3 import build_get_invalid_request
    from ._request_builders_py3 import build_get_overflow_int32_request
    from ._request_builders_py3 import build_get_underflow_int32_request
    from ._request_builders_py3 import build_get_overflow_int64_request
    from ._request_builders_py3 import build_get_underflow_int64_request
    from ._request_builders_py3 import build_put_max32_request
    from ._request_builders_py3 import build_put_max64_request
    from ._request_builders_py3 import build_put_min32_request
    from ._request_builders_py3 import build_put_min64_request
    from ._request_builders_py3 import build_get_unix_time_request
    from ._request_builders_py3 import build_put_unix_time_date_request
    from ._request_builders_py3 import build_get_invalid_unix_time_request
    from ._request_builders_py3 import build_get_null_unix_time_request
except (SyntaxError, ImportError):
    from ._request_builders import build_get_null_request  # type: ignore
    from ._request_builders import build_get_invalid_request  # type: ignore
    from ._request_builders import build_get_overflow_int32_request  # type: ignore
    from ._request_builders import build_get_underflow_int32_request  # type: ignore
    from ._request_builders import build_get_overflow_int64_request  # type: ignore
    from ._request_builders import build_get_underflow_int64_request  # type: ignore
    from ._request_builders import build_put_max32_request  # type: ignore
    from ._request_builders import build_put_max64_request  # type: ignore
    from ._request_builders import build_put_min32_request  # type: ignore
    from ._request_builders import build_put_min64_request  # type: ignore
    from ._request_builders import build_get_unix_time_request  # type: ignore
    from ._request_builders import build_put_unix_time_date_request  # type: ignore
    from ._request_builders import build_get_invalid_unix_time_request  # type: ignore
    from ._request_builders import build_get_null_unix_time_request  # type: ignore

__all__ = [
    "build_get_null_request",
    "build_get_invalid_request",
    "build_get_overflow_int32_request",
    "build_get_underflow_int32_request",
    "build_get_overflow_int64_request",
    "build_get_underflow_int64_request",
    "build_put_max32_request",
    "build_put_max64_request",
    "build_put_min32_request",
    "build_put_min64_request",
    "build_get_unix_time_request",
    "build_put_unix_time_date_request",
    "build_get_invalid_unix_time_request",
    "build_get_null_unix_time_request",
]