# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_custom_price import ComponentCustomPrice


class UpdateSubscriptionComponent(object):

    """Implementation of the 'Update Subscription Component' model.

    TODO: type model description here.

    Attributes:
        component_id (int): TODO: type description here.
        custom_price (ComponentCustomPrice): Create or update custom pricing
            unique to the subscription. Used in place of `price_point_id`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "custom_price": 'custom_price'
    }

    _optionals = [
        'component_id',
        'custom_price',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 custom_price=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the UpdateSubscriptionComponent class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if custom_price is not APIHelper.SKIP:
            self.custom_price = custom_price 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        custom_price = ComponentCustomPrice.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(component_id,
                   custom_price,
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
