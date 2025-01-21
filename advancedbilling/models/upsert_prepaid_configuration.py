# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpsertPrepaidConfiguration(object):

    """Implementation of the 'Upsert Prepaid Configuration' model.

    Attributes:
        initial_funding_amount_in_cents (int): The model property of type int.
        replenish_to_amount_in_cents (int): The model property of type int.
        auto_replenish (bool): The model property of type bool.
        replenish_threshold_amount_in_cents (int): The model property of type
            int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "initial_funding_amount_in_cents": 'initial_funding_amount_in_cents',
        "replenish_to_amount_in_cents": 'replenish_to_amount_in_cents',
        "auto_replenish": 'auto_replenish',
        "replenish_threshold_amount_in_cents": 'replenish_threshold_amount_in_cents'
    }

    _optionals = [
        'initial_funding_amount_in_cents',
        'replenish_to_amount_in_cents',
        'auto_replenish',
        'replenish_threshold_amount_in_cents',
    ]

    def __init__(self,
                 initial_funding_amount_in_cents=APIHelper.SKIP,
                 replenish_to_amount_in_cents=APIHelper.SKIP,
                 auto_replenish=APIHelper.SKIP,
                 replenish_threshold_amount_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the UpsertPrepaidConfiguration class"""

        # Initialize members of the class
        if initial_funding_amount_in_cents is not APIHelper.SKIP:
            self.initial_funding_amount_in_cents = initial_funding_amount_in_cents 
        if replenish_to_amount_in_cents is not APIHelper.SKIP:
            self.replenish_to_amount_in_cents = replenish_to_amount_in_cents 
        if auto_replenish is not APIHelper.SKIP:
            self.auto_replenish = auto_replenish 
        if replenish_threshold_amount_in_cents is not APIHelper.SKIP:
            self.replenish_threshold_amount_in_cents = replenish_threshold_amount_in_cents 

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
        initial_funding_amount_in_cents = dictionary.get("initial_funding_amount_in_cents") if dictionary.get("initial_funding_amount_in_cents") else APIHelper.SKIP
        replenish_to_amount_in_cents = dictionary.get("replenish_to_amount_in_cents") if dictionary.get("replenish_to_amount_in_cents") else APIHelper.SKIP
        auto_replenish = dictionary.get("auto_replenish") if "auto_replenish" in dictionary.keys() else APIHelper.SKIP
        replenish_threshold_amount_in_cents = dictionary.get("replenish_threshold_amount_in_cents") if dictionary.get("replenish_threshold_amount_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(initial_funding_amount_in_cents,
                   replenish_to_amount_in_cents,
                   auto_replenish,
                   replenish_threshold_amount_in_cents,
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
                f'initial_funding_amount_in_cents={self.initial_funding_amount_in_cents!r}, '
                f'replenish_to_amount_in_cents={self.replenish_to_amount_in_cents!r}, '
                f'auto_replenish={self.auto_replenish!r}, '
                f'replenish_threshold_amount_in_cents={self.replenish_threshold_amount_in_cents!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'initial_funding_amount_in_cents={self.initial_funding_amount_in_cents!s}, '
                f'replenish_to_amount_in_cents={self.replenish_to_amount_in_cents!s}, '
                f'auto_replenish={self.auto_replenish!s}, '
                f'replenish_threshold_amount_in_cents={self.replenish_threshold_amount_in_cents!s}, '
                f'additional_properties={self.additional_properties!s})')
