# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class IssueServiceCredit(object):

    """Implementation of the 'Issue Service Credit' model.

    TODO: type model description here.

    Attributes:
        amount (float | str): TODO: type description here.
        memo (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo'
    }

    _optionals = [
        'memo',
    ]

    def __init__(self,
                 amount=None,
                 memo=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the IssueServiceCredit class"""

        # Initialize members of the class
        self.amount = amount 
        if memo is not APIHelper.SKIP:
            self.memo = memo 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('IssueServiceCreditAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else None
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(amount,
                   memo,
                   dictionary)

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
            return UnionTypeLookUp.get('IssueServiceCreditAmount').validate(dictionary.amount).is_valid

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('IssueServiceCreditAmount').validate(dictionary.get('amount')).is_valid
