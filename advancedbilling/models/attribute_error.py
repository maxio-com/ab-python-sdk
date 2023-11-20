# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AttributeError(object):

    """Implementation of the 'Attribute Error' model.

    TODO: type model description here.

    Attributes:
        attribute (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attribute": 'attribute'
    }

    def __init__(self,
                 attribute=None):
        """Constructor for the AttributeError class"""

        # Initialize members of the class
        self.attribute = attribute 

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
        attribute = dictionary.get("attribute") if dictionary.get("attribute") else None
        # Return an object of this model
        return cls(attribute)
