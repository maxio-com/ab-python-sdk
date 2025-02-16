# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentCollectionMethodChanged(object):

    """Implementation of the 'Payment Collection Method Changed' model.

    Attributes:
        previous_value (str): The model property of type str.
        current_value (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "previous_value": 'previous_value',
        "current_value": 'current_value'
    }

    def __init__(self,
                 previous_value=None,
                 current_value=None,
                 additional_properties=None):
        """Constructor for the PaymentCollectionMethodChanged class"""

        # Initialize members of the class
        self.previous_value = previous_value 
        self.current_value = current_value 

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
        previous_value = dictionary.get("previous_value") if dictionary.get("previous_value") else None
        current_value = dictionary.get("current_value") if dictionary.get("current_value") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(previous_value,
                   current_value,
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
            return APIHelper.is_valid_type(value=dictionary.previous_value,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.current_value,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('previous_value'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_value'),
                                        type_callable=lambda value: isinstance(value, str))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'previous_value={self.previous_value!r}, '
                f'current_value={self.current_value!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'previous_value={self.previous_value!s}, '
                f'current_value={self.current_value!s}, '
                f'additional_properties={self.additional_properties!s})')
