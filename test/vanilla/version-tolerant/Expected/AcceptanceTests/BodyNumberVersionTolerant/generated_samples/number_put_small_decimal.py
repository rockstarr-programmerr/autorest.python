# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodynumberversiontolerant import AutoRestNumberTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install autorestnumbertestservice
# USAGE
    python number_put_small_decimal.py

"""


def main():
    client = AutoRestNumberTestService()

    response = client.number.put_small_decimal(
        number_body=2.5976931e-101,
    )
    print(response)


if __name__ == "__main__":
    main()
