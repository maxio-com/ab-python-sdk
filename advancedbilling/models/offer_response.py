# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.offer import Offer


class OfferResponse(object):

    """Implementation of the 'Offer Response' model.

    TODO: type model description here.

    Attributes:
        offer (Offer): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "offer": 'offer'
    }

    _optionals = [
        'offer',
    ]

    def __init__(self,
                 offer=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the OfferResponse class"""

        # Initialize members of the class
        if offer is not APIHelper.SKIP:
            self.offer = offer 

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
        offer = Offer.from_dictionary(dictionary.get('offer')) if 'offer' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(offer,
                   additional_properties)
