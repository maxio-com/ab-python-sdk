# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.chargeback_status import ChargebackStatus


class ChangeChargebackStatusEventData(object):

    """Implementation of the 'Change Chargeback Status Event Data' model.

    Example schema for an `change_chargeback_status` event

    Attributes:
        chargeback_status (ChargebackStatus): The model property of type
            ChargebackStatus.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargeback_status": 'chargeback_status'
    }

    def __init__(self,
                 chargeback_status=None,
                 additional_properties=None):
        """Constructor for the ChangeChargebackStatusEventData class"""

        # Initialize members of the class
        self.chargeback_status = chargeback_status 

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
        chargeback_status = dictionary.get("chargeback_status") if dictionary.get("chargeback_status") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(chargeback_status,
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
            return APIHelper.is_valid_type(value=dictionary.chargeback_status,
                                           type_callable=lambda value: ChargebackStatus.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('chargeback_status'),
                                       type_callable=lambda value: ChargebackStatus.validate(value))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'chargeback_status={self.chargeback_status!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'chargeback_status={self.chargeback_status!s}, '
                f'additional_properties={self.additional_properties!s})')
