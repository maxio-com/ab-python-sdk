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
        ip_address (str): Required when providing agreement acceptance
            params.
        terms_url (str): Required when creating a subscription with Maxio
            Payments. Either terms_url or provacy_policy_url required when
            providing agreement_acceptance params.
        privacy_policy_url (str): TODO: type description here.
        return_refund_policy_url (str): TODO: type description here.
        delivery_policy_url (str): TODO: type description here.
        secure_checkout_policy_url (str): TODO: type description here.

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
                 secure_checkout_policy_url=APIHelper.SKIP):
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
        ip_address = dictionary.get("ip_address") if dictionary.get("ip_address") else APIHelper.SKIP
        terms_url = dictionary.get("terms_url") if dictionary.get("terms_url") else APIHelper.SKIP
        privacy_policy_url = dictionary.get("privacy_policy_url") if dictionary.get("privacy_policy_url") else APIHelper.SKIP
        return_refund_policy_url = dictionary.get("return_refund_policy_url") if dictionary.get("return_refund_policy_url") else APIHelper.SKIP
        delivery_policy_url = dictionary.get("delivery_policy_url") if dictionary.get("delivery_policy_url") else APIHelper.SKIP
        secure_checkout_policy_url = dictionary.get("secure_checkout_policy_url") if dictionary.get("secure_checkout_policy_url") else APIHelper.SKIP
        # Return an object of this model
        return cls(ip_address,
                   terms_url,
                   privacy_policy_url,
                   return_refund_policy_url,
                   delivery_policy_url,
                   secure_checkout_policy_url)

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
