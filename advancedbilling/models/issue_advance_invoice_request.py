# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class IssueAdvanceInvoiceRequest(object):

    """Implementation of the 'Issue Advance Invoice Request' model.

    Attributes:
        force (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "force": 'force'
    }

    _optionals = [
        'force',
    ]

    def __init__(self,
                 force=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the IssueAdvanceInvoiceRequest class"""

        # Initialize members of the class
        if force is not APIHelper.SKIP:
            self.force = force 

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
        force = dictionary.get("force") if "force" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(force,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'force={(self.force if hasattr(self, "force") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'force={(self.force if hasattr(self, "force") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
