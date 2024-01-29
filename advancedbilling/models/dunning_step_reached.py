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

    TODO: type model description here.

    Attributes:
        dunner (DunnerData): TODO: type description here.
        current_step (DunningStepData): TODO: type description here.
        next_step (DunningStepData): TODO: type description here.

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
                 next_step=None):
        """Constructor for the DunningStepReached class"""

        # Initialize members of the class
        self.dunner = dunner 
        self.current_step = current_step 
        self.next_step = next_step 

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
        dunner = DunnerData.from_dictionary(dictionary.get('dunner')) if dictionary.get('dunner') else None
        current_step = DunningStepData.from_dictionary(dictionary.get('current_step')) if dictionary.get('current_step') else None
        next_step = DunningStepData.from_dictionary(dictionary.get('next_step')) if dictionary.get('next_step') else None
        # Return an object of this model
        return cls(dunner,
                   current_step,
                   next_step)

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
            return APIHelper.is_valid_type(value=dictionary.dunner, type_callable=lambda value: DunnerData.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.current_step, type_callable=lambda value: DunningStepData.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.next_step, type_callable=lambda value: DunningStepData.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('dunner'), type_callable=lambda value: DunnerData.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('current_step'), type_callable=lambda value: DunningStepData.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('next_step'), type_callable=lambda value: DunningStepData.validate(value))
