from os import getenv

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials


class TestBase():
    def setup_class(self):
        self.client = AdvancedBillingClient(
            subdomain=getenv("SUBDOMAIN"),
            domain=getenv("DOMAIN"),
            basic_auth_credentials=BasicAuthCredentials(
                username=getenv("BASIC_AUTH_USERNAME"),
                password=getenv("BASIC_AUTH_PASSWORD")
            )
        )
