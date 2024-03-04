# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SegmentPrice(object):

    """Implementation of the 'Segment Price' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        component_id (int): TODO: type description here.
        starting_quantity (int): TODO: type description here.
        ending_quantity (int): TODO: type description here.
        unit_price (str): TODO: type description here.
        price_point_id (int): TODO: type description here.
        formatted_unit_price (str): TODO: type description here.
        segment_id (int): TODO: type description here.

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
                 additional_properties={}):
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        ending_quantity = dictionary.get("ending_quantity") if "ending_quantity" in dictionary.keys() else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        formatted_unit_price = dictionary.get("formatted_unit_price") if dictionary.get("formatted_unit_price") else APIHelper.SKIP
        segment_id = dictionary.get("segment_id") if dictionary.get("segment_id") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   component_id,
                   starting_quantity,
                   ending_quantity,
                   unit_price,
                   price_point_id,
                   formatted_unit_price,
                   segment_id,
                   dictionary)

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
