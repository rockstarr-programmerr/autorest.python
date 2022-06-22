# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodybooleanversiontolerant import AutoRestBoolTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install autorestbooltestservice
# USAGE
    python bool_get_true.py

"""


def main():
    client = AutoRestBoolTestService()

    response = client.bool.get_true()
    print(response)


if __name__ == "__main__":
    main()
