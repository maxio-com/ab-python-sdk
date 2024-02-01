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
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.metadata import Metadata
from advancedbilling.models.metafield import Metafield
from advancedbilling.models.metafield_scope import MetafieldScope
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.resource_type import ResourceType
from advancedbilling.models.subscription import Subscription


class TestCustomFields:
    def test_create_multiple_metafields_given_subscription_resource_type_and_dropdown_type_and_not_configured_text_field_then_dropdown_has_enum_with_two_options_and_text_field_is_configured_as_text_input_by_default(  # noqa: E501
        self, custom_fields_controller: CustomFieldsController
    ):
        subscription_metafields: list[Metafield] = custom_fields_controller.create_metafields(
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
                        {"name": "Text Field"},
                    ]
                }
            ),
        )

        assert len(subscription_metafields) == 2
        dropdown_metafield, text_input_metafield = subscription_metafields

        dropdown_metafield_scope: MetafieldScope = dropdown_metafield.scope
        text_input_metafield_scope: MetafieldScope = text_input_metafield.scope

        assert len(dropdown_metafield.enum) == 2
        assert dropdown_metafield.enum == ["option 1", "option 2"]
        assert dropdown_metafield.input_type == "dropdown"
        assert dropdown_metafield_scope.csv == "0"
        assert dropdown_metafield_scope.invoices == "0"
        assert dropdown_metafield_scope.portal == "0"
        assert dropdown_metafield_scope.public_edit == "1"
        assert dropdown_metafield_scope.public_show == "1"
        assert dropdown_metafield_scope.statements == "0"

        assert text_input_metafield.input_type == "text"
        assert text_input_metafield.enum is None
        assert text_input_metafield_scope.csv == "0"
        assert text_input_metafield_scope.invoices == "0"
        assert text_input_metafield_scope.portal == "0"
        assert text_input_metafield_scope.public_edit == "0"
        assert text_input_metafield_scope.public_show == "0"
        assert text_input_metafield_scope.statements == "0"

    def test_create_single_metafields_given_customer_resource_type_and_radio_type_then_radio_has_enum_with_two_options(
        self, custom_fields_controller: CustomFieldsController
    ):
        customer_metafields = custom_fields_controller.create_metafields(
            ResourceType.CUSTOMERS,
            CreateMetafieldsRequest.from_dictionary(
                {
                    "metafields": {
                        "name": "Radio field",
                        "input_type": "radio",
                        "enum": ["option 1", "option 2"],
                        "scope": {"csv": "1", "invoices": "1", "portal": "1"},
                    }
                }
            ),
        )

        assert 1 == len(customer_metafields)
        dropdown_metafield: Metafield = customer_metafields[0]

        assert 2 == len(dropdown_metafield.enum)
        assert ["option 1", "option 2"] == dropdown_metafield.enum
        assert "radio" == dropdown_metafield.input_type
        assert "Radio field" == dropdown_metafield.name

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
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestCustomFields_Product_Family_Name_1",
                        "description": "TestCustomFields_Product_Family_Description_1",
                    }
                }
            )
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest.from_dictionary(
                {
                    "product": {
                        "name": "TestCustomFields_Product_Name_1",
                        "handle": "testcustomfields_product_handle_1",
                        "description": "TestCustomFields_Product_Description_1",
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
                        "first_name": "TestCustomFields_Customer_FirstName_1",
                        "last_name": "TestCustomFields_Customer_LastName_1",
                        "email": "tsce1@email.com",
                        "cc_emails": ["email@email.com"],
                        "organization": "TestCustomFields_CustomerOrganization_1",
                        "reference": "TestCustomFields_CustomerReference_1",
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

        # THEN
        metafields: list[Metafield] = custom_fields_controller.create_metafields(
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
                        {"name": "Text Field"},
                    ]
                }
            ),
        )

        assert len(metafields) == 2
        dropdown_metafield, text_input_metafield = metafields

        # THEN
        metadata: list[Metadata] = custom_fields_controller.create_metadata(
            ResourceType.SUBSCRIPTIONS,
            subscription.id,
            CreateMetadataRequest.from_dictionary(
                {
                    "metadata": [
                        {"name": "Dropdown field", "value": "option 1"},
                        {"name": "Text Field", "value": "Text field"},
                    ]
                }
            ),
        )

        assert len(metadata) == 2
        dropdown_metadata, text_field_metadata = metadata

        assert dropdown_metadata.resource_id == subscription.id
        assert dropdown_metadata.metafield_id == dropdown_metafield.id
        assert dropdown_metadata.value == "option 1"
        assert dropdown_metadata.name == "Dropdown field"

        assert text_field_metadata.resource_id == subscription.id
        assert text_field_metadata.metafield_id == text_input_metafield.id
        assert text_field_metadata.value == "Text field"
        assert text_field_metadata.name == "Text Field"

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)

    def test_create_metadata_for_customer_given_customer_with_metafields_then_customer_should_have_added_metadata(
        self,
        custom_fields_controller: CustomFieldsController,
        customers_controller: CustomersController,
    ):
        # GIVEN
        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest.from_dictionary(
                {
                    "customer": {
                        "first_name": "TestCustomFields_Customer_FirstName_1",
                        "last_name": "TestCustomFields_Customer_LastName_1",
                        "email": "tsce1@email.com",
                        "cc_emails": ["email@email.com"],
                        "organization": "TestCustomFields_CustomerOrganization_1",
                        "reference": "TestCustomFields_CustomerReference_1",
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

        # THEN
        metafields: list[Metafield] = custom_fields_controller.create_metafields(
            ResourceType.CUSTOMERS,
            CreateMetafieldsRequest.from_dictionary(
                {
                    "metafields": {
                        "name": "Radio field",
                        "input_type": "radio",
                        "enum": ["option 1", "option 2"],
                        "scope": {"csv": "1", "invoices": "1", "portal": "1"},
                    }
                }
            ),
        )

        assert len(metafields) == 1
        (created_metafield,) = metafields

        # THEN
        metadata: list[Metadata] = custom_fields_controller.create_metadata(
            ResourceType.CUSTOMERS,
            customer.id,
            CreateMetadataRequest.from_dictionary(
                {
                    "metadata": [
                        {"name": "Radio field", "value": "option 1"},
                    ]
                }
            ),
        )

        assert len(metadata) == 1
        (radio_metadata,) = metadata

        assert customer.id == radio_metadata.resource_id
        assert created_metafield.id == radio_metadata.metafield_id
        assert radio_metadata.value == "option 1"
        assert radio_metadata.name == "Radio field"

        customers_controller.delete_customer(customer.id)
