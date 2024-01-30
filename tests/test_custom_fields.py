from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_metadata_request import CreateMetadataRequest
from advancedbilling.models.create_metafields_request import CreateMetafieldsRequest
from advancedbilling.models.create_or_update_product_request import CreateOrUpdateProductRequest
from advancedbilling.models.create_payment_profile_request import CreatePaymentProfileRequest
from advancedbilling.models.create_product_family_request import CreateProductFamilyRequest
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
from tests.base import TestBase


class TestCustomFields(TestBase):
    def setup_class(self):
        super(TestCustomFields, self).setup_class(self)
        for resource_type in [ResourceType.SUBSCRIPTIONS, ResourceType.CUSTOMERS]:
            metafields = self.client.custom_fields.list_metafields({"resource_type": resource_type}).metafields
            while metafields:
                for m in metafields:
                    self.client.custom_fields.delete_metafield(resource_type, m.name)
                metafields = self.client.custom_fields.list_metafields({"resource_type": resource_type}).metafields

    def test_create_multiple_metafields_given_subscription_resource_type_and_dropdown_type_and_not_configured_text_field_then_dropdown_has_enum_with_two_options_and_text_field_is_configured_as_text_input_by_default(
            self):
        subscription_metafields = self.get_custom_fields_controller().create_metafields(
            ResourceType.SUBSCRIPTIONS,
            CreateMetafieldsRequest.from_dictionary(
                {
                    "metafields": [
                        {
                            "name": "Dropdown field",
                            "input_type": "dropdown",
                            "enum": [
                                "option 1",
                                "option 2"
                            ],
                            "scope": {
                                "public_edit": "1",
                                "public_show": "1"
                            }
                        },
                        {
                            "name": "Text Field"
                        }
                    ]
                }
            )
        )

        assert 2 == len(subscription_metafields)
        dropdown_metafield: Metafield = subscription_metafields[0]
        text_input_metafield: Metafield = subscription_metafields[1]

        assert 2 == len(dropdown_metafield.enum)
        assert ['option 1', 'option 2'] == dropdown_metafield.enum
        assert 'dropdown' == dropdown_metafield.input_type
        dropdown_metafield_scope: MetafieldScope = dropdown_metafield.scope
        assert "0" == dropdown_metafield_scope.csv
        assert "0" == dropdown_metafield_scope.invoices
        assert "0" == dropdown_metafield_scope.portal
        assert "1" == dropdown_metafield_scope.public_edit
        assert "1" == dropdown_metafield_scope.public_show
        assert "0" == dropdown_metafield_scope.statements

        assert 'text' == text_input_metafield.input_type
        assert None == text_input_metafield.enum
        text_input_metafield_scope: MetafieldScope = text_input_metafield.scope
        assert "0" == text_input_metafield_scope.csv
        assert "0" == text_input_metafield_scope.invoices
        assert "0" == text_input_metafield_scope.portal
        assert "0" == text_input_metafield_scope.public_edit
        assert "0" == text_input_metafield_scope.public_show
        assert "0" == text_input_metafield_scope.statements

    def test_create_single_metafields_given_customer_resource_type_and_radio_type_then_radio_has_enum_with_two_options(
            self):
        customer_metafields = self.get_custom_fields_controller().create_metafields(
            ResourceType.CUSTOMERS,
            CreateMetafieldsRequest.from_dictionary(
                {
                    "metafields":
                        {
                            "name": "Radio field",
                            "input_type": "radio",
                            "enum": [
                                "option 1",
                                "option 2"
                            ],
                            "scope": {
                                "csv": "1",
                                "invoices": "1",
                                "portal": "1"
                            }
                        }
                }
            )
        )

        assert 1 == len(customer_metafields)
        dropdown_metafield: Metafield = customer_metafields[0]

        assert 2 == len(dropdown_metafield.enum)
        assert ['option 1', 'option 2'] == dropdown_metafield.enum
        assert 'radio' == dropdown_metafield.input_type
        assert 'Radio field' == dropdown_metafield.name

    def test_create_metadata_for_subscription_given_subscription_with_metafields_then_subscription_should_have_added_metadata(
            self):
        # GIVEN
        product_family: ProductFamily = self.get_product_families_controller().create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestCustomFields_Product_Family_Name_1",
                        "description": "TestCustomFields_Product_Family_Description_1",
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
                            "name": "TestCustomFields_Product_Name_1",
                            "handle": "testcustomfields_product_handle_1",
                            "description": "TestCustomFields_Product_Description_1",
                            "interval": 1,
                            "price_in_cents": 10,
                            "interval_unit": IntervalUnit.DAY
                        }
                }
            )).product
        customer: Customer = self.get_customers_controller().create_customer(CreateCustomerRequest.from_dictionary(
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
                    }
                }
            )).subscription

        # THEN
        metafields = self.get_custom_fields_controller().create_metafields(
            ResourceType.SUBSCRIPTIONS,
            CreateMetafieldsRequest.from_dictionary(
                {
                    "metafields": [
                        {
                            "name": "Dropdown field",
                            "input_type": "dropdown",
                            "enum": [
                                "option 1",
                                "option 2"
                            ],
                            "scope": {
                                "public_edit": "1",
                                "public_show": "1"
                            }
                        },
                        {
                            "name": "Text Field"
                        }
                    ]
                }
            )
        )
        dropdown_metafield = metafields[0]
        text_input_metafield = metafields[1]

        # THEN
        metadata = self.get_custom_fields_controller().create_metadata(
            ResourceType.SUBSCRIPTIONS,
            subscription.id,
            CreateMetadataRequest.from_dictionary(
                {
                    "metadata": [
                        {
                            "name": "Dropdown field",
                            "value": "option 1"
                        },
                        {
                            "name": "Text Field",
                            "value": "Text field"
                        }
                    ]
                }
            )
        )

        assert 2 == len(metadata)

        dropdown_metadata: Metadata = metadata[0]
        text_field_metadata: Metadata = metadata[1]

        assert subscription.id == dropdown_metadata.resource_id
        assert dropdown_metafield.id == dropdown_metadata.metafield_id
        assert "option 1" == dropdown_metadata.value
        assert "Dropdown field" == dropdown_metadata.name

        assert subscription.id == text_field_metadata.resource_id
        assert text_input_metafield.id == text_field_metadata.metafield_id
        assert "Text field" == text_field_metadata.value
        assert "Text Field" == text_field_metadata.name

        self.get_subscriptions_controller().purge_subscription(subscription.id, customer.id)
        self.get_customers_controller().delete_customer(customer.id)

    def test_create_metadata_for_customer_given_customer_with_metafields_then_customer_should_have_added_metadata(self):
        # GIVEN
        customer: Customer = self.get_customers_controller().create_customer(CreateCustomerRequest.from_dictionary(
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
                    "locale": None
                }
            }
        )).customer
        # THEN
        metafields = self.get_custom_fields_controller().create_metafields(
            ResourceType.CUSTOMERS,
            CreateMetafieldsRequest.from_dictionary(
                {
                    "metafields":
                        {
                            "name": "Radio field",
                            "input_type": "radio",
                            "enum": [
                                "option 1",
                                "option 2"
                            ],
                            "scope": {
                                "csv": "1",
                                "invoices": "1",
                                "portal": "1"
                            }
                        }
                }
            )
        )
        created_metafield: Metafield = metafields[0]

        # THEN
        metadata = self.get_custom_fields_controller().create_metadata(
            ResourceType.CUSTOMERS,
            customer.id,
            CreateMetadataRequest.from_dictionary(
                {
                    "metadata": [
                        {
                            "name": "Radio field",
                            "value": "option 1"
                        },
                    ]
                }
            )
        )

        assert 1 == len(metadata)
        radio_metadata: Metadata = metadata[0]

        assert customer.id == radio_metadata.resource_id
        assert created_metafield.id == radio_metadata.metafield_id
        assert "option 1" == radio_metadata.value
        assert "Radio field" == radio_metadata.name

        self.get_customers_controller().delete_customer(customer.id)
