# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpdateSubscriptionNote(object):

    """Implementation of the 'Update Subscription Note' model.

    Updatable fields for Subscription Note

    Attributes:
        body (str): TODO: type description here.
        sticky (bool): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "body": 'body',
        "sticky": 'sticky'
    }

    def __init__(self,
                 body=None,
                 sticky=None,
                 additional_properties=None):
        """Constructor for the UpdateSubscriptionNote class"""

        # Initialize members of the class
        self.body = body 
        self.sticky = sticky 

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
        body = dictionary.get("body") if dictionary.get("body") else None
        sticky = dictionary.get("sticky") if "sticky" in dictionary.keys() else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(body,
                   sticky,
                   additional_properties)
