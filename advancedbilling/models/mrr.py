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

    Attributes:
        amount_in_cents (int): The model property of type int.
        amount_formatted (str): The model property of type str.
        currency (str): The model property of type str.
        currency_symbol (str): The model property of type str.
        breakouts (Breakouts): The model property of type Breakouts.
        at_time (datetime): ISO8601 timestamp
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 at_time=APIHelper.SKIP,
                 additional_properties=None):
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
            self.at_time = APIHelper.apply_datetime_converter(at_time, APIHelper.RFC3339DateTime) if at_time else None 

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
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        amount_formatted = dictionary.get("amount_formatted") if dictionary.get("amount_formatted") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        currency_symbol = dictionary.get("currency_symbol") if dictionary.get("currency_symbol") else APIHelper.SKIP
        breakouts = Breakouts.from_dictionary(dictionary.get('breakouts')) if 'breakouts' in dictionary.keys() else APIHelper.SKIP
        at_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("at_time")).datetime if dictionary.get("at_time") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount_in_cents,
                   amount_formatted,
                   currency,
                   currency_symbol,
                   breakouts,
                   at_time,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount_in_cents={self.amount_in_cents!r}, '
                f'amount_formatted={self.amount_formatted!r}, '
                f'currency={self.currency!r}, '
                f'currency_symbol={self.currency_symbol!r}, '
                f'breakouts={self.breakouts!r}, '
                f'at_time={self.at_time!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount_in_cents={self.amount_in_cents!s}, '
                f'amount_formatted={self.amount_formatted!s}, '
                f'currency={self.currency!s}, '
                f'currency_symbol={self.currency_symbol!s}, '
                f'breakouts={self.breakouts!s}, '
                f'at_time={self.at_time!s}, '
                f'additional_properties={self.additional_properties!s})')
