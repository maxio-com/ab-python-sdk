import pytest
from os import getenv

from apimatic_core.exceptions.auth_validation_exception import AuthValidationException

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.models.site_response import SiteResponse

from tests.base import TestBase


class TestAuthorization(TestBase):
    def test_no_token_or_password_to_client_create(self):
        with (pytest.raises(AuthValidationException)):
            client = AdvancedBillingClient(
                basic_auth_user_name="token",
                basic_auth_password=""
            )
            client.sites.read_site()

        with (pytest.raises(AuthValidationException)):
            client = AdvancedBillingClient(
                basic_auth_user_name="",
                basic_auth_password="password"
            )
            client.sites.read_site()

    def test_unauthorized(self):
        client = AdvancedBillingClient(
            subdomain=getenv("SUBDOMAIN"),
            domain=getenv("DOMAIN"),
            basic_auth_user_name="thisiswrongapitokenthisiswrongapitokenV8",
            basic_auth_password=getenv("BASIC_AUTH_PASSWORD")
        )

        with (pytest.raises(APIException)):
            client.sites.read_site()

    def test_authorized(self):
        result = self.client.sites.read_site()

        assert isinstance(result, SiteResponse)
