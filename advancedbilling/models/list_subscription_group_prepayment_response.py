# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.list_subscription_group_prepayment import ListSubscriptionGroupPrepayment


class ListSubscriptionGroupPrepaymentResponse(object):

    """Implementation of the 'List Subscription Group Prepayment Response' model.

    TODO: type model description here.

    Attributes:
        prepayments (List[ListSubscriptionGroupPrepayment]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepayments": 'prepayments'
    }

    def __init__(self,
                 prepayments=None,
                 additional_properties={}):
        """Constructor for the ListSubscriptionGroupPrepaymentResponse class"""

        # Initialize members of the class
        self.prepayments = prepayments 

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
        prepayments = None
        if dictionary.get('prepayments') is not None:
            prepayments = [ListSubscriptionGroupPrepayment.from_dictionary(x) for x in dictionary.get('prepayments')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(prepayments,
                   dictionary)
