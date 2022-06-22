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
    python datetime_put_local_positive_offset_max_date_time.py

"""


def main():
    client = AutoRestDateTimeTestService()

    response = client.datetime.put_local_positive_offset_max_date_time(
        datetime_body="9999-12-31T23:59:59.999+14:00",
    )
    print(response)


if __name__ == "__main__":
    main()
