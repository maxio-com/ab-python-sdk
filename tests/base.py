from os import getenv

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.controllers.components_controller import ComponentsController
from advancedbilling.controllers.customers_controller import CustomersController
from advancedbilling.controllers.payment_profiles_controller import PaymentProfilesController
from advancedbilling.controllers.product_families_controller import ProductFamiliesController
from advancedbilling.controllers.products_controller import ProductsController
from advancedbilling.controllers.sites_controller import SitesController
from advancedbilling.controllers.subscription_components_controller import SubscriptionComponentsController
from advancedbilling.controllers.subscriptions_controller import SubscriptionsController


class TestBase():
    def setup_class(self):
        self.client = AdvancedBillingClient(
            subdomain=getenv("SUBDOMAIN"),
            domain=getenv("DOMAIN"),
            basic_auth_user_name=getenv("BASIC_AUTH_USERNAME"),
            basic_auth_password=getenv("BASIC_AUTH_PASSWORD")
        )

    def get_products_controller(self) -> ProductsController:
        return self.client.products

    def get_product_families_controller(self) -> ProductFamiliesController:
        return self.client.product_families

    def get_customers_controller(self) -> CustomersController:
        return self.client.customers

    def get_subscriptions_controller(self) -> SubscriptionsController:
        return self.client.subscriptions

    def get_components_controller(self) -> ComponentsController:
        return self.client.components

    def get_payment_profiles_controller(self) -> PaymentProfilesController:
        return self.client.payment_profiles

    def get_sites_controller(self) -> SitesController:
        return self.client.sites

    def get_subscription_components_controller(self) -> SubscriptionComponentsController:
        return self.client.subscription_components
