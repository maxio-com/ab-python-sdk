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

    Attributes:
        component_code_id (int): The model property of type int.
        price_point_id (int): The model property of type int.
        product_id (int): The model property of type int.
        quantity (str): The model property of type str.
        amount (str): The model property of type str.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        tiers (List[ComponentCostDataRateTier]): The model property of type
            List[ComponentCostDataRateTier].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 tiers=APIHelper.SKIP,
                 additional_properties=None):
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
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_code_id,
                   price_point_id,
                   product_id,
                   quantity,
                   amount,
                   pricing_scheme,
                   tiers,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'component_code_id={self.component_code_id!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'product_id={self.product_id!r}, '
                f'quantity={self.quantity!r}, '
                f'amount={self.amount!r}, '
                f'pricing_scheme={self.pricing_scheme!r}, '
                f'tiers={self.tiers!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'component_code_id={self.component_code_id!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'product_id={self.product_id!s}, '
                f'quantity={self.quantity!s}, '
                f'amount={self.amount!s}, '
                f'pricing_scheme={self.pricing_scheme!s}, '
                f'tiers={self.tiers!s}, '
                f'additional_properties={self.additional_properties!s})')
