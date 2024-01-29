# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.offer import Offer


class ListOffersResponse(object):

    """Implementation of the 'List Offers Response' model.

    TODO: type model description here.

    Attributes:
        offers (List[Offer]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "offers": 'offers'
    }

    _optionals = [
        'offers',
    ]

    def __init__(self,
                 offers=APIHelper.SKIP):
        """Constructor for the ListOffersResponse class"""

        # Initialize members of the class
        if offers is not APIHelper.SKIP:
            self.offers = offers 

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
        offers = None
        if dictionary.get('offers') is not None:
            offers = [Offer.from_dictionary(x) for x in dictionary.get('offers')]
        else:
            offers = APIHelper.SKIP
        # Return an object of this model
        return cls(offers)
