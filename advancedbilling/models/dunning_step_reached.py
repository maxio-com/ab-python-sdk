# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.dunner_data import DunnerData
from advancedbilling.models.dunning_step_data import DunningStepData


class DunningStepReached(object):

    """Implementation of the 'Dunning Step Reached' model.

    Attributes:
        dunner (DunnerData): The model property of type DunnerData.
        current_step (DunningStepData): The model property of type
            DunningStepData.
        next_step (DunningStepData): The model property of type
            DunningStepData.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dunner": 'dunner',
        "current_step": 'current_step',
        "next_step": 'next_step'
    }

    def __init__(self,
                 dunner=None,
                 current_step=None,
                 next_step=None,
                 additional_properties=None):
        """Constructor for the DunningStepReached class"""

        # Initialize members of the class
        self.dunner = dunner 
        self.current_step = current_step 
        self.next_step = next_step 

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
        dunner = DunnerData.from_dictionary(dictionary.get('dunner')) if dictionary.get('dunner') else None
        current_step = DunningStepData.from_dictionary(dictionary.get('current_step')) if dictionary.get('current_step') else None
        next_step = DunningStepData.from_dictionary(dictionary.get('next_step')) if dictionary.get('next_step') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(dunner,
                   current_step,
                   next_step,
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
            return APIHelper.is_valid_type(value=dictionary.dunner,
                                           type_callable=lambda value: DunnerData.validate(value),
                                           is_model_dict=True) \
                and APIHelper.is_valid_type(value=dictionary.current_step,
                                            type_callable=lambda value: DunningStepData.validate(value),
                                            is_model_dict=True) \
                and APIHelper.is_valid_type(value=dictionary.next_step,
                                            type_callable=lambda value: DunningStepData.validate(value),
                                            is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('dunner'),
                                       type_callable=lambda value: DunnerData.validate(value),
                                       is_model_dict=True) \
            and APIHelper.is_valid_type(value=dictionary.get('current_step'),
                                        type_callable=lambda value: DunningStepData.validate(value),
                                        is_model_dict=True) \
            and APIHelper.is_valid_type(value=dictionary.get('next_step'),
                                        type_callable=lambda value: DunningStepData.validate(value),
                                        is_model_dict=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'dunner={self.dunner!r}, '
                f'current_step={self.current_step!r}, '
                f'next_step={self.next_step!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'dunner={self.dunner!s}, '
                f'current_step={self.current_step!s}, '
                f'next_step={self.next_step!s}, '
                f'additional_properties={self.additional_properties!s})')
