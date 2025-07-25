# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreatePrepayment(object):

    """Implementation of the 'Create Prepayment' model.

    Attributes:
        amount (float): The model property of type float.
        details (str): The model property of type str.
        memo (str): The model property of type str.
        method (CreatePrepaymentMethod): :- When the `method` specified is
            `"credit_card_on_file"`, the prepayment amount will be collected
            using the default credit card payment profile and applied to the
            prepayment account balance. This is especially useful for manual
            replenishment of prepaid subscriptions.
        payment_profile_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "details": 'details',
        "memo": 'memo',
        "method": 'method',
        "payment_profile_id": 'payment_profile_id'
    }

    _optionals = [
        'payment_profile_id',
    ]

    def __init__(self,
                 amount=None,
                 details=None,
                 memo=None,
                 method=None,
                 payment_profile_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreatePrepayment class"""

        # Initialize members of the class
        self.amount = amount 
        self.details = details 
        self.memo = memo 
        self.method = method 
        if payment_profile_id is not APIHelper.SKIP:
            self.payment_profile_id = payment_profile_id 

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
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount,
                   details,
                   memo,
                   method,
                   payment_profile_id,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount={self.amount!r}, '
                f'details={self.details!r}, '
                f'memo={self.memo!r}, '
                f'method={self.method!r}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount={self.amount!s}, '
                f'details={self.details!s}, '
                f'memo={self.memo!s}, '
                f'method={self.method!s}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
