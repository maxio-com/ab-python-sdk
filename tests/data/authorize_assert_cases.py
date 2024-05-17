class AuthorizeAssertCases:
    @staticmethod
    def get_result_data() -> dict:
        return {
            "site": {
                "id": 86561,
                "name": "Python SDK",
                "subdomain": "python-sdk",
                "currency": "USD",
                "seller_id": 56887,
                "relationship_invoicing_enabled": True,
                "customer_hierarchy_enabled": False,
                "whopays_enabled": False,
                "whopays_default_payer": "self-ungrouped",
                "test": True,
                "default_payment_collection_method": "automatic",
                "allocation_settings": {
                    "accrue_charge": "true",
                    "upgrade_charge": "prorated",
                    "downgrade_credit": "none",
                },
                "organization_address": {
                    "street": "Asdf Street",
                    "line_2": "123/444",
                    "city": "San Antonio",
                    "state": "TX",
                    "zip": "78015",
                    "country": "US",
                    "name": "Developer Experience",
                    "phone": "555 111 222",
                },
                "tax_configuration": {
                    "kind": "custom",
                    "destination_address": "shipping_then_billing",
                    "fully_configured": False,
                },
                "net_terms": {
                    "default_net_terms": 0,
                    "automatic_net_terms": 0,
                },
            },
        }
