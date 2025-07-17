# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.list_public_keys_meta import ListPublicKeysMeta
from advancedbilling.models.public_key import PublicKey


class ListPublicKeysResponse(object):

    """Implementation of the 'List Public Keys Response' model.

    Attributes:
        chargify_js_keys (List[PublicKey]): The model property of type
            List[PublicKey].
        meta (ListPublicKeysMeta): The model property of type
            ListPublicKeysMeta.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify_js_keys": 'chargify_js_keys',
        "meta": 'meta'
    }

    _optionals = [
        'chargify_js_keys',
        'meta',
    ]

    def __init__(self,
                 chargify_js_keys=APIHelper.SKIP,
                 meta=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListPublicKeysResponse class"""

        # Initialize members of the class
        if chargify_js_keys is not APIHelper.SKIP:
            self.chargify_js_keys = chargify_js_keys 
        if meta is not APIHelper.SKIP:
            self.meta = meta 

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
        chargify_js_keys = None
        if dictionary.get('chargify_js_keys') is not None:
            chargify_js_keys = [PublicKey.from_dictionary(x) for x in dictionary.get('chargify_js_keys')]
        else:
            chargify_js_keys = APIHelper.SKIP
        meta = ListPublicKeysMeta.from_dictionary(dictionary.get('meta')) if 'meta' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(chargify_js_keys,
                   meta,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'chargify_js_keys={(self.chargify_js_keys if hasattr(self, "chargify_js_keys") else None)!r}, '
                f'meta={(self.meta if hasattr(self, "meta") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'chargify_js_keys={(self.chargify_js_keys if hasattr(self, "chargify_js_keys") else None)!s}, '
                f'meta={(self.meta if hasattr(self, "meta") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
