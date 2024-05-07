# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CouponRestriction(object):

    """Implementation of the 'Coupon Restriction' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        item_type (RestrictionType): TODO: type description here.
        item_id (int): TODO: type description here.
        name (str): TODO: type description here.
        handle (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "item_type": 'item_type',
        "item_id": 'item_id',
        "name": 'name',
        "handle": 'handle'
    }

    _optionals = [
        'id',
        'item_type',
        'item_id',
        'name',
        'handle',
    ]

    _nullables = [
        'handle',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 item_type=APIHelper.SKIP,
                 item_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CouponRestriction class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if item_type is not APIHelper.SKIP:
            self.item_type = item_type 
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 

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
        item_type = dictionary.get("item_type") if dictionary.get("item_type") else APIHelper.SKIP
        item_id = dictionary.get("item_id") if dictionary.get("item_id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if "handle" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   item_type,
                   item_id,
                   name,
                   handle,
                   dictionary)
