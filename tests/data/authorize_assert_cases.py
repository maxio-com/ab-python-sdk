class AuthorizeAssertCases:
    @staticmethod
    def get_site_data() -> dict:
        return {
            "id": 4502,
            "name": "Python SDK Env",
            "subdomain": "python-sdk",
            "currency": "USD",
            "seller_id": 722159,
            "relationship_invoicing_enabled": True,
            "customer_hierarchy_enabled": False,
            "whopays_enabled": False,
            "whopays_default_payer": "self-ungrouped",
            "test": True,
            "default_payment_collection_method": "automatic",
        }

    @staticmethod
    def get_allocation_settings_data() -> dict:
        return {
            "accrue_charge": "true",
            "upgrade_charge": "prorated",
            "downgrade_credit": "none",
        }

    @staticmethod
    def get_organization_address_data() -> dict:
        return {
            "street": "Asdf Street",
            "line_2": "123/444",
            "city": "San Antonio",
            "state": "TX",
            "zip": "78015",
            "country": "US",
            "name": "Developer Experience",
            "phone": "555 111 222",
        }

    @staticmethod
    def get_tax_configuration_data() -> dict:
        return {
            "kind": "custom",
            "destination_address": "shipping_then_billing",
            "fully_configured": False,
        }

    @staticmethod
    def get_net_terms_data() -> dict:
        return {
            "default_net_terms": 0,
            "automatic_net_terms": 0,
        }
