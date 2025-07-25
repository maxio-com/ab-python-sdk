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

    Attributes:
        page (int): The model property of type int.
        per_page (int): The model property of type int.
        total_pages (int): The model property of type int.
        total_entries (int): The model property of type int.
        currency (str): The model property of type str.
        currency_symbol (str): The model property of type str.
        movements (List[Movement]): The model property of type List[Movement].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(page,
                   per_page,
                   total_pages,
                   total_entries,
                   currency,
                   currency_symbol,
                   movements,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'page={(self.page if hasattr(self, "page") else None)!r}, '
                f'per_page={(self.per_page if hasattr(self, "per_page") else None)!r}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!r}, '
                f'total_entries={(self.total_entries if hasattr(self, "total_entries") else None)!r}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!r}, '
                f'currency_symbol={(self.currency_symbol if hasattr(self, "currency_symbol") else None)!r}, '
                f'movements={(self.movements if hasattr(self, "movements") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'page={(self.page if hasattr(self, "page") else None)!s}, '
                f'per_page={(self.per_page if hasattr(self, "per_page") else None)!s}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!s}, '
                f'total_entries={(self.total_entries if hasattr(self, "total_entries") else None)!s}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!s}, '
                f'currency_symbol={(self.currency_symbol if hasattr(self, "currency_symbol") else None)!s}, '
                f'movements={(self.movements if hasattr(self, "movements") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
