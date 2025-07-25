# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ACHAgreement(object):

    """Implementation of the 'ACH Agreement' model.

    (Optional) If passed, the proof of the authorized ACH agreement terms will
    be persisted.

    Attributes:
        agreement_terms (str): (Required when providing ACH agreement params)
            The ACH authorization agreement terms.
        authorizer_first_name (str): (Required when providing ACH agreement
            params) The first name of the person authorizing the ACH agreement.
        authorizer_last_name (str): (Required when providing ACH agreement
            params) The last name of the person authorizing the ACH agreement.
        ip_address (str): (Required when providing ACH agreement params) The
            IP address of the person authorizing the ACH agreement.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agreement_terms": 'agreement_terms',
        "authorizer_first_name": 'authorizer_first_name',
        "authorizer_last_name": 'authorizer_last_name',
        "ip_address": 'ip_address'
    }

    _optionals = [
        'agreement_terms',
        'authorizer_first_name',
        'authorizer_last_name',
        'ip_address',
    ]

    def __init__(self,
                 agreement_terms=APIHelper.SKIP,
                 authorizer_first_name=APIHelper.SKIP,
                 authorizer_last_name=APIHelper.SKIP,
                 ip_address=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ACHAgreement class"""

        # Initialize members of the class
        if agreement_terms is not APIHelper.SKIP:
            self.agreement_terms = agreement_terms 
        if authorizer_first_name is not APIHelper.SKIP:
            self.authorizer_first_name = authorizer_first_name 
        if authorizer_last_name is not APIHelper.SKIP:
            self.authorizer_last_name = authorizer_last_name 
        if ip_address is not APIHelper.SKIP:
            self.ip_address = ip_address 

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
        agreement_terms = dictionary.get("agreement_terms") if dictionary.get("agreement_terms") else APIHelper.SKIP
        authorizer_first_name = dictionary.get("authorizer_first_name") if dictionary.get("authorizer_first_name") else APIHelper.SKIP
        authorizer_last_name = dictionary.get("authorizer_last_name") if dictionary.get("authorizer_last_name") else APIHelper.SKIP
        ip_address = dictionary.get("ip_address") if dictionary.get("ip_address") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(agreement_terms,
                   authorizer_first_name,
                   authorizer_last_name,
                   ip_address,
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
                f'agreement_terms={(self.agreement_terms if hasattr(self, "agreement_terms") else None)!r}, '
                f'authorizer_first_name={(self.authorizer_first_name if hasattr(self, "authorizer_first_name") else None)!r}, '
                f'authorizer_last_name={(self.authorizer_last_name if hasattr(self, "authorizer_last_name") else None)!r}, '
                f'ip_address={(self.ip_address if hasattr(self, "ip_address") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'agreement_terms={(self.agreement_terms if hasattr(self, "agreement_terms") else None)!s}, '
                f'authorizer_first_name={(self.authorizer_first_name if hasattr(self, "authorizer_first_name") else None)!s}, '
                f'authorizer_last_name={(self.authorizer_last_name if hasattr(self, "authorizer_last_name") else None)!s}, '
                f'ip_address={(self.ip_address if hasattr(self, "ip_address") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
