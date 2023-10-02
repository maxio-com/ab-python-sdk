# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper
from maxioadvancedbillingformerlychargifyapi.models.subscription_1 import Subscription1


class Errors18(object):

    """Implementation of the 'Errors18' model.

    TODO: type model description here.

    Attributes:
        subscription (Subscription1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription": 'subscription'
    }

    _optionals = [
        'subscription',
    ]

    def __init__(self,
                 subscription=APIHelper.SKIP):
        """Constructor for the Errors18 class"""

        # Initialize members of the class
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 

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
        subscription = Subscription1.from_dictionary(dictionary.get('subscription')) if 'subscription' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(subscription)