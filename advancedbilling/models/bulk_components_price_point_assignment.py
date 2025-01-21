# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_price_point_assignment import ComponentPricePointAssignment


class BulkComponentsPricePointAssignment(object):

    """Implementation of the 'Bulk Components Price Point Assignment' model.

    Attributes:
        components (List[ComponentPricePointAssignment]): The model property
            of type List[ComponentPricePointAssignment].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "components": 'components'
    }

    _optionals = [
        'components',
    ]

    def __init__(self,
                 components=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the BulkComponentsPricePointAssignment class"""

        # Initialize members of the class
        if components is not APIHelper.SKIP:
            self.components = components 

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
        components = None
        if dictionary.get('components') is not None:
            components = [ComponentPricePointAssignment.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(components,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'components={self.components!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'components={self.components!s}, '
                f'additional_properties={self.additional_properties!s})')
