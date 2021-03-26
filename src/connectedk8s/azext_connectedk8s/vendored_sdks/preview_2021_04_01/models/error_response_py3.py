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


class ErrorResponse(Model):
    """Error response.

    Common error response for all Azure Resource Manager APIs to return error
    details for failed operations. (This also follows the OData error response
    format.).

    :param error: The error object.
    :type error: ~azure.mgmt.hybridkubernetes.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)
