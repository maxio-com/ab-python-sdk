# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ActivateSubscriptionRequest(object):

    """Implementation of the 'Activate Subscription Request' model.

    Attributes:
        revert_on_failure (bool): You may choose how to handle the activation
            failure. `true` means do not change the subscription’s state and
            billing period. `false`  means to continue through with the
            activation and enter an end of life state. If this parameter is
            omitted or `null` is passed it will default to value set in the 
            site settings (default: `true`)
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 revert_on_failure=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ActivateSubscriptionRequest class"""

        # Initialize members of the class
        if revert_on_failure is not APIHelper.SKIP:
            self.revert_on_failure = revert_on_failure 

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
        revert_on_failure = dictionary.get("revert_on_failure") if "revert_on_failure" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(revert_on_failure,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'revert_on_failure={self.revert_on_failure!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'revert_on_failure={self.revert_on_failure!s}, '
                f'additional_properties={self.additional_properties!s})')
