import pytest
from apimatic_core.exceptions.auth_validation_exception import AuthValidationException

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.site_response import SiteResponse

from .data import AuthorizeAssertCases
from .utils import assert_properties


class TestAuthorization:
    def test_no_token_or_password_to_client_create(self):
        with pytest.raises(AuthValidationException):
            client = AdvancedBillingClient(basic_auth_credentials=BasicAuthCredentials(
                username="token",
                password=""
            ))
            client.sites.read_site()

        with pytest.raises(AuthValidationException):
            client = AdvancedBillingClient(basic_auth_credentials=BasicAuthCredentials(
                username="",
                password="password"
            ))
            client.sites.read_site()

    def test_unauthorized(self, unauthorized_client: AdvancedBillingClient):
        with pytest.raises(APIException):
            unauthorized_client.sites.read_site()

    def test_authorized(self, client: AdvancedBillingClient):
        result = client.sites.read_site()

        assert isinstance(result, SiteResponse)
        assert_properties(result, AuthorizeAssertCases.get_result_data())
