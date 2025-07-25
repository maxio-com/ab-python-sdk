# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProformaInvoicePayment(object):

    """Implementation of the 'Proforma Invoice Payment' model.

    Attributes:
        memo (str): The model property of type str.
        original_amount (str): The model property of type str.
        applied_amount (str): The model property of type str.
        prepayment (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "prepayment": 'prepayment'
    }

    _optionals = [
        'memo',
        'original_amount',
        'applied_amount',
        'prepayment',
    ]

    def __init__(self,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 prepayment=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ProformaInvoicePayment class"""

        # Initialize members of the class
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if prepayment is not APIHelper.SKIP:
            self.prepayment = prepayment 

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
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        prepayment = dictionary.get("prepayment") if "prepayment" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(memo,
                   original_amount,
                   applied_amount,
                   prepayment,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'original_amount={(self.original_amount if hasattr(self, "original_amount") else None)!r}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!r}, '
                f'prepayment={(self.prepayment if hasattr(self, "prepayment") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'original_amount={(self.original_amount if hasattr(self, "original_amount") else None)!s}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!s}, '
                f'prepayment={(self.prepayment if hasattr(self, "prepayment") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
