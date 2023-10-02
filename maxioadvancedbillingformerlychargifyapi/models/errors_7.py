# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper


class Errors7(object):

    """Implementation of the 'Errors7' model.

    TODO: type model description here.

    Attributes:
        customer (object): TODO: type description here.
        payment_profile (object): TODO: type description here.
        subscriptions (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer": 'customer',
        "payment_profile": 'payment_profile',
        "subscriptions": 'subscriptions'
    }

    _optionals = [
        'customer',
        'payment_profile',
        'subscriptions',
    ]

    def __init__(self,
                 customer=APIHelper.SKIP,
                 payment_profile=APIHelper.SKIP,
                 subscriptions=APIHelper.SKIP):
        """Constructor for the Errors7 class"""

        # Initialize members of the class
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if payment_profile is not APIHelper.SKIP:
            self.payment_profile = payment_profile 
        if subscriptions is not APIHelper.SKIP:
            self.subscriptions = subscriptions 

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
        customer = dictionary.get("customer") if dictionary.get("customer") else APIHelper.SKIP
        payment_profile = dictionary.get("payment_profile") if dictionary.get("payment_profile") else APIHelper.SKIP
        subscriptions = dictionary.get("subscriptions") if dictionary.get("subscriptions") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer,
                   payment_profile,
                   subscriptions)