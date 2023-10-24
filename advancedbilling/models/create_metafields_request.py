# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateMetafieldsRequest(object):

    """Implementation of the 'Create Metafields Request' model.

    TODO: type model description here.

    Attributes:
        metafields (CreateMetafield | List[CreateMetafield]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metafields": 'metafields'
    }

    def __init__(self,
                 metafields=None):
        """Constructor for the CreateMetafieldsRequest class"""

        # Initialize members of the class
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        metafields = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateMetafieldsRequestMetafields'), dictionary.get('metafields'), False) if dictionary.get('metafields') is not None else None
        # Return an object of this model
        return cls(metafields)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('CreateMetafieldsRequestMetafields').validate(dictionary.metafields)

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('CreateMetafieldsRequestMetafields').validate(dictionary.get('metafields'))
