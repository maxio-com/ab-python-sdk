# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.price import Price


class ComponentCustomPrice(object):

    """Implementation of the 'Component Custom Price' model.

    Create or update custom pricing unique to the subscription. Used in place
    of `price_point_id`.

    Attributes:
        pricing_scheme (PricingScheme): Omit for On/Off components
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        prices (List[Price]): On/off components only need one price bracket
            starting at 1

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": 'pricing_scheme',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "prices": 'prices'
    }

    _optionals = [
        'pricing_scheme',
        'interval',
        'interval_unit',
        'prices',
    ]

    def __init__(self,
                 pricing_scheme=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ComponentCustomPrice class"""

        # Initialize members of the class
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if prices is not APIHelper.SKIP:
            self.prices = prices 

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
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(pricing_scheme,
                   interval,
                   interval_unit,
                   prices,
                   dictionary)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
