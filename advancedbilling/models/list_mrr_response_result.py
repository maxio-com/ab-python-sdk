# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.movement import Movement


class ListMRRResponseResult(object):

    """Implementation of the 'List MRR Response Result' model.

    TODO: type model description here.

    Attributes:
        page (int): TODO: type description here.
        per_page (int): TODO: type description here.
        total_pages (int): TODO: type description here.
        total_entries (int): TODO: type description here.
        currency (str): TODO: type description here.
        currency_symbol (str): TODO: type description here.
        movements (List[Movement]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "page": 'page',
        "per_page": 'per_page',
        "total_pages": 'total_pages',
        "total_entries": 'total_entries',
        "currency": 'currency',
        "currency_symbol": 'currency_symbol',
        "movements": 'movements'
    }

    _optionals = [
        'page',
        'per_page',
        'total_pages',
        'total_entries',
        'currency',
        'currency_symbol',
        'movements',
    ]

    def __init__(self,
                 page=APIHelper.SKIP,
                 per_page=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 total_entries=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 currency_symbol=APIHelper.SKIP,
                 movements=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListMRRResponseResult class"""

        # Initialize members of the class
        if page is not APIHelper.SKIP:
            self.page = page 
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
        if total_entries is not APIHelper.SKIP:
            self.total_entries = total_entries 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if currency_symbol is not APIHelper.SKIP:
            self.currency_symbol = currency_symbol 
        if movements is not APIHelper.SKIP:
            self.movements = movements 

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
        page = dictionary.get("page") if dictionary.get("page") else APIHelper.SKIP
        per_page = dictionary.get("per_page") if dictionary.get("per_page") else APIHelper.SKIP
        total_pages = dictionary.get("total_pages") if dictionary.get("total_pages") else APIHelper.SKIP
        total_entries = dictionary.get("total_entries") if dictionary.get("total_entries") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        currency_symbol = dictionary.get("currency_symbol") if dictionary.get("currency_symbol") else APIHelper.SKIP
        movements = None
        if dictionary.get('movements') is not None:
            movements = [Movement.from_dictionary(x) for x in dictionary.get('movements')]
        else:
            movements = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(page,
                   per_page,
                   total_pages,
                   total_entries,
                   currency,
                   currency_symbol,
                   movements,
                   dictionary)
