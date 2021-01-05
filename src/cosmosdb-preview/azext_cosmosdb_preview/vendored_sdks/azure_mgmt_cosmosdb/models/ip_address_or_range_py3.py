# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IpAddressOrRange(Model):
    """IpAddressOrRange object.

    :param ip_address_or_range: A single IPv4 address or a single IPv4 address
     range in CIDR format. Provided IPs must be well-formatted and cannot be
     contained in one of the following ranges: 10.0.0.0/8, 100.64.0.0/10,
     172.16.0.0/12, 192.168.0.0/16, since these are not enforceable by the IP
     address filter. Example of valid inputs: “23.40.210.245” or
     “23.40.210.0/8”.
    :type ip_address_or_range: str
    """

    _attribute_map = {
        'ip_address_or_range': {'key': 'ipAddressOrRange', 'type': 'str'},
    }

    def __init__(self, *, ip_address_or_range: str=None, **kwargs) -> None:
        super(IpAddressOrRange, self).__init__(**kwargs)
        self.ip_address_or_range = ip_address_or_range
