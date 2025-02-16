# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SubscriptionGroupPrepayment(object):

    """Implementation of the 'Subscription Group Prepayment' model.

    Attributes:
        amount (int): The model property of type int.
        details (str): The model property of type str.
        memo (str): The model property of type str.
        method (SubscriptionGroupPrepaymentMethod): The model property of type
            SubscriptionGroupPrepaymentMethod.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "details": 'details',
        "memo": 'memo',
        "method": 'method'
    }

    def __init__(self,
                 amount=None,
                 details=None,
                 memo=None,
                 method=None,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupPrepayment class"""

        # Initialize members of the class
        self.amount = amount 
        self.details = details 
        self.memo = memo 
        self.method = method 

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
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        details = dictionary.get("details") if dictionary.get("details") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        method = dictionary.get("method") if dictionary.get("method") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount,
                   details,
                   memo,
                   method,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount={self.amount!r}, '
                f'details={self.details!r}, '
                f'memo={self.memo!r}, '
                f'method={self.method!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount={self.amount!s}, '
                f'details={self.details!s}, '
                f'memo={self.memo!s}, '
                f'method={self.method!s}, '
                f'additional_properties={self.additional_properties!s})')
