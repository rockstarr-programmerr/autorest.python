# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodydate import AutoRestDateTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install autorestdatetestservice
# USAGE
    python date_put_max_date.py

"""


def main():
    client = AutoRestDateTestService()

    response = client.date.put_max_date(
        date_body="9999-12-31",
    )
    print(response)


if __name__ == "__main__":
    main()
