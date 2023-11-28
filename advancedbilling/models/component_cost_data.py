# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_cost_data_rate_tier import ComponentCostDataRateTier


class ComponentCostData(object):

    """Implementation of the 'Component Cost Data' model.

    TODO: type model description here.

    Attributes:
        component_code_id (int): TODO: type description here.
        price_point_id (int): TODO: type description here.
        product_id (int): TODO: type description here.
        quantity (str): TODO: type description here.
        amount (str): TODO: type description here.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        tiers (List[ComponentCostDataRateTier]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_code_id": 'component_code_id',
        "price_point_id": 'price_point_id',
        "product_id": 'product_id',
        "quantity": 'quantity',
        "amount": 'amount',
        "pricing_scheme": 'pricing_scheme',
        "tiers": 'tiers'
    }

    _optionals = [
        'component_code_id',
        'price_point_id',
        'product_id',
        'quantity',
        'amount',
        'pricing_scheme',
        'tiers',
    ]

    _nullables = [
        'component_code_id',
    ]

    def __init__(self,
                 component_code_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 tiers=APIHelper.SKIP):
        """Constructor for the ComponentCostData class"""

        # Initialize members of the class
        if component_code_id is not APIHelper.SKIP:
            self.component_code_id = component_code_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if tiers is not APIHelper.SKIP:
            self.tiers = tiers 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        component_code_id = dictionary.get("component_code_id") if "component_code_id" in dictionary.keys() else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        tiers = None
        if dictionary.get('tiers') is not None:
            tiers = [ComponentCostDataRateTier.from_dictionary(x) for x in dictionary.get('tiers')]
        else:
            tiers = APIHelper.SKIP
        # Return an object of this model
        return cls(component_code_id,
                   price_point_id,
                   product_id,
                   quantity,
                   amount,
                   pricing_scheme,
                   tiers)

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
