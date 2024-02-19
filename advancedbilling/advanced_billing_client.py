# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from advancedbilling.configuration import Configuration
from advancedbilling.controllers.base_controller import BaseController
from advancedbilling.configuration import Environment
from advancedbilling.http.auth.basic_auth import BasicAuth
from advancedbilling.controllers.api_exports_controller\
    import APIExportsController
from advancedbilling.controllers.advance_invoice_controller\
    import AdvanceInvoiceController
from advancedbilling.controllers.billing_portal_controller\
    import BillingPortalController
from advancedbilling.controllers.coupons_controller import CouponsController
from advancedbilling.controllers.components_controller\
    import ComponentsController
from advancedbilling.controllers.customers_controller\
    import CustomersController
from advancedbilling.controllers.custom_fields_controller\
    import CustomFieldsController
from advancedbilling.controllers.events_controller import EventsController
from advancedbilling.controllers.events_based_billing_segments_controller\
    import EventsBasedBillingSegmentsController
from advancedbilling.controllers.insights_controller import InsightsController
from advancedbilling.controllers.invoices_controller import InvoicesController
from advancedbilling.controllers.offers_controller import OffersController
from advancedbilling.controllers.payment_profiles_controller\
    import PaymentProfilesController
from advancedbilling.controllers.product_families_controller\
    import ProductFamiliesController
from advancedbilling.controllers.products_controller import ProductsController
from advancedbilling.controllers.product_price_points_controller\
    import ProductPricePointsController
from advancedbilling.controllers.proforma_invoices_controller\
    import ProformaInvoicesController
from advancedbilling.controllers.reason_codes_controller\
    import ReasonCodesController
from advancedbilling.controllers.referral_codes_controller\
    import ReferralCodesController
from advancedbilling.controllers.sales_commissions_controller\
    import SalesCommissionsController
from advancedbilling.controllers.sites_controller import SitesController
from advancedbilling.controllers.subscriptions_controller\
    import SubscriptionsController
from advancedbilling.controllers.subscription_components_controller\
    import SubscriptionComponentsController
from advancedbilling.controllers.subscription_groups_controller\
    import SubscriptionGroupsController
from advancedbilling.controllers.subscription_group_invoice_account_controller\
    import SubscriptionGroupInvoiceAccountController
from advancedbilling.controllers.subscription_group_status_controller\
    import SubscriptionGroupStatusController
from advancedbilling.controllers.subscription_invoice_account_controller\
    import SubscriptionInvoiceAccountController
from advancedbilling.controllers.subscription_notes_controller\
    import SubscriptionNotesController
from advancedbilling.controllers.subscription_products_controller\
    import SubscriptionProductsController
from advancedbilling.controllers.subscription_status_controller\
    import SubscriptionStatusController
from advancedbilling.controllers.webhooks_controller import WebhooksController


class AdvancedBillingClient(object):
    @LazyProperty
    def api_exports(self):
        return APIExportsController(self.global_configuration)

    @LazyProperty
    def advance_invoice(self):
        return AdvanceInvoiceController(self.global_configuration)

    @LazyProperty
    def billing_portal(self):
        return BillingPortalController(self.global_configuration)

    @LazyProperty
    def coupons(self):
        return CouponsController(self.global_configuration)

    @LazyProperty
    def components(self):
        return ComponentsController(self.global_configuration)

    @LazyProperty
    def customers(self):
        return CustomersController(self.global_configuration)

    @LazyProperty
    def custom_fields(self):
        return CustomFieldsController(self.global_configuration)

    @LazyProperty
    def events(self):
        return EventsController(self.global_configuration)

    @LazyProperty
    def events_based_billing_segments(self):
        return EventsBasedBillingSegmentsController(self.global_configuration)

    @LazyProperty
    def insights(self):
        return InsightsController(self.global_configuration)

    @LazyProperty
    def invoices(self):
        return InvoicesController(self.global_configuration)

    @LazyProperty
    def offers(self):
        return OffersController(self.global_configuration)

    @LazyProperty
    def payment_profiles(self):
        return PaymentProfilesController(self.global_configuration)

    @LazyProperty
    def product_families(self):
        return ProductFamiliesController(self.global_configuration)

    @LazyProperty
    def products(self):
        return ProductsController(self.global_configuration)

    @LazyProperty
    def product_price_points(self):
        return ProductPricePointsController(self.global_configuration)

    @LazyProperty
    def proforma_invoices(self):
        return ProformaInvoicesController(self.global_configuration)

    @LazyProperty
    def reason_codes(self):
        return ReasonCodesController(self.global_configuration)

    @LazyProperty
    def referral_codes(self):
        return ReferralCodesController(self.global_configuration)

    @LazyProperty
    def sales_commissions(self):
        return SalesCommissionsController(self.global_configuration)

    @LazyProperty
    def sites(self):
        return SitesController(self.global_configuration)

    @LazyProperty
    def subscriptions(self):
        return SubscriptionsController(self.global_configuration)

    @LazyProperty
    def subscription_components(self):
        return SubscriptionComponentsController(self.global_configuration)

    @LazyProperty
    def subscription_groups(self):
        return SubscriptionGroupsController(self.global_configuration)

    @LazyProperty
    def subscription_group_invoice_account(self):
        return SubscriptionGroupInvoiceAccountController(self.global_configuration)

    @LazyProperty
    def subscription_group_status(self):
        return SubscriptionGroupStatusController(self.global_configuration)

    @LazyProperty
    def subscription_invoice_account(self):
        return SubscriptionInvoiceAccountController(self.global_configuration)

    @LazyProperty
    def subscription_notes(self):
        return SubscriptionNotesController(self.global_configuration)

    @LazyProperty
    def subscription_products(self):
        return SubscriptionProductsController(self.global_configuration)

    @LazyProperty
    def subscription_status(self):
        return SubscriptionStatusController(self.global_configuration)

    @LazyProperty
    def webhooks(self):
        return WebhooksController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=30, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION, subdomain='subdomain',
                 domain='chargify.com', basic_auth_credentials=None,
                 config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, subdomain=subdomain, domain=domain,
            basic_auth_credentials=basic_auth_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())

        self.auth_managers = {key: None for key in ['BasicAuth']}
        self.auth_managers['BasicAuth'] = BasicAuth(
            self.config.basic_auth_credentials)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

