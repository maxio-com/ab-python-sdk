# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentAllocationErrorItem(object):

    """Implementation of the 'Component Allocation Error Item' model.

    TODO: type model description here.

    Attributes:
        component_id (int): TODO: type description here.
        message (str): TODO: type description here.
        kind (str): TODO: type description here.
        on (str): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_id": 'component_id',
        "message": 'message',
        "kind": 'kind',
        "on": 'on'
    }

    _optionals = [
        'component_id',
        'message',
        'kind',
        'on',
    ]

    def __init__(self,
                 component_id=APIHelper.SKIP,
                 message=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 on=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ComponentAllocationErrorItem class"""

        # Initialize members of the class
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if message is not APIHelper.SKIP:
            self.message = message 
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if on is not APIHelper.SKIP:
            self.on = on 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        on = dictionary.get("on") if dictionary.get("on") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(component_id,
                   message,
                   kind,
                   on,
                   additional_properties)
