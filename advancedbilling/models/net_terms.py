# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class NetTerms(object):

    """Implementation of the 'Net Terms' model.

    TODO: type model description here.

    Attributes:
        default_net_terms (int): TODO: type description here.
        automatic_net_terms (int): TODO: type description here.
        remittance_net_terms (int): TODO: type description here.
        net_terms_on_remittance_signups_enabled (bool): TODO: type description
            here.
        custom_net_terms_enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_net_terms": 'default_net_terms',
        "automatic_net_terms": 'automatic_net_terms',
        "remittance_net_terms": 'remittance_net_terms',
        "net_terms_on_remittance_signups_enabled": 'net_terms_on_remittance_signups_enabled',
        "custom_net_terms_enabled": 'custom_net_terms_enabled'
    }

    _optionals = [
        'default_net_terms',
        'automatic_net_terms',
        'remittance_net_terms',
        'net_terms_on_remittance_signups_enabled',
        'custom_net_terms_enabled',
    ]

    def __init__(self,
                 default_net_terms=0,
                 automatic_net_terms=0,
                 remittance_net_terms=0,
                 net_terms_on_remittance_signups_enabled=False,
                 custom_net_terms_enabled=False,
                 additional_properties={}):
        """Constructor for the NetTerms class"""

        # Initialize members of the class
        self.default_net_terms = default_net_terms 
        self.automatic_net_terms = automatic_net_terms 
        self.remittance_net_terms = remittance_net_terms 
        self.net_terms_on_remittance_signups_enabled = net_terms_on_remittance_signups_enabled 
        self.custom_net_terms_enabled = custom_net_terms_enabled 

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
        default_net_terms = dictionary.get("default_net_terms") if dictionary.get("default_net_terms") else 0
        automatic_net_terms = dictionary.get("automatic_net_terms") if dictionary.get("automatic_net_terms") else 0
        remittance_net_terms = dictionary.get("remittance_net_terms") if dictionary.get("remittance_net_terms") else 0
        net_terms_on_remittance_signups_enabled = dictionary.get("net_terms_on_remittance_signups_enabled") if dictionary.get("net_terms_on_remittance_signups_enabled") else False
        custom_net_terms_enabled = dictionary.get("custom_net_terms_enabled") if dictionary.get("custom_net_terms_enabled") else False
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(default_net_terms,
                   automatic_net_terms,
                   remittance_net_terms,
                   net_terms_on_remittance_signups_enabled,
                   custom_net_terms_enabled,
                   dictionary)
