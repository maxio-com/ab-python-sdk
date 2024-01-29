# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ActivateSubscriptionRequest(object):

    """Implementation of the 'Activate Subscription Request' model.

    TODO: type model description here.

    Attributes:
        revert_on_failure (bool): You may choose how to handle the activation
            failure. `true` means do not change the subscription’s state and
            billing period. `false`  means to continue through with the
            activation and enter an end of life state. If this parameter is
            omitted or `null` is passed it will default to value set in the 
            site settings (default: `true`)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "revert_on_failure": 'revert_on_failure'
    }

    _optionals = [
        'revert_on_failure',
    ]

    _nullables = [
        'revert_on_failure',
    ]

    def __init__(self,
                 revert_on_failure=APIHelper.SKIP):
        """Constructor for the ActivateSubscriptionRequest class"""

        # Initialize members of the class
        if revert_on_failure is not APIHelper.SKIP:
            self.revert_on_failure = revert_on_failure 

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
        revert_on_failure = dictionary.get("revert_on_failure") if "revert_on_failure" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(revert_on_failure)
