import os
from time import sleep

import pytest

from advancedbilling.advanced_billing_client import (
    AdvancedBillingClient,
    ComponentsController,
    CouponsController,
    CustomersController,
    CustomFieldsController,
    InvoicesController,
    PaymentProfilesController,
    ProductFamiliesController,
    ProductsController,
    SitesController,
    SubscriptionComponentsController,
    SubscriptionsController,
)
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.resource_type import ResourceType

BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
DOMAIN = os.getenv("DOMAIN")
SUBDOMAIN = os.getenv("SUBDOMAIN")


def clean_custom_fields(client: AdvancedBillingClient):
    for resource_type in [ResourceType.SUBSCRIPTIONS, ResourceType.CUSTOMERS]:
        options = {"resource_type": resource_type}

        metafields = client.custom_fields.list_metafields(options).metafields
        while metafields:
            for m in metafields:
                client.custom_fields.delete_metafield(resource_type, m.name)

            metafields = client.custom_fields.list_metafields(options).metafields


@pytest.fixture(scope="session", autouse=True)
def client() -> AdvancedBillingClient:
    client = AdvancedBillingClient(
        subdomain=SUBDOMAIN,
        domain=DOMAIN,
        basic_auth_credentials=BasicAuthCredentials(
            username=BASIC_AUTH_USERNAME,
            password=BASIC_AUTH_PASSWORD
        )
    )

    clean_custom_fields(client)
    client.sites.clear_site()
    sleep(10)  # Wait for site to be cleared as it takes some time

    yield client


@pytest.fixture(scope="session")
def unauthorized_client() -> AdvancedBillingClient:
    return AdvancedBillingClient(
        subdomain=SUBDOMAIN,
        domain=DOMAIN,
        basic_auth_credentials=BasicAuthCredentials(
            username="thisiswrongapitokenthisiswrongapitokenV8",
            password=BASIC_AUTH_PASSWORD
        )
    )


@pytest.fixture(scope="session")
def products_controller(client) -> ProductsController:
    return client.products


@pytest.fixture(scope="session")
def product_families_controller(client) -> ProductFamiliesController:
    return client.product_families


@pytest.fixture(scope="session")
def customers_controller(client) -> CustomersController:
    return client.customers


@pytest.fixture(scope="session")
def subscriptions_controller(client) -> SubscriptionsController:
    return client.subscriptions


@pytest.fixture(scope="session")
def components_controller(client) -> ComponentsController:
    return client.components


@pytest.fixture(scope="session")
def payment_profiles_controller(client) -> PaymentProfilesController:
    return client.payment_profiles


@pytest.fixture(scope="session")
def sites_controller(client) -> SitesController:
    return client.sites


@pytest.fixture(scope="session")
def subscription_components_controller(client) -> SubscriptionComponentsController:
    return client.subscription_components


@pytest.fixture(scope="session")
def custom_fields_controller(client) -> CustomFieldsController:
    return client.custom_fields


@pytest.fixture(scope="session")
def coupons_controller(client) -> CouponsController:
    return client.coupons


@pytest.fixture(scope="session")
def invoices_controller(client) -> InvoicesController:
    return client.invoices
