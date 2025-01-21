# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateOrUpdateSegmentPrice(object):

    """Implementation of the 'Create or Update Segment Price' model.

    Attributes:
        starting_quantity (int): The model property of type int.
        ending_quantity (int): The model property of type int.
        unit_price (str | float): The price can contain up to 8 decimal
            places. i.e. 1.00 or 0.0012 or 0.00000065
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "unit_price": 'unit_price',
        "starting_quantity": 'starting_quantity',
        "ending_quantity": 'ending_quantity'
    }

    _optionals = [
        'starting_quantity',
        'ending_quantity',
    ]

    def __init__(self,
                 unit_price=None,
                 starting_quantity=APIHelper.SKIP,
                 ending_quantity=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateOrUpdateSegmentPrice class"""

        # Initialize members of the class
        if starting_quantity is not APIHelper.SKIP:
            self.starting_quantity = starting_quantity 
        if ending_quantity is not APIHelper.SKIP:
            self.ending_quantity = ending_quantity 
        self.unit_price = unit_price 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateOrUpdateSegmentPriceUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else None
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        ending_quantity = dictionary.get("ending_quantity") if dictionary.get("ending_quantity") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(unit_price,
                   starting_quantity,
                   ending_quantity,
                   additional_properties)

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
            return UnionTypeLookUp.get('CreateOrUpdateSegmentPriceUnitPrice').validate(dictionary.unit_price).is_valid

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('CreateOrUpdateSegmentPriceUnitPrice').validate(dictionary.get('unit_price')).is_valid

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'starting_quantity={self.starting_quantity!r}, '
                f'ending_quantity={self.ending_quantity!r}, '
                f'unit_price={self.unit_price!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'starting_quantity={self.starting_quantity!s}, '
                f'ending_quantity={self.ending_quantity!s}, '
                f'unit_price={self.unit_price!s}, '
                f'additional_properties={self.additional_properties!s})')
