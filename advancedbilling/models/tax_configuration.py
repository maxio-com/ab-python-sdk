# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class TaxConfiguration(object):

    """Implementation of the 'Tax Configuration' model.

    TODO: type model description here.

    Attributes:
        kind (TaxConfigurationKind): TODO: type description here.
        destination_address (TaxDestinationAddress): TODO: type description
            here.
        fully_configured (bool): Returns `true` when Chargify has been
            properly configured to charge tax using the specified tax system.
            More details about taxes:
            https://maxio.zendesk.com/hc/en-us/articles/24287012608909-Taxes-Ov
            erview
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kind": 'kind',
        "destination_address": 'destination_address',
        "fully_configured": 'fully_configured'
    }

    _optionals = [
        'kind',
        'destination_address',
        'fully_configured',
    ]

    def __init__(self,
                 kind='custom',
                 destination_address=APIHelper.SKIP,
                 fully_configured=False,
                 additional_properties=None):
        """Constructor for the TaxConfiguration class"""

        # Initialize members of the class
        self.kind = kind 
        if destination_address is not APIHelper.SKIP:
            self.destination_address = destination_address 
        self.fully_configured = fully_configured 

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
        kind = dictionary.get("kind") if dictionary.get("kind") else 'custom'
        destination_address = dictionary.get("destination_address") if dictionary.get("destination_address") else APIHelper.SKIP
        fully_configured = dictionary.get("fully_configured") if dictionary.get("fully_configured") else False
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(kind,
                   destination_address,
                   fully_configured,
                   additional_properties)
