from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_invoice_request import CreateInvoiceRequest
from advancedbilling.models.create_or_update_coupon import CreateOrUpdateCoupon
from advancedbilling.models.create_or_update_product_request import CreateOrUpdateProductRequest
from advancedbilling.models.create_payment_profile_request import CreatePaymentProfileRequest
from advancedbilling.models.create_product_family_request import CreateProductFamilyRequest
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.subscription import Subscription
from tests.base import TestBase


class TestInvoices(TestBase):
    def test_create_invoice_given_subscription_given_subscription_then_return_correct_invoice(self):
        # GIVEN
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestInvoices_Product_Family_Name_1",
                        "description": "TestInvoices_Product_Family_Description_1",
                    }
                }
            )
        ).product_family
        product: Product = self.get_products_controller().create_product(
            product_family.id,

            CreateOrUpdateProductRequest.from_dictionary(
                {
                    "product":
                        {
                            "name": "TestInvoices_Product_Name_1",
                            "handle": "testinvoices_product_handle_1",
                            "description": "TestInvoices_Product_Description_1",
                            "interval": 1,
                            "price_in_cents": 10,
                            "interval_unit": IntervalUnit.DAY
                        }
                }
            )).product
        customer: Customer = self.get_customers_controller().create_customer(CreateCustomerRequest.from_dictionary(
            {
                "customer": {
                    "first_name": "TestInvoices_Customer_FirstName_1",
                    "last_name": "TestInvoices_Customer_LastName_1",
                    "email": "tsce1@email.com",
                    "cc_emails": ["email@email.com"],
                    "organization": "TestInvoices_CustomerOrganization_1",
                    "reference": "TestInvoices_CustomerReference_1",
                    "address": "test address",
                    "address_2": "test address two",
                    "city": "Ohio",
                    "state": "TX",
                    "zip": "test zip",
                    "country": "US",
                    "phone": "+00 123 456 789",
                    "tax_exempt": False,
                    "vat_number": "test vat number",
                    "parent_id": None,
                    "locale": None
                }
            }
        )).customer
        payment_profile: CreditCardPaymentProfile = self.get_payment_profiles_controller().create_payment_profile(
            CreatePaymentProfileRequest.from_dictionary(
                {
                    "payment_profile": {
                        "customer_id": customer.id,
                        "payment_type": PaymentType.CREDIT_CARD,
                        "expiration_month": 12,
                        "expiration_year": 2027,
                        "full_number": "4111111111111111"
                    }
                }
            )
        ).payment_profile
        coupon = self.get_coupons_controller().create_coupon(
            product_family.id,
            CreateOrUpdateCoupon.from_dictionary(
                {
                    "coupon": {
                        "name": "15% off",
                        "code": "15OFF",
                        "description": "15% off for life",
                        "percentage": "15.0",
                        "allow_negative_balance": False,
                        "recurring": False,
                        "end_date": "2999-08-29T12:00:00-04:00",
                        "product_family_id": product_family.id,
                        "stackable": False,
                        "compounding_strategy": "compound",
                        "exclude_mid_period_allocations": True,
                        "apply_on_cancel_at_end_of_period": True
                    },
                }
            ))
        subscription: Subscription = self.get_subscriptions_controller().create_subscription(
            CreateSubscriptionRequest.from_dictionary(
                {
                    "subscription": {
                        "product_id": product.id,
                        'customer_id': customer.id,
                        "dunning_communication_delay_enabled": False,
                        "payment_collection_method": "automatic",
                        "skip_billing_manifest_taxes": False,
                        "payment_profile_id": payment_profile.id,
                        "coupon_code": "15OFF"
                    }
                }
            )).subscription

        # THEN
        invoice = self.get_invoices_controller().create_invoice(subscription.id, CreateInvoiceRequest.from_dictionary(
            {
                "invoice": {
                    "issue_date": "2024-01-01",
                    "billing_address": {
                        "first_name": "Hilario",
                        "last_name": "Schmidt",
                        "phone": "282-329-2085",
                        "address": "65581 Auer Expressway",
                        "zip": "15217",
                        "country": "US"
                    },
                    "line_items": [
                        {
                            "title": "TestInvoices_Product_Name_1",
                            "quantity": 12,
                            "unit_price": "150.00",
                            "description": "test invoice"
                        }
                    ],
                    "coupons": [
                        {
                            "code": "15OFF",
                            "percentage": 15.0
                        }
                    ]
                }
            }
        ))

        assert True == True
