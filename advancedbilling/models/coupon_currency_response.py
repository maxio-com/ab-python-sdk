# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.coupon_currency import CouponCurrency


class CouponCurrencyResponse(object):

    """Implementation of the 'Coupon Currency Response' model.

    TODO: type model description here.

    Attributes:
        currency_prices (List[CouponCurrency]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency_prices": 'currency_prices'
    }

    _optionals = [
        'currency_prices',
    ]

    def __init__(self,
                 currency_prices=APIHelper.SKIP):
        """Constructor for the CouponCurrencyResponse class"""

        # Initialize members of the class
        if currency_prices is not APIHelper.SKIP:
            self.currency_prices = currency_prices 

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
            currency_prices = [CouponCurrency.from_dictionary(x) for x in dictionary.get('currency_prices')]
        else:
            currency_prices = APIHelper.SKIP
        # Return an object of this model
        return cls(currency_prices)
