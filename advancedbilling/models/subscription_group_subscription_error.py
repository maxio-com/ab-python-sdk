# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupSubscriptionError(object):

    """Implementation of the 'Subscription Group Subscription Error' model.

    Object which contains subscription errors.

    Attributes:
        product (List[str]): TODO: type description here.
        product_price_point_id (List[str]): TODO: type description here.
        payment_profile (List[str]): TODO: type description here.
        payment_profile_chargify_token (List[str]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product": 'product',
        "product_price_point_id": 'product_price_point_id',
        "payment_profile": 'payment_profile',
        "payment_profile_chargify_token": 'payment_profile.chargify_token'
    }

    _optionals = [
        'product',
        'product_price_point_id',
        'payment_profile',
        'payment_profile_chargify_token',
    ]

    def __init__(self,
                 product=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 payment_profile=APIHelper.SKIP,
                 payment_profile_chargify_token=APIHelper.SKIP):
        """Constructor for the SubscriptionGroupSubscriptionError class"""

        # Initialize members of the class
        if product is not APIHelper.SKIP:
            self.product = product 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if payment_profile is not APIHelper.SKIP:
            self.payment_profile = payment_profile 
        if payment_profile_chargify_token is not APIHelper.SKIP:
            self.payment_profile_chargify_token = payment_profile_chargify_token 

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
        product = dictionary.get("product") if dictionary.get("product") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        payment_profile = dictionary.get("payment_profile") if dictionary.get("payment_profile") else APIHelper.SKIP
        payment_profile_chargify_token = dictionary.get("payment_profile.chargify_token") if dictionary.get("payment_profile.chargify_token") else APIHelper.SKIP
        # Return an object of this model
        return cls(product,
                   product_price_point_id,
                   payment_profile,
                   payment_profile_chargify_token)
