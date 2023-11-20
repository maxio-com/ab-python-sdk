# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RefundInvoice(object):

    """Implementation of the 'Refund Invoice' model.

    Refund an invoice or a segment of a consolidated invoice.

    Attributes:
        amount (str): The amount to be refunded in decimal format as a string.
            Example: "10.50". Must not exceed the remaining refundable balance
            of the payment.
        memo (str): A description that will be attached to the refund
        payment_id (int): The ID of the payment to be refunded
        external (bool): Flag that marks refund as external (no money is
            returned to the customer). Defaults to `false`.
        apply_credit (bool): If set to true, creates credit and applies it to
            an invoice. Defaults to `false`.
        void_invoice (bool): If `apply_credit` set to false and refunding full
            amount, if `void_invoice` set to true, invoice will be voided
            after refund. Defaults to `false`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo',
        "payment_id": 'payment_id',
        "external": 'external',
        "apply_credit": 'apply_credit',
        "void_invoice": 'void_invoice'
    }

    _optionals = [
        'external',
        'apply_credit',
        'void_invoice',
    ]

    def __init__(self,
                 amount=None,
                 memo=None,
                 payment_id=None,
                 external=APIHelper.SKIP,
                 apply_credit=APIHelper.SKIP,
                 void_invoice=APIHelper.SKIP):
        """Constructor for the RefundInvoice class"""

        # Initialize members of the class
        self.amount = amount 
        self.memo = memo 
        self.payment_id = payment_id 
        if external is not APIHelper.SKIP:
            self.external = external 
        if apply_credit is not APIHelper.SKIP:
            self.apply_credit = apply_credit 
        if void_invoice is not APIHelper.SKIP:
            self.void_invoice = void_invoice 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else None
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        apply_credit = dictionary.get("apply_credit") if "apply_credit" in dictionary.keys() else APIHelper.SKIP
        void_invoice = dictionary.get("void_invoice") if "void_invoice" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   memo,
                   payment_id,
                   external,
                   apply_credit,
                   void_invoice)

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
            return APIHelper.is_valid_type(value=dictionary.amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.memo, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.payment_id, type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_id'), type_callable=lambda value: isinstance(value, int))
