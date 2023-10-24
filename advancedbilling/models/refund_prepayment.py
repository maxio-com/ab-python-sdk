# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RefundPrepayment(object):

    """Implementation of the 'Refund Prepayment' model.

    TODO: type model description here.

    Attributes:
        amount_in_cents (float): `amount` is not required if you pass
            `amount_in_cents`.
        amount (str | float): `amount_in_cents` is not required if you pass
            `amount`.
        memo (str): TODO: type description here.
        external (bool): Specify the type of refund you wish to initiate. When
            the prepayment is external, the `external` flag is optional. But
            if the prepayment was made through a payment profile, the
            `external` flag is required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_in_cents": 'amount_in_cents',
        "amount": 'amount',
        "memo": 'memo',
        "external": 'external'
    }

    _optionals = [
        'external',
    ]

    def __init__(self,
                 amount_in_cents=None,
                 amount=None,
                 memo=None,
                 external=APIHelper.SKIP):
        """Constructor for the RefundPrepayment class"""

        # Initialize members of the class
        self.amount_in_cents = amount_in_cents 
        self.amount = amount 
        self.memo = memo 
        if external is not APIHelper.SKIP:
            self.external = external 

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
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else None
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RefundPrepaymentAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(amount_in_cents,
                   amount,
                   memo,
                   external)

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
            return APIHelper.is_valid_type(value=dictionary.amount_in_cents, type_callable=lambda value: isinstance(value, float)) \
                and UnionTypeLookUp.get('RefundPrepaymentAmount').validate(dictionary.amount) \
                and APIHelper.is_valid_type(value=dictionary.memo, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('amount_in_cents'), type_callable=lambda value: isinstance(value, float)) \
            and UnionTypeLookUp.get('RefundPrepaymentAmount').validate(dictionary.get('amount')) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'), type_callable=lambda value: isinstance(value, str))
