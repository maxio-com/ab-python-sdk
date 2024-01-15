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
    # Production server
    PRODUCTION = 0
    # Production server
    ENVIRONMENT2 = 1


class Server(Enum):
    """An enum for API servers"""
    DEFAULT = 0


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def subdomain(self):
        return self._subdomain

    @property
    def domain(self):
        return self._domain

    @property
    def basic_auth_user_name(self):
        return self._basic_auth_user_name

    @property
    def basic_auth_password(self):
        return self._basic_auth_password

    def __init__(
        self, http_client_instance=None,
        override_http_client_configuration=False, http_call_back=None,
        timeout=30, max_retries=0, backoff_factor=2,
        retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
        retry_methods=['GET', 'PUT'], environment=Environment.PRODUCTION,
        subdomain='subdomain', domain='chargify.com',
        basic_auth_user_name='TODO: Replace',
        basic_auth_password='TODO: Replace'
    ):
        super().__init__(http_client_instance, override_http_client_configuration, http_call_back, timeout, max_retries,
                         backoff_factor, retry_statuses, retry_methods)
        # Current API environment
        self._environment = environment

        # The subdomain for your Chargify site.
        self._subdomain = subdomain

        # The Chargify server domain.
        self._domain = domain

        # The username to use with basic authentication
        self._basic_auth_user_name = basic_auth_user_name

        # The password to use with basic authentication
        self._basic_auth_password = basic_auth_password

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   subdomain=None, domain=None, basic_auth_user_name=None,
                   basic_auth_password=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        subdomain = subdomain or self.subdomain
        domain = domain or self.domain
        basic_auth_user_name = basic_auth_user_name or self.basic_auth_user_name
        basic_auth_password = basic_auth_password or self.basic_auth_password
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, subdomain=subdomain, domain=domain,
            basic_auth_user_name=basic_auth_user_name,
            basic_auth_password=basic_auth_password
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
        Environment.PRODUCTION: {
            Server.DEFAULT: 'https://{subdomain}.{domain}'
        },
        Environment.ENVIRONMENT2: {
            Server.DEFAULT: 'https://events.chargify.com'
        }
    }

    def get_base_uri(self, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
            "subdomain": {'value': self.subdomain, 'encode': False},
            "domain": {'value': self.domain, 'encode': False},
        }

        return APIHelper.append_url_with_template_parameters(
            self.environments[self.environment][server], parameters
        )
