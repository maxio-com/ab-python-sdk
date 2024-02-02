from uuid import uuid4

from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.product import Product


class CustomFieldsInitCases:
    @staticmethod
    def get_metafields_dropdown_request() -> list[dict]:
        return [
            {
                "name": "Dropdown field",
                "input_type": "dropdown",
                "enum": ["option 1", "option 2"],
                "scope": {"public_edit": "1", "public_show": "1"},
            },
            {"name": "Text Field"},
        ]

    @staticmethod
    def get_metafields_radio_request() -> dict:
        return {
            "name": "Radio field",
            "input_type": "radio",
            "enum": ["option 1", "option 2"],
            "scope": {"csv": "1", "invoices": "1", "portal": "1"},
        }

    @staticmethod
    def get_product_family_request() -> dict:
        product_family_id = str(uuid4())
        return {
            "name": f"TestCustomFields_Product_Family_Name_{product_family_id}",
            "description": f"TestCustomFields_Product_Family_Description_{product_family_id}",
        }

    @staticmethod
    def get_product_request() -> dict:
        product_id = str(uuid4())
        return {
            "name": f"TestCustomFields_Product_Name_{product_id}",
            "handle": f"testcustomfields_product_handle_{product_id}",
            "description": f"TestCustomFields_Product_Description_{product_id}",
            "interval": 1,
            "price_in_cents": 10,
            "interval_unit": IntervalUnit.DAY,
        }

    @staticmethod
    def get_customer_request() -> dict:
        customer_id = str(uuid4())
        return {
            "first_name": f"TestCustomFields_Customer_FirstName_{customer_id}",
            "last_name": f"TestCustomFields_Customer_LastName_{customer_id}",
            "email": "tsce1@email.com",
            "cc_emails": ["email@email.com"],
            "organization": f"TestCustomFields_CustomerOrganization_{customer_id}",
            "reference": f"TestCustomFields_CustomerReference_{customer_id}",
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

    @staticmethod
    def get_payment_profile_request(customer: Customer) -> dict:
        return {
            "customer_id": customer.id,
            "payment_type": PaymentType.CREDIT_CARD,
            "expiration_month": 12,
            "expiration_year": 2027,
            "full_number": "4111111111111111",
        }

    @staticmethod
    def get_subscription_request(product: Product, customer: Customer, payment_profile: CreditCardPaymentProfile) -> dict:
        return {
            "product_id": product.id,
            "customer_id": customer.id,
            "dunning_communication_delay_enabled": False,
            "payment_collection_method": "automatic",
            "skip_billing_manifest_taxes": False,
            "payment_profile_id": payment_profile.id,
        }

    @staticmethod
    def get_metadata_dropdown_request() -> list[dict]:
        return [
            {"name": "Dropdown field", "value": "option 1"},
            {"name": "Text Field", "value": "Text field"},
        ]

    @staticmethod
    def get_metadata_radio_request() -> list[dict]:
        return [{"name": "Radio field", "value": "option 1"}]
