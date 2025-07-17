# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class NetTerms(object):

    """Implementation of the 'Net Terms' model.

    Attributes:
        default_net_terms (int): The model property of type int.
        automatic_net_terms (int): The model property of type int.
        remittance_net_terms (int): The model property of type int.
        net_terms_on_remittance_signups_enabled (bool): The model property of
            type bool.
        custom_net_terms_enabled (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
        """Constructor for the NetTerms class"""

        # Initialize members of the class
        self.default_net_terms = default_net_terms 
        self.automatic_net_terms = automatic_net_terms 
        self.remittance_net_terms = remittance_net_terms 
        self.net_terms_on_remittance_signups_enabled = net_terms_on_remittance_signups_enabled 
        self.custom_net_terms_enabled = custom_net_terms_enabled 

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
        default_net_terms = dictionary.get("default_net_terms") if dictionary.get("default_net_terms") else 0
        automatic_net_terms = dictionary.get("automatic_net_terms") if dictionary.get("automatic_net_terms") else 0
        remittance_net_terms = dictionary.get("remittance_net_terms") if dictionary.get("remittance_net_terms") else 0
        net_terms_on_remittance_signups_enabled = dictionary.get("net_terms_on_remittance_signups_enabled") if dictionary.get("net_terms_on_remittance_signups_enabled") else False
        custom_net_terms_enabled = dictionary.get("custom_net_terms_enabled") if dictionary.get("custom_net_terms_enabled") else False
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(default_net_terms,
                   automatic_net_terms,
                   remittance_net_terms,
                   net_terms_on_remittance_signups_enabled,
                   custom_net_terms_enabled,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'default_net_terms={(self.default_net_terms if hasattr(self, "default_net_terms") else None)!r}, '
                f'automatic_net_terms={(self.automatic_net_terms if hasattr(self, "automatic_net_terms") else None)!r}, '
                f'remittance_net_terms={(self.remittance_net_terms if hasattr(self, "remittance_net_terms") else None)!r}, '
                f'net_terms_on_remittance_signups_enabled={(self.net_terms_on_remittance_signups_enabled if hasattr(self, "net_terms_on_remittance_signups_enabled") else None)!r}, '
                f'custom_net_terms_enabled={(self.custom_net_terms_enabled if hasattr(self, "custom_net_terms_enabled") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'default_net_terms={(self.default_net_terms if hasattr(self, "default_net_terms") else None)!s}, '
                f'automatic_net_terms={(self.automatic_net_terms if hasattr(self, "automatic_net_terms") else None)!s}, '
                f'remittance_net_terms={(self.remittance_net_terms if hasattr(self, "remittance_net_terms") else None)!s}, '
                f'net_terms_on_remittance_signups_enabled={(self.net_terms_on_remittance_signups_enabled if hasattr(self, "net_terms_on_remittance_signups_enabled") else None)!s}, '
                f'custom_net_terms_enabled={(self.custom_net_terms_enabled if hasattr(self, "custom_net_terms_enabled") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
