# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_s_price_point_assignment import ComponentSPricePointAssignment


class BulkComponentSPricePointAssignment(object):

    """Implementation of the 'Bulk Component's Price Point Assignment' model.

    TODO: type model description here.

    Attributes:
        components (List[ComponentSPricePointAssignment]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "components": 'components'
    }

    _optionals = [
        'components',
    ]

    def __init__(self,
                 components=APIHelper.SKIP):
        """Constructor for the BulkComponentSPricePointAssignment class"""

        # Initialize members of the class
        if components is not APIHelper.SKIP:
            self.components = components 

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
        components = None
        if dictionary.get('components') is not None:
            components = [ComponentSPricePointAssignment.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        # Return an object of this model
        return cls(components)
