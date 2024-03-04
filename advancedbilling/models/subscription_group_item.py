# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupItem(object):

    """Implementation of the 'Subscription Group Item' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        reference (str): TODO: type description here.
        product_id (int): TODO: type description here.
        product_handle (str): TODO: type description here.
        product_price_point_id (int): TODO: type description here.
        product_price_point_handle (str): TODO: type description here.
        currency (str): TODO: type description here.
        coupon_code (str): TODO: type description here.
        total_revenue_in_cents (long|int): TODO: type description here.
        balance_in_cents (long|int): TODO: type description here.

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
                 additional_properties={}):
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
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
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
                   dictionary)
