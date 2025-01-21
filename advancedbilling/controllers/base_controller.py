# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import platform
from apimatic_core.api_call import ApiCall
from apimatic_core.types.error_case import ErrorCase
from advancedbilling.exceptions.api_exception import APIException


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        new_api_call_builder (APICall): Returns the API Call builder instance.

    """

    @staticmethod
    def user_agent():
        return 'AB SDK Python:6.1.0 on OS {os-info}'

    @staticmethod
    def user_agent_parameters():
        return {
            'os-info': {'value': platform.system(), 'encode': False},
        }

    @staticmethod
    def global_errors():
        return {
            'default': ErrorCase().error_message_template('HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.').exception_type(APIException),
            '404': ErrorCase().error_message_template('Not Found:\'{$response.body}\'').exception_type(APIException),
        }

    def __init__(self, config):
        self._config = config.get_http_client_configuration()
        self._http_call_back = self.config.http_callback
        self.api_call = ApiCall(config)

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    @property
    def new_api_call_builder(self):
        return self.api_call.new_builder
