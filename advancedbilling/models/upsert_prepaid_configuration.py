# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpsertPrepaidConfiguration(object):

    """Implementation of the 'Upsert Prepaid Configuration' model.

    TODO: type model description here.

    Attributes:
        initial_funding_amount_in_cents (long|int): TODO: type description
            here.
        replenish_to_amount_in_cents (long|int): TODO: type description here.
        auto_replenish (bool): TODO: type description here.
        replenish_threshold_amount_in_cents (long|int): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "initial_funding_amount_in_cents": 'initial_funding_amount_in_cents',
        "replenish_to_amount_in_cents": 'replenish_to_amount_in_cents',
        "auto_replenish": 'auto_replenish',
        "replenish_threshold_amount_in_cents": 'replenish_threshold_amount_in_cents'
    }

    _optionals = [
        'initial_funding_amount_in_cents',
        'replenish_to_amount_in_cents',
        'auto_replenish',
        'replenish_threshold_amount_in_cents',
    ]

    def __init__(self,
                 initial_funding_amount_in_cents=APIHelper.SKIP,
                 replenish_to_amount_in_cents=APIHelper.SKIP,
                 auto_replenish=APIHelper.SKIP,
                 replenish_threshold_amount_in_cents=APIHelper.SKIP):
        """Constructor for the UpsertPrepaidConfiguration class"""

        # Initialize members of the class
        if initial_funding_amount_in_cents is not APIHelper.SKIP:
            self.initial_funding_amount_in_cents = initial_funding_amount_in_cents 
        if replenish_to_amount_in_cents is not APIHelper.SKIP:
            self.replenish_to_amount_in_cents = replenish_to_amount_in_cents 
        if auto_replenish is not APIHelper.SKIP:
            self.auto_replenish = auto_replenish 
        if replenish_threshold_amount_in_cents is not APIHelper.SKIP:
            self.replenish_threshold_amount_in_cents = replenish_threshold_amount_in_cents 

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
        initial_funding_amount_in_cents = dictionary.get("initial_funding_amount_in_cents") if dictionary.get("initial_funding_amount_in_cents") else APIHelper.SKIP
        replenish_to_amount_in_cents = dictionary.get("replenish_to_amount_in_cents") if dictionary.get("replenish_to_amount_in_cents") else APIHelper.SKIP
        auto_replenish = dictionary.get("auto_replenish") if "auto_replenish" in dictionary.keys() else APIHelper.SKIP
        replenish_threshold_amount_in_cents = dictionary.get("replenish_threshold_amount_in_cents") if dictionary.get("replenish_threshold_amount_in_cents") else APIHelper.SKIP
        # Return an object of this model
        return cls(initial_funding_amount_in_cents,
                   replenish_to_amount_in_cents,
                   auto_replenish,
                   replenish_threshold_amount_in_cents)
