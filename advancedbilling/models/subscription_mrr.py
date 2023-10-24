# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_mrr_breakout import SubscriptionMRRBreakout


class SubscriptionMRR(object):

    """Implementation of the 'Subscription MRR' model.

    TODO: type model description here.

    Attributes:
        subscription_id (float): TODO: type description here.
        mrr_amount_in_cents (float): TODO: type description here.
        breakouts (SubscriptionMRRBreakout): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_id": 'subscription_id',
        "mrr_amount_in_cents": 'mrr_amount_in_cents',
        "breakouts": 'breakouts'
    }

    _optionals = [
        'breakouts',
    ]

    def __init__(self,
                 subscription_id=None,
                 mrr_amount_in_cents=None,
                 breakouts=APIHelper.SKIP):
        """Constructor for the SubscriptionMRR class"""

        # Initialize members of the class
        self.subscription_id = subscription_id 
        self.mrr_amount_in_cents = mrr_amount_in_cents 
        if breakouts is not APIHelper.SKIP:
            self.breakouts = breakouts 

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
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        mrr_amount_in_cents = dictionary.get("mrr_amount_in_cents") if dictionary.get("mrr_amount_in_cents") else None
        breakouts = SubscriptionMRRBreakout.from_dictionary(dictionary.get('breakouts')) if 'breakouts' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(subscription_id,
                   mrr_amount_in_cents,
                   breakouts)
