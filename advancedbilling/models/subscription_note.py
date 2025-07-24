# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionNote(object):

    """Implementation of the 'Subscription Note' model.

    Attributes:
        id (int): The model property of type int.
        body (str): The model property of type str.
        subscription_id (int): The model property of type int.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        sticky (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "body": 'body',
        "subscription_id": 'subscription_id',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "sticky": 'sticky'
    }

    _optionals = [
        'id',
        'body',
        'subscription_id',
        'created_at',
        'updated_at',
        'sticky',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 body=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 sticky=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionNote class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if body is not APIHelper.SKIP:
            self.body = body 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if sticky is not APIHelper.SKIP:
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        body = dictionary.get("body") if dictionary.get("body") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        sticky = dictionary.get("sticky") if "sticky" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   body,
                   subscription_id,
                   created_at,
                   updated_at,
                   sticky,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'body={(self.body if hasattr(self, "body") else None)!r}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'sticky={(self.sticky if hasattr(self, "sticky") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'body={(self.body if hasattr(self, "body") else None)!s}, '
                f'subscription_id={(self.subscription_id if hasattr(self, "subscription_id") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'sticky={(self.sticky if hasattr(self, "sticky") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
