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

    def __init__(self,
                 details=None,
                 kind=None,
                 memo=None,
                 mtype='external'):
        """Constructor for the PaymentMethodExternalType class"""

        # Initialize members of the class
        self.details = details 
        self.kind = kind 
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
        details = dictionary.get("details") if dictionary.get("details") else None
        kind = dictionary.get("kind") if dictionary.get("kind") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
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
            return APIHelper.is_valid_type(value=dictionary.details, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.kind, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.memo, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.mtype, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('details'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('kind'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('type'), type_callable=lambda value: isinstance(value, str))
