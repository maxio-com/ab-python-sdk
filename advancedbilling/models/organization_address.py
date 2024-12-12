# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class OrganizationAddress(object):

    """Implementation of the 'Organization Address' model.

    TODO: type model description here.

    Attributes:
        street (str): TODO: type description here.
        line_2 (str): TODO: type description here.
        city (str): TODO: type description here.
        state (str): TODO: type description here.
        zip (str): TODO: type description here.
        country (str): TODO: type description here.
        name (str): TODO: type description here.
        phone (str): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "street": 'street',
        "line_2": 'line2',
        "city": 'city',
        "state": 'state',
        "zip": 'zip',
        "country": 'country',
        "name": 'name',
        "phone": 'phone'
    }

    _optionals = [
        'street',
        'line_2',
        'city',
        'state',
        'zip',
        'country',
        'name',
        'phone',
    ]

    _nullables = [
        'street',
        'line_2',
        'city',
        'state',
        'zip',
        'country',
        'name',
        'phone',
    ]

    def __init__(self,
                 street=APIHelper.SKIP,
                 line_2=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 zip=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the OrganizationAddress class"""

        # Initialize members of the class
        if street is not APIHelper.SKIP:
            self.street = street 
        if line_2 is not APIHelper.SKIP:
            self.line_2 = line_2 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if zip is not APIHelper.SKIP:
            self.zip = zip 
        if country is not APIHelper.SKIP:
            self.country = country 
        if name is not APIHelper.SKIP:
            self.name = name 
        if phone is not APIHelper.SKIP:
            self.phone = phone 

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
        street = dictionary.get("street") if "street" in dictionary.keys() else APIHelper.SKIP
        line_2 = dictionary.get("line2") if "line2" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get("city") if "city" in dictionary.keys() else APIHelper.SKIP
        state = dictionary.get("state") if "state" in dictionary.keys() else APIHelper.SKIP
        zip = dictionary.get("zip") if "zip" in dictionary.keys() else APIHelper.SKIP
        country = dictionary.get("country") if "country" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        phone = dictionary.get("phone") if "phone" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(street,
                   line_2,
                   city,
                   state,
                   zip,
                   country,
                   name,
                   phone,
                   additional_properties)
