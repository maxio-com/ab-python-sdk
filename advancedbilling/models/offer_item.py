# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.currency_price import CurrencyPrice


class OfferItem(object):

    """Implementation of the 'Offer Item' model.

    Attributes:
        component_id (int): The model property of type int.
        price_point_id (int): The model property of type int.
        starting_quantity (str): The model property of type str.
        editable (bool): The model property of type bool.
        component_unit_price (str): The model property of type str.
        component_name (str): The model property of type str.
        price_point_name (str): The model property of type str.
        currency_prices (List[CurrencyPrice]): The model property of type
            List[CurrencyPrice].
        interval (int): The numerical interval. i.e. an interval of '30'
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "price_point_id": 'price_point_id',
        "starting_quantity": 'starting_quantity',
        "editable": 'editable',
        "component_unit_price": 'component_unit_price',
        "component_name": 'component_name',
        "price_point_name": 'price_point_name',
        "currency_prices": 'currency_prices',
        "interval": 'interval',
        "interval_unit": 'interval_unit'
    }

    _optionals = [
        'component_id',
        'price_point_id',
        'starting_quantity',
        'editable',
        'component_unit_price',
        'component_name',
        'price_point_name',
        'currency_prices',
        'interval',
        'interval_unit',
    ]

    _nullables = [
        'interval_unit',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 starting_quantity=APIHelper.SKIP,
                 editable=APIHelper.SKIP,
                 component_unit_price=APIHelper.SKIP,
                 component_name=APIHelper.SKIP,
                 price_point_name=APIHelper.SKIP,
                 currency_prices=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the OfferItem class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if starting_quantity is not APIHelper.SKIP:
            self.starting_quantity = starting_quantity 
        if editable is not APIHelper.SKIP:
            self.editable = editable 
        if component_unit_price is not APIHelper.SKIP:
            self.component_unit_price = component_unit_price 
        if component_name is not APIHelper.SKIP:
            self.component_name = component_name 
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name 
        if currency_prices is not APIHelper.SKIP:
            self.currency_prices = currency_prices 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        editable = dictionary.get("editable") if "editable" in dictionary.keys() else APIHelper.SKIP
        component_unit_price = dictionary.get("component_unit_price") if dictionary.get("component_unit_price") else APIHelper.SKIP
        component_name = dictionary.get("component_name") if dictionary.get("component_name") else APIHelper.SKIP
        price_point_name = dictionary.get("price_point_name") if dictionary.get("price_point_name") else APIHelper.SKIP
        currency_prices = None
        if dictionary.get('currency_prices') is not None:
            currency_prices = [CurrencyPrice.from_dictionary(x) for x in dictionary.get('currency_prices')]
        else:
            currency_prices = APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   price_point_id,
                   starting_quantity,
                   editable,
                   component_unit_price,
                   component_name,
                   price_point_name,
                   currency_prices,
                   interval,
                   interval_unit,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={self.component_id!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'starting_quantity={self.starting_quantity!r}, '
                f'editable={self.editable!r}, '
                f'component_unit_price={self.component_unit_price!r}, '
                f'component_name={self.component_name!r}, '
                f'price_point_name={self.price_point_name!r}, '
                f'currency_prices={self.currency_prices!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'component_id={self.component_id!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'starting_quantity={self.starting_quantity!s}, '
                f'editable={self.editable!s}, '
                f'component_unit_price={self.component_unit_price!s}, '
                f'component_name={self.component_name!s}, '
                f'price_point_name={self.price_point_name!s}, '
                f'currency_prices={self.currency_prices!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'additional_properties={self.additional_properties!s})')
