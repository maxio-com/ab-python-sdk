# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_address import InvoiceAddress
from advancedbilling.models.invoice_credit import InvoiceCredit
from advancedbilling.models.invoice_custom_field import InvoiceCustomField
from advancedbilling.models.invoice_customer import InvoiceCustomer
from advancedbilling.models.invoice_discount import InvoiceDiscount
from advancedbilling.models.invoice_line_item import InvoiceLineItem
from advancedbilling.models.invoice_payment import InvoicePayment
from advancedbilling.models.invoice_previous_balance import InvoicePreviousBalance
from advancedbilling.models.invoice_refund import InvoiceRefund
from advancedbilling.models.invoice_seller import InvoiceSeller
from advancedbilling.models.invoice_tax import InvoiceTax


class Invoice(object):

    """Implementation of the 'Invoice' model.

    TODO: type model description here.

    Attributes:
        uid (str): Unique identifier for the invoice. It is generated
            automatically by Chargify and has the prefix "inv_" followed by
            alphanumeric characters.
        site_id (int): ID of the site to which the invoice belongs.
        customer_id (int): ID of the customer to which the invoice belongs.
        subscription_id (int): ID of the subscription that generated the
            invoice.
        number (str): A unique, identifying string that appears on the invoice
            and in places the invoice is referenced.  While the UID is long
            and not appropriate to show to customers, the number is usually
            shorter and consumable by the customer and the merchant alike.
        sequence_number (int): A monotonically increasing number assigned to
            invoices as they are created.  This number is unique within a site
            and can be used to sort and order invoices.
        issue_date (str): Date the invoice was issued to the customer.  This
            is the date that the invoice was made available for payment.  The
            format is `"YYYY-MM-DD"`.
        due_date (str): Date the invoice is due.  The format is
            `"YYYY-MM-DD"`.
        paid_date (str): Date the invoice became fully paid.  If partial
            payments are applied to the invoice, this date will not be present
            until payment has been made in full.  The format is
            `"YYYY-MM-DD"`.
        status (Status): The current status of the invoice. See [Invoice
            Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494
            171#line-item-breakdowns) for more.
        collection_method (str): The collection method of the invoice, which
            is either "automatic" (tried and retried on an existing payment
            method by Chargify) or "remittance" (payment must be remitted by
            the customer or keyed in by the merchant).
        payment_instructions (str): A message that is printed on the invoice
            when it is marked for remittance collection. It is intended to
            describe to the customer how they may make payment, and is
            configured by the merchant.
        currency (str): The ISO 4217 currency code (3 character string)
            representing the currency of invoice transaction.
        consolidation_level (InvoiceConsolidationLevel): Consolidation level
            of the invoice, which is applicable to invoice consolidation.  It
            will hold one of the following values:  * "none": A normal invoice
            with no consolidation. * "child": An invoice segment which has
            been combined into a consolidated invoice. * "parent": A
            consolidated invoice, whose contents are composed of invoice
            segments.  "Parent" invoices do not have lines of their own, but
            they have subtotals and totals which aggregate the member invoice
            segments.  See also the [invoice consolidation
            documentation](https://chargify.zendesk.com/hc/en-us/articles/44077
            46391835).
        parent_invoice_uid (str): For invoices with `consolidation_level` of
            `child`, this specifies the UID of the parent (consolidated)
            invoice.
        parent_invoice_number (int): For invoices with `consolidation_level`
            of `child`, this specifies the number of the parent (consolidated)
            invoice.
        group_primary_subscription_id (int): For invoices with
            `consolidation_level` of `parent`, this specifies the ID of the
            subscription which was the primary subscription of the
            subscription group that generated the invoice.
        product_name (str): The name of the product subscribed when the
            invoice was generated.
        product_family_name (str): The name of the product family subscribed
            when the invoice was generated.
        seller (InvoiceSeller): Information about the seller (merchant) listed
            on the masthead of the invoice.
        customer (InvoiceCustomer): Information about the customer who is
            owner or recipient the invoiced subscription.
        memo (str): The memo printed on invoices of any collection type.  This
            message is in control of the merchant.
        billing_address (InvoiceAddress): The invoice billing address.
        shipping_address (InvoiceAddress): The invoice shipping address.
        subtotal_amount (str): Subtotal of the invoice, which is the sum of
            all line items before discounts or taxes.
        discount_amount (str): Total discount applied to the invoice.
        tax_amount (str): Total tax on the invoice.
        total_amount (str): The invoice total, which is `subtotal_amount -
            discount_amount + tax_amount`.'
        credit_amount (str): The amount of credit (from credit notes) applied
            to this invoice.  Credits offset the amount due from the
            customer.
        refund_amount (str): TODO: type description here.
        paid_amount (str): The amount paid on the invoice by the customer.
        due_amount (str): Amount due on the invoice, which is `total_amount -
            credit_amount - paid_amount`.
        line_items (List[InvoiceLineItem]): Line items on the invoice.
        discounts (List[InvoiceDiscount]): TODO: type description here.
        taxes (List[InvoiceTax]): TODO: type description here.
        credits (List[InvoiceCredit]): TODO: type description here.
        refunds (List[InvoiceRefund]): TODO: type description here.
        payments (List[InvoicePayment]): TODO: type description here.
        custom_fields (List[InvoiceCustomField]): TODO: type description
            here.
        public_url (str): The public URL of the invoice
        previous_balance_data (InvoicePreviousBalance): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "site_id": 'site_id',
        "customer_id": 'customer_id',
        "subscription_id": 'subscription_id',
        "number": 'number',
        "sequence_number": 'sequence_number',
        "issue_date": 'issue_date',
        "due_date": 'due_date',
        "paid_date": 'paid_date',
        "status": 'status',
        "collection_method": 'collection_method',
        "payment_instructions": 'payment_instructions',
        "currency": 'currency',
        "consolidation_level": 'consolidation_level',
        "parent_invoice_uid": 'parent_invoice_uid',
        "parent_invoice_number": 'parent_invoice_number',
        "group_primary_subscription_id": 'group_primary_subscription_id',
        "product_name": 'product_name',
        "product_family_name": 'product_family_name',
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
        "refund_amount": 'refund_amount',
        "paid_amount": 'paid_amount',
        "due_amount": 'due_amount',
        "line_items": 'line_items',
        "discounts": 'discounts',
        "taxes": 'taxes',
        "credits": 'credits',
        "refunds": 'refunds',
        "payments": 'payments',
        "custom_fields": 'custom_fields',
        "public_url": 'public_url',
        "previous_balance_data": 'previous_balance_data'
    }

    _optionals = [
        'uid',
        'site_id',
        'customer_id',
        'subscription_id',
        'number',
        'sequence_number',
        'issue_date',
        'due_date',
        'paid_date',
        'status',
        'collection_method',
        'payment_instructions',
        'currency',
        'consolidation_level',
        'parent_invoice_uid',
        'parent_invoice_number',
        'group_primary_subscription_id',
        'product_name',
        'product_family_name',
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
        'refund_amount',
        'paid_amount',
        'due_amount',
        'line_items',
        'discounts',
        'taxes',
        'credits',
        'refunds',
        'payments',
        'custom_fields',
        'public_url',
        'previous_balance_data',
    ]

    _nullables = [
        'paid_date',
        'parent_invoice_uid',
        'parent_invoice_number',
        'group_primary_subscription_id',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 sequence_number=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 due_date=APIHelper.SKIP,
                 paid_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 collection_method=APIHelper.SKIP,
                 payment_instructions=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 consolidation_level=APIHelper.SKIP,
                 parent_invoice_uid=APIHelper.SKIP,
                 parent_invoice_number=APIHelper.SKIP,
                 group_primary_subscription_id=APIHelper.SKIP,
                 product_name=APIHelper.SKIP,
                 product_family_name=APIHelper.SKIP,
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
                 refund_amount=APIHelper.SKIP,
                 paid_amount=APIHelper.SKIP,
                 due_amount=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 taxes=APIHelper.SKIP,
                 credits=APIHelper.SKIP,
                 refunds=APIHelper.SKIP,
                 payments=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 public_url=APIHelper.SKIP,
                 previous_balance_data=APIHelper.SKIP):
        """Constructor for the Invoice class"""

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
        if issue_date is not APIHelper.SKIP:
            self.issue_date = issue_date 
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date 
        if paid_date is not APIHelper.SKIP:
            self.paid_date = paid_date 
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
        if parent_invoice_uid is not APIHelper.SKIP:
            self.parent_invoice_uid = parent_invoice_uid 
        if parent_invoice_number is not APIHelper.SKIP:
            self.parent_invoice_number = parent_invoice_number 
        if group_primary_subscription_id is not APIHelper.SKIP:
            self.group_primary_subscription_id = group_primary_subscription_id 
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name 
        if product_family_name is not APIHelper.SKIP:
            self.product_family_name = product_family_name 
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
        if refund_amount is not APIHelper.SKIP:
            self.refund_amount = refund_amount 
        if paid_amount is not APIHelper.SKIP:
            self.paid_amount = paid_amount 
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
        if refunds is not APIHelper.SKIP:
            self.refunds = refunds 
        if payments is not APIHelper.SKIP:
            self.payments = payments 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if public_url is not APIHelper.SKIP:
            self.public_url = public_url 
        if previous_balance_data is not APIHelper.SKIP:
            self.previous_balance_data = previous_balance_data 

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
        issue_date = dictionary.get("issue_date") if dictionary.get("issue_date") else APIHelper.SKIP
        due_date = dictionary.get("due_date") if dictionary.get("due_date") else APIHelper.SKIP
        paid_date = dictionary.get("paid_date") if "paid_date" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        collection_method = dictionary.get("collection_method") if dictionary.get("collection_method") else APIHelper.SKIP
        payment_instructions = dictionary.get("payment_instructions") if dictionary.get("payment_instructions") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else APIHelper.SKIP
        parent_invoice_uid = dictionary.get("parent_invoice_uid") if "parent_invoice_uid" in dictionary.keys() else APIHelper.SKIP
        parent_invoice_number = dictionary.get("parent_invoice_number") if "parent_invoice_number" in dictionary.keys() else APIHelper.SKIP
        group_primary_subscription_id = dictionary.get("group_primary_subscription_id") if "group_primary_subscription_id" in dictionary.keys() else APIHelper.SKIP
        product_name = dictionary.get("product_name") if dictionary.get("product_name") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
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
        refund_amount = dictionary.get("refund_amount") if dictionary.get("refund_amount") else APIHelper.SKIP
        paid_amount = dictionary.get("paid_amount") if dictionary.get("paid_amount") else APIHelper.SKIP
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [InvoiceLineItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        discounts = None
        if dictionary.get('discounts') is not None:
            discounts = [InvoiceDiscount.from_dictionary(x) for x in dictionary.get('discounts')]
        else:
            discounts = APIHelper.SKIP
        taxes = None
        if dictionary.get('taxes') is not None:
            taxes = [InvoiceTax.from_dictionary(x) for x in dictionary.get('taxes')]
        else:
            taxes = APIHelper.SKIP
        credits = None
        if dictionary.get('credits') is not None:
            credits = [InvoiceCredit.from_dictionary(x) for x in dictionary.get('credits')]
        else:
            credits = APIHelper.SKIP
        refunds = None
        if dictionary.get('refunds') is not None:
            refunds = [InvoiceRefund.from_dictionary(x) for x in dictionary.get('refunds')]
        else:
            refunds = APIHelper.SKIP
        payments = None
        if dictionary.get('payments') is not None:
            payments = [InvoicePayment.from_dictionary(x) for x in dictionary.get('payments')]
        else:
            payments = APIHelper.SKIP
        custom_fields = None
        if dictionary.get('custom_fields') is not None:
            custom_fields = [InvoiceCustomField.from_dictionary(x) for x in dictionary.get('custom_fields')]
        else:
            custom_fields = APIHelper.SKIP
        public_url = dictionary.get("public_url") if dictionary.get("public_url") else APIHelper.SKIP
        previous_balance_data = InvoicePreviousBalance.from_dictionary(dictionary.get('previous_balance_data')) if 'previous_balance_data' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   site_id,
                   customer_id,
                   subscription_id,
                   number,
                   sequence_number,
                   issue_date,
                   due_date,
                   paid_date,
                   status,
                   collection_method,
                   payment_instructions,
                   currency,
                   consolidation_level,
                   parent_invoice_uid,
                   parent_invoice_number,
                   group_primary_subscription_id,
                   product_name,
                   product_family_name,
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
                   refund_amount,
                   paid_amount,
                   due_amount,
                   line_items,
                   discounts,
                   taxes,
                   credits,
                   refunds,
                   payments,
                   custom_fields,
                   public_url,
                   previous_balance_data)
