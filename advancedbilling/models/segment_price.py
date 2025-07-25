# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SegmentPrice(object):

    """Implementation of the 'Segment Price' model.

    Attributes:
        id (int): The model property of type int.
        component_id (int): The model property of type int.
        starting_quantity (int): The model property of type int.
        ending_quantity (int): The model property of type int.
        unit_price (str): The model property of type str.
        price_point_id (int): The model property of type int.
        formatted_unit_price (str): The model property of type str.
        segment_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "component_id": 'component_id',
        "starting_quantity": 'starting_quantity',
        "ending_quantity": 'ending_quantity',
        "unit_price": 'unit_price',
        "price_point_id": 'price_point_id',
        "formatted_unit_price": 'formatted_unit_price',
        "segment_id": 'segment_id'
    }

    _optionals = [
        'id',
        'component_id',
        'starting_quantity',
        'ending_quantity',
        'unit_price',
        'price_point_id',
        'formatted_unit_price',
        'segment_id',
    ]

    _nullables = [
        'ending_quantity',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 starting_quantity=APIHelper.SKIP,
                 ending_quantity=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 formatted_unit_price=APIHelper.SKIP,
                 segment_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SegmentPrice class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if starting_quantity is not APIHelper.SKIP:
            self.starting_quantity = starting_quantity 
        if ending_quantity is not APIHelper.SKIP:
            self.ending_quantity = ending_quantity 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if formatted_unit_price is not APIHelper.SKIP:
            self.formatted_unit_price = formatted_unit_price 
        if segment_id is not APIHelper.SKIP:
            self.segment_id = segment_id 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        ending_quantity = dictionary.get("ending_quantity") if "ending_quantity" in dictionary.keys() else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        formatted_unit_price = dictionary.get("formatted_unit_price") if dictionary.get("formatted_unit_price") else APIHelper.SKIP
        segment_id = dictionary.get("segment_id") if dictionary.get("segment_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   component_id,
                   starting_quantity,
                   ending_quantity,
                   unit_price,
                   price_point_id,
                   formatted_unit_price,
                   segment_id,
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

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'starting_quantity={(self.starting_quantity if hasattr(self, "starting_quantity") else None)!r}, '
                f'ending_quantity={(self.ending_quantity if hasattr(self, "ending_quantity") else None)!r}, '
                f'unit_price={(self.unit_price if hasattr(self, "unit_price") else None)!r}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!r}, '
                f'formatted_unit_price={(self.formatted_unit_price if hasattr(self, "formatted_unit_price") else None)!r}, '
                f'segment_id={(self.segment_id if hasattr(self, "segment_id") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'starting_quantity={(self.starting_quantity if hasattr(self, "starting_quantity") else None)!s}, '
                f'ending_quantity={(self.ending_quantity if hasattr(self, "ending_quantity") else None)!s}, '
                f'unit_price={(self.unit_price if hasattr(self, "unit_price") else None)!s}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!s}, '
                f'formatted_unit_price={(self.formatted_unit_price if hasattr(self, "formatted_unit_price") else None)!s}, '
                f'segment_id={(self.segment_id if hasattr(self, "segment_id") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
