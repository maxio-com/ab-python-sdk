# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.billing_address import BillingAddress
from advancedbilling.models.credit_note_application import CreditNoteApplication
from advancedbilling.models.credit_note_line_item import CreditNoteLineItem
from advancedbilling.models.customer_1 import Customer1
from advancedbilling.models.invoice_discount import InvoiceDiscount
from advancedbilling.models.invoice_refund import InvoiceRefund
from advancedbilling.models.invoice_tax import InvoiceTax
from advancedbilling.models.origin_invoice import OriginInvoice
from advancedbilling.models.seller import Seller
from advancedbilling.models.shipping_address import ShippingAddress


class CreditNote1(object):

    """Implementation of the 'Credit Note1' model.

    TODO: type model description here.

    Attributes:
        uid (str): Unique identifier for the credit note. It is generated
            automatically by Chargify and has the prefix "cn_" followed by
            alphanumeric characters.
        site_id (int): ID of the site to which the credit note belongs.
        customer_id (int): ID of the customer to which the credit note
            belongs.
        subscription_id (int): ID of the subscription that generated the
            credit note.
        number (str): A unique, identifying string that appears on the credit
            note and in places it is referenced.  While the UID is long and
            not appropriate to show to customers, the number is usually
            shorter and consumable by the customer and the merchant alike.
        sequence_number (int): A monotonically increasing number assigned to
            credit notes as they are created.  This number is unique within a
            site and can be used to sort and order credit notes.
        issue_date (str): Date the credit note was issued to the customer. 
            This is the date that the credit was made available for
            application, and may come before it is fully applied.  The format
            is `"YYYY-MM-DD"`.
        applied_date (str): Credit notes are applied to invoices to offset
            invoiced amounts - they reduce the amount due. This field is the
            date the credit note became fully applied to invoices.  If the
            credit note has been partially applied, this field will not have a
            value until it has been fully applied.  The format is
            `"YYYY-MM-DD"`.
        status (str): Current status of the credit note. Valid values:  * open
            * applied
        currency (str): The ISO 4217 currency code (3 character string)
            representing the currency of the credit note amount fields.
        memo (str): The memo printed on credit note, which is a description of
            the reason for the credit.
        seller (Seller): TODO: type description here.
        customer (Customer1): TODO: type description here.
        billing_address (BillingAddress): TODO: type description here.
        shipping_address (ShippingAddress): TODO: type description here.
        subtotal_amount (str): Subtotal of the credit note, which is the sum
            of all line items before discounts or taxes. Note that this is a
            positive amount representing the credit back to the customer.
        discount_amount (str): Total discount applied to the credit note. Note
            that this is a positive amount representing the discount amount
            being credited back to the customer (i.e. a credit on an earlier
            discount). For example, if the original purchase was $1.00 and the
            original discount was $0.10, a credit of $0.50 of the original
            purchase (half) would have a discount credit of $0.05 (also
            half).
        tax_amount (str): Total tax of the credit note. Note that this is a
            positive amount representing a previously taxex amount being
            credited back to the customer (i.e. a credit of an earlier tax).
            For example, if the original purchase was $1.00 and the original
            tax was $0.10, a credit of $0.50 of the original purchase (half)
            would also have a tax credit of $0.05 (also half).
        total_amount (str): The credit note total, which is `subtotal_amount -
            discount_amount + tax_amount`.'
        applied_amount (str): The amount of the credit note that has already
            been applied to invoices.
        remaining_amount (str): The amount of the credit note remaining to be
            applied to invoices, which is `total_amount - applied_amount`.
        line_items (List[CreditNoteLineItem]): Line items on the credit note.
        discounts (List[InvoiceDiscount]): TODO: type description here.
        taxes (List[InvoiceTax]): TODO: type description here.
        applications (List[CreditNoteApplication]): TODO: type description
            here.
        refunds (List[InvoiceRefund]): TODO: type description here.
        origin_invoices (List[OriginInvoice]): An array of origin invoices for
            the credit note. Learn more about [Origin Invoice from our
            docs](https://chargify.zendesk.com/hc/en-us/articles/4407753036699#
            origin-invoices)

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
        "applied_date": 'applied_date',
        "status": 'status',
        "currency": 'currency',
        "memo": 'memo',
        "seller": 'seller',
        "customer": 'customer',
        "billing_address": 'billing_address',
        "shipping_address": 'shipping_address',
        "subtotal_amount": 'subtotal_amount',
        "discount_amount": 'discount_amount',
        "tax_amount": 'tax_amount',
        "total_amount": 'total_amount',
        "applied_amount": 'applied_amount',
        "remaining_amount": 'remaining_amount',
        "line_items": 'line_items',
        "discounts": 'discounts',
        "taxes": 'taxes',
        "applications": 'applications',
        "refunds": 'refunds',
        "origin_invoices": 'origin_invoices'
    }

    _optionals = [
        'uid',
        'site_id',
        'customer_id',
        'subscription_id',
        'number',
        'sequence_number',
        'issue_date',
        'applied_date',
        'status',
        'currency',
        'memo',
        'seller',
        'customer',
        'billing_address',
        'shipping_address',
        'subtotal_amount',
        'discount_amount',
        'tax_amount',
        'total_amount',
        'applied_amount',
        'remaining_amount',
        'line_items',
        'discounts',
        'taxes',
        'applications',
        'refunds',
        'origin_invoices',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 sequence_number=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 applied_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 seller=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 shipping_address=APIHelper.SKIP,
                 subtotal_amount=APIHelper.SKIP,
                 discount_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 total_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 remaining_amount=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 taxes=APIHelper.SKIP,
                 applications=APIHelper.SKIP,
                 refunds=APIHelper.SKIP,
                 origin_invoices=APIHelper.SKIP):
        """Constructor for the CreditNote1 class"""

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
        if applied_date is not APIHelper.SKIP:
            self.applied_date = applied_date 
        if status is not APIHelper.SKIP:
            self.status = status 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if seller is not APIHelper.SKIP:
            self.seller = seller 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
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
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if remaining_amount is not APIHelper.SKIP:
            self.remaining_amount = remaining_amount 
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        if taxes is not APIHelper.SKIP:
            self.taxes = taxes 
        if applications is not APIHelper.SKIP:
            self.applications = applications 
        if refunds is not APIHelper.SKIP:
            self.refunds = refunds 
        if origin_invoices is not APIHelper.SKIP:
            self.origin_invoices = origin_invoices 

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
        applied_date = dictionary.get("applied_date") if dictionary.get("applied_date") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        seller = Seller.from_dictionary(dictionary.get('seller')) if 'seller' in dictionary.keys() else APIHelper.SKIP
        customer = Customer1.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        billing_address = BillingAddress.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        shipping_address = ShippingAddress.from_dictionary(dictionary.get('shipping_address')) if 'shipping_address' in dictionary.keys() else APIHelper.SKIP
        subtotal_amount = dictionary.get("subtotal_amount") if dictionary.get("subtotal_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        remaining_amount = dictionary.get("remaining_amount") if dictionary.get("remaining_amount") else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [CreditNoteLineItem.from_dictionary(x) for x in dictionary.get('line_items')]
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
        applications = None
        if dictionary.get('applications') is not None:
            applications = [CreditNoteApplication.from_dictionary(x) for x in dictionary.get('applications')]
        else:
            applications = APIHelper.SKIP
        refunds = None
        if dictionary.get('refunds') is not None:
            refunds = [InvoiceRefund.from_dictionary(x) for x in dictionary.get('refunds')]
        else:
            refunds = APIHelper.SKIP
        origin_invoices = None
        if dictionary.get('origin_invoices') is not None:
            origin_invoices = [OriginInvoice.from_dictionary(x) for x in dictionary.get('origin_invoices')]
        else:
            origin_invoices = APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   site_id,
                   customer_id,
                   subscription_id,
                   number,
                   sequence_number,
                   issue_date,
                   applied_date,
                   status,
                   currency,
                   memo,
                   seller,
                   customer,
                   billing_address,
                   shipping_address,
                   subtotal_amount,
                   discount_amount,
                   tax_amount,
                   total_amount,
                   applied_amount,
                   remaining_amount,
                   line_items,
                   discounts,
                   taxes,
                   applications,
                   refunds,
                   origin_invoices)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
