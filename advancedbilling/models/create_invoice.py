# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_invoice_address import CreateInvoiceAddress
from advancedbilling.models.create_invoice_coupon import CreateInvoiceCoupon
from advancedbilling.models.create_invoice_item import CreateInvoiceItem


class CreateInvoice(object):

    """Implementation of the 'Create Invoice' model.

    Attributes:
        line_items (List[CreateInvoiceItem]): The model property of type
            List[CreateInvoiceItem].
        issue_date (date): The model property of type date.
        net_terms (int): By default, invoices will be created with a due date
            matching the date of invoice creation. If a different due date is
            desired, the net_terms parameter can be sent indicating the number
            of days in advance the due date should be.
        payment_instructions (str): The model property of type str.
        memo (str): A custom memo can be sent to override the site's default.
        seller_address (CreateInvoiceAddress): Overrides the defaults for the
            site
        billing_address (CreateInvoiceAddress): Overrides the default for the
            customer
        shipping_address (CreateInvoiceAddress): Overrides the default for the
            customer
        coupons (List[CreateInvoiceCoupon]): The model property of type
            List[CreateInvoiceCoupon].
        status (CreateInvoiceStatus): The model property of type
            CreateInvoiceStatus.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 status='open',
                 additional_properties=None):
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

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [CreateInvoiceItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        issue_date = dateutil.parser.parse(dictionary.get('issue_date')).date() if dictionary.get('issue_date') else APIHelper.SKIP
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
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   status,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!r}, '
                f'issue_date={(self.issue_date if hasattr(self, "issue_date") else None)!r}, '
                f'net_terms={(self.net_terms if hasattr(self, "net_terms") else None)!r}, '
                f'payment_instructions={(self.payment_instructions if hasattr(self, "payment_instructions") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'seller_address={(self.seller_address if hasattr(self, "seller_address") else None)!r}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!r}, '
                f'shipping_address={(self.shipping_address if hasattr(self, "shipping_address") else None)!r}, '
                f'coupons={(self.coupons if hasattr(self, "coupons") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!s}, '
                f'issue_date={(self.issue_date if hasattr(self, "issue_date") else None)!s}, '
                f'net_terms={(self.net_terms if hasattr(self, "net_terms") else None)!s}, '
                f'payment_instructions={(self.payment_instructions if hasattr(self, "payment_instructions") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'seller_address={(self.seller_address if hasattr(self, "seller_address") else None)!s}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!s}, '
                f'shipping_address={(self.shipping_address if hasattr(self, "shipping_address") else None)!s}, '
                f'coupons={(self.coupons if hasattr(self, "coupons") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
