# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdateMetafieldsRequest(object):

    """Implementation of the 'Update Metafields Request' model.

    TODO: type model description here.

    Attributes:
        metafields (UpdateMetafield | List[UpdateMetafield] | None): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metafields": 'metafields'
    }

    _optionals = [
        'metafields',
    ]

    def __init__(self,
                 metafields=APIHelper.SKIP):
        """Constructor for the UpdateMetafieldsRequest class"""

        # Initialize members of the class
        if metafields is not APIHelper.SKIP:
            self.metafields = metafields 

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
        metafields = APIHelper.deserialize_union_type(UnionTypeLookUp.get('UpdateMetafieldsRequestMetafields'), dictionary.get('metafields'), False) if dictionary.get('metafields') is not None else APIHelper.SKIP
        # Return an object of this model
        return cls(metafields)
