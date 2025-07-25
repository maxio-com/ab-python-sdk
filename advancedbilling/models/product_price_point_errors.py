# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ProductPricePointErrors(object):

    """Implementation of the 'Product Price Point Errors' model.

    Attributes:
        price_point (str): The model property of type str.
        interval (List[str]): The model property of type List[str].
        interval_unit (List[str]): The model property of type List[str].
        name (List[str]): The model property of type List[str].
        price (List[str]): The model property of type List[str].
        price_in_cents (List[str]): The model property of type List[str].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_point": 'price_point',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "name": 'name',
        "price": 'price',
        "price_in_cents": 'price_in_cents'
    }

    _optionals = [
        'price_point',
        'interval',
        'interval_unit',
        'name',
        'price',
        'price_in_cents',
    ]

    def __init__(self,
                 price_point=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ProductPricePointErrors class"""

        # Initialize members of the class
        if price_point is not APIHelper.SKIP:
            self.price_point = price_point 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if name is not APIHelper.SKIP:
            self.name = name 
        if price is not APIHelper.SKIP:
            self.price = price 
        if price_in_cents is not APIHelper.SKIP:
            self.price_in_cents = price_in_cents 

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
        price_point = dictionary.get("price_point") if dictionary.get("price_point") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        price = dictionary.get("price") if dictionary.get("price") else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(price_point,
                   interval,
                   interval_unit,
                   name,
                   price,
                   price_in_cents,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'price_point={(self.price_point if hasattr(self, "price_point") else None)!r}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!r}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'price={(self.price if hasattr(self, "price") else None)!r}, '
                f'price_in_cents={(self.price_in_cents if hasattr(self, "price_in_cents") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'price_point={(self.price_point if hasattr(self, "price_point") else None)!s}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!s}, '
                f'interval_unit={(self.interval_unit if hasattr(self, "interval_unit") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'price={(self.price if hasattr(self, "price") else None)!s}, '
                f'price_in_cents={(self.price_in_cents if hasattr(self, "price_in_cents") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
