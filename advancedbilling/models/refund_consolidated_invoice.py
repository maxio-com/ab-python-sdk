# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RefundConsolidatedInvoice(object):

    """Implementation of the 'Refund Consolidated Invoice' model.

    Refund consolidated invoice

    Attributes:
        memo (str): A description for the refund
        payment_id (int): The ID of the payment to be refunded
        segment_uids (List[str] | str): An array of segment uids to refund or
            the string 'all' to indicate that all segments should be refunded
        external (bool): Flag that marks refund as external (no money is
            returned to the customer). Defaults to `false`.
        apply_credit (bool): If set to true, creates credit and applies it to
            an invoice. Defaults to `false`.
        amount (str): The amount of payment to be refunded in decimal format.
            Example: "10.50". This will default to the full amount of the
            payment if not provided.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "memo": 'memo',
        "payment_id": 'payment_id',
        "segment_uids": 'segment_uids',
        "external": 'external',
        "apply_credit": 'apply_credit',
        "amount": 'amount'
    }

    _optionals = [
        'external',
        'apply_credit',
        'amount',
    ]

    def __init__(self,
                 memo=None,
                 payment_id=None,
                 segment_uids=None,
                 external=APIHelper.SKIP,
                 apply_credit=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the RefundConsolidatedInvoice class"""

        # Initialize members of the class
        self.memo = memo 
        self.payment_id = payment_id 
        self.segment_uids = segment_uids 
        if external is not APIHelper.SKIP:
            self.external = external 
        if apply_credit is not APIHelper.SKIP:
            self.apply_credit = apply_credit 
        if amount is not APIHelper.SKIP:
            self.amount = amount 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else None
        segment_uids = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RefundConsolidatedInvoiceSegmentUids'), dictionary.get('segment_uids'), False) if dictionary.get('segment_uids') is not None else None
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        apply_credit = dictionary.get("apply_credit") if "apply_credit" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(memo,
                   payment_id,
                   segment_uids,
                   external,
                   apply_credit,
                   amount,
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.memo,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.payment_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and UnionTypeLookUp.get('RefundConsolidatedInvoiceSegmentUids').validate(dictionary.segment_uids).is_valid

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('memo'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and UnionTypeLookUp.get('RefundConsolidatedInvoiceSegmentUids').validate(dictionary.get('segment_uids')).is_valid

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'memo={self.memo!r}, '
                f'payment_id={self.payment_id!r}, '
                f'segment_uids={self.segment_uids!r}, '
                f'external={(self.external if hasattr(self, "external") else None)!r}, '
                f'apply_credit={(self.apply_credit if hasattr(self, "apply_credit") else None)!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'memo={self.memo!s}, '
                f'payment_id={self.payment_id!s}, '
                f'segment_uids={self.segment_uids!s}, '
                f'external={(self.external if hasattr(self, "external") else None)!s}, '
                f'apply_credit={(self.apply_credit if hasattr(self, "apply_credit") else None)!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
