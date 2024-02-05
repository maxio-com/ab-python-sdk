from advancedbilling.models.customer import Customer
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.subscription import Subscription


class InvoiceAssertCases:
    @staticmethod
    def get_invoice_data(
        customer: Customer,
        product: Product,
        product_family: ProductFamily,
        subscription: Subscription,
    ) -> dict:
        return {
            "billing_address": {
                "city": "test City",
                "country": "US",
                "line_2": None,
                "state": "test State",
                "street": "65581 Auer Expressway",
                "zip": "15217",
            },
            "collection_method": "remittance",
            "consolidation_level": "none",
            "credit_amount": "0.0",
            "currency": "USD",
            "customer": {
                "chargify_id": customer.id,
                "email": customer.email,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "organization": customer.organization,
                "reference": customer.reference,
                "vat_number": customer.vat_number,
            },
            "customer_id": customer.id,
            "discount_amount": "270.0",
            "due_amount": "1530.0",
            "group_primary_subscription_id": None,
            "line_items": [
                {
                    "title": "TestCase_Product_Name_1",
                    "quantity": "12.0",
                    "unit_price": "150.0",
                    "total_amount": "1530.0",
                }
            ],
            "memo": "Thanks for your business! If you have any questions, please contact your account manager.",
            "paid_amount": "0.0",
            "parent_invoice_uid": None,
            "parent_invoice_number": None,
            "payment_instructions": 'Please make checks payable to "Acme, Inc."',
            "product_family_name": product_family.name,
            "product_name": product.name,
            "refund_amount": "0.0",
            "role": "adhoc",
            "status": "open",
            "subscription_id": subscription.id,
            "subtotal_amount": "1800.0",
            "tax_amount": "0.0",
            "total_amount": "1530.0",
            "seller": {
                "name": "Developer Experience",
                "phone": "555 111 222",
                "address": {
                    "city": "San Antonio",
                    "country": "US",
                    "line_2": "123/444",
                    "state": "TX",
                    "street": "Asdf Street",
                    "zip": "78015",
                },
            },
            "shipping_address": {
                "city": "Ohio",
                "country": "US",
                "line_2": "test address two",
                "state": "TX",
                "street": "test address",
                "zip": "test zip",
            },
        }
