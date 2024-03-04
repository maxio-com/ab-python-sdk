# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ResumeOptions(object):

    """Implementation of the 'Resume Options' model.

    TODO: type model description here.

    Attributes:
        require_resume (bool): Chargify will only attempt to resume the
            subscription's billing period. If not resumable, the subscription
            will be left in it's current state.
        forgive_balance (bool): Indicates whether or not Chargify should clear
            the subscription's existing balance before attempting to resume
            the subscription. If subscription cannot be resumed, the balance
            will remain as it was before the attempt to resume was made.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "require_resume": 'require_resume',
        "forgive_balance": 'forgive_balance'
    }

    _optionals = [
        'require_resume',
        'forgive_balance',
    ]

    def __init__(self,
                 require_resume=APIHelper.SKIP,
                 forgive_balance=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ResumeOptions class"""

        # Initialize members of the class
        if require_resume is not APIHelper.SKIP:
            self.require_resume = require_resume 
        if forgive_balance is not APIHelper.SKIP:
            self.forgive_balance = forgive_balance 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        require_resume = dictionary.get("require_resume") if "require_resume" in dictionary.keys() else APIHelper.SKIP
        forgive_balance = dictionary.get("forgive_balance") if "forgive_balance" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(require_resume,
                   forgive_balance,
                   dictionary)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
