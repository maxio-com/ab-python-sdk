# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentProfileResponse(object):

    """Implementation of the 'Payment Profile Response' model.

    Attributes:
        payment_profile (ApplePayPaymentProfile | BankAccountPaymentProfile |
            CreditCardPaymentProfile | PaypalPaymentProfile): The model
            property of type ApplePayPaymentProfile |
            BankAccountPaymentProfile | CreditCardPaymentProfile |
            PaypalPaymentProfile.
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
        """Constructor for the PaymentProfileResponse class"""

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        payment_profile = APIHelper.deserialize_union_type(UnionTypeLookUp.get('Payment-Profile'), dictionary.get('payment_profile'), False) if dictionary.get('payment_profile') is not None else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payment_profile,
                   additional_properties)

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('Payment-Profile').validate(dictionary.payment_profile).is_valid

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('Payment-Profile').validate(dictionary.get('payment_profile')).is_valid

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'payment_profile={self.payment_profile!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'payment_profile={self.payment_profile!s}, '
                f'additional_properties={self.additional_properties!s})')
