# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CustomerBillingAddressChange(object):

    """Implementation of the 'Customer Billing Address Change' model.

    TODO: type model description here.

    Attributes:
        before (object): TODO: type description here.
        after (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before": 'before',
        "after": 'after'
    }

    _optionals = [
        'before',
        'after',
    ]

    def __init__(self,
                 before=APIHelper.SKIP,
                 after=APIHelper.SKIP):
        """Constructor for the CustomerBillingAddressChange class"""

        # Initialize members of the class
        if before is not APIHelper.SKIP:
            self.before = before 
        if after is not APIHelper.SKIP:
            self.after = after 

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
        before = dictionary.get("before") if dictionary.get("before") else APIHelper.SKIP
        after = dictionary.get("after") if dictionary.get("after") else APIHelper.SKIP
        # Return an object of this model
        return cls(before,
                   after)
