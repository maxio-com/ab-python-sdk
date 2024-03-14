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
        base (List[str]): TODO: type description here.
        payment_profile_expiration_month (List[str]): TODO: type description
            here.
        payment_profile_expiration_year (List[str]): TODO: type description
            here.
        payment_profile_full_number (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product": 'product',
        "product_price_point_id": 'product_price_point_id',
        "payment_profile": 'payment_profile',
        "payment_profile_chargify_token": 'payment_profile.chargify_token',
        "base": 'base',
        "payment_profile_expiration_month": 'payment_profile.expiration_month',
        "payment_profile_expiration_year": 'payment_profile.expiration_year',
        "payment_profile_full_number": 'payment_profile.full_number'
    }

    _optionals = [
        'product',
        'product_price_point_id',
        'payment_profile',
        'payment_profile_chargify_token',
        'base',
        'payment_profile_expiration_month',
        'payment_profile_expiration_year',
        'payment_profile_full_number',
    ]

    def __init__(self,
                 product=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 payment_profile=APIHelper.SKIP,
                 payment_profile_chargify_token=APIHelper.SKIP,
                 base=APIHelper.SKIP,
                 payment_profile_expiration_month=APIHelper.SKIP,
                 payment_profile_expiration_year=APIHelper.SKIP,
                 payment_profile_full_number=APIHelper.SKIP,
                 additional_properties={}):
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
        if base is not APIHelper.SKIP:
            self.base = base 
        if payment_profile_expiration_month is not APIHelper.SKIP:
            self.payment_profile_expiration_month = payment_profile_expiration_month 
        if payment_profile_expiration_year is not APIHelper.SKIP:
            self.payment_profile_expiration_year = payment_profile_expiration_year 
        if payment_profile_full_number is not APIHelper.SKIP:
            self.payment_profile_full_number = payment_profile_full_number 

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        product = dictionary.get("product") if dictionary.get("product") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        payment_profile = dictionary.get("payment_profile") if dictionary.get("payment_profile") else APIHelper.SKIP
        payment_profile_chargify_token = dictionary.get("payment_profile.chargify_token") if dictionary.get("payment_profile.chargify_token") else APIHelper.SKIP
        base = dictionary.get("base") if dictionary.get("base") else APIHelper.SKIP
        payment_profile_expiration_month = dictionary.get("payment_profile.expiration_month") if dictionary.get("payment_profile.expiration_month") else APIHelper.SKIP
        payment_profile_expiration_year = dictionary.get("payment_profile.expiration_year") if dictionary.get("payment_profile.expiration_year") else APIHelper.SKIP
        payment_profile_full_number = dictionary.get("payment_profile.full_number") if dictionary.get("payment_profile.full_number") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(product,
                   product_price_point_id,
                   payment_profile,
                   payment_profile_chargify_token,
                   base,
                   payment_profile_expiration_month,
                   payment_profile_expiration_year,
                   payment_profile_full_number,
                   dictionary)
