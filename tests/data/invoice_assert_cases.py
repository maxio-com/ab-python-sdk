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
        # billing_address: InvoiceAddress = invoice.billing_address
        # assert "test City" == billing_address.city
        # assert "US" == billing_address.country
        # assert None == billing_address.line_2
        # assert "test State" == billing_address.state
        # assert "65581 Auer Expressway" == billing_address.street
        # assert "15217" == billing_address.zip

        # assert "remittance" == invoice.collection_method
        # assert "none" == invoice.consolidation_level
        # assert "0.0" == invoice.credit_amount
        # assert 0 == len(invoice.credits)
        # assert "USD" == invoice.currency
        # assert 0 == len(invoice.custom_fields)

        # invoice_customer: InvoiceCustomer = invoice.customer
        # assert customer.id == invoice_customer.chargify_id
        # assert customer.email == invoice_customer.email
        # assert customer.first_name == invoice_customer.first_name
        # assert customer.last_name == invoice_customer.last_name
        # assert customer.organization == invoice_customer.organization
        # assert customer.reference == invoice_customer.reference
        # assert customer.vat_number == invoice_customer.vat_number

        # assert customer.id == invoice.customer_id
        # assert "270.0" == invoice.discount_amount
        # assert 1 == len(invoice.discounts)
        # assert "1530.0" == invoice.due_amount
        # assert invoice.group_primary_subscription_id is None
        # assert 1 == len(invoice.line_items)

        # line_item: InvoiceLineItem = invoice.line_items[0]
        # assert "TestInvoices_Product_Name_1" == line_item.title
        # assert "12.0" == line_item.quantity
        # assert "150.0" == line_item.unit_price
        # assert "1530.0" == line_item.total_amount

        # assert "Thanks for your business! If you have any questions, please contact your account manager." == invoice.memo
        # assert "0.0" == invoice.paid_amount
        # assert invoice.parent_invoice_uid is None
        # assert invoice.parent_invoice_number is None
        # assert 'Please make checks payable to "Acme, Inc."' == invoice.payment_instructions
        # assert 0 == len(invoice.payments)
        # assert product_family.name == invoice.product_family_name
        # assert product.name == invoice.product_name
        # assert "0.0" == invoice.refund_amount
        # assert 0 == len(invoice.refunds)
        # assert "adhoc" == invoice.role
        # assert "open" == invoice.status
        # assert subscription.id == invoice.subscription_id
        # assert "1800.0" == invoice.subtotal_amount
        # assert "0.0" == invoice.tax_amount
        # assert 0 == len(invoice.taxes)
        # assert "1530.0" == invoice.total_amount

        # seller: InvoiceSeller = invoice.seller
        # assert "Developer Experience" == seller.name
        # assert "555 111 222" == seller.phone

        # seller_address: InvoiceAddress = seller.address
        # assert "San Antonio" == seller_address.city
        # assert "US" == seller_address.country
        # assert "123/444" == seller_address.line_2
        # assert "TX" == seller_address.state
        # assert "Asdf Street" == seller_address.street
        # assert "78015" == seller_address.zip

        # shipping_address: InvoiceAddress = invoice.shipping_address
        # assert "Ohio" == shipping_address.city
        # assert "US" == shipping_address.country
        # assert "test address two" == shipping_address.line_2
        # assert "TX" == shipping_address.state
        # assert "test address" == shipping_address.street
        # assert "test zip" == shipping_address.zip
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
