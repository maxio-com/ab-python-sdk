# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Breakouts(object):

    """Implementation of the 'Breakouts' model.

    TODO: type model description here.

    Attributes:
        plan_amount_in_cents (int): TODO: type description here.
        plan_amount_formatted (str): TODO: type description here.
        usage_amount_in_cents (int): TODO: type description here.
        usage_amount_formatted (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "plan_amount_in_cents": 'plan_amount_in_cents',
        "plan_amount_formatted": 'plan_amount_formatted',
        "usage_amount_in_cents": 'usage_amount_in_cents',
        "usage_amount_formatted": 'usage_amount_formatted'
    }

    _optionals = [
        'plan_amount_in_cents',
        'plan_amount_formatted',
        'usage_amount_in_cents',
        'usage_amount_formatted',
    ]

    def __init__(self,
                 plan_amount_in_cents=APIHelper.SKIP,
                 plan_amount_formatted=APIHelper.SKIP,
                 usage_amount_in_cents=APIHelper.SKIP,
                 usage_amount_formatted=APIHelper.SKIP):
        """Constructor for the Breakouts class"""

        # Initialize members of the class
        if plan_amount_in_cents is not APIHelper.SKIP:
            self.plan_amount_in_cents = plan_amount_in_cents 
        if plan_amount_formatted is not APIHelper.SKIP:
            self.plan_amount_formatted = plan_amount_formatted 
        if usage_amount_in_cents is not APIHelper.SKIP:
            self.usage_amount_in_cents = usage_amount_in_cents 
        if usage_amount_formatted is not APIHelper.SKIP:
            self.usage_amount_formatted = usage_amount_formatted 

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
        plan_amount_in_cents = dictionary.get("plan_amount_in_cents") if dictionary.get("plan_amount_in_cents") else APIHelper.SKIP
        plan_amount_formatted = dictionary.get("plan_amount_formatted") if dictionary.get("plan_amount_formatted") else APIHelper.SKIP
        usage_amount_in_cents = dictionary.get("usage_amount_in_cents") if dictionary.get("usage_amount_in_cents") else APIHelper.SKIP
        usage_amount_formatted = dictionary.get("usage_amount_formatted") if dictionary.get("usage_amount_formatted") else APIHelper.SKIP
        # Return an object of this model
        return cls(plan_amount_in_cents,
                   plan_amount_formatted,
                   usage_amount_in_cents,
                   usage_amount_formatted)
