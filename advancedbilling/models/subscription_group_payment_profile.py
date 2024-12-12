# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupPaymentProfile(object):

    """Implementation of the 'Subscription Group Payment Profile' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        first_name (str): TODO: type description here.
        last_name (str): TODO: type description here.
        masked_card_number (str): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "masked_card_number": 'masked_card_number'
    }

    _optionals = [
        'id',
        'first_name',
        'last_name',
        'masked_card_number',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 masked_card_number=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupPaymentProfile class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if masked_card_number is not APIHelper.SKIP:
            self.masked_card_number = masked_card_number 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   first_name,
                   last_name,
                   masked_card_number,
                   additional_properties)
