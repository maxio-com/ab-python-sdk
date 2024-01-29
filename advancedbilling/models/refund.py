# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Refund(object):

    """Implementation of the 'Refund' model.

    TODO: type model description here.

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
        segment_uids (List[str] | str | None): An array of segment uids to
            refund or the string 'all' to indicate that all segments should be
            refunded

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo',
        "payment_id": 'payment_id',
        "external": 'external',
        "apply_credit": 'apply_credit',
        "void_invoice": 'void_invoice',
        "segment_uids": 'segment_uids'
    }

    _optionals = [
        'amount',
        'memo',
        'payment_id',
        'external',
        'apply_credit',
        'void_invoice',
        'segment_uids',
    ]

    def __init__(self,
                 amount=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 payment_id=APIHelper.SKIP,
                 external=APIHelper.SKIP,
                 apply_credit=APIHelper.SKIP,
                 void_invoice=APIHelper.SKIP,
                 segment_uids=APIHelper.SKIP):
        """Constructor for the Refund class"""

        # Initialize members of the class
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if payment_id is not APIHelper.SKIP:
            self.payment_id = payment_id 
        if external is not APIHelper.SKIP:
            self.external = external 
        if apply_credit is not APIHelper.SKIP:
            self.apply_credit = apply_credit 
        if void_invoice is not APIHelper.SKIP:
            self.void_invoice = void_invoice 
        if segment_uids is not APIHelper.SKIP:
            self.segment_uids = segment_uids 

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
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else APIHelper.SKIP
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        apply_credit = dictionary.get("apply_credit") if "apply_credit" in dictionary.keys() else APIHelper.SKIP
        void_invoice = dictionary.get("void_invoice") if "void_invoice" in dictionary.keys() else APIHelper.SKIP
        segment_uids = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RefundSegmentUids'), dictionary.get('segment_uids'), False) if dictionary.get('segment_uids') is not None else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   memo,
                   payment_id,
                   external,
                   apply_credit,
                   void_invoice,
                   segment_uids)
