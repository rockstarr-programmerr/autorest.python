# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from custombaseurlpaging import AutoRestParameterizedHostTestPagingClient

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install autorestparameterizedhosttestpagingclient
# USAGE
    python paging_get_pages_partial_url.py

"""


def main():
    client = AutoRestParameterizedHostTestPagingClient()

    response = client.paging.get_pages_partial_url(
        account_name="testaccount",
    )
    response = [item for item in response]
    print(response)


if __name__ == "__main__":
    main()
