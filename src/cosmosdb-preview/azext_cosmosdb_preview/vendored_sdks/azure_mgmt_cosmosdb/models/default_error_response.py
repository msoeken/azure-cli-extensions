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
from msrest.exceptions import HttpOperationError


class DefaultErrorResponse(Model):
    """An error response from the service.

    :param error:
    :type error: ~azure.mgmt.cosmosdb.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(DefaultErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class DefaultErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'DefaultErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(DefaultErrorResponseException, self).__init__(deserialize, response, 'DefaultErrorResponse', *args)
