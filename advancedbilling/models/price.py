# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Price(object):

    """Implementation of the 'Price' model.

    TODO: type model description here.

    Attributes:
        starting_quantity (int | str): TODO: type description here.
        ending_quantity (int | str | None): TODO: type description here.
        unit_price (float | str): The price can contain up to 8 decimal
            places. i.e. 1.00 or 0.0012 or 0.00000065

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "starting_quantity": 'starting_quantity',
        "unit_price": 'unit_price',
        "ending_quantity": 'ending_quantity'
    }

    _optionals = [
        'ending_quantity',
    ]

    _nullables = [
        'ending_quantity',
    ]

    def __init__(self,
                 starting_quantity=None,
                 unit_price=None,
                 ending_quantity=APIHelper.SKIP):
        """Constructor for the Price class"""

        # Initialize members of the class
        self.starting_quantity = starting_quantity 
        if ending_quantity is not APIHelper.SKIP:
            self.ending_quantity = ending_quantity 
        self.unit_price = unit_price 

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        starting_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PriceStartingQuantity'), dictionary.get('starting_quantity'), False) if dictionary.get('starting_quantity') is not None else None
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PriceUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else None
        if 'ending_quantity' in dictionary.keys():
            ending_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PriceEndingQuantity'), dictionary.get('ending_quantity'), False) if dictionary.get('ending_quantity') is not None else None
        else:
            ending_quantity = APIHelper.SKIP
        # Return an object of this model
        return cls(starting_quantity,
                   unit_price,
                   ending_quantity)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('PriceStartingQuantity').validate(dictionary.starting_quantity).is_valid \
                and UnionTypeLookUp.get('PriceUnitPrice').validate(dictionary.unit_price).is_valid

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('PriceStartingQuantity').validate(dictionary.get('starting_quantity')).is_valid \
            and UnionTypeLookUp.get('PriceUnitPrice').validate(dictionary.get('unit_price')).is_valid
