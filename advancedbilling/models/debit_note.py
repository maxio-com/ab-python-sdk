# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.credit_note_line_item import CreditNoteLineItem
from advancedbilling.models.invoice_address import InvoiceAddress
from advancedbilling.models.invoice_customer import InvoiceCustomer
from advancedbilling.models.invoice_discount import InvoiceDiscount
from advancedbilling.models.invoice_refund import InvoiceRefund
from advancedbilling.models.invoice_seller import InvoiceSeller
from advancedbilling.models.invoice_tax import InvoiceTax


class DebitNote(object):

    """Implementation of the 'Debit Note' model.

    TODO: type model description here.

    Attributes:
        uid (str): Unique identifier for the debit note. It is generated
            automatically by Chargify and has the prefix "db_" followed by
            alphanumeric characters.
        site_id (int): ID of the site to which the debit note belongs.
        customer_id (int): ID of the customer to which the debit note belongs.
        subscription_id (int): ID of the subscription that generated the debit
            note.
        number (int): A unique, identifier that appears on the debit note and
            in places it is referenced.
        sequence_number (int): A monotonically increasing number assigned to
            debit notes as they are created.
        origin_credit_note_uid (str): Unique identifier for the connected
            credit note. It is generated automatically by Chargify and has the
            prefix "cn_" followed by alphanumeric characters.  While the UID
            is long and not appropriate to show to customers, the number is
            usually shorter and consumable by the customer and the merchant
            alike.
        origin_credit_note_number (str): A unique, identifying string of the
            connected credit note.
        issue_date (date): Date the document was issued to the customer. This
            is the date that the document was made available for payment.  The
            format is "YYYY-MM-DD".
        applied_date (date): Debit notes are applied to invoices to offset
            invoiced amounts - they adjust the amount due. This field is the
            date the debit note document became fully applied to the invoice. 
            The format is "YYYY-MM-DD".
        due_date (date): Date the document is due for payment. The format is
            "YYYY-MM-DD".
        status (DebitNoteStatus): Current status of the debit note.
        memo (str): The memo printed on debit note, which is a description of
            the reason for the debit.
        role (DebitNoteRole): The role of the debit note.
        currency (str): The ISO 4217 currency code (3 character string)
            representing the currency of the credit note amount fields.
        seller (InvoiceSeller): Information about the seller (merchant) listed
            on the masthead of the debit note.
        customer (InvoiceCustomer): Information about the customer who is
            owner or recipient the debited subscription.
        billing_address (InvoiceAddress): The billing address of the debited
            subscription.
        shipping_address (InvoiceAddress): The shipping address of the debited
            subscription.
        line_items (List[CreditNoteLineItem]): Line items on the debit note.
        discounts (List[InvoiceDiscount]): TODO: type description here.
        taxes (List[InvoiceTax]): TODO: type description here.
        refunds (List[InvoiceRefund]): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "site_id": 'site_id',
        "customer_id": 'customer_id',
        "subscription_id": 'subscription_id',
        "number": 'number',
        "sequence_number": 'sequence_number',
        "origin_credit_note_uid": 'origin_credit_note_uid',
        "origin_credit_note_number": 'origin_credit_note_number',
        "issue_date": 'issue_date',
        "applied_date": 'applied_date',
        "due_date": 'due_date',
        "status": 'status',
        "memo": 'memo',
        "role": 'role',
        "currency": 'currency',
        "seller": 'seller',
        "customer": 'customer',
        "billing_address": 'billing_address',
        "shipping_address": 'shipping_address',
        "line_items": 'line_items',
        "discounts": 'discounts',
        "taxes": 'taxes',
        "refunds": 'refunds'
    }

    _optionals = [
        'uid',
        'site_id',
        'customer_id',
        'subscription_id',
        'number',
        'sequence_number',
        'origin_credit_note_uid',
        'origin_credit_note_number',
        'issue_date',
        'applied_date',
        'due_date',
        'status',
        'memo',
        'role',
        'currency',
        'seller',
        'customer',
        'billing_address',
        'shipping_address',
        'line_items',
        'discounts',
        'taxes',
        'refunds',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 sequence_number=APIHelper.SKIP,
                 origin_credit_note_uid=APIHelper.SKIP,
                 origin_credit_note_number=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 applied_date=APIHelper.SKIP,
                 due_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 role=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 seller=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 shipping_address=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 taxes=APIHelper.SKIP,
                 refunds=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the DebitNote class"""

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
        if origin_credit_note_uid is not APIHelper.SKIP:
            self.origin_credit_note_uid = origin_credit_note_uid 
        if origin_credit_note_number is not APIHelper.SKIP:
            self.origin_credit_note_number = origin_credit_note_number 
        if issue_date is not APIHelper.SKIP:
            self.issue_date = issue_date 
        if applied_date is not APIHelper.SKIP:
            self.applied_date = applied_date 
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date 
        if status is not APIHelper.SKIP:
            self.status = status 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if role is not APIHelper.SKIP:
            self.role = role 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if seller is not APIHelper.SKIP:
            self.seller = seller 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if shipping_address is not APIHelper.SKIP:
            self.shipping_address = shipping_address 
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        if taxes is not APIHelper.SKIP:
            self.taxes = taxes 
        if refunds is not APIHelper.SKIP:
            self.refunds = refunds 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        sequence_number = dictionary.get("sequence_number") if dictionary.get("sequence_number") else APIHelper.SKIP
        origin_credit_note_uid = dictionary.get("origin_credit_note_uid") if dictionary.get("origin_credit_note_uid") else APIHelper.SKIP
        origin_credit_note_number = dictionary.get("origin_credit_note_number") if dictionary.get("origin_credit_note_number") else APIHelper.SKIP
        issue_date = dateutil.parser.parse(dictionary.get('issue_date')).date() if dictionary.get('issue_date') else APIHelper.SKIP
        applied_date = dateutil.parser.parse(dictionary.get('applied_date')).date() if dictionary.get('applied_date') else APIHelper.SKIP
        due_date = dateutil.parser.parse(dictionary.get('due_date')).date() if dictionary.get('due_date') else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        seller = InvoiceSeller.from_dictionary(dictionary.get('seller')) if 'seller' in dictionary.keys() else APIHelper.SKIP
        customer = InvoiceCustomer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        billing_address = InvoiceAddress.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        shipping_address = InvoiceAddress.from_dictionary(dictionary.get('shipping_address')) if 'shipping_address' in dictionary.keys() else APIHelper.SKIP
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
        refunds = None
        if dictionary.get('refunds') is not None:
            refunds = [InvoiceRefund.from_dictionary(x) for x in dictionary.get('refunds')]
        else:
            refunds = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   site_id,
                   customer_id,
                   subscription_id,
                   number,
                   sequence_number,
                   origin_credit_note_uid,
                   origin_credit_note_number,
                   issue_date,
                   applied_date,
                   due_date,
                   status,
                   memo,
                   role,
                   currency,
                   seller,
                   customer,
                   billing_address,
                   shipping_address,
                   line_items,
                   discounts,
                   taxes,
                   refunds,
                   additional_properties)

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
