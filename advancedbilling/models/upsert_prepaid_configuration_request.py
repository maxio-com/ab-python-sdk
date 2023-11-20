# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.upsert_prepaid_configuration import UpsertPrepaidConfiguration


class UpsertPrepaidConfigurationRequest(object):

    """Implementation of the 'Upsert Prepaid Configuration Request' model.

    TODO: type model description here.

    Attributes:
        prepaid_configuration (UpsertPrepaidConfiguration): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepaid_configuration": 'prepaid_configuration'
    }

    def __init__(self,
                 prepaid_configuration=None):
        """Constructor for the UpsertPrepaidConfigurationRequest class"""

        # Initialize members of the class
        self.prepaid_configuration = prepaid_configuration 

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
        prepaid_configuration = UpsertPrepaidConfiguration.from_dictionary(dictionary.get('prepaid_configuration')) if dictionary.get('prepaid_configuration') else None
        # Return an object of this model
        return cls(prepaid_configuration)
