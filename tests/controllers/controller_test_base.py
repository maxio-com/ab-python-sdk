# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import unittest
from tests.http_response_catcher import HttpResponseCatcher
from maxioadvancedbillingformerlychargifyapi.configuration import Configuration
from maxioadvancedbillingformerlychargifyapi.configuration import Environment
from maxioadvancedbillingformerlychargifyapi.maxioadvancedbillingformerlychargifyapi_client import MaxioadvancedbillingformerlychargifyapiClient


class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 30
        cls.assert_precision = 0.01
        cls.config = ControllerTestBase.create_configuration()
        cls.client = MaxioadvancedbillingformerlychargifyapiClient(config=cls.config)
        cls.auth_managers = cls.client.auth_managers

    @staticmethod
    def create_configuration():
        return Configuration(http_call_back=HttpResponseCatcher())