# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_offer_component import CreateOfferComponent


class CreateOffer(object):

    """Implementation of the 'Create Offer' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        description (str): TODO: type description here.
        product_id (int): TODO: type description here.
        product_price_point_id (int): TODO: type description here.
        components (List[CreateOfferComponent]): TODO: type description here.
        coupons (List[str]): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "handle": 'handle',
        "product_id": 'product_id',
        "description": 'description',
        "product_price_point_id": 'product_price_point_id',
        "components": 'components',
        "coupons": 'coupons'
    }

    _optionals = [
        'description',
        'product_price_point_id',
        'components',
        'coupons',
    ]

    def __init__(self,
                 name=None,
                 handle=None,
                 product_id=None,
                 description=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 components=APIHelper.SKIP,
                 coupons=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateOffer class"""

        # Initialize members of the class
        self.name = name 
        self.handle = handle 
        if description is not APIHelper.SKIP:
            self.description = description 
        self.product_id = product_id 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if components is not APIHelper.SKIP:
            self.components = components 
        if coupons is not APIHelper.SKIP:
            self.coupons = coupons 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        handle = dictionary.get("handle") if dictionary.get("handle") else None
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else None
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        components = None
        if dictionary.get('components') is not None:
            components = [CreateOfferComponent.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        coupons = dictionary.get("coupons") if dictionary.get("coupons") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   handle,
                   product_id,
                   description,
                   product_price_point_id,
                   components,
                   coupons,
                   additional_properties)
