# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.proforma_custom_field import ProformaCustomField


class CustomerCustomFieldsChange(object):

    """Implementation of the 'Customer Custom Fields Change' model.

    TODO: type model description here.

    Attributes:
        before (List[ProformaCustomField]): TODO: type description here.
        after (List[ProformaCustomField]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before": 'before',
        "after": 'after'
    }

    _optionals = [
        'before',
        'after',
    ]

    def __init__(self,
                 before=APIHelper.SKIP,
                 after=APIHelper.SKIP):
        """Constructor for the CustomerCustomFieldsChange class"""

        # Initialize members of the class
        if before is not APIHelper.SKIP:
            self.before = before 
        if after is not APIHelper.SKIP:
            self.after = after 

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
        before = None
        if dictionary.get('before') is not None:
            before = [ProformaCustomField.from_dictionary(x) for x in dictionary.get('before')]
        else:
            before = APIHelper.SKIP
        after = None
        if dictionary.get('after') is not None:
            after = [ProformaCustomField.from_dictionary(x) for x in dictionary.get('after')]
        else:
            after = APIHelper.SKIP
        # Return an object of this model
        return cls(before,
                   after)
