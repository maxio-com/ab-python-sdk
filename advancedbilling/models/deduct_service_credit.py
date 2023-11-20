# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class DeductServiceCredit(object):

    """Implementation of the 'Deduct Service Credit' model.

    TODO: type model description here.

    Attributes:
        amount (str | float): TODO: type description here.
        memo (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo'
    }

    def __init__(self,
                 amount=None,
                 memo=None):
        """Constructor for the DeductServiceCredit class"""

        # Initialize members of the class
        self.amount = amount 
        self.memo = memo 

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
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('DeductServiceCreditAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        # Return an object of this model
        return cls(amount,
                   memo)

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
            return UnionTypeLookUp.get('DeductServiceCreditAmount').validate(dictionary.amount) \
                and APIHelper.is_valid_type(value=dictionary.memo, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('DeductServiceCreditAmount').validate(dictionary.get('amount')) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'), type_callable=lambda value: isinstance(value, str))
