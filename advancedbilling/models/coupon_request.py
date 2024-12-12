# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.coupon_payload import CouponPayload


class CouponRequest(object):

    """Implementation of the 'Coupon Request' model.

    TODO: type model description here.

    Attributes:
        coupon (CouponPayload): TODO: type description here.
        restricted_products (Dict[str, bool]): An object where the keys are
            product_ids and the values are booleans indicating if the coupon
            should be applicable to the product
        restricted_components (Dict[str, bool]): An object where the keys are
            component_ids and the values are booleans indicating if the coupon
            should be applicable to the component
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "coupon": 'coupon',
        "restricted_products": 'restricted_products',
        "restricted_components": 'restricted_components'
    }

    _optionals = [
        'coupon',
        'restricted_products',
        'restricted_components',
    ]

    def __init__(self,
                 coupon=APIHelper.SKIP,
                 restricted_products=APIHelper.SKIP,
                 restricted_components=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CouponRequest class"""

        # Initialize members of the class
        if coupon is not APIHelper.SKIP:
            self.coupon = coupon 
        if restricted_products is not APIHelper.SKIP:
            self.restricted_products = restricted_products 
        if restricted_components is not APIHelper.SKIP:
            self.restricted_components = restricted_components 

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
        coupon = CouponPayload.from_dictionary(dictionary.get('coupon')) if 'coupon' in dictionary.keys() else APIHelper.SKIP
        restricted_products = dictionary.get("restricted_products") if "restricted_products" in dictionary.keys() else APIHelper.SKIP
        restricted_components = dictionary.get("restricted_components") if "restricted_components" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(coupon,
                   restricted_products,
                   restricted_components,
                   additional_properties)
