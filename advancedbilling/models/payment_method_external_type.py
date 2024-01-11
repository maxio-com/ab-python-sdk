# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentMethodExternalType(object):

    """Implementation of the 'Payment Method External Type' model.

    TODO: type model description here.

    Attributes:
        details (str): TODO: type description here.
        kind (str): TODO: type description here.
        memo (str): TODO: type description here.
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "details": 'details',
        "kind": 'kind',
        "memo": 'memo',
        "mtype": 'type'
    }

    _optionals = [
        'details',
        'kind',
        'memo',
        'mtype',
    ]

    def __init__(self,
                 details=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 mtype='external'):
        """Constructor for the PaymentMethodExternalType class"""

        # Initialize members of the class
        if details is not APIHelper.SKIP:
            self.details = details 
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        self.mtype = mtype 

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
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'external'
        # Return an object of this model
        return cls(details,
                   kind,
                   memo,
                   mtype)

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
