# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_test_one_request
    from ._preparers_py3 import prepare_test_different_calls_request
    from ._preparers_py3 import prepare_operationgroupone_test_two_request
    from ._preparers_py3 import prepare_operationgroupone_test_three_request
    from ._preparers_py3 import prepare_operationgrouptwo_test_four_request
except (SyntaxError, ImportError):
    from ._preparers import prepare_test_one_request  # type: ignore
    from ._preparers import prepare_test_different_calls_request  # type: ignore
    from ._preparers import prepare_operationgroupone_test_two_request  # type: ignore
    from ._preparers import prepare_operationgroupone_test_three_request  # type: ignore
    from ._preparers import prepare_operationgrouptwo_test_four_request  # type: ignore

__all__ = [
    'prepare_test_one_request',
    'prepare_test_different_calls_request',
    'prepare_operationgroupone_test_two_request',
    'prepare_operationgroupone_test_three_request',
    'prepare_operationgrouptwo_test_four_request',
]