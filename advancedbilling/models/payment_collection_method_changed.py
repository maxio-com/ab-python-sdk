# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentCollectionMethodChanged(object):

    """Implementation of the 'Payment Collection Method Changed' model.

    TODO: type model description here.

    Attributes:
        previous_value (str): TODO: type description here.
        current_value (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "previous_value": 'previous_value',
        "current_value": 'current_value'
    }

    def __init__(self,
                 previous_value=None,
                 current_value=None):
        """Constructor for the PaymentCollectionMethodChanged class"""

        # Initialize members of the class
        self.previous_value = previous_value 
        self.current_value = current_value 

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
        previous_value = dictionary.get("previous_value") if dictionary.get("previous_value") else None
        current_value = dictionary.get("current_value") if dictionary.get("current_value") else None
        # Return an object of this model
        return cls(previous_value,
                   current_value)

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
            return APIHelper.is_valid_type(value=dictionary.previous_value, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.current_value, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('previous_value'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_value'), type_callable=lambda value: isinstance(value, str))
