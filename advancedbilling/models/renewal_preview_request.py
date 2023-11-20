# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.renewal_preview_component import RenewalPreviewComponent


class RenewalPreviewRequest(object):

    """Implementation of the 'Renewal Preview Request' model.

    TODO: type model description here.

    Attributes:
        components (List[RenewalPreviewComponent]): An optional array of
            component definitions to preview. Providing any component
            definitions here will override the actual components on the
            subscription (and their quantities), and the billing preview will
            contain only these components (in addition to any product base
            fees).

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
        """Constructor for the RenewalPreviewRequest class"""

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
            components = [RenewalPreviewComponent.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        # Return an object of this model
        return cls(components)
