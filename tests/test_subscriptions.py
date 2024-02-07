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
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.resource_type import ResourceType
from advancedbilling.models.subscription import Subscription

from .data import InitCases, SubscriptionsAssertCases
from .utils import assert_properties


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

        on_off_component: Component = components_controller.create_on_off_component(
            product_family.id,
            CreateOnOffComponent(InitCases.get_on_off_component_data()),
        ).component

        prepaid_component: Component = components_controller.create_prepaid_usage_component(
            product_family.id,
            CreatePrepaidComponent(InitCases.get_prepaid_component_data()),
        ).component

        # THEN
        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(
                InitCases.get_subscription_request_with_components(
                    product.id,
                    customer.id,
                    payment_profile.id,
                    components=[on_off_component, prepaid_component],
                )
            )
        ).subscription

        assert_properties(
            subscription,
            SubscriptionsAssertCases.get_subscription_data(product, customer, payment_profile),
        )

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
            CreateProductFamilyRequest(InitCases.get_product_family_request())
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest(InitCases.get_product_request()),
        ).product

        # THEN
        with pytest.raises(ErrorListResponseException) as e:
            subscriptions_controller.create_subscription(
                CreateSubscriptionRequest(
                    InitCases.get_subscription_request(
                        product.id,
                        not_existing_customer_id,
                        not_existing_payment_profile_id,
                    )
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
                CreateSubscriptionRequest(
                    InitCases.get_subscription_request(
                        product_id=2132441,
                        customer_id=23214,
                        payment_profile_id=213412,
                    )
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

        # THEN
        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription

        custom_fields_controller.create_metafields(
            ResourceType.SUBSCRIPTIONS,
            CreateMetafieldsRequest(InitCases.get_metafields_dropdown_request()),
        )
        custom_fields_controller.create_metadata(
            ResourceType.SUBSCRIPTIONS,
            subscription.id,
            CreateMetadataRequest(InitCases.get_metadata_dropdown_request()),
        )

        # THEN
        results = subscriptions_controller.list_subscriptions({"metadata": {"Dropdown field": "option 1"}})

        assert len(results) == 1
        found_subscription: Subscription = results[0].subscription

        assert subscription.id == found_subscription.id

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)
