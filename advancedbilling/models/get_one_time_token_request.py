# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.get_one_time_token_payment_profile import GetOneTimeTokenPaymentProfile


class GetOneTimeTokenRequest(object):

    """Implementation of the 'Get One Time Token Request' model.

    Attributes:
        payment_profile (GetOneTimeTokenPaymentProfile): The model property of
            type GetOneTimeTokenPaymentProfile.
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
        """Constructor for the GetOneTimeTokenRequest class"""

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
        payment_profile = GetOneTimeTokenPaymentProfile.from_dictionary(dictionary.get('payment_profile')) if dictionary.get('payment_profile') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payment_profile,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'payment_profile={self.payment_profile!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'payment_profile={self.payment_profile!s}, '
                f'additional_properties={self.additional_properties!s})')
