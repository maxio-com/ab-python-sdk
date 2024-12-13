# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SubscriptionGroupPrepayment(object):

    """Implementation of the 'Subscription Group Prepayment' model.

    TODO: type model description here.

    Attributes:
        amount (int): TODO: type description here.
        details (str): TODO: type description here.
        memo (str): TODO: type description here.
        method (SubscriptionGroupPrepaymentMethod): TODO: type description
            here.
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
