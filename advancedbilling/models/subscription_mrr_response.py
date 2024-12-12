# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.subscription_mrr import SubscriptionMRR


class SubscriptionMRRResponse(object):

    """Implementation of the 'Subscription MRR Response' model.

    TODO: type model description here.

    Attributes:
        subscriptions_mrr (List[SubscriptionMRR]): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscriptions_mrr": 'subscriptions_mrr'
    }

    def __init__(self,
                 subscriptions_mrr=None,
                 additional_properties=None):
        """Constructor for the SubscriptionMRRResponse class"""

        # Initialize members of the class
        self.subscriptions_mrr = subscriptions_mrr 

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
        subscriptions_mrr = None
        if dictionary.get('subscriptions_mrr') is not None:
            subscriptions_mrr = [SubscriptionMRR.from_dictionary(x) for x in dictionary.get('subscriptions_mrr')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscriptions_mrr,
                   additional_properties)
