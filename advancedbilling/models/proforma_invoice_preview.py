# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_address import InvoiceAddress
from advancedbilling.models.invoice_customer import InvoiceCustomer
from advancedbilling.models.invoice_line_item import InvoiceLineItem
from advancedbilling.models.invoice_seller import InvoiceSeller
from advancedbilling.models.proforma_custom_field import ProformaCustomField
from advancedbilling.models.proforma_invoice_credit import ProformaInvoiceCredit
from advancedbilling.models.proforma_invoice_discount import ProformaInvoiceDiscount
from advancedbilling.models.proforma_invoice_payment import ProformaInvoicePayment
from advancedbilling.models.proforma_invoice_tax import ProformaInvoiceTax


class ProformaInvoicePreview(object):

    """Implementation of the 'Proforma Invoice Preview' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        site_id (int): TODO: type description here.
        customer_id (int): TODO: type description here.
        subscription_id (int): TODO: type description here.
        number (str): TODO: type description here.
        sequence_number (int): TODO: type description here.
        created_at (str): TODO: type description here.
        delivery_date (str): TODO: type description here.
        status (str): TODO: type description here.
        collection_method (str): TODO: type description here.
        payment_instructions (str): TODO: type description here.
        currency (str): TODO: type description here.
        consolidation_level (str): TODO: type description here.
        product_name (str): TODO: type description here.
        product_family_name (str): TODO: type description here.
        role (str): TODO: type description here.
        seller (InvoiceSeller): Information about the seller (merchant) listed
            on the masthead of the invoice.
        customer (InvoiceCustomer): Information about the customer who is
            owner or recipient the invoiced subscription.
        memo (str): TODO: type description here.
        billing_address (InvoiceAddress): TODO: type description here.
        shipping_address (InvoiceAddress): TODO: type description here.
        subtotal_amount (str): TODO: type description here.
        discount_amount (str): TODO: type description here.
        tax_amount (str): TODO: type description here.
        total_amount (str): TODO: type description here.
        credit_amount (str): TODO: type description here.
        paid_amount (str): TODO: type description here.
        refund_amount (str): TODO: type description here.
        due_amount (str): TODO: type description here.
        line_items (List[InvoiceLineItem]): TODO: type description here.
        discounts (List[ProformaInvoiceDiscount]): TODO: type description
            here.
        taxes (List[ProformaInvoiceTax]): TODO: type description here.
        credits (List[ProformaInvoiceCredit]): TODO: type description here.
        payments (List[ProformaInvoicePayment]): TODO: type description here.
        custom_fields (List[ProformaCustomField]): TODO: type description
            here.
        public_url (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "site_id": 'site_id',
        "customer_id": 'customer_id',
        "subscription_id": 'subscription_id',
        "number": 'number',
        "sequence_number": 'sequence_number',
        "created_at": 'created_at',
        "delivery_date": 'delivery_date',
        "status": 'status',
        "collection_method": 'collection_method',
        "payment_instructions": 'payment_instructions',
        "currency": 'currency',
        "consolidation_level": 'consolidation_level',
        "product_name": 'product_name',
        "product_family_name": 'product_family_name',
        "role": 'role',
        "seller": 'seller',
        "customer": 'customer',
        "memo": 'memo',
        "billing_address": 'billing_address',
        "shipping_address": 'shipping_address',
        "subtotal_amount": 'subtotal_amount',
        "discount_amount": 'discount_amount',
        "tax_amount": 'tax_amount',
        "total_amount": 'total_amount',
        "credit_amount": 'credit_amount',
        "paid_amount": 'paid_amount',
        "refund_amount": 'refund_amount',
        "due_amount": 'due_amount',
        "line_items": 'line_items',
        "discounts": 'discounts',
        "taxes": 'taxes',
        "credits": 'credits',
        "payments": 'payments',
        "custom_fields": 'custom_fields',
        "public_url": 'public_url'
    }

    _optionals = [
        'uid',
        'site_id',
        'customer_id',
        'subscription_id',
        'number',
        'sequence_number',
        'created_at',
        'delivery_date',
        'status',
        'collection_method',
        'payment_instructions',
        'currency',
        'consolidation_level',
        'product_name',
        'product_family_name',
        'role',
        'seller',
        'customer',
        'memo',
        'billing_address',
        'shipping_address',
        'subtotal_amount',
        'discount_amount',
        'tax_amount',
        'total_amount',
        'credit_amount',
        'paid_amount',
        'refund_amount',
        'due_amount',
        'line_items',
        'discounts',
        'taxes',
        'credits',
        'payments',
        'custom_fields',
        'public_url',
    ]

    def __init__(self,
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
                 public_url=APIHelper.SKIP):
        """Constructor for the ProformaInvoicePreview class"""

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
            self.created_at = created_at 
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

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        sequence_number = dictionary.get("sequence_number") if dictionary.get("sequence_number") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        delivery_date = dictionary.get("delivery_date") if dictionary.get("delivery_date") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        collection_method = dictionary.get("collection_method") if dictionary.get("collection_method") else APIHelper.SKIP
        payment_instructions = dictionary.get("payment_instructions") if dictionary.get("payment_instructions") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else APIHelper.SKIP
        product_name = dictionary.get("product_name") if dictionary.get("product_name") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        seller = InvoiceSeller.from_dictionary(dictionary.get('seller')) if 'seller' in dictionary.keys() else APIHelper.SKIP
        customer = InvoiceCustomer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        billing_address = InvoiceAddress.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        shipping_address = InvoiceAddress.from_dictionary(dictionary.get('shipping_address')) if 'shipping_address' in dictionary.keys() else APIHelper.SKIP
        subtotal_amount = dictionary.get("subtotal_amount") if dictionary.get("subtotal_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        credit_amount = dictionary.get("credit_amount") if dictionary.get("credit_amount") else APIHelper.SKIP
        paid_amount = dictionary.get("paid_amount") if dictionary.get("paid_amount") else APIHelper.SKIP
        refund_amount = dictionary.get("refund_amount") if dictionary.get("refund_amount") else APIHelper.SKIP
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [InvoiceLineItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        discounts = None
        if dictionary.get('discounts') is not None:
            discounts = [ProformaInvoiceDiscount.from_dictionary(x) for x in dictionary.get('discounts')]
        else:
            discounts = APIHelper.SKIP
        taxes = None
        if dictionary.get('taxes') is not None:
            taxes = [ProformaInvoiceTax.from_dictionary(x) for x in dictionary.get('taxes')]
        else:
            taxes = APIHelper.SKIP
        credits = None
        if dictionary.get('credits') is not None:
            credits = [ProformaInvoiceCredit.from_dictionary(x) for x in dictionary.get('credits')]
        else:
            credits = APIHelper.SKIP
        payments = None
        if dictionary.get('payments') is not None:
            payments = [ProformaInvoicePayment.from_dictionary(x) for x in dictionary.get('payments')]
        else:
            payments = APIHelper.SKIP
        custom_fields = None
        if dictionary.get('custom_fields') is not None:
            custom_fields = [ProformaCustomField.from_dictionary(x) for x in dictionary.get('custom_fields')]
        else:
            custom_fields = APIHelper.SKIP
        public_url = dictionary.get("public_url") if dictionary.get("public_url") else APIHelper.SKIP
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
                   public_url)
