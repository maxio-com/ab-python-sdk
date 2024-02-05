from uuid import uuid4

from advancedbilling.models.component import Component
from advancedbilling.models.coupon import Coupon
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.pricing_scheme import PricingScheme


class InitCases:
    @staticmethod
    def get_metafields_dropdown_with_text_field_request() -> list[dict]:
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
    def get_metafields_dropdown_request() -> dict:
        return {
            "name": "Dropdown field",
            "input_type": "dropdown",
            "enum": ["option 1", "option 2"],
            "scope": {"public_edit": "1", "public_show": "1"},
        }

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
        product_family_id = uuid4()
        return {
            "name": f"TestCase_Product_Family_Name_{product_family_id}",
            "description": f"TestCase_Product_Family_Description_{product_family_id}",
        }

    @staticmethod
    def get_product_request() -> dict:
        product_id = uuid4()
        return {
            "name": f"TestCase_Product_Name_{product_id}",
            "handle": f"testcase_product_handle_{product_id}",
            "description": f"TestCase_Product_Description_{product_id}",
            "interval": 1,
            "price_in_cents": 10,
            "interval_unit": IntervalUnit.DAY,
        }

    @staticmethod
    def get_customer_request() -> dict:
        customer_id = uuid4()
        return {
            "first_name": f"TestCase_Customer_FirstName_{customer_id}",
            "last_name": f"TestCase_Customer_LastName_{customer_id}",
            "email": "tsce1@email.com",
            "cc_emails": ["email@email.com"],
            "organization": f"TestCase_CustomerOrganization_{customer_id}",
            "reference": f"TestCase_CustomerReference_{customer_id}",
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
    def get_payment_profile_request(customer_id: int) -> dict:
        return {
            "customer_id": customer_id,
            "payment_type": PaymentType.CREDIT_CARD,
            "expiration_month": 12,
            "expiration_year": 2027,
            "full_number": "4111111111111111",
        }

    @staticmethod
    def get_subscription_request(product_id: int, customer_id: int, payment_profile_id: int) -> dict:
        return {
            "product_id": product_id,
            "customer_id": customer_id,
            "dunning_communication_delay_enabled": False,
            "payment_collection_method": "automatic",
            "skip_billing_manifest_taxes": False,
            "payment_profile_id": payment_profile_id,
        }

    @staticmethod
    def get_subscription_request_with_components(
        product_id: int, customer_id: int, payment_profile_id: int, components: list[Component]
    ):
        return {
            "product_id": product_id,
            "customer_id": customer_id,
            "dunning_communication_delay_enabled": False,
            "payment_collection_method": "automatic",
            "skip_billing_manifest_taxes": False,
            "payment_profile_id": payment_profile_id,
            "components": [{"component_id": component.id, "enabled": True} for component in components],
        }

    @staticmethod
    def get_metadata_dropdown_with_text_field_request() -> list[dict]:
        return [
            {"name": "Dropdown field", "value": "option 1"},
            {"name": "Text Field", "value": "Text field"},
        ]

    @staticmethod
    def get_metadata_dropdown_request() -> list[dict]:
        return [{"name": "Dropdown field", "value": "option 1"}]

    @staticmethod
    def get_metadata_radio_request() -> list[dict]:
        return [{"name": "Radio field", "value": "option 1"}]

    @staticmethod
    def get_on_off_component_data() -> dict:
        component_id = uuid4()
        return {
            "name": f"TestCase_On_Off_Component_Name_{component_id}",
            "unit_price": "1.0",
            "prices": [{"unit_price": "0.10", "starting_quantity": "0"}],
        }

    @staticmethod
    def get_prepaid_component_data() -> dict:
        component_id = uuid4()
        return {
            "name": f"TestCase_Prepaid_Component_Name_{component_id}",
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

    @staticmethod
    def get_quantity_based_component_data() -> dict:
        component_id = uuid4()
        return {
            "name": f"TestCase_QuantityBased_Component_Name_{component_id}",
            "unit_name": "Component",
            "unit_price": "1.0",
            "allow_fractional_quantities": True,
            "pricing_scheme": PricingScheme.PER_UNIT,
        }

    @staticmethod
    def get_allocation_request(
        on_off_component_id: int,
        quantity_based_component_1_id: int,
        quantity_based_component_2_id: int,
    ) -> list[dict]:
        component_id = uuid4()
        return [
            {
                "component_id": on_off_component_id,
                "memo": f"TestSubscriptionComponents_On_Off_Component_memo_{component_id}",
                "quantity": "1",
            },
            {
                "component_id": quantity_based_component_1_id,
                "memo": f"TestSubscriptionComponents_QuantityBased_Component_memo_{component_id}",
                "quantity": "10.5",
            },
            {
                "component_id": quantity_based_component_2_id,
                "memo": f"TestSubscriptionComponents_QuantityBased_Component_memo_{component_id}",
                "quantity": 1,
            },
        ]

    @staticmethod
    def get_coupon_data() -> dict:
        return {
            "name": "15% off",
            "code": "15OFF",
            "percentage": "15",
            "description": "15% off for life",
            "allow_negative_balance": False,
            "recurring": False,
            "end_date": "2999-08-29T12:00:00-04:00",
            "stackable": False,
            "compounding_strategy": "compound",
            "exclude_mid_period_allocations": True,
            "apply_on_cancel_at_end_of_period": True,
        }

    @classmethod
    def get_invoice_request(cls) -> dict:
        return {
            "issue_date": "2024-01-01",
            "billing_address": {
                "first_name": "Hilario",
                "last_name": "Schmidt",
                "phone": "282-329-2085",
                "address": "65581 Auer Expressway",
                "zip": "15217",
                "country": "US",
                "city": "test City",
                "state": "test State",
            },
            "line_items": [
                {
                    "title": "TestCase_Product_Name_1",
                    "quantity": "12",
                    "unit_price": "150.00",
                    "description": "test invoice",
                }
            ],
        }

    @classmethod
    def get_invoice_request_with_coupon(cls, coupon: Coupon) -> dict:
        invoice_request = cls.get_invoice_request()
        invoice_request["coupons"] = [{"code": coupon.code, "percentage": coupon.percentage}]

        return invoice_request

    @staticmethod
    def get_invoice_request_with_invalid_period() -> dict:
        return {
            "issue_date": "2024-01-01",
            "billing_address": {
                "first_name": "Hilario",
                "last_name": "Schmidt",
                "phone": "282-329-2085",
                "address": "65581 Auer Expressway",
                "zip": "15217",
                "country": "US",
                "city": "test City",
                "state": "test State",
            },
            "line_items": [
                {
                    "title": "TestCase_Product_Name_1",
                    "quantity": "12",
                    "unit_price": "150.00",
                    "description": "test invoice",
                    "period_range_start": "2024-01-01",
                    "period_range_end": "2023-01-01",
                }
            ],
        }
