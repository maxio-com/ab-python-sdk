# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payer_attributes import PayerAttributes


class CustomerPayerChange(object):

    """Implementation of the 'Customer Payer Change' model.

    TODO: type model description here.

    Attributes:
        before (PayerAttributes): TODO: type description here.
        after (PayerAttributes): TODO: type description here.

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
        """Constructor for the CustomerPayerChange class"""

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
        before = PayerAttributes.from_dictionary(dictionary.get('before')) if 'before' in dictionary.keys() else APIHelper.SKIP
        after = PayerAttributes.from_dictionary(dictionary.get('after')) if 'after' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(before,
                   after)
