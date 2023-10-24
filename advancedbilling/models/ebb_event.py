# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.chargify_ebb import ChargifyEBB


class EBBEvent(object):

    """Implementation of the 'EBB Event' model.

    TODO: type model description here.

    Attributes:
        chargify (ChargifyEBB): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify": 'chargify'
    }

    _optionals = [
        'chargify',
    ]

    def __init__(self,
                 chargify=APIHelper.SKIP):
        """Constructor for the EBBEvent class"""

        # Initialize members of the class
        if chargify is not APIHelper.SKIP:
            self.chargify = chargify 

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
        chargify = ChargifyEBB.from_dictionary(dictionary.get('chargify')) if 'chargify' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(chargify)
