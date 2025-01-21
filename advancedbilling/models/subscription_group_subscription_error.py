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
        product (List[str]): The model property of type List[str].
        product_price_point_id (List[str]): The model property of type
            List[str].
        payment_profile (List[str]): The model property of type List[str].
        payment_profile_chargify_token (List[str]): The model property of type
            List[str].
        base (List[str]): The model property of type List[str].
        payment_profile_expiration_month (List[str]): The model property of
            type List[str].
        payment_profile_expiration_year (List[str]): The model property of
            type List[str].
        payment_profile_full_number (List[str]): The model property of type
            List[str].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        product = dictionary.get("product") if dictionary.get("product") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        payment_profile = dictionary.get("payment_profile") if dictionary.get("payment_profile") else APIHelper.SKIP
        payment_profile_chargify_token = dictionary.get("payment_profile.chargify_token") if dictionary.get("payment_profile.chargify_token") else APIHelper.SKIP
        base = dictionary.get("base") if dictionary.get("base") else APIHelper.SKIP
        payment_profile_expiration_month = dictionary.get("payment_profile.expiration_month") if dictionary.get("payment_profile.expiration_month") else APIHelper.SKIP
        payment_profile_expiration_year = dictionary.get("payment_profile.expiration_year") if dictionary.get("payment_profile.expiration_year") else APIHelper.SKIP
        payment_profile_full_number = dictionary.get("payment_profile.full_number") if dictionary.get("payment_profile.full_number") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(product,
                   product_price_point_id,
                   payment_profile,
                   payment_profile_chargify_token,
                   base,
                   payment_profile_expiration_month,
                   payment_profile_expiration_year,
                   payment_profile_full_number,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product={self.product!r}, '
                f'product_price_point_id={self.product_price_point_id!r}, '
                f'payment_profile={self.payment_profile!r}, '
                f'payment_profile_chargify_token={self.payment_profile_chargify_token!r}, '
                f'base={self.base!r}, '
                f'payment_profile_expiration_month={self.payment_profile_expiration_month!r}, '
                f'payment_profile_expiration_year={self.payment_profile_expiration_year!r}, '
                f'payment_profile_full_number={self.payment_profile_full_number!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product={self.product!s}, '
                f'product_price_point_id={self.product_price_point_id!s}, '
                f'payment_profile={self.payment_profile!s}, '
                f'payment_profile_chargify_token={self.payment_profile_chargify_token!s}, '
                f'base={self.base!s}, '
                f'payment_profile_expiration_month={self.payment_profile_expiration_month!s}, '
                f'payment_profile_expiration_year={self.payment_profile_expiration_year!s}, '
                f'payment_profile_full_number={self.payment_profile_full_number!s}, '
                f'additional_properties={self.additional_properties!s})')
