from os import getenv

import pytest

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.models.component import Component
from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_on_off_component import CreateOnOffComponent
from advancedbilling.models.create_or_update_product_request import CreateOrUpdateProductRequest
from advancedbilling.models.create_payment_profile_request import CreatePaymentProfileRequest
from advancedbilling.models.create_prepaid_component import CreatePrepaidComponent
from advancedbilling.models.create_product_family_request import CreateProductFamilyRequest
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.subscription import Subscription
from tests.base import TestBase


class TestSubscriptions(TestBase):
    def test_create_subscription_given_exiting_product_and_customer_and_prepaid_component_and_on_off_component_then_subscription_created(
            self):
        # GIVEN
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestSubscriptions_Product_Family_Name_1",
                        "description": "TestSubscriptions_Product_Family_Description_1",
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
                            "name": "TestSubscriptions_Product_Name_1",
                            "handle": "testsubscriptions_product_handle_1",
                            "description": "TestSubscriptions_Product_Description_1",
                            "interval": 1,
                            "price_in_cents": 10,
                            "interval_unit": IntervalUnit.DAY
                        }
                }
            )).product
        customer: Customer = self.get_customers_controller().create_customer(CreateCustomerRequest.from_dictionary(
            {
                "customer": {
                    "first_name": "TestSubscriptions_Customer_FirstName_1",
                    "last_name": "TestSubscriptions_Customer_LastName_1",
                    "email": "tsce1@email.com",
                    "cc_emails": ["email@email.com"],
                    "organization": "TestSubscriptions_CustomerOrganization_1",
                    "reference": "TestSubscriptions_CustomerReference_1",
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
        on_off_component: Component = self.get_components_controller().create_on_off_component(
            product_family.id,
            CreateOnOffComponent.from_dictionary(
                {
                    "on_off_component": {
                        "name": "TestSubscriptions_On_Off_Component_Name_1",
                        'unit_price': "1.0",
                        "prices": [
                            {
                                "unit_price": "0.10",
                                "starting_quantity": "0"
                            }
                        ],
                    }
                }
            )).component
        prepaid_component: Component = self.get_components_controller().create_prepaid_usage_component(
            product_family.id,
            CreatePrepaidComponent.from_dictionary(
                {
                    "prepaid_usage_component": {
                        "name": "TestSubscriptions_Prepaid_Component_Name_1",
                        "unit_price": "1.0",
                        "unit_name": "minutes",
                        "pricing_scheme": PricingScheme.STAIRSTEP,
                        "prices": [
                            {
                                "starting_quantity": 1,
                                "ending_quantity": 100,
                                "unit_price": "3"
                            }
                        ],
                        "overage_pricing": {
                            "pricing_scheme": "stairstep",
                            "prices": [
                                {
                                    "starting_quantity": 1,
                                    "ending_quantity": 100,
                                    "unit_price": "3"
                                },
                                {
                                    "starting_quantity": 101,
                                    "unit_price": "5"
                                }
                            ]
                        }
                    }
                }
            )).component

        # THEN
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
                        "components": [
                            {
                                "component_id": on_off_component.id,
                                "enabled": True
                            },
                            {
                                "component_id": prepaid_component.id,
                                "enabled": True
                            }
                        ]
                    }
                }
            )).subscription

        assert product.id == subscription.product.id
        assert customer.id == subscription.customer.id
        assert payment_profile.payment_type == subscription.payment_type

        assert "active" == subscription.state
        assert 410 == subscription.total_revenue_in_cents
        assert 10 == subscription.product_price_in_cents
        assert 1 == subscription.product_version_number
        assert None == subscription.cancellation_message
        assert None == subscription.cancellation_method
        assert None == subscription.cancel_at_end_of_period
        assert None == subscription.canceled_at
        assert "active" == subscription.previous_state
        assert "4.10" == subscription.signup_revenue
        assert None == subscription.coupon_code
        assert None == subscription.snap_day
        assert "automatic" == subscription.payment_collection_method
        assert "visa" == subscription.credit_card.card_type
        assert "bogus" == subscription.credit_card.current_vault
        assert customer.id == subscription.credit_card.customer_id
        assert None == subscription.group
        assert "credit_card" == subscription.payment_type
        assert None == subscription.referral_code
        assert None == subscription.next_product_id
        assert None == subscription.next_product_handle
        assert None == subscription.coupon_use_count
        assert None == subscription.coupon_uses_allowed
        assert None == subscription.reason_code
        assert None == subscription.automatically_resume_at
        assert None == subscription.offer_id
        assert None == subscription.payer_id
        assert "default" == subscription.product_price_point_type
        assert None == subscription.next_product_price_point_id
        assert None == subscription.net_terms
        assert None == subscription.stored_credential_transaction_id
        assert None == subscription.reference
        assert None == subscription.on_hold_at
        assert False == subscription.dunning_communication_delay_enabled
        assert None == subscription.dunning_communication_delay_time_zone
        assert None == subscription.receives_invoice_emails
        assert None == subscription.locale
        assert "USD" == subscription.currency
        assert None == subscription.scheduled_cancellation_at

        subscription_components = self.get_subscription_components_controller().list_subscription_components(
            {
                "subscription_id": subscription.id,
                "sort": "name"
            }
        )

        assert 2 == len(subscription_components)
        first_component = subscription_components[0].component
        second_component = subscription_components[1].component

        assert on_off_component.id == first_component.component_id
        assert prepaid_component.id == second_component.component_id

        self.get_subscriptions_controller().purge_subscription(subscription.id, customer.id)
        self.get_customers_controller().delete_customer(customer.id)

    def test_create_subscription_given_existing_product_and_not_existing_customer_then_thrown_exception_with_422_status_code(
            self):
        # GIVEN
        not_existing_customer_id = 1234567
        not_existing_payment_profile_id = 123245612
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestSubscriptions_Product_Family_Name_2",
                        "description": "TestSubscriptions_Product_Family_Description_2",
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
                            "name": "TestSubscriptions_Product_Name_2",
                            "handle": "testsubscriptions_product_handle_2",
                            "description": "TestSubscriptions_Product_Description_2",
                            "interval": 1,
                            "price_in_cents": 10,
                            "interval_unit": IntervalUnit.DAY
                        }
                }
            )).product

        # THEN
        with pytest.raises(ErrorListResponseException) as e:
            self.get_subscriptions_controller().create_subscription(
                CreateSubscriptionRequest.from_dictionary(
                    {
                        "subscription": {
                            "product_id": product.id,
                            'customer_id': not_existing_customer_id,
                            "dunning_communication_delay_enabled": False,
                            "payment_collection_method": "automatic",
                            "skip_billing_manifest_taxes": False,
                            "payment_profile_id": not_existing_payment_profile_id,
                        }
                    }
                ))

            assert 422 == e.value.response_code
            assert "A Customer must be specified for the subscription to be valid." == e.value.message

    def test_create_subscription_given_invalid_credentials_then_thrown_exception_with_401_status_code(self):
        client = AdvancedBillingClient(
            subdomain=getenv("SUBDOMAIN"),
            domain=getenv("DOMAIN"),
            basic_auth_user_name="thisiswrongapitokenthisiswrongapitokenV8",
            basic_auth_password=getenv("BASIC_AUTH_PASSWORD")
        )

        with pytest.raises(APIException) as e:
            client.subscriptions.create_subscription(
                CreateSubscriptionRequest.from_dictionary(
                    {
                        "subscription": {
                            "product_id": 2132441,
                            'customer_id': 23214,
                            "dunning_communication_delay_enabled": False,
                            "payment_collection_method": "automatic",
                            "skip_billing_manifest_taxes": False,
                            "payment_profile_id": 213412,
                        }
                    }
                ))

            assert 401 == e.value.response_code
