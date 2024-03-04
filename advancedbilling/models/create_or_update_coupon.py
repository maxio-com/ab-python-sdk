# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateOrUpdateCoupon(object):

    """Implementation of the 'Create or Update Coupon' model.

    TODO: type model description here.

    Attributes:
        coupon (CreateOrUpdatePercentageCoupon |
            CreateOrUpdateFlatAmountCoupon | None): TODO: type description
            here.
        restricted_products (Dict[str, bool]): An object where the keys are
            product_ids and the values are booleans indicating if the coupon
            should be applicable to the product
        restricted_components (Dict[str, bool]): An object where the keys are
            component_ids and the values are booleans indicating if the coupon
            should be applicable to the component

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
                 additional_properties={}):
        """Constructor for the CreateOrUpdateCoupon class"""

        # Initialize members of the class
        if coupon is not APIHelper.SKIP:
            self.coupon = coupon 
        if restricted_products is not APIHelper.SKIP:
            self.restricted_products = restricted_products 
        if restricted_components is not APIHelper.SKIP:
            self.restricted_components = restricted_components 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        coupon = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateOrUpdateCouponCoupon'), dictionary.get('coupon'), False) if dictionary.get('coupon') is not None else APIHelper.SKIP
        restricted_products = dictionary.get("restricted_products") if "restricted_products" in dictionary.keys() else APIHelper.SKIP
        restricted_components = dictionary.get("restricted_components") if "restricted_components" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(coupon,
                   restricted_products,
                   restricted_components,
                   dictionary)
