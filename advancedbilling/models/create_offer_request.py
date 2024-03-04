# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_offer import CreateOffer


class CreateOfferRequest(object):

    """Implementation of the 'Create Offer Request' model.

    TODO: type model description here.

    Attributes:
        offer (CreateOffer): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "offer": 'offer'
    }

    def __init__(self,
                 offer=None,
                 additional_properties={}):
        """Constructor for the CreateOfferRequest class"""

        # Initialize members of the class
        self.offer = offer 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        offer = CreateOffer.from_dictionary(dictionary.get('offer')) if dictionary.get('offer') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(offer,
                   dictionary)
