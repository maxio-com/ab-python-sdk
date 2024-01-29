# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.list_subcription_group_prepayment_item import ListSubcriptionGroupPrepaymentItem


class ListSubscriptionGroupPrepayment(object):

    """Implementation of the 'List Subscription Group Prepayment' model.

    TODO: type model description here.

    Attributes:
        prepayment (ListSubcriptionGroupPrepaymentItem): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepayment": 'prepayment'
    }

    def __init__(self,
                 prepayment=None):
        """Constructor for the ListSubscriptionGroupPrepayment class"""

        # Initialize members of the class
        self.prepayment = prepayment 

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
        prepayment = ListSubcriptionGroupPrepaymentItem.from_dictionary(dictionary.get('prepayment')) if dictionary.get('prepayment') else None
        # Return an object of this model
        return cls(prepayment)
