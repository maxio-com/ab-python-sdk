# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ReplayWebhooksRequest(object):

    """Implementation of the 'Replay Webhooks Request' model.

    Attributes:
        ids (List[int]): The model property of type List[int].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ids": 'ids'
    }

    def __init__(self,
                 ids=None,
                 additional_properties=None):
        """Constructor for the ReplayWebhooksRequest class"""

        # Initialize members of the class
        self.ids = ids 

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
        ids = dictionary.get("ids") if dictionary.get("ids") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(ids,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'ids={self.ids!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'ids={self.ids!s}, '
                f'additional_properties={self.additional_properties!s})')
