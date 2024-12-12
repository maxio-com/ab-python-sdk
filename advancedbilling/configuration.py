# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from enum import Enum
from advancedbilling.api_helper import APIHelper
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    # Default Advanced Billing environment hosted in US. Valid for the majority of our customers.
    US = 0
    # Advanced Billing environment hosted in EU. Use only when you requested EU hosting for your AB account.
    EU = 1


class Server(Enum):
    """An enum for API servers"""
    PRODUCTION = 0
    EBB = 1


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def site(self):
        return self._site

    @property
    def basic_auth_credentials(self):
        return self._basic_auth_credentials

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=120, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.US, site='subdomain',
                 basic_auth_credentials=None):
        if retry_methods is None:
            retry_methods = ['GET', 'PUT']

        if retry_statuses is None:
            retry_statuses = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]

        super().__init__(http_client_instance,
                         override_http_client_configuration, http_call_back,
                         timeout, max_retries, backoff_factor, retry_statuses,
                         retry_methods)

        # Current API environment
        self._environment = environment

        # The subdomain for your Advanced Billing site.
        self._site = site

        self._basic_auth_credentials = basic_auth_credentials

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   site=None, basic_auth_credentials=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        site = site or self.site
        basic_auth_credentials = basic_auth_credentials or self.basic_auth_credentials
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, site=site,
            basic_auth_credentials=basic_auth_credentials
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout, max_retries=self.max_retries,
            backoff_factor=self.backoff_factor, retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
            response_factory=self.http_response_factory
        )

    # All the environments the SDK can run in
    environments = {
        Environment.US: {
            Server.PRODUCTION: 'https://{site}.chargify.com',
            Server.EBB: 'https://events.chargify.com/{site}'
        },
        Environment.EU: {
            Server.PRODUCTION: 'https://{site}.ebilling.maxio.com',
            Server.EBB: 'https://events.chargify.com/{site}'
        }
    }

    def get_base_uri(self, server=Server.PRODUCTION):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
            "site": {'value': self.site, 'encode': False},
        }

        return APIHelper.append_url_with_template_parameters(
            self.environments[self.environment][server], parameters
        )
