# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.credit_note import CreditNote


class RefundInvoiceEventData(object):

    """Implementation of the 'Refund Invoice Event Data' model.

    Example schema for an `refund_invoice` event

    Attributes:
        apply_credit (bool): If true, credit was created and applied it to the
            invoice.
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
        credit_note_attributes (CreditNote): TODO: type description here.
        memo (str): The refund memo.
        original_amount (str): The full, original amount of the refund.
        payment_id (int): The ID of the payment transaction to be refunded.
        refund_amount (str): The amount of the refund.
        refund_id (int): The ID of the refund transaction.
        transaction_time (datetime): The time the refund was applied, in ISO
            8601 format, i.e. "2019-06-07T17:20:06Z"

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "apply_credit": 'apply_credit',
        "credit_note_attributes": 'credit_note_attributes',
        "payment_id": 'payment_id',
        "refund_amount": 'refund_amount',
        "refund_id": 'refund_id',
        "transaction_time": 'transaction_time',
        "consolidation_level": 'consolidation_level',
        "memo": 'memo',
        "original_amount": 'original_amount'
    }

    _optionals = [
        'consolidation_level',
        'memo',
        'original_amount',
    ]

    def __init__(self,
                 apply_credit=None,
                 credit_note_attributes=None,
                 payment_id=None,
                 refund_amount=None,
                 refund_id=None,
                 transaction_time=None,
                 consolidation_level=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP):
        """Constructor for the RefundInvoiceEventData class"""

        # Initialize members of the class
        self.apply_credit = apply_credit 
        if consolidation_level is not APIHelper.SKIP:
            self.consolidation_level = consolidation_level 
        self.credit_note_attributes = credit_note_attributes 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        self.payment_id = payment_id 
        self.refund_amount = refund_amount 
        self.refund_id = refund_id 
        self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 

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
        apply_credit = dictionary.get("apply_credit") if "apply_credit" in dictionary.keys() else None
        credit_note_attributes = CreditNote.from_dictionary(dictionary.get('credit_note_attributes')) if dictionary.get('credit_note_attributes') else None
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else None
        refund_amount = dictionary.get("refund_amount") if dictionary.get("refund_amount") else None
        refund_id = dictionary.get("refund_id") if dictionary.get("refund_id") else None
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else None
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(apply_credit,
                   credit_note_attributes,
                   payment_id,
                   refund_amount,
                   refund_id,
                   transaction_time,
                   consolidation_level,
                   memo,
                   original_amount)

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
            return APIHelper.is_valid_type(value=dictionary.apply_credit, type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.credit_note_attributes, type_callable=lambda value: CreditNote.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.payment_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.refund_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.refund_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.transaction_time, type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('apply_credit'), type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('credit_note_attributes'), type_callable=lambda value: CreditNote.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('refund_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('refund_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_time'), type_callable=lambda value: isinstance(value, str))
