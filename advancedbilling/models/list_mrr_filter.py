# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListMrrFilter(object):

    """Implementation of the 'List Mrr Filter' model.

    TODO: type model description here.

    Attributes:
        subscription_ids (List[int]): Submit ids in order to limit results.
            Use in query: `filter[subscription_ids]=1,2,3`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_ids": 'subscription_ids'
    }

    _optionals = [
        'subscription_ids',
    ]

    def __init__(self,
                 subscription_ids=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListMrrFilter class"""

        # Initialize members of the class
        if subscription_ids is not APIHelper.SKIP:
            self.subscription_ids = subscription_ids 

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
        subscription_ids = dictionary.get("subscription_ids") if dictionary.get("subscription_ids") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(subscription_ids,
                   dictionary)
