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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "handle": 'handle',
        "description": 'description',
        "product_id": 'product_id',
        "product_price_point_id": 'product_price_point_id',
        "components": 'components',
        "coupons": 'coupons'
    }

    _optionals = [
        'name',
        'handle',
        'description',
        'product_id',
        'product_price_point_id',
        'components',
        'coupons',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 components=APIHelper.SKIP,
                 coupons=APIHelper.SKIP):
        """Constructor for the CreateOffer class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if description is not APIHelper.SKIP:
            self.description = description 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if components is not APIHelper.SKIP:
            self.components = components 
        if coupons is not APIHelper.SKIP:
            self.coupons = coupons 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        components = None
        if dictionary.get('components') is not None:
            components = [CreateOfferComponent.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        coupons = dictionary.get("coupons") if dictionary.get("coupons") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   handle,
                   description,
                   product_id,
                   product_price_point_id,
                   components,
                   coupons)
