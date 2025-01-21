# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupItem(object):

    """Implementation of the 'Subscription Group Item' model.

    Attributes:
        id (int): The model property of type int.
        reference (str): The model property of type str.
        product_id (int): The model property of type int.
        product_handle (str): The model property of type str.
        product_price_point_id (int): The model property of type int.
        product_price_point_handle (str): The model property of type str.
        currency (str): The model property of type str.
        coupon_code (str): The model property of type str.
        total_revenue_in_cents (int): The model property of type int.
        balance_in_cents (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "reference": 'reference',
        "product_id": 'product_id',
        "product_handle": 'product_handle',
        "product_price_point_id": 'product_price_point_id',
        "product_price_point_handle": 'product_price_point_handle',
        "currency": 'currency',
        "coupon_code": 'coupon_code',
        "total_revenue_in_cents": 'total_revenue_in_cents',
        "balance_in_cents": 'balance_in_cents'
    }

    _optionals = [
        'id',
        'reference',
        'product_id',
        'product_handle',
        'product_price_point_id',
        'product_price_point_handle',
        'currency',
        'coupon_code',
        'total_revenue_in_cents',
        'balance_in_cents',
    ]

    _nullables = [
        'reference',
        'product_handle',
        'coupon_code',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_handle=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 product_price_point_handle=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 coupon_code=APIHelper.SKIP,
                 total_revenue_in_cents=APIHelper.SKIP,
                 balance_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupItem class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_handle is not APIHelper.SKIP:
            self.product_handle = product_handle 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if product_price_point_handle is not APIHelper.SKIP:
            self.product_price_point_handle = product_price_point_handle 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if coupon_code is not APIHelper.SKIP:
            self.coupon_code = coupon_code 
        if total_revenue_in_cents is not APIHelper.SKIP:
            self.total_revenue_in_cents = total_revenue_in_cents 
        if balance_in_cents is not APIHelper.SKIP:
            self.balance_in_cents = balance_in_cents 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        reference = dictionary.get("reference") if "reference" in dictionary.keys() else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_handle = dictionary.get("product_handle") if "product_handle" in dictionary.keys() else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        product_price_point_handle = dictionary.get("product_price_point_handle") if dictionary.get("product_price_point_handle") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        coupon_code = dictionary.get("coupon_code") if "coupon_code" in dictionary.keys() else APIHelper.SKIP
        total_revenue_in_cents = dictionary.get("total_revenue_in_cents") if dictionary.get("total_revenue_in_cents") else APIHelper.SKIP
        balance_in_cents = dictionary.get("balance_in_cents") if dictionary.get("balance_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   reference,
                   product_id,
                   product_handle,
                   product_price_point_id,
                   product_price_point_handle,
                   currency,
                   coupon_code,
                   total_revenue_in_cents,
                   balance_in_cents,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'reference={self.reference!r}, '
                f'product_id={self.product_id!r}, '
                f'product_handle={self.product_handle!r}, '
                f'product_price_point_id={self.product_price_point_id!r}, '
                f'product_price_point_handle={self.product_price_point_handle!r}, '
                f'currency={self.currency!r}, '
                f'coupon_code={self.coupon_code!r}, '
                f'total_revenue_in_cents={self.total_revenue_in_cents!r}, '
                f'balance_in_cents={self.balance_in_cents!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'reference={self.reference!s}, '
                f'product_id={self.product_id!s}, '
                f'product_handle={self.product_handle!s}, '
                f'product_price_point_id={self.product_price_point_id!s}, '
                f'product_price_point_handle={self.product_price_point_handle!s}, '
                f'currency={self.currency!s}, '
                f'coupon_code={self.coupon_code!s}, '
                f'total_revenue_in_cents={self.total_revenue_in_cents!s}, '
                f'balance_in_cents={self.balance_in_cents!s}, '
                f'additional_properties={self.additional_properties!s})')
