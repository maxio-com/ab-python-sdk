from os import getenv

import pytest
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

        site = result.site
        assert 4502 == site.id
        assert 'Python SDK Env' == site.name
        assert 'python-sdk' == site.subdomain
        assert 'USD' == site.currency
        assert 722159 == site.seller_id
        assert True == site.relationship_invoicing_enabled
        assert False == site.customer_hierarchy_enabled
        assert False == site.whopays_enabled
        assert 'self-ungrouped' == site.whopays_default_payer
        assert True == site.test
        assert 'automatic' == site.default_payment_collection_method

        allocation_settings = site.allocation_settings
        assert 'true' == allocation_settings.accrue_charge
        assert 'prorated' == allocation_settings.upgrade_charge
        assert 'none' == allocation_settings.downgrade_credit

        organization_address = site.organization_address
        assert 'Asdf Street' == organization_address.street
        assert '123/444' == organization_address.line_2
        assert 'San Antonio' == organization_address.city
        assert 'TX' == organization_address.state
        assert '78015' == organization_address.zip
        assert 'US' == organization_address.country
        assert 'Developer Experience' == organization_address.name
        assert '555 111 222' == organization_address.phone

        tax_configuration = site.tax_configuration
        assert 'custom' == tax_configuration.kind
        assert 'shipping_then_billing' == tax_configuration.destination_address
        assert False == tax_configuration.fully_configured

        net_terms = site.net_terms
        assert 0 == net_terms.default_net_terms
        assert 0 == net_terms.automatic_net_terms
        assert 0 == net_terms.remittance_net_terms
        assert False == net_terms.net_terms_on_remittance_signups_enabled
        assert False == net_terms.custom_net_terms_enabled
