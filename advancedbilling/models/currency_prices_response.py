# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.currency_price import CurrencyPrice


class CurrencyPricesResponse(object):

    """Implementation of the 'Currency Prices Response' model.

    Attributes:
        currency_prices (List[CurrencyPrice]): The model property of type
            List[CurrencyPrice].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency_prices": 'currency_prices'
    }

    def __init__(self,
                 currency_prices=None,
                 additional_properties=None):
        """Constructor for the CurrencyPricesResponse class"""

        # Initialize members of the class
        self.currency_prices = currency_prices 

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
        currency_prices = None
        if dictionary.get('currency_prices') is not None:
            currency_prices = [CurrencyPrice.from_dictionary(x) for x in dictionary.get('currency_prices')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(currency_prices,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'currency_prices={self.currency_prices!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'currency_prices={self.currency_prices!s}, '
                f'additional_properties={self.additional_properties!s})')
