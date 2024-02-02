from advancedbilling.models.metafield import Metafield
from advancedbilling.models.subscription import Subscription
from advancedbilling.models.customer import Customer


class CustomFieldsAssertCases:
    @staticmethod
    def get_dropdown_subscriptions_metafield_data() -> dict:
        return {
            "enum": ["option 1", "option 2"],
            "input_type": "dropdown",
        }

    @staticmethod
    def get_text_input_subscriptions_metafield_data() -> dict:
        return {
            "input_type": "text",
            "enum": None,
        }

    @staticmethod
    def get_dropdown_subscriptions_metafield_scope_data() -> dict:
        return {
            "csv": "0",
            "invoices": "0",
            "portal": "0",
            "public_edit": "1",
            "public_show": "1",
            "statements": "0",
        }

    @staticmethod
    def get_text_input_subscriptions_metafield_scope_data() -> dict:
        return {
            "csv": "0",
            "invoices": "0",
            "portal": "0",
            "public_edit": "0",
            "public_show": "0",
            "statements": "0",
        }

    @staticmethod
    def get_dropdown_customer_metafield_data() -> dict:
        return {
            "enum": ["option 1", "option 2"],
            "input_type": "radio",
            "name": "Radio field",
        }

    @staticmethod
    def get_dropdown_subscription_metadata_data(subscription: Subscription, dropdown_metafield: Metafield) -> dict:
        return {
            "resource_id": subscription.id,
            "metafield_id": dropdown_metafield.id,
            "value": "option 1",
            "name": "Dropdown field",
        }

    @staticmethod
    def get_text_field_metadata_data(subscription: Subscription, text_input_metafield: Metafield) -> dict:
        return {
            "resource_id": subscription.id,
            "metafield_id": text_input_metafield.id,
            "value": "Text field",
            "name": "Text Field",
        }

    @staticmethod
    def get_radio_customers_metadata_data(customer: Customer, radio_metafield: Metafield) -> dict:
        return {
            "resource_id": customer.id,
            "metafield_id": radio_metafield.id,
            "value": "option 1",
            "name": "Radio field",
        }
