# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.subscription_group_prepayment import SubscriptionGroupPrepayment


class SubscriptionGroupPrepaymentRequest(object):

    """Implementation of the 'Subscription Group Prepayment Request' model.

    TODO: type model description here.

    Attributes:
        prepayment (SubscriptionGroupPrepayment): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepayment": 'prepayment'
    }

    def __init__(self,
                 prepayment=None,
                 additional_properties={}):
        """Constructor for the SubscriptionGroupPrepaymentRequest class"""

        # Initialize members of the class
        self.prepayment = prepayment 

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
        prepayment = SubscriptionGroupPrepayment.from_dictionary(dictionary.get('prepayment')) if dictionary.get('prepayment') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(prepayment,
                   dictionary)
