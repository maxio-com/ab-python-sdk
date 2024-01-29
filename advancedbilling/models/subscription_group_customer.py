# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupCustomer(object):

    """Implementation of the 'Subscription Group Customer' model.

    TODO: type model description here.

    Attributes:
        first_name (str): TODO: type description here.
        last_name (str): TODO: type description here.
        organization (str): TODO: type description here.
        email (str): TODO: type description here.
        reference (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'first_name',
        "last_name": 'last_name',
        "organization": 'organization',
        "email": 'email',
        "reference": 'reference'
    }

    _optionals = [
        'first_name',
        'last_name',
        'organization',
        'email',
        'reference',
    ]

    def __init__(self,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 organization=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 reference=APIHelper.SKIP):
        """Constructor for the SubscriptionGroupCustomer class"""

        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if organization is not APIHelper.SKIP:
            self.organization = organization 
        if email is not APIHelper.SKIP:
            self.email = email 
        if reference is not APIHelper.SKIP:
            self.reference = reference 

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
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        organization = dictionary.get("organization") if dictionary.get("organization") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   organization,
                   email,
                   reference)
