# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_payment_profile import CreatePaymentProfile


class CreatePaymentProfileRequest(object):

    """Implementation of the 'Create Payment Profile Request' model.

    TODO: type model description here.

    Attributes:
        payment_profile (CreatePaymentProfile): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_profile": 'payment_profile'
    }

    def __init__(self,
                 payment_profile=None,
                 additional_properties=None):
        """Constructor for the CreatePaymentProfileRequest class"""

        # Initialize members of the class
        self.payment_profile = payment_profile 

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
        payment_profile = CreatePaymentProfile.from_dictionary(dictionary.get('payment_profile')) if dictionary.get('payment_profile') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payment_profile,
                   additional_properties)
