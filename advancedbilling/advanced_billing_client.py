"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from apimatic_core.configurations.global_configuration import (
    GlobalConfiguration,
)
from apimatic_core.decorators.lazy_property import (
    LazyProperty,
)

from advancedbilling.configuration import (
    Configuration,
    Environment,
)
from advancedbilling.controllers.advance_invoice_controller import (
    AdvanceInvoiceController,
)
from advancedbilling.controllers.api_exports_controller import (
    APIExportsController,
)
from advancedbilling.controllers.base_controller import (
    BaseController,
)
from advancedbilling.controllers.billing_portal_controller import (
    BillingPortalController,
)
from advancedbilling.controllers.component_price_points_controller import (
    ComponentPricePointsController,
)
from advancedbilling.controllers.components_controller import (
    ComponentsController,
)
from advancedbilling.controllers.coupons_controller import (
    CouponsController,
)
from advancedbilling.controllers.custom_fields_controller import (
    CustomFieldsController,
)
from advancedbilling.controllers.customers_controller import (
    CustomersController,
)
from advancedbilling.controllers.events_based_billing_segments_controller import (
    EventsBasedBillingSegmentsController,
)
from advancedbilling.controllers.events_controller import (
    EventsController,
)
from advancedbilling.controllers.insights_controller import (
    InsightsController,
)
from advancedbilling.controllers.invoices_controller import (
    InvoicesController,
)
from advancedbilling.controllers.offers_controller import (
    OffersController,
)
from advancedbilling.controllers.payment_profiles_controller import (
    PaymentProfilesController,
)
from advancedbilling.controllers.product_families_controller import (
    ProductFamiliesController,
)
from advancedbilling.controllers.product_price_points_controller import (
    ProductPricePointsController,
)
from advancedbilling.controllers.products_controller import (
    ProductsController,
)
from advancedbilling.controllers.proforma_invoices_controller import (
    ProformaInvoicesController,
)
from advancedbilling.controllers.reason_codes_controller import (
    ReasonCodesController,
)
from advancedbilling.controllers.referral_codes_controller import (
    ReferralCodesController,
)
from advancedbilling.controllers.sales_commissions_controller import (
    SalesCommissionsController,
)
from advancedbilling.controllers.sites_controller import (
    SitesController,
)
from advancedbilling.controllers.subscription_components_controller import (
    SubscriptionComponentsController,
)
from advancedbilling.controllers.subscription_group_invoice_account_controller import (
    SubscriptionGroupInvoiceAccountController,
)
from advancedbilling.controllers.subscription_group_status_controller import (
    SubscriptionGroupStatusController,
)
from advancedbilling.controllers.subscription_groups_controller import (
    SubscriptionGroupsController,
)
from advancedbilling.controllers.subscription_invoice_account_controller import (
    SubscriptionInvoiceAccountController,
)
from advancedbilling.controllers.subscription_notes_controller import (
    SubscriptionNotesController,
)
from advancedbilling.controllers.subscription_products_controller import (
    SubscriptionProductsController,
)
from advancedbilling.controllers.subscription_renewals_controller import (
    SubscriptionRenewalsController,
)
from advancedbilling.controllers.subscription_status_controller import (
    SubscriptionStatusController,
)
from advancedbilling.controllers.subscriptions_controller import (
    SubscriptionsController,
)
from advancedbilling.controllers.webhooks_controller import (
    WebhooksController,
)
from advancedbilling.http.auth.basic_auth import (
    BasicAuth,
)


class AdvancedBillingClient(object):
    """Client that provide access to the AdvancedBillingClient APIs."""

    @LazyProperty
    def api_exports(self):
        """Provide access to the APIExportsController endpoints."""
        return APIExportsController(self.global_configuration)

    @LazyProperty
    def advance_invoice(self):
        """Provide access to the AdvanceInvoiceController endpoints."""
        return AdvanceInvoiceController(self.global_configuration)

    @LazyProperty
    def billing_portal(self):
        """Provide access to the BillingPortalController endpoints."""
        return BillingPortalController(self.global_configuration)

    @LazyProperty
    def coupons(self):
        """Provide access to the CouponsController endpoints."""
        return CouponsController(self.global_configuration)

    @LazyProperty
    def components(self):
        """Provide access to the ComponentsController endpoints."""
        return ComponentsController(self.global_configuration)

    @LazyProperty
    def component_price_points(self):
        """Provide access to the ComponentPricePointsController endpoints."""
        return ComponentPricePointsController(self.global_configuration)

    @LazyProperty
    def customers(self):
        """Provide access to the CustomersController endpoints."""
        return CustomersController(self.global_configuration)

    @LazyProperty
    def custom_fields(self):
        """Provide access to the CustomFieldsController endpoints."""
        return CustomFieldsController(self.global_configuration)

    @LazyProperty
    def events(self):
        """Provide access to the EventsController endpoints."""
        return EventsController(self.global_configuration)

    @LazyProperty
    def events_based_billing_segments(self):
        """Provide access to the EventsBasedBillingSegmentsController endpoints."""
        return EventsBasedBillingSegmentsController(self.global_configuration)

    @LazyProperty
    def insights(self):
        """Provide access to the InsightsController endpoints."""
        return InsightsController(self.global_configuration)

    @LazyProperty
    def invoices(self):
        """Provide access to the InvoicesController endpoints."""
        return InvoicesController(self.global_configuration)

    @LazyProperty
    def offers(self):
        """Provide access to the OffersController endpoints."""
        return OffersController(self.global_configuration)

    @LazyProperty
    def payment_profiles(self):
        """Provide access to the PaymentProfilesController endpoints."""
        return PaymentProfilesController(self.global_configuration)

    @LazyProperty
    def product_families(self):
        """Provide access to the ProductFamiliesController endpoints."""
        return ProductFamiliesController(self.global_configuration)

    @LazyProperty
    def products(self):
        """Provide access to the ProductsController endpoints."""
        return ProductsController(self.global_configuration)

    @LazyProperty
    def product_price_points(self):
        """Provide access to the ProductPricePointsController endpoints."""
        return ProductPricePointsController(self.global_configuration)

    @LazyProperty
    def proforma_invoices(self):
        """Provide access to the ProformaInvoicesController endpoints."""
        return ProformaInvoicesController(self.global_configuration)

    @LazyProperty
    def reason_codes(self):
        """Provide access to the ReasonCodesController endpoints."""
        return ReasonCodesController(self.global_configuration)

    @LazyProperty
    def referral_codes(self):
        """Provide access to the ReferralCodesController endpoints."""
        return ReferralCodesController(self.global_configuration)

    @LazyProperty
    def sales_commissions(self):
        """Provide access to the SalesCommissionsController endpoints."""
        return SalesCommissionsController(self.global_configuration)

    @LazyProperty
    def sites(self):
        """Provide access to the SitesController endpoints."""
        return SitesController(self.global_configuration)

    @LazyProperty
    def subscriptions(self):
        """Provide access to the SubscriptionsController endpoints."""
        return SubscriptionsController(self.global_configuration)

    @LazyProperty
    def subscription_components(self):
        """Provide access to the SubscriptionComponentsController endpoints."""
        return SubscriptionComponentsController(self.global_configuration)

    @LazyProperty
    def subscription_groups(self):
        """Provide access to the SubscriptionGroupsController endpoints."""
        return SubscriptionGroupsController(self.global_configuration)

    @LazyProperty
    def subscription_group_invoice_account(self):
        """Provide access to the
        SubscriptionGroupInvoiceAccountController endpoints.
        """
        return SubscriptionGroupInvoiceAccountController(self.global_configuration)

    @LazyProperty
    def subscription_group_status(self):
        """Provide access to the SubscriptionGroupStatusController endpoints."""
        return SubscriptionGroupStatusController(self.global_configuration)

    @LazyProperty
    def subscription_invoice_account(self):
        """Provide access to the SubscriptionInvoiceAccountController endpoints."""
        return SubscriptionInvoiceAccountController(self.global_configuration)

    @LazyProperty
    def subscription_notes(self):
        """Provide access to the SubscriptionNotesController endpoints."""
        return SubscriptionNotesController(self.global_configuration)

    @LazyProperty
    def subscription_products(self):
        """Provide access to the SubscriptionProductsController endpoints."""
        return SubscriptionProductsController(self.global_configuration)

    @LazyProperty
    def subscription_renewals(self):
        """Provide access to the SubscriptionRenewalsController endpoints."""
        return SubscriptionRenewalsController(self.global_configuration)

    @LazyProperty
    def subscription_status(self):
        """Provide access to the SubscriptionStatusController endpoints."""
        return SubscriptionStatusController(self.global_configuration)

    @LazyProperty
    def webhooks(self):
        """Provide access to the WebhooksController endpoints."""
        return WebhooksController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=120, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None, proxy_settings=None,
                 environment=Environment.US, site="subdomain",
                 basic_auth_credentials=None, config=None):
        """Initialize a new instance of AdvancedBillingClient."""
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            proxy_settings=proxy_settings, environment=environment, site=site,
            basic_auth_credentials=basic_auth_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(),
                BaseController.user_agent_parameters())

        self.auth_managers = {
            "BasicAuth": BasicAuth(self.config.basic_auth_credentials),
        }
        self.global_configuration =\
            self.global_configuration.auth_managers(self.auth_managers)

    @classmethod
    def from_environment(cls, dotenv_path=None, **overrides):
        """Create a client instance using environment variables.

        Returns:
            AdvancedBillingClient instance.

        """
        return cls(config=Configuration
            .from_environment(dotenv_path=dotenv_path, **overrides))
