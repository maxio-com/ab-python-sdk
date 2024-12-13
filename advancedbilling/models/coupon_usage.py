# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CouponUsage(object):

    """Implementation of the 'Coupon Usage' model.

    TODO: type model description here.

    Attributes:
        id (int): The Chargify id of the product
        name (str): Name of the product
        signups (int): Number of times the coupon has been applied
        savings (int): Dollar amount of customer savings as a result of the
            coupon.
        savings_in_cents (long|int): Dollar amount of customer savings as a
            result of the coupon.
        revenue (int): Total revenue of the all subscriptions that have
            received a discount from this coupon.
        revenue_in_cents (long|int): Total revenue of the all subscriptions
            that have received a discount from this coupon.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "signups": 'signups',
        "savings": 'savings',
        "savings_in_cents": 'savings_in_cents',
        "revenue": 'revenue',
        "revenue_in_cents": 'revenue_in_cents'
    }

    _optionals = [
        'id',
        'name',
        'signups',
        'savings',
        'savings_in_cents',
        'revenue',
        'revenue_in_cents',
    ]

    _nullables = [
        'savings',
        'savings_in_cents',
        'revenue',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 signups=APIHelper.SKIP,
                 savings=APIHelper.SKIP,
                 savings_in_cents=APIHelper.SKIP,
                 revenue=APIHelper.SKIP,
                 revenue_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CouponUsage class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if signups is not APIHelper.SKIP:
            self.signups = signups 
        if savings is not APIHelper.SKIP:
            self.savings = savings 
        if savings_in_cents is not APIHelper.SKIP:
            self.savings_in_cents = savings_in_cents 
        if revenue is not APIHelper.SKIP:
            self.revenue = revenue 
        if revenue_in_cents is not APIHelper.SKIP:
            self.revenue_in_cents = revenue_in_cents 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        signups = dictionary.get("signups") if dictionary.get("signups") else APIHelper.SKIP
        savings = dictionary.get("savings") if "savings" in dictionary.keys() else APIHelper.SKIP
        savings_in_cents = dictionary.get("savings_in_cents") if "savings_in_cents" in dictionary.keys() else APIHelper.SKIP
        revenue = dictionary.get("revenue") if "revenue" in dictionary.keys() else APIHelper.SKIP
        revenue_in_cents = dictionary.get("revenue_in_cents") if dictionary.get("revenue_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   signups,
                   savings,
                   savings_in_cents,
                   revenue,
                   revenue_in_cents,
                   additional_properties)
