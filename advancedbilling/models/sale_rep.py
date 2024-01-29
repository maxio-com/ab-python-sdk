# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.sale_rep_subscription import SaleRepSubscription


class SaleRep(object):

    """Implementation of the 'Sale Rep' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        full_name (str): TODO: type description here.
        subscriptions_count (int): TODO: type description here.
        test_mode (bool): TODO: type description here.
        subscriptions (List[SaleRepSubscription]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "full_name": 'full_name',
        "subscriptions_count": 'subscriptions_count',
        "test_mode": 'test_mode',
        "subscriptions": 'subscriptions'
    }

    _optionals = [
        'id',
        'full_name',
        'subscriptions_count',
        'test_mode',
        'subscriptions',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 full_name=APIHelper.SKIP,
                 subscriptions_count=APIHelper.SKIP,
                 test_mode=APIHelper.SKIP,
                 subscriptions=APIHelper.SKIP):
        """Constructor for the SaleRep class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if full_name is not APIHelper.SKIP:
            self.full_name = full_name 
        if subscriptions_count is not APIHelper.SKIP:
            self.subscriptions_count = subscriptions_count 
        if test_mode is not APIHelper.SKIP:
            self.test_mode = test_mode 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        full_name = dictionary.get("full_name") if dictionary.get("full_name") else APIHelper.SKIP
        subscriptions_count = dictionary.get("subscriptions_count") if dictionary.get("subscriptions_count") else APIHelper.SKIP
        test_mode = dictionary.get("test_mode") if "test_mode" in dictionary.keys() else APIHelper.SKIP
        subscriptions = None
        if dictionary.get('subscriptions') is not None:
            subscriptions = [SaleRepSubscription.from_dictionary(x) for x in dictionary.get('subscriptions')]
        else:
            subscriptions = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   full_name,
                   subscriptions_count,
                   test_mode,
                   subscriptions)
