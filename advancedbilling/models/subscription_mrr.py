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

    Attributes:
        subscription_id (int): The model property of type int.
        mrr_amount_in_cents (int): The model property of type int.
        breakouts (SubscriptionMRRBreakout): The model property of type
            SubscriptionMRRBreakout.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 breakouts=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionMRR class"""

        # Initialize members of the class
        self.subscription_id = subscription_id 
        self.mrr_amount_in_cents = mrr_amount_in_cents 
        if breakouts is not APIHelper.SKIP:
            self.breakouts = breakouts 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        mrr_amount_in_cents = dictionary.get("mrr_amount_in_cents") if dictionary.get("mrr_amount_in_cents") else None
        breakouts = SubscriptionMRRBreakout.from_dictionary(dictionary.get('breakouts')) if 'breakouts' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscription_id,
                   mrr_amount_in_cents,
                   breakouts,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_id={self.subscription_id!r}, '
                f'mrr_amount_in_cents={self.mrr_amount_in_cents!r}, '
                f'breakouts={(self.breakouts if hasattr(self, "breakouts") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_id={self.subscription_id!s}, '
                f'mrr_amount_in_cents={self.mrr_amount_in_cents!s}, '
                f'breakouts={(self.breakouts if hasattr(self, "breakouts") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
