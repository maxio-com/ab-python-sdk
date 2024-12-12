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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metafields": 'metafields'
    }

    _optionals = [
        'metafields',
    ]

    def __init__(self,
                 metafields=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the UpdateMetafieldsRequest class"""

        # Initialize members of the class
        if metafields is not APIHelper.SKIP:
            self.metafields = metafields 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        metafields = APIHelper.deserialize_union_type(UnionTypeLookUp.get('UpdateMetafieldsRequestMetafields'), dictionary.get('metafields'), False) if dictionary.get('metafields') is not None else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(metafields,
                   additional_properties)
