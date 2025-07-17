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
        tax_included (bool): Whether or not the price point includes tax
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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prices": 'prices',
        "tax_included": 'tax_included',
        "pricing_scheme": 'pricing_scheme',
        "interval": 'interval',
        "interval_unit": 'interval_unit'
    }

    _optionals = [
        'tax_included',
        'pricing_scheme',
        'interval',
        'interval_unit',
    ]

    _nullables = [
        'interval_unit',
    ]

    def __init__(self,
                 prices=None,
                 tax_included=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ComponentCustomPrice class"""

        # Initialize members of the class
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        self.prices = prices 

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
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        tax_included = dictionary.get("tax_included") if "tax_included" in dictionary.keys() else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(prices,
                   tax_included,
                   pricing_scheme,
                   interval,
                   interval_unit,
                   additional_properties)

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
            return APIHelper.is_valid_type(value=dictionary.prices,
                                           type_callable=lambda value: Price.validate(value),
                                           is_model_dict=True,
                                           is_inner_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('prices'),
                                       type_callable=lambda value: Price.validate(value),
                                       is_model_dict=True,
                                       is_inner_model_dict=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'tax_included={(self.tax_included if hasattr(self, "tax_included") else None)!r}, '
                f'pricing_scheme={(self.pricing_scheme if hasattr(self, "pricing_scheme") else None)!r}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!r}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!r}, '
                f'prices={self.prices!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tax_included={(self.tax_included if hasattr(self, "tax_included") else None)!s}, '
                f'pricing_scheme={(self.pricing_scheme if hasattr(self, "pricing_scheme") else None)!s}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!s}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!s}, '
                f'prices={self.prices!s}, '
                f'additional_properties={self.additional_properties!s})')
