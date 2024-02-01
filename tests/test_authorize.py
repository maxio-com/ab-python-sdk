import pytest
from apimatic_core.exceptions.auth_validation_exception import AuthValidationException

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.models.site_response import SiteResponse


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
        assert site.id == 4502
        assert site.name == "Python SDK Env"
        assert site.subdomain == "python-sdk"
        assert site.currency == "USD"
        assert site.seller_id == 722159
        assert site.relationship_invoicing_enabled is True
        assert site.customer_hierarchy_enabled is False
        assert site.whopays_enabled is False
        assert site.whopays_default_payer == "self-ungrouped"
        assert site.test is True
        assert site.default_payment_collection_method == "automatic"

        allocation_settings = site.allocation_settings
        assert allocation_settings.accrue_charge == "true"
        assert allocation_settings.upgrade_charge == "prorated"
        assert allocation_settings.downgrade_credit == "none"

        organization_address = site.organization_address
        assert organization_address.street == "Asdf Street"
        assert organization_address.line_2 == "123/444"
        assert organization_address.city == "San Antonio"
        assert organization_address.state == "TX"
        assert organization_address.zip == "78015"
        assert organization_address.country == "US"
        assert organization_address.name == "Developer Experience"
        assert organization_address.phone == "555 111 222"

        tax_configuration = site.tax_configuration
        assert tax_configuration.kind == "custom"
        assert tax_configuration.destination_address == "shipping_then_billing"
        assert tax_configuration.fully_configured is False

        net_terms = site.net_terms
        assert net_terms.default_net_terms == 0
        assert net_terms.automatic_net_terms == 0
        assert net_terms.remittance_net_terms == 0
        assert net_terms.net_terms_on_remittance_signups_enabled is False
        assert net_terms.custom_net_terms_enabled is False
