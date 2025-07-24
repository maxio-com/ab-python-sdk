# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AgreementAcceptance(object):

    """Implementation of the 'Agreement Acceptance' model.

    Required when creating a subscription with Maxio Payments.

    Attributes:
        ip_address (str): Required when providing agreement acceptance params.
        terms_url (str): Required when creating a subscription with Maxio
            Payments. Either terms_url or provacy_policy_url required when
            providing agreement_acceptance params.
        privacy_policy_url (str): The model property of type str.
        return_refund_policy_url (str): The model property of type str.
        delivery_policy_url (str): The model property of type str.
        secure_checkout_policy_url (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip_address": 'ip_address',
        "terms_url": 'terms_url',
        "privacy_policy_url": 'privacy_policy_url',
        "return_refund_policy_url": 'return_refund_policy_url',
        "delivery_policy_url": 'delivery_policy_url',
        "secure_checkout_policy_url": 'secure_checkout_policy_url'
    }

    _optionals = [
        'ip_address',
        'terms_url',
        'privacy_policy_url',
        'return_refund_policy_url',
        'delivery_policy_url',
        'secure_checkout_policy_url',
    ]

    def __init__(self,
                 ip_address=APIHelper.SKIP,
                 terms_url=APIHelper.SKIP,
                 privacy_policy_url=APIHelper.SKIP,
                 return_refund_policy_url=APIHelper.SKIP,
                 delivery_policy_url=APIHelper.SKIP,
                 secure_checkout_policy_url=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the AgreementAcceptance class"""

        # Initialize members of the class
        if ip_address is not APIHelper.SKIP:
            self.ip_address = ip_address 
        if terms_url is not APIHelper.SKIP:
            self.terms_url = terms_url 
        if privacy_policy_url is not APIHelper.SKIP:
            self.privacy_policy_url = privacy_policy_url 
        if return_refund_policy_url is not APIHelper.SKIP:
            self.return_refund_policy_url = return_refund_policy_url 
        if delivery_policy_url is not APIHelper.SKIP:
            self.delivery_policy_url = delivery_policy_url 
        if secure_checkout_policy_url is not APIHelper.SKIP:
            self.secure_checkout_policy_url = secure_checkout_policy_url 

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
        ip_address = dictionary.get("ip_address") if dictionary.get("ip_address") else APIHelper.SKIP
        terms_url = dictionary.get("terms_url") if dictionary.get("terms_url") else APIHelper.SKIP
        privacy_policy_url = dictionary.get("privacy_policy_url") if dictionary.get("privacy_policy_url") else APIHelper.SKIP
        return_refund_policy_url = dictionary.get("return_refund_policy_url") if dictionary.get("return_refund_policy_url") else APIHelper.SKIP
        delivery_policy_url = dictionary.get("delivery_policy_url") if dictionary.get("delivery_policy_url") else APIHelper.SKIP
        secure_checkout_policy_url = dictionary.get("secure_checkout_policy_url") if dictionary.get("secure_checkout_policy_url") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(ip_address,
                   terms_url,
                   privacy_policy_url,
                   return_refund_policy_url,
                   delivery_policy_url,
                   secure_checkout_policy_url,
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

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'ip_address={(self.ip_address if hasattr(self, "ip_address") else None)!r}, '
                f'terms_url={(self.terms_url if hasattr(self, "terms_url") else None)!r}, '
                f'privacy_policy_url={(self.privacy_policy_url if hasattr(self, "privacy_policy_url") else None)!r}, '
                f'return_refund_policy_url={(self.return_refund_policy_url if hasattr(self, "return_refund_policy_url") else None)!r}, '
                f'delivery_policy_url={(self.delivery_policy_url if hasattr(self, "delivery_policy_url") else None)!r}, '
                f'secure_checkout_policy_url={(self.secure_checkout_policy_url if hasattr(self, "secure_checkout_policy_url") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'ip_address={(self.ip_address if hasattr(self, "ip_address") else None)!s}, '
                f'terms_url={(self.terms_url if hasattr(self, "terms_url") else None)!s}, '
                f'privacy_policy_url={(self.privacy_policy_url if hasattr(self, "privacy_policy_url") else None)!s}, '
                f'return_refund_policy_url={(self.return_refund_policy_url if hasattr(self, "return_refund_policy_url") else None)!s}, '
                f'delivery_policy_url={(self.delivery_policy_url if hasattr(self, "delivery_policy_url") else None)!s}, '
                f'secure_checkout_policy_url={(self.secure_checkout_policy_url if hasattr(self, "secure_checkout_policy_url") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
