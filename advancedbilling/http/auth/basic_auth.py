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
        """Display error message on occurrence of authentication failure
        in BasicAuth

        """
        return "BasicAuth: BasicAuthUserName or BasicAuthPassword is undefined."

    def __init__(self, basic_auth_credentials):
        auth_params = {}
        if basic_auth_credentials is not None \
                and basic_auth_credentials.username and basic_auth_credentials.password:
            auth_params = {"Authorization": "Basic {}".format(
                AuthHelper.get_base64_encoded_value(basic_auth_credentials.username, basic_auth_credentials.password))}
        super().__init__(auth_params=auth_params)


class BasicAuthCredentials:

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def __init__(self, username, password):
        if username is None:
            raise ValueError('username cannot be None')
        self._username = username
        if password is None:
            raise ValueError('password cannot be None')
        self._password = password

    def clone_with(self, username=None, password=None):
        return BasicAuthCredentials(username or self.username,
                                    password or self.password)
