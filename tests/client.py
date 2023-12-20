from os import getenv

from advancedbilling.advanced_billing_client import AdvancedBillingClient


def create_client():
    return AdvancedBillingClient(
        subdomain=getenv("SUBDOMAIN"),
        domain=getenv("DOMAIN"),
        basic_auth_user_name=getenv("BASIC_AUTH_USERNAME"),
        basic_auth_password=getenv("BASIC_AUTH_PASSWORD")
    )
