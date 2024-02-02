import pytest
from apimatic_core.exceptions.auth_validation_exception import AuthValidationException

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.models.site_response import SiteResponse

from .data import AuthorizeAssertCases
from .utils import assert_properties


class TestAuthorization:
    def test_no_token_or_password_to_client_create(self):
        with pytest.raises(AuthValidationException):
            client = AdvancedBillingClient(basic_auth_user_name="token", basic_auth_password="")
            client.sites.read_site()

        with pytest.raises(AuthValidationException):
            client = AdvancedBillingClient(basic_auth_user_name="", basic_auth_password="password")
            client.sites.read_site()

    def test_unauthorized(self, unauthorized_client: AdvancedBillingClient):
        with pytest.raises(APIException):
            unauthorized_client.sites.read_site()

    def test_authorized(self, client: AdvancedBillingClient):
        result = client.sites.read_site()

        assert isinstance(result, SiteResponse)

        site = result.site
        assert_properties(site, AuthorizeAssertCases.get_site_data())

        allocation_settings = site.allocation_settings
        assert_properties(allocation_settings, AuthorizeAssertCases.get_allocation_settings_data())

        organization_address = site.organization_address
        assert_properties(organization_address, AuthorizeAssertCases.get_organization_address_data())

        tax_configuration = site.tax_configuration
        assert_properties(tax_configuration, AuthorizeAssertCases.get_tax_configuration_data())

        net_terms = site.net_terms
        assert_properties(net_terms, AuthorizeAssertCases.get_net_terms_data())
