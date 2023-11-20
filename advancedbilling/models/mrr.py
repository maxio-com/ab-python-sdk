# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.breakouts import Breakouts


class MRR(object):

    """Implementation of the 'MRR' model.

    TODO: type model description here.

    Attributes:
        amount_in_cents (long|int): TODO: type description here.
        amount_formatted (str): TODO: type description here.
        currency (str): TODO: type description here.
        currency_symbol (str): TODO: type description here.
        breakouts (Breakouts): TODO: type description here.
        at_time (str): ISO8601 timestamp

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_in_cents": 'amount_in_cents',
        "amount_formatted": 'amount_formatted',
        "currency": 'currency',
        "currency_symbol": 'currency_symbol',
        "breakouts": 'breakouts',
        "at_time": 'at_time'
    }

    _optionals = [
        'amount_in_cents',
        'amount_formatted',
        'currency',
        'currency_symbol',
        'breakouts',
        'at_time',
    ]

    def __init__(self,
                 amount_in_cents=APIHelper.SKIP,
                 amount_formatted=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 currency_symbol=APIHelper.SKIP,
                 breakouts=APIHelper.SKIP,
                 at_time=APIHelper.SKIP):
        """Constructor for the MRR class"""

        # Initialize members of the class
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if amount_formatted is not APIHelper.SKIP:
            self.amount_formatted = amount_formatted 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if currency_symbol is not APIHelper.SKIP:
            self.currency_symbol = currency_symbol 
        if breakouts is not APIHelper.SKIP:
            self.breakouts = breakouts 
        if at_time is not APIHelper.SKIP:
            self.at_time = at_time 

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
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        amount_formatted = dictionary.get("amount_formatted") if dictionary.get("amount_formatted") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        currency_symbol = dictionary.get("currency_symbol") if dictionary.get("currency_symbol") else APIHelper.SKIP
        breakouts = Breakouts.from_dictionary(dictionary.get('breakouts')) if 'breakouts' in dictionary.keys() else APIHelper.SKIP
        at_time = dictionary.get("at_time") if dictionary.get("at_time") else APIHelper.SKIP
        # Return an object of this model
        return cls(amount_in_cents,
                   amount_formatted,
                   currency,
                   currency_symbol,
                   breakouts,
                   at_time)
