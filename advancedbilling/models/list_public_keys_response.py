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

    TODO: type model description here.

    Attributes:
        chargify_js_keys (List[PublicKey]): TODO: type description here.
        meta (ListPublicKeysMeta): TODO: type description here.

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
                 meta=APIHelper.SKIP):
        """Constructor for the ListPublicKeysResponse class"""

        # Initialize members of the class
        if chargify_js_keys is not APIHelper.SKIP:
            self.chargify_js_keys = chargify_js_keys 
        if meta is not APIHelper.SKIP:
            self.meta = meta 

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
        chargify_js_keys = None
        if dictionary.get('chargify_js_keys') is not None:
            chargify_js_keys = [PublicKey.from_dictionary(x) for x in dictionary.get('chargify_js_keys')]
        else:
            chargify_js_keys = APIHelper.SKIP
        meta = ListPublicKeysMeta.from_dictionary(dictionary.get('meta')) if 'meta' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(chargify_js_keys,
                   meta)
