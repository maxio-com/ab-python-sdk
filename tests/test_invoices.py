import time
from datetime import date, timedelta

import pytest

from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException
from advancedbilling.models.coupon import Coupon
from advancedbilling.models.create_customer import CreateCustomer
from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_invoice import CreateInvoice
from advancedbilling.models.create_invoice_address import CreateInvoiceAddress
from advancedbilling.models.create_invoice_coupon import CreateInvoiceCoupon
from advancedbilling.models.create_invoice_item import CreateInvoiceItem
from advancedbilling.models.create_invoice_request import CreateInvoiceRequest
from advancedbilling.models.create_or_update_coupon import CreateOrUpdateCoupon
from advancedbilling.models.create_or_update_percentage_coupon import CreateOrUpdatePercentageCoupon
from advancedbilling.models.create_or_update_product import CreateOrUpdateProduct
from advancedbilling.models.create_or_update_product_request import CreateOrUpdateProductRequest
from advancedbilling.models.create_payment_profile import CreatePaymentProfile
from advancedbilling.models.create_payment_profile_request import CreatePaymentProfileRequest
from advancedbilling.models.create_product_family import CreateProductFamily
from advancedbilling.models.create_product_family_request import CreateProductFamilyRequest
from advancedbilling.models.create_subscription import CreateSubscription
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_address import InvoiceAddress
from advancedbilling.models.invoice_customer import InvoiceCustomer
from advancedbilling.models.invoice_event import InvoiceEvent
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.invoice_line_item import InvoiceLineItem
from advancedbilling.models.invoice_seller import InvoiceSeller
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.subscription import Subscription
from advancedbilling.models.void_invoice import VoidInvoice
from advancedbilling.models.void_invoice_request import VoidInvoiceRequest
from tests.base import TestBase


class TestInvoices(TestBase):
    def test_create_invoice_given_subscription_then_return_correct_invoice(self):
        # GIVEN
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest(product_family=CreateProductFamily(
                name="TestInvoices_Product_Family_Name_1",
                description="TestInvoices_Product_Family_Description_1"
            ))
        ).product_family

        product: Product = self.get_products_controller().create_product(
            product_family_id=product_family.id,
            body=CreateOrUpdateProductRequest(product=CreateOrUpdateProduct(
                name="TestInvoices_Product_Name_1",
                handle="testinvoices_product_handle_1",
                description="TestInvoices_Product_Description_1",
                interval=1,
                price_in_cents=10,
                interval_unit=IntervalUnit.DAY
            ))
        ).product

        customer: Customer = self.get_customers_controller().create_customer(
            body=CreateCustomerRequest(customer=CreateCustomer(
                first_name="TestInvoices_Customer_FirstName_1",
                last_name="TestInvoices_Customer_LastName_1",
                email="tsce1@email.com",
                cc_emails=["email@email.com"],
                organization="TestInvoices_CustomerOrganization_1",
                reference="TestInvoices_CustomerReference_1",
                address="test address",
                address_2="test address two",
                city="Ohio",
                state="TX",
                zip="test zip",
                country="US",
                phone="+00 123 456 789",
                tax_exempt=False,
                vat_number="test vat number",
                parent_id=None,
                locale=None
            ))
        ).customer
        payment_profile: CreditCardPaymentProfile = self.get_payment_profiles_controller().create_payment_profile(
            CreatePaymentProfileRequest(
                CreatePaymentProfile(
                    customer_id=customer.id,
                    payment_type=PaymentType.CREDIT_CARD,
                    expiration_month=12,
                    expiration_year=2027,
                    full_number="4111111111111111"
                )

            )
        ).payment_profile
        coupon: Coupon = self.get_coupons_controller().create_coupon(
            product_family_id=product_family.id,
            body=CreateOrUpdateCoupon(coupon=CreateOrUpdatePercentageCoupon(
                name="15% off",
                code="15OFF",
                percentage="15",
                description="15% off for life",
                allow_negative_balance=False,
                recurring=False,
                end_date="2999-08-29T12:00:00-04:00",
                stackable=False,
                compounding_strategy="compound",
                exclude_mid_period_allocations=True,
                apply_on_cancel_at_end_of_period=True
            ))
        ).coupon

        subscription: Subscription = self.get_subscriptions_controller().create_subscription(
            CreateSubscriptionRequest(
                CreateSubscription(
                    product_id=product.id,
                    customer_id=customer.id,
                    dunning_communication_delay_enabled=False,
                    payment_collection_method="automatic",
                    payment_profile_id=payment_profile.id,
                    coupon_code=coupon.code
                )
            )
        ).subscription

        # THEN
        invoice: Invoice = self.get_invoices_controller().create_invoice(
            subscription_id=subscription.id,
            body=CreateInvoiceRequest(CreateInvoice(
                issue_date="2024-01-01",
                billing_address=CreateInvoiceAddress(
                    first_name="Hilario",
                    last_name="Schmidt",
                    phone="282-329-2085",
                    address="65581 Auer Expressway",
                    zip="15217",
                    country="US",
                    city="test City",
                    state="test State"
                ),
                line_items=[
                    CreateInvoiceItem(
                        title="TestInvoices_Product_Name_1",
                        quantity="12",
                        unit_price="150.00",
                        description="test invoice"
                    )
                ],
                coupons=[CreateInvoiceCoupon(
                    code=coupon.code,
                    percentage=coupon.percentage
                )]
            ))
        ).invoice

        billing_address: InvoiceAddress = invoice.billing_address
        assert "test City" == billing_address.city
        assert "US" == billing_address.country
        assert None == billing_address.line_2
        assert "test State" == billing_address.state
        assert "65581 Auer Expressway" == billing_address.street
        assert "15217" == billing_address.zip

        assert "remittance" == invoice.collection_method
        assert "none" == invoice.consolidation_level
        assert "0.0" == invoice.credit_amount
        assert 0 == len(invoice.credits)
        assert "USD" == invoice.currency
        assert 0 == len(invoice.custom_fields)

        invoice_customer: InvoiceCustomer = invoice.customer
        assert customer.id == invoice_customer.chargify_id
        assert customer.email == invoice_customer.email
        assert customer.first_name == invoice_customer.first_name
        assert customer.last_name == invoice_customer.last_name
        assert customer.organization == invoice_customer.organization
        assert customer.reference == invoice_customer.reference
        assert customer.vat_number == invoice_customer.vat_number

        assert customer.id == invoice.customer_id
        assert "270.0" == invoice.discount_amount
        assert 1 == len(invoice.discounts)
        assert "1530.0" == invoice.due_amount
        assert invoice.group_primary_subscription_id is None
        assert 1 == len(invoice.line_items)

        line_item: InvoiceLineItem = invoice.line_items[0]
        assert "TestInvoices_Product_Name_1" == line_item.title
        assert "12.0" == line_item.quantity
        assert "150.0" == line_item.unit_price
        assert "1530.0" == line_item.total_amount

        assert "Thanks for your business! If you have any questions, please contact your account manager." == invoice.memo
        assert "0.0" == invoice.paid_amount
        assert invoice.parent_invoice_uid is None
        assert invoice.parent_invoice_number is None
        assert "Please make checks payable to \"Acme, Inc.\"" == invoice.payment_instructions
        assert 0 == len(invoice.payments)
        assert product_family.name == invoice.product_family_name
        assert product.name == invoice.product_name
        assert "0.0" == invoice.refund_amount
        assert 0 == len(invoice.refunds)
        assert "adhoc" == invoice.role
        assert "open" == invoice.status
        assert subscription.id == invoice.subscription_id
        assert "1800.0" == invoice.subtotal_amount
        assert "0.0" == invoice.tax_amount
        assert 0 == len(invoice.taxes)
        assert "1530.0" == invoice.total_amount

        seller: InvoiceSeller = invoice.seller
        assert "Developer Experience" == seller.name
        assert "555 111 222" == seller.phone

        seller_address: InvoiceAddress = seller.address
        assert "San Antonio" == seller_address.city
        assert "US" == seller_address.country
        assert "123/444" == seller_address.line_2
        assert "TX" == seller_address.state
        assert "Asdf Street" == seller_address.street
        assert "78015" == seller_address.zip

        shipping_address: InvoiceAddress = invoice.shipping_address
        assert "Ohio" == shipping_address.city
        assert "US" == shipping_address.country
        assert "test address two" == shipping_address.line_2
        assert "TX" == shipping_address.state
        assert "test address" == shipping_address.street
        assert "test zip" == shipping_address.zip

        self.get_subscriptions_controller().purge_subscription(subscription.id, customer.id)
        self.get_customers_controller().delete_customer(customer.id)

    def test_void_invoice_given_invoice_then_should_be_voided(self):
        # GIVEN
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest(product_family=CreateProductFamily(
                name="TestInvoices_Product_Family_Name_2",
                description="TestInvoices_Product_Family_Description_2"
            ))
        ).product_family

        product: Product = self.get_products_controller().create_product(
            product_family_id=product_family.id,
            body=CreateOrUpdateProductRequest(product=CreateOrUpdateProduct(
                name="TestInvoices_Product_Name_2",
                handle="testinvoices_product_handle_2",
                description="TestInvoices_Product_Description_2",
                interval=1,
                price_in_cents=10,
                interval_unit=IntervalUnit.DAY
            ))
        ).product

        customer: Customer = self.get_customers_controller().create_customer(
            body=CreateCustomerRequest(customer=CreateCustomer(
                first_name="TestInvoices_Customer_FirstName_2",
                last_name="TestInvoices_Customer_LastName_2",
                email="tsce1@email.com",
                cc_emails=["email@email.com"],
                organization="TestInvoices_CustomerOrganization_2",
                reference="TestInvoices_CustomerReference_2",
                address="test address",
                address_2="test address two",
                city="Ohio",
                state="TX",
                zip="test zip",
                country="US",
                phone="+00 123 456 789",
                tax_exempt=False,
                vat_number="test vat number",
                parent_id=None,
                locale=None
            ))
        ).customer

        payment_profile: CreditCardPaymentProfile = self.get_payment_profiles_controller().create_payment_profile(
            body=CreatePaymentProfileRequest(payment_profile=CreatePaymentProfile(
                customer_id=customer.id,
                payment_type=PaymentType.CREDIT_CARD,
                expiration_month=12,
                expiration_year=2027,
                full_number="4111111111111111"
            ))
        ).payment_profile

        subscription: Subscription = self.get_subscriptions_controller().create_subscription(
            body=CreateSubscriptionRequest(CreateSubscription(
                product_id=product.id,
                customer_id=customer.id,
                dunning_communication_delay_enabled=False,
                payment_collection_method="automatic",
                skip_billing_manifest_taxes=False,
                payment_profile_id=payment_profile.id,
            ))
        ).subscription

        invoice: Invoice = self.get_invoices_controller().create_invoice(
            subscription_id=subscription.id,
            body=CreateInvoiceRequest(CreateInvoice(
                issue_date="2024-01-01",
                billing_address=CreateInvoiceAddress(
                    first_name="Hilario",
                    last_name="Schmidt",
                    phone="282-329-2085",
                    address="65581 Auer Expressway",
                    zip="15217",
                    country="US",
                    city="test City",
                    state="test State"
                ),
                line_items=[
                    CreateInvoiceItem(
                        title="TestInvoices_Product_Name_1",
                        quantity="12",
                        unit_price="150.00",
                        description="test invoice"
                    )
                ]
            ))
        ).invoice

        # THEN
        response: Invoice = self.get_invoices_controller().void_invoice(
            uid=invoice.uid,
            body=VoidInvoiceRequest(void=VoidInvoice(
                reason="Duplicate invoice"
            ))
        )

        assert "voided" == response.status
        assert invoice.uid == response.uid

        self.get_subscriptions_controller().purge_subscription(subscription.id, customer.id)
        self.get_customers_controller().delete_customer(customer.id)

    def test_list_invoice_events_given_voided_invoice_then_return_void_invoice_event_and_issue_invoice_event(self):
        pytest.skip("Waiting for sdk update.")
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest(product_family=CreateProductFamily(
                name="TestInvoices_Product_Family_Name_3",
                description="TestInvoices_Product_Family_Description_3"
            ))
        ).product_family

        product: Product = self.get_products_controller().create_product(
            product_family_id=product_family.id,
            body=CreateOrUpdateProductRequest(product=CreateOrUpdateProduct(
                name="TestInvoices_Product_Name_3",
                handle="testinvoices_product_handle_3",
                description="TestInvoices_Product_Description_3",
                interval=1,
                price_in_cents=10,
                interval_unit=IntervalUnit.DAY
            ))
        ).product

        customer: Customer = self.get_customers_controller().create_customer(
            body=CreateCustomerRequest(customer=CreateCustomer(
                first_name="TestInvoices_Customer_FirstName_3",
                last_name="TestInvoices_Customer_LastName_3",
                email="tsce1@email.com",
                cc_emails=["email@email.com"],
                organization="TestInvoices_CustomerOrganization_4",
                reference="TestInvoices_CustomerReference_4",
                address="test address",
                address_2="test address two",
                city="Ohio",
                state="TX",
                zip="test zip",
                country="US",
                phone="+00 123 456 789",
                tax_exempt=False,
                vat_number="test vat number",
                parent_id=None,
                locale=None
            ))
        ).customer
        payment_profile: CreditCardPaymentProfile = self.get_payment_profiles_controller().create_payment_profile(
            CreatePaymentProfileRequest(
                CreatePaymentProfile(
                    customer_id=customer.id,
                    payment_type=PaymentType.CREDIT_CARD,
                    expiration_month=12,
                    expiration_year=2027,
                    full_number="4111111111111111"
                )

            )
        ).payment_profile
        subscription: Subscription = self.get_subscriptions_controller().create_subscription(
            body=CreateSubscriptionRequest(CreateSubscription(
                product_id=product.id,
                customer_id=customer.id,
                dunning_communication_delay_enabled=False,
                payment_collection_method="automatic",
                skip_billing_manifest_taxes=False,
                payment_profile_id=payment_profile.id,
            ))
        ).subscription
        invoice: Invoice = self.get_invoices_controller().create_invoice(
            subscription_id=subscription.id,
            body=CreateInvoiceRequest(CreateInvoice(
                issue_date="2024-01-01",
                billing_address=CreateInvoiceAddress(
                    first_name="Hilario",
                    last_name="Schmidt",
                    phone="282-329-2085",
                    address="65581 Auer Expressway",
                    zip="15217",
                    country="US",
                    city="test City",
                    state="test State"
                ),
                line_items=[
                    CreateInvoiceItem(
                        title="TestInvoices_Product_Name_1",
                        quantity="12",
                        unit_price="150.00",
                        description="test invoice",
                    )
                ]
            ))
        ).invoice
        self.get_invoices_controller().void_invoice(
            uid=invoice.uid,
            body=VoidInvoiceRequest(void=VoidInvoice(
                reason="Duplicate invoice"
            ))
        )
        time.sleep(1.0)

        # THEN
        events = self.get_invoices_controller().list_invoice_events(
            {
                "event_types": [InvoiceEventType.VOID_INVOICE, InvoiceEventType.ISSUE_INVOICE],
                "since_date": date.today() - timedelta(days=1)
            }
        ).events

        assert 2 < len(events)

        event: InvoiceEvent
        for event in events:
            assert InvoiceEventType.ISSUE_INVOICE == event.event_type or InvoiceEventType.VOID_INVOICE == event.event_type

        self.get_subscriptions_controller().purge_subscription(subscription.id, customer.id)
        self.get_customers_controller().delete_customer(customer.id)

    def test_create_invoice_given_invalid_period_range_end_value_then_should_throw_exception_with_422_status_code(self):
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest(product_family=CreateProductFamily(
                name="TestInvoices_Product_Family_Name_4",
                description="TestInvoices_Product_Family_Description_4"
            ))
        ).product_family

        product: Product = self.get_products_controller().create_product(
            product_family_id=product_family.id,
            body=CreateOrUpdateProductRequest(product=CreateOrUpdateProduct(
                name="TestInvoices_Product_Name_4",
                handle="testinvoices_product_handle_4",
                description="TestInvoices_Product_Description_4",
                interval=1,
                price_in_cents=10,
                interval_unit=IntervalUnit.DAY
            ))
        ).product

        customer: Customer = self.get_customers_controller().create_customer(
            body=CreateCustomerRequest(customer=CreateCustomer(
                first_name="TestInvoices_Customer_FirstName_4",
                last_name="TestInvoices_Customer_LastName_4",
                email="tsce1@email.com",
                cc_emails=["email@email.com"],
                organization="TestInvoices_CustomerOrganization_4",
                reference="TestInvoices_CustomerReference_4",
                address="test address",
                address_2="test address two",
                city="Ohio",
                state="TX",
                zip="test zip",
                country="US",
                phone="+00 123 456 789",
                tax_exempt=False,
                vat_number="test vat number",
                parent_id=None,
                locale=None
            ))
        ).customer
        payment_profile: CreditCardPaymentProfile = self.get_payment_profiles_controller().create_payment_profile(
            CreatePaymentProfileRequest(
                CreatePaymentProfile(
                    customer_id=customer.id,
                    payment_type=PaymentType.CREDIT_CARD,
                    expiration_month=12,
                    expiration_year=2027,
                    full_number="4111111111111111"
                )

            )
        ).payment_profile
        subscription: Subscription = self.get_subscriptions_controller().create_subscription(
            body=CreateSubscriptionRequest(CreateSubscription(
                product_id=product.id,
                customer_id=customer.id,
                dunning_communication_delay_enabled=False,
                payment_collection_method="automatic",
                skip_billing_manifest_taxes=False,
                payment_profile_id=payment_profile.id,
            ))
        ).subscription

        with pytest.raises(ErrorArrayMapResponseException) as exception_info:
            self.get_invoices_controller().create_invoice(
                subscription_id=subscription.id,
                body=CreateInvoiceRequest(CreateInvoice(
                    issue_date="2024-01-01",
                    billing_address=CreateInvoiceAddress(
                        first_name="Hilario",
                        last_name="Schmidt",
                        phone="282-329-2085",
                        address="65581 Auer Expressway",
                        zip="15217",
                        country="US",
                        city="test City",
                        state="test State"
                    ),
                    line_items=[
                        CreateInvoiceItem(
                            title="TestInvoices_Product_Name_1",
                            quantity="12",
                            unit_price="150.00",
                            description="test invoice",
                            period_range_start="2024-01-01",
                            period_range_end="2023-01-01"
                        )
                    ]
                ))
            )

            exception_info.errisinstance(ErrorArrayMapResponseException)
            assert 422 == exception_info.value.response_code
            errors = exception_info.value.errors
            assert 1 == len(errors)
            assert {"line_items[0].period_range_end": ["Must be greater or equal to period_range_start."]} == errors

        self.get_subscriptions_controller().purge_subscription(subscription.id, customer.id)
        self.get_customers_controller().delete_customer(customer.id)
