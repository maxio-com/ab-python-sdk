# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.currency_price import CurrencyPrice


class CurrencyPricesResponse(object):

    """Implementation of the 'Currency Prices Response' model.

    TODO: type model description here.

    Attributes:
        currency_prices (List[CurrencyPrice]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency_prices": 'currency_prices'
    }

    def __init__(self,
                 currency_prices=None,
                 additional_properties={}):
        """Constructor for the CurrencyPricesResponse class"""

        # Initialize members of the class
        self.currency_prices = currency_prices 

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        currency_prices = None
        if dictionary.get('currency_prices') is not None:
            currency_prices = [CurrencyPrice.from_dictionary(x) for x in dictionary.get('currency_prices')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(currency_prices,
                   dictionary)
