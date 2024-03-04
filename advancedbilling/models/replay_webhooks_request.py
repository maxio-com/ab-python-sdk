# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ReplayWebhooksRequest(object):

    """Implementation of the 'Replay Webhooks Request' model.

    TODO: type model description here.

    Attributes:
        ids (List[long|int]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ids": 'ids'
    }

    def __init__(self,
                 ids=None,
                 additional_properties={}):
        """Constructor for the ReplayWebhooksRequest class"""

        # Initialize members of the class
        self.ids = ids 

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
        ids = dictionary.get("ids") if dictionary.get("ids") else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(ids,
                   dictionary)
