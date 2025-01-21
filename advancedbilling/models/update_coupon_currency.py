# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpdateCouponCurrency(object):

    """Implementation of the 'Update Coupon Currency' model.

    Attributes:
        currency (str): ISO code for the site defined currency.
        price (int): Price for the given currency.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'currency',
        "price": 'price'
    }

    def __init__(self,
                 currency=None,
                 price=None,
                 additional_properties=None):
        """Constructor for the UpdateCouponCurrency class"""

        # Initialize members of the class
        self.currency = currency 
        self.price = price 

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
        currency = dictionary.get("currency") if dictionary.get("currency") else None
        price = dictionary.get("price") if dictionary.get("price") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(currency,
                   price,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'currency={self.currency!r}, '
                f'price={self.price!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'currency={self.currency!s}, '
                f'price={self.price!s}, '
                f'additional_properties={self.additional_properties!s})')
