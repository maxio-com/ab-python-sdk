"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.available_actions import (
    AvailableActions,
)
from advancedbilling.models.invoice_address import (
    InvoiceAddress,
)
from advancedbilling.models.invoice_custom_field import (
    InvoiceCustomField,
)
from advancedbilling.models.invoice_customer import (
    InvoiceCustomer,
)
from advancedbilling.models.invoice_line_item import (
    InvoiceLineItem,
)
from advancedbilling.models.invoice_seller import (
    InvoiceSeller,
)
from advancedbilling.models.proforma_invoice_credit import (
    ProformaInvoiceCredit,
)
from advancedbilling.models.proforma_invoice_discount import (
    ProformaInvoiceDiscount,
)
from advancedbilling.models.proforma_invoice_payment import (
    ProformaInvoicePayment,
)
from advancedbilling.models.proforma_invoice_tax import (
    ProformaInvoiceTax,
)


class ProformaInvoice(object):
    """Implementation of the 'Proforma Invoice' model.

    Attributes:
        uid (str): The model property of type str.
        site_id (int): The model property of type int.
        customer_id (int): The model property of type int.
        subscription_id (int): The model property of type int.
        number (int): The model property of type int.
        sequence_number (int): The model property of type int.
        created_at (datetime): The model property of type datetime.
        delivery_date (date): The model property of type date.
        status (ProformaInvoiceStatus): The model property of type
            ProformaInvoiceStatus.
        collection_method (CollectionMethod): The type of payment collection to be
            used in the subscription. For legacy Statements Architecture valid
            options are - `invoice`, `automatic`. For current Relationship Invoicing
            Architecture valid options are - `remittance`, `automatic`, `prepaid`.
        payment_instructions (str): The model property of type str.
        currency (str): The model property of type str.
        consolidation_level (InvoiceConsolidationLevel): Consolidation level of the
            invoice, which is applicable to invoice consolidation.  It will hold one
            of the following values:  * "none": A normal invoice with no
            consolidation. * "child": An invoice segment which has been combined into
            a consolidated invoice. * "parent": A consolidated invoice, whose
            contents are composed of invoice segments.  "Parent" invoices do not have
            lines of their own, but they have subtotals and totals which aggregate
            the member invoice segments.  See also the [invoice consolidation
            documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-
            Invoice-Consolidation).
        product_name (str): The model property of type str.
        product_family_name (str): The model property of type str.
        role (ProformaInvoiceRole): 'proforma' value is deprecated in favor of
            proforma_adhoc and proforma_automatic
        seller (InvoiceSeller): Information about the seller (merchant) listed on the
            masthead of the invoice.
        customer (InvoiceCustomer): Information about the customer who is owner or
            recipient the invoiced subscription.
        memo (str): The model property of type str.
        billing_address (InvoiceAddress): The model property of type InvoiceAddress.
        shipping_address (InvoiceAddress): The model property of type InvoiceAddress.
        subtotal_amount (str): The model property of type str.
        discount_amount (str): The model property of type str.
        tax_amount (str): The model property of type str.
        total_amount (str): The model property of type str.
        credit_amount (str): The model property of type str.
        paid_amount (str): The model property of type str.
        refund_amount (str): The model property of type str.
        due_amount (str): The model property of type str.
        line_items (List[InvoiceLineItem]): The model property of type
            List[InvoiceLineItem].
        discounts (List[ProformaInvoiceDiscount]): The model property of type
            List[ProformaInvoiceDiscount].
        taxes (List[ProformaInvoiceTax]): The model property of type
            List[ProformaInvoiceTax].
        credits (List[ProformaInvoiceCredit]): The model property of type
            List[ProformaInvoiceCredit].
        payments (List[ProformaInvoicePayment]): The model property of type
            List[ProformaInvoicePayment].
        custom_fields (List[InvoiceCustomField]): The model property of type
            List[InvoiceCustomField].
        public_url (str): The model property of type str.
        available_actions (AvailableActions): The model property of type
            AvailableActions.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": "uid",
        "site_id": "site_id",
        "customer_id": "customer_id",
        "subscription_id": "subscription_id",
        "number": "number",
        "sequence_number": "sequence_number",
        "created_at": "created_at",
        "delivery_date": "delivery_date",
        "status": "status",
        "collection_method": "collection_method",
        "payment_instructions": "payment_instructions",
        "currency": "currency",
        "consolidation_level": "consolidation_level",
        "product_name": "product_name",
        "product_family_name": "product_family_name",
        "role": "role",
        "seller": "seller",
        "customer": "customer",
        "memo": "memo",
        "billing_address": "billing_address",
        "shipping_address": "shipping_address",
        "subtotal_amount": "subtotal_amount",
        "discount_amount": "discount_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "credit_amount": "credit_amount",
        "paid_amount": "paid_amount",
        "refund_amount": "refund_amount",
        "due_amount": "due_amount",
        "line_items": "line_items",
        "discounts": "discounts",
        "taxes": "taxes",
        "credits": "credits",
        "payments": "payments",
        "custom_fields": "custom_fields",
        "public_url": "public_url",
        "available_actions": "available_actions",
    }

    _optionals = [
        "uid",
        "site_id",
        "customer_id",
        "subscription_id",
        "number",
        "sequence_number",
        "created_at",
        "delivery_date",
        "status",
        "collection_method",
        "payment_instructions",
        "currency",
        "consolidation_level",
        "product_name",
        "product_family_name",
        "role",
        "seller",
        "customer",
        "memo",
        "billing_address",
        "shipping_address",
        "subtotal_amount",
        "discount_amount",
        "tax_amount",
        "total_amount",
        "credit_amount",
        "paid_amount",
        "refund_amount",
        "due_amount",
        "line_items",
        "discounts",
        "taxes",
        "credits",
        "payments",
        "custom_fields",
        "public_url",
        "available_actions",
    ]

    _nullables = [
        "customer_id",
        "subscription_id",
        "number",
        "sequence_number",
        "public_url",
    ]

    def __init__(
        self,
        uid=APIHelper.SKIP,
        site_id=APIHelper.SKIP,
        customer_id=APIHelper.SKIP,
        subscription_id=APIHelper.SKIP,
        number=APIHelper.SKIP,
        sequence_number=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        delivery_date=APIHelper.SKIP,
        status=APIHelper.SKIP,
        collection_method=APIHelper.SKIP,
        payment_instructions=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        consolidation_level=APIHelper.SKIP,
        product_name=APIHelper.SKIP,
        product_family_name=APIHelper.SKIP,
        role=APIHelper.SKIP,
        seller=APIHelper.SKIP,
        customer=APIHelper.SKIP,
        memo=APIHelper.SKIP,
        billing_address=APIHelper.SKIP,
        shipping_address=APIHelper.SKIP,
        subtotal_amount=APIHelper.SKIP,
        discount_amount=APIHelper.SKIP,
        tax_amount=APIHelper.SKIP,
        total_amount=APIHelper.SKIP,
        credit_amount=APIHelper.SKIP,
        paid_amount=APIHelper.SKIP,
        refund_amount=APIHelper.SKIP,
        due_amount=APIHelper.SKIP,
        line_items=APIHelper.SKIP,
        discounts=APIHelper.SKIP,
        taxes=APIHelper.SKIP,
        credits=APIHelper.SKIP,
        payments=APIHelper.SKIP,
        custom_fields=APIHelper.SKIP,
        public_url=APIHelper.SKIP,
        available_actions=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ProformaInvoice instance."""
        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id
        if number is not APIHelper.SKIP:
            self.number = number
        if sequence_number is not APIHelper.SKIP:
            self.sequence_number = sequence_number
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None
        if delivery_date is not APIHelper.SKIP:
            self.delivery_date = delivery_date
        if status is not APIHelper.SKIP:
            self.status = status
        if collection_method is not APIHelper.SKIP:
            self.collection_method = collection_method
        if payment_instructions is not APIHelper.SKIP:
            self.payment_instructions = payment_instructions
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if consolidation_level is not APIHelper.SKIP:
            self.consolidation_level = consolidation_level
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name
        if product_family_name is not APIHelper.SKIP:
            self.product_family_name = product_family_name
        if role is not APIHelper.SKIP:
            self.role = role
        if seller is not APIHelper.SKIP:
            self.seller = seller
        if customer is not APIHelper.SKIP:
            self.customer = customer
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address
        if shipping_address is not APIHelper.SKIP:
            self.shipping_address = shipping_address
        if subtotal_amount is not APIHelper.SKIP:
            self.subtotal_amount = subtotal_amount
        if discount_amount is not APIHelper.SKIP:
            self.discount_amount = discount_amount
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount
        if total_amount is not APIHelper.SKIP:
            self.total_amount = total_amount
        if credit_amount is not APIHelper.SKIP:
            self.credit_amount = credit_amount
        if paid_amount is not APIHelper.SKIP:
            self.paid_amount = paid_amount
        if refund_amount is not APIHelper.SKIP:
            self.refund_amount = refund_amount
        if due_amount is not APIHelper.SKIP:
            self.due_amount = due_amount
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts
        if taxes is not APIHelper.SKIP:
            self.taxes = taxes
        if credits is not APIHelper.SKIP:
            self.credits = credits
        if payments is not APIHelper.SKIP:
            self.payments = payments
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields
        if public_url is not APIHelper.SKIP:
            self.public_url = public_url
        if available_actions is not APIHelper.SKIP:
            self.available_actions = available_actions

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else APIHelper.SKIP
        site_id =\
            dictionary.get("site_id")\
            if dictionary.get("site_id")\
                else APIHelper.SKIP
        customer_id =\
            dictionary.get("customer_id")\
            if "customer_id" in dictionary.keys()\
                else APIHelper.SKIP
        subscription_id =\
            dictionary.get("subscription_id")\
            if "subscription_id" in dictionary.keys()\
                else APIHelper.SKIP
        number =\
            dictionary.get("number")\
            if "number" in dictionary.keys()\
                else APIHelper.SKIP
        sequence_number =\
            dictionary.get("sequence_number")\
            if "sequence_number" in dictionary.keys()\
                else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP
        delivery_date = dateutil.parser.parse(
            dictionary.get("delivery_date")).date()\
            if dictionary.get("delivery_date") else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        collection_method =\
            dictionary.get("collection_method")\
            if dictionary.get("collection_method")\
                else APIHelper.SKIP
        payment_instructions =\
            dictionary.get("payment_instructions")\
            if dictionary.get("payment_instructions")\
                else APIHelper.SKIP
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        consolidation_level =\
            dictionary.get("consolidation_level")\
            if dictionary.get("consolidation_level")\
                else APIHelper.SKIP
        product_name =\
            dictionary.get("product_name")\
            if dictionary.get("product_name")\
                else APIHelper.SKIP
        product_family_name =\
            dictionary.get("product_family_name")\
            if dictionary.get("product_family_name")\
                else APIHelper.SKIP
        role =\
            dictionary.get("role")\
            if dictionary.get("role")\
                else APIHelper.SKIP
        seller =\
            InvoiceSeller.from_dictionary(
                dictionary.get("seller"))\
                if "seller" in dictionary.keys()\
                else APIHelper.SKIP
        customer =\
            InvoiceCustomer.from_dictionary(
                dictionary.get("customer"))\
                if "customer" in dictionary.keys()\
                else APIHelper.SKIP
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else APIHelper.SKIP
        billing_address =\
            InvoiceAddress.from_dictionary(
                dictionary.get("billing_address"))\
                if "billing_address" in dictionary.keys()\
                else APIHelper.SKIP
        shipping_address =\
            InvoiceAddress.from_dictionary(
                dictionary.get("shipping_address"))\
                if "shipping_address" in dictionary.keys()\
                else APIHelper.SKIP
        subtotal_amount =\
            dictionary.get("subtotal_amount")\
            if dictionary.get("subtotal_amount")\
                else APIHelper.SKIP
        discount_amount =\
            dictionary.get("discount_amount")\
            if dictionary.get("discount_amount")\
                else APIHelper.SKIP
        tax_amount =\
            dictionary.get("tax_amount")\
            if dictionary.get("tax_amount")\
                else APIHelper.SKIP
        total_amount =\
            dictionary.get("total_amount")\
            if dictionary.get("total_amount")\
                else APIHelper.SKIP
        credit_amount =\
            dictionary.get("credit_amount")\
            if dictionary.get("credit_amount")\
                else APIHelper.SKIP
        paid_amount =\
            dictionary.get("paid_amount")\
            if dictionary.get("paid_amount")\
                else APIHelper.SKIP
        refund_amount =\
            dictionary.get("refund_amount")\
            if dictionary.get("refund_amount")\
                else APIHelper.SKIP
        due_amount =\
            dictionary.get("due_amount")\
            if dictionary.get("due_amount")\
                else APIHelper.SKIP
        line_items = None
        if dictionary.get("line_items") is not None:
            line_items = [
                InvoiceLineItem.from_dictionary(x)
                    for x in dictionary.get("line_items")
            ]
        else:
            line_items = APIHelper.SKIP
        discounts = None
        if dictionary.get("discounts") is not None:
            discounts = [
                ProformaInvoiceDiscount.from_dictionary(x)
                    for x in dictionary.get("discounts")
            ]
        else:
            discounts = APIHelper.SKIP
        taxes = None
        if dictionary.get("taxes") is not None:
            taxes = [
                ProformaInvoiceTax.from_dictionary(x)
                    for x in dictionary.get("taxes")
            ]
        else:
            taxes = APIHelper.SKIP
        credits = None
        if dictionary.get("credits") is not None:
            credits = [
                ProformaInvoiceCredit.from_dictionary(x)
                    for x in dictionary.get("credits")
            ]
        else:
            credits = APIHelper.SKIP
        payments = None
        if dictionary.get("payments") is not None:
            payments = [
                ProformaInvoicePayment.from_dictionary(x)
                    for x in dictionary.get("payments")
            ]
        else:
            payments = APIHelper.SKIP
        custom_fields = None
        if dictionary.get("custom_fields") is not None:
            custom_fields = [
                InvoiceCustomField.from_dictionary(x)
                    for x in dictionary.get("custom_fields")
            ]
        else:
            custom_fields = APIHelper.SKIP
        public_url =\
            dictionary.get("public_url")\
            if "public_url" in dictionary.keys()\
                else APIHelper.SKIP
        available_actions =\
            AvailableActions.from_dictionary(
                dictionary.get("available_actions"))\
                if "available_actions" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(uid,
                   site_id,
                   customer_id,
                   subscription_id,
                   number,
                   sequence_number,
                   created_at,
                   delivery_date,
                   status,
                   collection_method,
                   payment_instructions,
                   currency,
                   consolidation_level,
                   product_name,
                   product_family_name,
                   role,
                   seller,
                   customer,
                   memo,
                   billing_address,
                   shipping_address,
                   subtotal_amount,
                   discount_amount,
                   tax_amount,
                   total_amount,
                   credit_amount,
                   paid_amount,
                   refund_amount,
                   due_amount,
                   line_items,
                   discounts,
                   taxes,
                   credits,
                   payments,
                   custom_fields,
                   public_url,
                   available_actions,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _number=(
            self.number
            if hasattr(self, "number")
            else None
        )
        _sequence_number=(
            self.sequence_number
            if hasattr(self, "sequence_number")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _delivery_date=(
            self.delivery_date
            if hasattr(self, "delivery_date")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _collection_method=(
            self.collection_method
            if hasattr(self, "collection_method")
            else None
        )
        _payment_instructions=(
            self.payment_instructions
            if hasattr(self, "payment_instructions")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _consolidation_level=(
            self.consolidation_level
            if hasattr(self, "consolidation_level")
            else None
        )
        _product_name=(
            self.product_name
            if hasattr(self, "product_name")
            else None
        )
        _product_family_name=(
            self.product_family_name
            if hasattr(self, "product_family_name")
            else None
        )
        _role=(
            self.role
            if hasattr(self, "role")
            else None
        )
        _seller=(
            self.seller
            if hasattr(self, "seller")
            else None
        )
        _customer=(
            self.customer
            if hasattr(self, "customer")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _billing_address=(
            self.billing_address
            if hasattr(self, "billing_address")
            else None
        )
        _shipping_address=(
            self.shipping_address
            if hasattr(self, "shipping_address")
            else None
        )
        _subtotal_amount=(
            self.subtotal_amount
            if hasattr(self, "subtotal_amount")
            else None
        )
        _discount_amount=(
            self.discount_amount
            if hasattr(self, "discount_amount")
            else None
        )
        _tax_amount=(
            self.tax_amount
            if hasattr(self, "tax_amount")
            else None
        )
        _total_amount=(
            self.total_amount
            if hasattr(self, "total_amount")
            else None
        )
        _credit_amount=(
            self.credit_amount
            if hasattr(self, "credit_amount")
            else None
        )
        _paid_amount=(
            self.paid_amount
            if hasattr(self, "paid_amount")
            else None
        )
        _refund_amount=(
            self.refund_amount
            if hasattr(self, "refund_amount")
            else None
        )
        _due_amount=(
            self.due_amount
            if hasattr(self, "due_amount")
            else None
        )
        _line_items=(
            self.line_items
            if hasattr(self, "line_items")
            else None
        )
        _discounts=(
            self.discounts
            if hasattr(self, "discounts")
            else None
        )
        _taxes=(
            self.taxes
            if hasattr(self, "taxes")
            else None
        )
        _credits=(
            self.credits
            if hasattr(self, "credits")
            else None
        )
        _payments=(
            self.payments
            if hasattr(self, "payments")
            else None
        )
        _custom_fields=(
            self.custom_fields
            if hasattr(self, "custom_fields")
            else None
        )
        _public_url=(
            self.public_url
            if hasattr(self, "public_url")
            else None
        )
        _available_actions=(
            self.available_actions
            if hasattr(self, "available_actions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!r}, "
            f"site_id={_site_id!r}, "
            f"customer_id={_customer_id!r}, "
            f"subscription_id={_subscription_id!r}, "
            f"number={_number!r}, "
            f"sequence_number={_sequence_number!r}, "
            f"created_at={_created_at!r}, "
            f"delivery_date={_delivery_date!r}, "
            f"status={_status!r}, "
            f"collection_method={_collection_method!r}, "
            f"payment_instructions={_payment_instructions!r}, "
            f"currency={_currency!r}, "
            f"consolidation_level={_consolidation_level!r}, "
            f"product_name={_product_name!r}, "
            f"product_family_name={_product_family_name!r}, "
            f"role={_role!r}, "
            f"seller={_seller!r}, "
            f"customer={_customer!r}, "
            f"memo={_memo!r}, "
            f"billing_address={_billing_address!r}, "
            f"shipping_address={_shipping_address!r}, "
            f"subtotal_amount={_subtotal_amount!r}, "
            f"discount_amount={_discount_amount!r}, "
            f"tax_amount={_tax_amount!r}, "
            f"total_amount={_total_amount!r}, "
            f"credit_amount={_credit_amount!r}, "
            f"paid_amount={_paid_amount!r}, "
            f"refund_amount={_refund_amount!r}, "
            f"due_amount={_due_amount!r}, "
            f"line_items={_line_items!r}, "
            f"discounts={_discounts!r}, "
            f"taxes={_taxes!r}, "
            f"credits={_credits!r}, "
            f"payments={_payments!r}, "
            f"custom_fields={_custom_fields!r}, "
            f"public_url={_public_url!r}, "
            f"available_actions={_available_actions!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _number=(
            self.number
            if hasattr(self, "number")
            else None
        )
        _sequence_number=(
            self.sequence_number
            if hasattr(self, "sequence_number")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _delivery_date=(
            self.delivery_date
            if hasattr(self, "delivery_date")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _collection_method=(
            self.collection_method
            if hasattr(self, "collection_method")
            else None
        )
        _payment_instructions=(
            self.payment_instructions
            if hasattr(self, "payment_instructions")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _consolidation_level=(
            self.consolidation_level
            if hasattr(self, "consolidation_level")
            else None
        )
        _product_name=(
            self.product_name
            if hasattr(self, "product_name")
            else None
        )
        _product_family_name=(
            self.product_family_name
            if hasattr(self, "product_family_name")
            else None
        )
        _role=(
            self.role
            if hasattr(self, "role")
            else None
        )
        _seller=(
            self.seller
            if hasattr(self, "seller")
            else None
        )
        _customer=(
            self.customer
            if hasattr(self, "customer")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _billing_address=(
            self.billing_address
            if hasattr(self, "billing_address")
            else None
        )
        _shipping_address=(
            self.shipping_address
            if hasattr(self, "shipping_address")
            else None
        )
        _subtotal_amount=(
            self.subtotal_amount
            if hasattr(self, "subtotal_amount")
            else None
        )
        _discount_amount=(
            self.discount_amount
            if hasattr(self, "discount_amount")
            else None
        )
        _tax_amount=(
            self.tax_amount
            if hasattr(self, "tax_amount")
            else None
        )
        _total_amount=(
            self.total_amount
            if hasattr(self, "total_amount")
            else None
        )
        _credit_amount=(
            self.credit_amount
            if hasattr(self, "credit_amount")
            else None
        )
        _paid_amount=(
            self.paid_amount
            if hasattr(self, "paid_amount")
            else None
        )
        _refund_amount=(
            self.refund_amount
            if hasattr(self, "refund_amount")
            else None
        )
        _due_amount=(
            self.due_amount
            if hasattr(self, "due_amount")
            else None
        )
        _line_items=(
            self.line_items
            if hasattr(self, "line_items")
            else None
        )
        _discounts=(
            self.discounts
            if hasattr(self, "discounts")
            else None
        )
        _taxes=(
            self.taxes
            if hasattr(self, "taxes")
            else None
        )
        _credits=(
            self.credits
            if hasattr(self, "credits")
            else None
        )
        _payments=(
            self.payments
            if hasattr(self, "payments")
            else None
        )
        _custom_fields=(
            self.custom_fields
            if hasattr(self, "custom_fields")
            else None
        )
        _public_url=(
            self.public_url
            if hasattr(self, "public_url")
            else None
        )
        _available_actions=(
            self.available_actions
            if hasattr(self, "available_actions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!s}, "
            f"site_id={_site_id!s}, "
            f"customer_id={_customer_id!s}, "
            f"subscription_id={_subscription_id!s}, "
            f"number={_number!s}, "
            f"sequence_number={_sequence_number!s}, "
            f"created_at={_created_at!s}, "
            f"delivery_date={_delivery_date!s}, "
            f"status={_status!s}, "
            f"collection_method={_collection_method!s}, "
            f"payment_instructions={_payment_instructions!s}, "
            f"currency={_currency!s}, "
            f"consolidation_level={_consolidation_level!s}, "
            f"product_name={_product_name!s}, "
            f"product_family_name={_product_family_name!s}, "
            f"role={_role!s}, "
            f"seller={_seller!s}, "
            f"customer={_customer!s}, "
            f"memo={_memo!s}, "
            f"billing_address={_billing_address!s}, "
            f"shipping_address={_shipping_address!s}, "
            f"subtotal_amount={_subtotal_amount!s}, "
            f"discount_amount={_discount_amount!s}, "
            f"tax_amount={_tax_amount!s}, "
            f"total_amount={_total_amount!s}, "
            f"credit_amount={_credit_amount!s}, "
            f"paid_amount={_paid_amount!s}, "
            f"refund_amount={_refund_amount!s}, "
            f"due_amount={_due_amount!s}, "
            f"line_items={_line_items!s}, "
            f"discounts={_discounts!s}, "
            f"taxes={_taxes!s}, "
            f"credits={_credits!s}, "
            f"payments={_payments!s}, "
            f"custom_fields={_custom_fields!s}, "
            f"public_url={_public_url!s}, "
            f"available_actions={_available_actions!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
