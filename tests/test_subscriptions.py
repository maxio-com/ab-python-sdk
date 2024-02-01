import pytest

from advancedbilling.advanced_billing_client import (
    AdvancedBillingClient,
    ComponentsController,
    CustomersController,
    CustomFieldsController,
    PaymentProfilesController,
    ProductFamiliesController,
    ProductsController,
    SubscriptionComponentsController,
    SubscriptionsController,
)
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import (
    ErrorListResponseException,
)
from advancedbilling.models.component import Component
from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_metadata_request import CreateMetadataRequest
from advancedbilling.models.create_metafields_request import CreateMetafieldsRequest
from advancedbilling.models.create_on_off_component import CreateOnOffComponent
from advancedbilling.models.create_or_update_product_request import (
    CreateOrUpdateProductRequest,
)
from advancedbilling.models.create_payment_profile_request import (
    CreatePaymentProfileRequest,
)
from advancedbilling.models.create_prepaid_component import CreatePrepaidComponent
from advancedbilling.models.create_product_family_request import (
    CreateProductFamilyRequest,
)
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.resource_type import ResourceType
from advancedbilling.models.subscription import Subscription


class TestSubscriptions:
    def test_create_subscription_given_exiting_product_and_customer_and_prepaid_component_and_on_off_component_then_subscription_created(  # noqa: E501
        self,
        components_controller: ComponentsController,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        subscription_components_controller: SubscriptionComponentsController,
        subscriptions_controller: SubscriptionsController,
    ):
        # GIVEN
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestSubscriptions_Product_Family_Name_1",
                        "description": "TestSubscriptions_Product_Family_Description_1",
                    }
                }
            )
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest.from_dictionary(
                {
                    "product": {
                        "name": "TestSubscriptions_Product_Name_1",
                        "handle": "testsubscriptions_product_handle_1",
                        "description": "TestSubscriptions_Product_Description_1",
                        "interval": 1,
                        "price_in_cents": 10,
                        "interval_unit": IntervalUnit.DAY,
                    }
                }
            ),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest.from_dictionary(
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
                        "locale": None,
                    }
                }
            )
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest.from_dictionary(
                {
                    "payment_profile": {
                        "customer_id": customer.id,
                        "payment_type": PaymentType.CREDIT_CARD,
                        "expiration_month": 12,
                        "expiration_year": 2027,
                        "full_number": "4111111111111111",
                    }
                }
            )
        ).payment_profile

        on_off_component: Component = components_controller.create_on_off_component(
            product_family.id,
            CreateOnOffComponent.from_dictionary(
                {
                    "on_off_component": {
                        "name": "TestSubscriptions_On_Off_Component_Name_1",
                        "unit_price": "1.0",
                        "prices": [{"unit_price": "0.10", "starting_quantity": "0"}],
                    }
                }
            ),
        ).component

        prepaid_component: Component = components_controller.create_prepaid_usage_component(
            product_family.id,
            CreatePrepaidComponent.from_dictionary(
                {
                    "prepaid_usage_component": {
                        "name": "TestSubscriptions_Prepaid_Component_Name_1",
                        "unit_price": "1.0",
                        "unit_name": "minutes",
                        "pricing_scheme": PricingScheme.STAIRSTEP,
                        "prices": [{"starting_quantity": 1, "ending_quantity": 100, "unit_price": "3"}],
                        "overage_pricing": {
                            "pricing_scheme": "stairstep",
                            "prices": [
                                {"starting_quantity": 1, "ending_quantity": 100, "unit_price": "3"},
                                {"starting_quantity": 101, "unit_price": "5"},
                            ],
                        },
                    }
                }
            ),
        ).component

        # THEN
        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest.from_dictionary(
                {
                    "subscription": {
                        "product_id": product.id,
                        "customer_id": customer.id,
                        "dunning_communication_delay_enabled": False,
                        "payment_collection_method": "automatic",
                        "skip_billing_manifest_taxes": False,
                        "payment_profile_id": payment_profile.id,
                        "components": [
                            {"component_id": on_off_component.id, "enabled": True},
                            {"component_id": prepaid_component.id, "enabled": True},
                        ],
                    }
                }
            )
        ).subscription

        assert product.id == subscription.product.id
        assert customer.id == subscription.customer.id
        assert payment_profile.payment_type == subscription.payment_type

        assert subscription.state == "active"
        assert subscription.total_revenue_in_cents == 410
        assert subscription.product_price_in_cents == 10
        assert subscription.product_version_number == 1
        assert subscription.cancellation_message is None
        assert subscription.cancellation_method is None
        assert subscription.cancel_at_end_of_period is None
        assert subscription.canceled_at is None
        assert subscription.previous_state == "active"
        assert subscription.signup_revenue == "4.10"
        assert subscription.coupon_code is None
        assert subscription.snap_day is None
        assert subscription.payment_collection_method == "automatic"
        assert subscription.credit_card.card_type == "visa"
        assert subscription.credit_card.current_vault == "bogus"
        assert subscription.credit_card.customer_id == customer.id
        assert subscription.group is None
        assert subscription.payment_type == "credit_card"
        assert subscription.referral_code is None
        assert subscription.next_product_id is None
        assert subscription.next_product_handle is None
        assert subscription.coupon_use_count is None
        assert subscription.coupon_uses_allowed is None
        assert subscription.reason_code is None
        assert subscription.automatically_resume_at is None
        assert subscription.offer_id is None
        assert subscription.payer_id is None
        assert subscription.product_price_point_type == "default"
        assert subscription.next_product_price_point_id is None
        assert subscription.net_terms is None
        assert subscription.stored_credential_transaction_id is None
        assert subscription.reference is None
        assert subscription.on_hold_at is None
        assert subscription.dunning_communication_delay_enabled is False
        assert subscription.dunning_communication_delay_time_zone is None
        assert subscription.receives_invoice_emails is None
        assert subscription.locale is None
        assert subscription.currency == "USD"
        assert subscription.scheduled_cancellation_at is None

        subscription_components: list = subscription_components_controller.list_subscription_components(
            {"subscription_id": subscription.id, "sort": "name"}
        )

        assert len(subscription_components) == 2
        first_component, second_component = [component.component for component in subscription_components]

        assert on_off_component.id == first_component.component_id
        assert prepaid_component.id == second_component.component_id

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)

    def test_create_subscription_given_existing_product_and_not_existing_customer_then_thrown_exception_with_422_status_code(
        self,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        subscriptions_controller: SubscriptionsController,
    ):
        # GIVEN
        not_existing_customer_id = 1234567
        not_existing_payment_profile_id = 123245612
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestSubscriptions_Product_Family_Name_2",
                        "description": "TestSubscriptions_Product_Family_Description_2",
                    }
                }
            )
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest.from_dictionary(
                {
                    "product": {
                        "name": "TestSubscriptions_Product_Name_2",
                        "handle": "testsubscriptions_product_handle_2",
                        "description": "TestSubscriptions_Product_Description_2",
                        "interval": 1,
                        "price_in_cents": 10,
                        "interval_unit": IntervalUnit.DAY,
                    }
                }
            ),
        ).product

        # THEN
        with pytest.raises(ErrorListResponseException) as e:
            subscriptions_controller.create_subscription(
                CreateSubscriptionRequest.from_dictionary(
                    {
                        "subscription": {
                            "product_id": product.id,
                            "customer_id": not_existing_customer_id,
                            "dunning_communication_delay_enabled": False,
                            "payment_collection_method": "automatic",
                            "skip_billing_manifest_taxes": False,
                            "payment_profile_id": not_existing_payment_profile_id,
                        }
                    }
                )
            )

            assert e.value.response_code == 422
            assert e.value.message == "A Customer must be specified for the subscription to be valid."

    def test_create_subscription_given_invalid_credentials_then_thrown_exception_with_401_status_code(
        self,
        unauthorized_client: AdvancedBillingClient,
    ):
        with pytest.raises(APIException) as e:
            unauthorized_client.subscriptions.create_subscription(
                CreateSubscriptionRequest.from_dictionary(
                    {
                        "subscription": {
                            "product_id": 2132441,
                            "customer_id": 23214,
                            "dunning_communication_delay_enabled": False,
                            "payment_collection_method": "automatic",
                            "skip_billing_manifest_taxes": False,
                            "payment_profile_id": 213412,
                        }
                    }
                )
            )

            assert e.value.response_code == 401

    def test_list_subscriptions_filtering_by_metadata_given_filter_by_metadata_then_return_subscription_having_this_metadata(
        self,
        custom_fields_controller: CustomFieldsController,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        subscriptions_controller: SubscriptionsController,
    ):
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestSubscriptions_Product_Family_Name_3",
                        "description": "TestSubscriptions_Product_Family_Description_3",
                    }
                }
            )
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest.from_dictionary(
                {
                    "product": {
                        "name": "TestSubscriptions_Product_Name_3",
                        "handle": "testsubscriptions_product_handle_3",
                        "description": "TestSubscriptions_Product_Description_3",
                        "interval": 1,
                        "price_in_cents": 10,
                        "interval_unit": IntervalUnit.DAY,
                    }
                }
            ),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest.from_dictionary(
                {
                    "customer": {
                        "first_name": "TestSubscriptions_Customer_FirstName_3",
                        "last_name": "TestSubscriptions_Customer_LastName_3",
                        "email": "tsce2@email.com",
                        "cc_emails": ["email@email.com"],
                        "organization": "TestSubscriptions_CustomerOrganization_3",
                        "reference": "TestSubscriptions_CustomerReference_3",
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
                        "locale": None,
                    }
                }
            )
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest.from_dictionary(
                {
                    "payment_profile": {
                        "customer_id": customer.id,
                        "payment_type": PaymentType.CREDIT_CARD,
                        "expiration_month": 12,
                        "expiration_year": 2027,
                        "full_number": "4111111111111111",
                    }
                }
            )
        ).payment_profile

        # THEN
        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest.from_dictionary(
                {
                    "subscription": {
                        "product_id": product.id,
                        "customer_id": customer.id,
                        "dunning_communication_delay_enabled": False,
                        "payment_collection_method": "automatic",
                        "skip_billing_manifest_taxes": False,
                        "payment_profile_id": payment_profile.id,
                    }
                }
            )
        ).subscription

        custom_fields_controller.create_metafields(
            ResourceType.SUBSCRIPTIONS,
            CreateMetafieldsRequest.from_dictionary(
                {
                    "metafields": [
                        {
                            "name": "Dropdown field",
                            "input_type": "dropdown",
                            "enum": ["option 1", "option 2"],
                            "scope": {"public_edit": "1", "public_show": "1"},
                        },
                    ]
                }
            ),
        )
        custom_fields_controller.create_metadata(
            ResourceType.SUBSCRIPTIONS,
            subscription.id,
            CreateMetadataRequest.from_dictionary(
                {
                    "metadata": [
                        {"name": "Dropdown field", "value": "option 1"},
                    ]
                }
            ),
        )

        # THEN
        results = subscriptions_controller.list_subscriptions({"metadata": {"Dropdown field": "option 1"}})

        assert len(results) == 1
        found_subscription: Subscription = results[0].subscription

        assert subscription.id == found_subscription.id

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)
