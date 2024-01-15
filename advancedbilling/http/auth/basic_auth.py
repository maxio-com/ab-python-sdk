# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth
from apimatic_core.utilities.auth_helper import AuthHelper


class BasicAuth(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication faliure
        in BasicAuth

        """
        return "BasicAuth: BasicAuthUserName or BasicAuthPassword is undefined."

    def __init__(self, basic_auth_user_name, basic_auth_password):
        auth_params = {}
        if basic_auth_user_name and basic_auth_password:
            auth_params = {"Authorization": "Basic {}".format(
                AuthHelper.get_base64_encoded_value(basic_auth_user_name, basic_auth_password))}
        super().__init__(auth_params=auth_params)
        self._basic_auth_user_name = basic_auth_user_name
        self._basic_auth_password = basic_auth_password
