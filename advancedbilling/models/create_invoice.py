# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_invoice_address import CreateInvoiceAddress
from advancedbilling.models.create_invoice_coupon import CreateInvoiceCoupon
from advancedbilling.models.create_invoice_item import CreateInvoiceItem


class CreateInvoice(object):

    """Implementation of the 'Create Invoice' model.

    TODO: type model description here.

    Attributes:
        line_items (List[CreateInvoiceItem]): TODO: type description here.
        issue_date (str): TODO: type description here.
        net_terms (int): By default, invoices will be created with a due date
            matching the date of invoice creation. If a different due date is
            desired, the net_terms parameter can be sent indicating the number
            of days in advance the due date should be.
        payment_instructions (str): TODO: type description here.
        memo (str): A custom memo can be sent to override the site's default.
        seller_address (CreateInvoiceAddress): Overrides the defaults for the
            site
        billing_address (CreateInvoiceAddress): Overrides the default for the
            customer
        shipping_address (CreateInvoiceAddress): Overrides the default for the
            customer
        coupons (List[CreateInvoiceCoupon]): TODO: type description here.
        status (Status1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "line_items": 'line_items',
        "issue_date": 'issue_date',
        "net_terms": 'net_terms',
        "payment_instructions": 'payment_instructions',
        "memo": 'memo',
        "seller_address": 'seller_address',
        "billing_address": 'billing_address',
        "shipping_address": 'shipping_address',
        "coupons": 'coupons',
        "status": 'status'
    }

    _optionals = [
        'line_items',
        'issue_date',
        'net_terms',
        'payment_instructions',
        'memo',
        'seller_address',
        'billing_address',
        'shipping_address',
        'coupons',
        'status',
    ]

    def __init__(self,
                 line_items=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 payment_instructions=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 seller_address=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 shipping_address=APIHelper.SKIP,
                 coupons=APIHelper.SKIP,
                 status='open'):
        """Constructor for the CreateInvoice class"""

        # Initialize members of the class
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if issue_date is not APIHelper.SKIP:
            self.issue_date = issue_date 
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms 
        if payment_instructions is not APIHelper.SKIP:
            self.payment_instructions = payment_instructions 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if seller_address is not APIHelper.SKIP:
            self.seller_address = seller_address 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if shipping_address is not APIHelper.SKIP:
            self.shipping_address = shipping_address 
        if coupons is not APIHelper.SKIP:
            self.coupons = coupons 
        self.status = status 

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
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [CreateInvoiceItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        issue_date = dictionary.get("issue_date") if dictionary.get("issue_date") else APIHelper.SKIP
        net_terms = dictionary.get("net_terms") if dictionary.get("net_terms") else APIHelper.SKIP
        payment_instructions = dictionary.get("payment_instructions") if dictionary.get("payment_instructions") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        seller_address = CreateInvoiceAddress.from_dictionary(dictionary.get('seller_address')) if 'seller_address' in dictionary.keys() else APIHelper.SKIP
        billing_address = CreateInvoiceAddress.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        shipping_address = CreateInvoiceAddress.from_dictionary(dictionary.get('shipping_address')) if 'shipping_address' in dictionary.keys() else APIHelper.SKIP
        coupons = None
        if dictionary.get('coupons') is not None:
            coupons = [CreateInvoiceCoupon.from_dictionary(x) for x in dictionary.get('coupons')]
        else:
            coupons = APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else 'open'
        # Return an object of this model
        return cls(line_items,
                   issue_date,
                   net_terms,
                   payment_instructions,
                   memo,
                   seller_address,
                   billing_address,
                   shipping_address,
                   coupons,
                   status)
