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

    Attributes:
        offers (List[Offer]): The model property of type List[Offer].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "offers": 'offers'
    }

    _optionals = [
        'offers',
    ]

    def __init__(self,
                 offers=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListOffersResponse class"""

        # Initialize members of the class
        if offers is not APIHelper.SKIP:
            self.offers = offers 

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
        offers = None
        if dictionary.get('offers') is not None:
            offers = [Offer.from_dictionary(x) for x in dictionary.get('offers')]
        else:
            offers = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(offers,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'offers={(self.offers if hasattr(self, "offers") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'offers={(self.offers if hasattr(self, "offers") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
