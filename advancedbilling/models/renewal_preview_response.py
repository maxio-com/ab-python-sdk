# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.renewal_preview import RenewalPreview


class RenewalPreviewResponse(object):

    """Implementation of the 'Renewal Preview Response' model.

    TODO: type model description here.

    Attributes:
        renewal_preview (RenewalPreview): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "renewal_preview": 'renewal_preview'
    }

    def __init__(self,
                 renewal_preview=None):
        """Constructor for the RenewalPreviewResponse class"""

        # Initialize members of the class
        self.renewal_preview = renewal_preview 

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
        renewal_preview = RenewalPreview.from_dictionary(dictionary.get('renewal_preview')) if dictionary.get('renewal_preview') else None
        # Return an object of this model
        return cls(renewal_preview)
