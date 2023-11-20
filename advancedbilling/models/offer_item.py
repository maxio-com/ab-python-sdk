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

    TODO: type model description here.

    Attributes:
        component_id (int): TODO: type description here.
        price_point_id (int): TODO: type description here.
        starting_quantity (str): TODO: type description here.
        editable (bool): TODO: type description here.
        component_unit_price (str): TODO: type description here.
        component_name (str): TODO: type description here.
        price_point_name (str): TODO: type description here.
        currency_prices (List[CurrencyPrice]): TODO: type description here.

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
        "currency_prices": 'currency_prices'
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
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 starting_quantity=APIHelper.SKIP,
                 editable=APIHelper.SKIP,
                 component_unit_price=APIHelper.SKIP,
                 component_name=APIHelper.SKIP,
                 price_point_name=APIHelper.SKIP,
                 currency_prices=APIHelper.SKIP):
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
        # Return an object of this model
        return cls(component_id,
                   price_point_id,
                   starting_quantity,
                   editable,
                   component_unit_price,
                   component_name,
                   price_point_name,
                   currency_prices)
