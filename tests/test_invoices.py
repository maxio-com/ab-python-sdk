import time
from datetime import date, timedelta

import pytest

from advancedbilling.advanced_billing_client import (
    CouponsController,
    CustomersController,
    InvoicesController,
    PaymentProfilesController,
    ProductFamiliesController,
    ProductsController,
    SubscriptionsController,
)
from advancedbilling.exceptions.error_array_map_response_exception import (
    ErrorArrayMapResponseException,
)
from advancedbilling.models.coupon import Coupon
from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_invoice_request import CreateInvoiceRequest
from advancedbilling.models.create_or_update_coupon import CreateOrUpdateCoupon
from advancedbilling.models.create_or_update_product_request import (
    CreateOrUpdateProductRequest,
)
from advancedbilling.models.create_payment_profile_request import (
    CreatePaymentProfileRequest,
)
from advancedbilling.models.create_product_family_request import (
    CreateProductFamilyRequest,
)
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event import InvoiceEvent
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.subscription import Subscription
from advancedbilling.models.void_invoice import VoidInvoice
from advancedbilling.models.void_invoice_request import VoidInvoiceRequest

from .data import InitCases, InvoiceAssertCases
from .utils import assert_properties


class TestInvoices:
    def test_create_invoice_given_subscription_then_return_correct_invoice(
        self,
        coupons_controller: CouponsController,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        invoices_controller: InvoicesController,
        subscriptions_controller: SubscriptionsController,
    ):
        # GIVEN
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest(InitCases.get_product_family_request())
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest(InitCases.get_product_request()),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest(InitCases.get_customer_request())
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest(InitCases.get_payment_profile_request(customer.id))
        ).payment_profile

        coupon: Coupon = coupons_controller.create_coupon(
            product_family.id, CreateOrUpdateCoupon(InitCases.get_coupon_data())
        ).coupon

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription

        # THEN
        invoice: Invoice = invoices_controller.create_invoice(
            subscription.id,
            CreateInvoiceRequest(InitCases.get_invoice_request_with_coupon(coupon)),
        ).invoice

        # NOTE: No way of getting it to assert_propert nicely with the current structure
        assert len(invoice.credits) == 0
        assert len(invoice.custom_fields) == 0
        assert len(invoice.discounts) == 1
        assert len(invoice.line_items) == 1
        assert len(invoice.payments) == 0
        assert len(invoice.refunds) == 0
        assert len(invoice.taxes) == 0

        assert_properties(
            invoice,
            InvoiceAssertCases.get_invoice_data(customer, product, product_family, subscription),
        )

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)

    def test_void_invoice_given_invoice_then_should_be_voided(
        self,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        invoices_controller: InvoicesController,
        subscriptions_controller: SubscriptionsController,
    ):
        # GIVEN
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest(InitCases.get_product_family_request())
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id, CreateOrUpdateProductRequest(InitCases.get_product_request())
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest(InitCases.get_customer_request())
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest(InitCases.get_payment_profile_request(customer.id))
        ).payment_profile

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription

        invoice: Invoice = invoices_controller.create_invoice(
            subscription.id,
            CreateInvoiceRequest(InitCases.get_invoice_request()),
        ).invoice

        # THEN
        response: Invoice = invoices_controller.void_invoice(
            uid=invoice.uid, body=VoidInvoiceRequest(void=VoidInvoice(reason="Duplicate invoice"))
        )

        assert response.status == "voided"
        assert response.uid == invoice.uid

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)

    def test_list_invoice_events_given_voided_invoice_then_return_void_invoice_event_and_issue_invoice_event(
        self,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        invoices_controller: InvoicesController,
        subscriptions_controller: SubscriptionsController,
    ):
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest(InitCases.get_product_family_request())
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest(InitCases.get_product_request()),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest(InitCases.get_customer_request())
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest(InitCases.get_payment_profile_request(customer.id))
        ).payment_profile

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription

        invoice: Invoice = invoices_controller.create_invoice(
            subscription.id,
            CreateInvoiceRequest(InitCases.get_invoice_request()),
        ).invoice

        invoices_controller.void_invoice(
            uid=invoice.uid, body=VoidInvoiceRequest(void=VoidInvoice(reason="Duplicate invoice"))
        )
        time.sleep(1.0)

        # THEN
        events = invoices_controller.list_invoice_events(
            {
                "event_types": [InvoiceEventType.VOID_INVOICE, InvoiceEventType.ISSUE_INVOICE],
                "since_date": date.today() - timedelta(days=1),
            }
        ).events

        assert len(events) > 2

        event: InvoiceEvent
        for event in events:
            assert event.event_type in (InvoiceEventType.ISSUE_INVOICE, InvoiceEventType.VOID_INVOICE)

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)

    def test_create_invoice_given_invalid_period_range_end_value_then_should_throw_exception_with_422_status_code(
        self,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        invoices_controller: InvoicesController,
        subscriptions_controller: SubscriptionsController,
    ):
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest(InitCases.get_product_family_request())
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest(InitCases.get_product_request()),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest(InitCases.get_customer_request())
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest(InitCases.get_payment_profile_request(customer.id))
        ).payment_profile

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription

        with pytest.raises(ErrorArrayMapResponseException) as exception_info:
            invoices_controller.create_invoice(
                subscription.id,
                CreateInvoiceRequest(InitCases.get_invoice_request_with_invalid_period()),
            )

            errors = exception_info.value.errors

            assert exception_info.value.response_code == 422
            assert len(errors) == 1
            assert errors == {"line_items[0].period_range_end": ["Must be greater or equal to period_range_start."]}

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)
