# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionProductChange(object):

    """Implementation of the 'Subscription Product Change' model.

    TODO: type model description here.

    Attributes:
        previous_product_id (int): TODO: type description here.
        new_product_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "previous_product_id": 'previous_product_id',
        "new_product_id": 'new_product_id'
    }

    def __init__(self,
                 previous_product_id=None,
                 new_product_id=None):
        """Constructor for the SubscriptionProductChange class"""

        # Initialize members of the class
        self.previous_product_id = previous_product_id 
        self.new_product_id = new_product_id 

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
        previous_product_id = dictionary.get("previous_product_id") if dictionary.get("previous_product_id") else None
        new_product_id = dictionary.get("new_product_id") if dictionary.get("new_product_id") else None
        # Return an object of this model
        return cls(previous_product_id,
                   new_product_id)

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
            return APIHelper.is_valid_type(value=dictionary.previous_product_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.new_product_id, type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('previous_product_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('new_product_id'), type_callable=lambda value: isinstance(value, int))
