# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodydatetimeversiontolerant import AutoRestDateTimeTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install autorestdatetimetestservice
# USAGE
    python datetime_get_local_positive_offset_lowercase_max_date_time.py

"""


def main():
    client = AutoRestDateTimeTestService()

    response = client.datetime.get_local_positive_offset_lowercase_max_date_time()
    print(response)


if __name__ == "__main__":
    main()
