from advancedbilling.advanced_billing_client import (
    CustomersController,
    CustomFieldsController,
    PaymentProfilesController,
    ProductFamiliesController,
    ProductsController,
    SubscriptionsController,
)
from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_metadata_request import CreateMetadataRequest
from advancedbilling.models.create_metafields_request import CreateMetafieldsRequest
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
from advancedbilling.models.metadata import Metadata
from advancedbilling.models.metafield import Metafield
from advancedbilling.models.metafield_scope import MetafieldScope
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.resource_type import ResourceType
from advancedbilling.models.subscription import Subscription

from .data import CustomFieldsAssertCases, InitCases
from .utils import assert_properties


class TestCustomFields:
    def test_create_multiple_metafields_given_subscription_resource_type_and_dropdown_type_and_not_configured_text_field_then_dropdown_has_enum_with_two_options_and_text_field_is_configured_as_text_input_by_default(  # noqa: E501
        self, custom_fields_controller: CustomFieldsController
    ):
        subscription_metafields: list[Metafield] = custom_fields_controller.create_metafields(
            ResourceType.SUBSCRIPTIONS,
            CreateMetafieldsRequest(InitCases.get_metafields_dropdown_with_text_field_request()),
        )

        assert len(subscription_metafields) == 2
        dropdown_metafield, text_input_metafield = subscription_metafields

        dropdown_metafield_scope: MetafieldScope = dropdown_metafield.scope
        text_input_metafield_scope: MetafieldScope = text_input_metafield.scope

        assert len(dropdown_metafield.enum) == 2

        assert_properties(dropdown_metafield, CustomFieldsAssertCases.get_dropdown_subscriptions_metafield_data())
        assert_properties(text_input_metafield, CustomFieldsAssertCases.get_text_input_subscriptions_metafield_data())
        assert_properties(
            text_input_metafield_scope,
            CustomFieldsAssertCases.get_text_input_subscriptions_metafield_scope_data(),
        )
        assert_properties(dropdown_metafield_scope, CustomFieldsAssertCases.get_dropdown_subscriptions_metafield_scope_data())

    def test_create_single_metafields_given_customer_resource_type_and_radio_type_then_radio_has_enum_with_two_options(
        self, custom_fields_controller: CustomFieldsController
    ):
        customer_metafields = custom_fields_controller.create_metafields(
            ResourceType.CUSTOMERS,
            CreateMetafieldsRequest(InitCases.get_metafields_radio_request()),
        )

        assert len(customer_metafields) == 1
        dropdown_metafield: Metafield = customer_metafields[0]
        assert len(dropdown_metafield.enum) == 2

        assert_properties(dropdown_metafield, CustomFieldsAssertCases.get_dropdown_customer_metafield_data())

    def test_create_metadata_for_subscription_given_subscription_with_metafields_then_subscription_should_have_added_metadata(
        self,
        custom_fields_controller: CustomFieldsController,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
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

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription

        # THEN
        metafields: list[Metafield] = custom_fields_controller.create_metafields(
            ResourceType.SUBSCRIPTIONS,
            CreateMetafieldsRequest(metafields=InitCases.get_metafields_dropdown_with_text_field_request()),
        )

        assert len(metafields) == 2
        dropdown_metafield, text_input_metafield = metafields

        # THEN
        metadata: list[Metadata] = custom_fields_controller.create_metadata(
            ResourceType.SUBSCRIPTIONS,
            subscription.id,
            CreateMetadataRequest(InitCases.get_metadata_dropdown_with_text_field_request()),
        )

        assert len(metadata) == 2
        dropdown_metadata, text_field_metadata = metadata

        assert_properties(
            dropdown_metadata,
            CustomFieldsAssertCases.get_dropdown_subscription_metadata_data(subscription, dropdown_metafield),
        )
        assert_properties(
            text_field_metadata,
            CustomFieldsAssertCases.get_text_field_metadata_data(subscription, text_input_metafield),
        )

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)

    def test_create_metadata_for_customer_given_customer_with_metafields_then_customer_should_have_added_metadata(
        self,
        custom_fields_controller: CustomFieldsController,
        customers_controller: CustomersController,
    ):
        # GIVEN
        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest(InitCases.get_customer_request())
        ).customer

        # THEN
        metafields: list[Metafield] = custom_fields_controller.create_metafields(
            ResourceType.CUSTOMERS,
            CreateMetafieldsRequest(metafields=InitCases.get_metafields_radio_request()),
        )

        assert len(metafields) == 1
        (created_metafield,) = metafields

        # THEN
        metadata: list[Metadata] = custom_fields_controller.create_metadata(
            ResourceType.CUSTOMERS,
            customer.id,
            CreateMetadataRequest(InitCases.get_metadata_radio_request()),
        )

        assert len(metadata) == 1
        (radio_metadata,) = metadata

        assert_properties(
            radio_metadata, CustomFieldsAssertCases.get_radio_customers_metadata_data(customer, created_metafield)
        )

        customers_controller.delete_customer(customer.id)
