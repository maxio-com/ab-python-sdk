# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateInvoiceAddress(object):

    """Implementation of the 'Create Invoice Address' model.

    Overrides the default address.

    Attributes:
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        phone (str): The model property of type str.
        address (str): The model property of type str.
        address_2 (str): The model property of type str.
        city (str): The model property of type str.
        state (str): The model property of type str.
        zip (str): The model property of type str.
        country (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'first_name',
        "last_name": 'last_name',
        "phone": 'phone',
        "address": 'address',
        "address_2": 'address_2',
        "city": 'city',
        "state": 'state',
        "zip": 'zip',
        "country": 'country'
    }

    _optionals = [
        'first_name',
        'last_name',
        'phone',
        'address',
        'address_2',
        'city',
        'state',
        'zip',
        'country',
    ]

    def __init__(self,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 address_2=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 zip=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateInvoiceAddress class"""

        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if address is not APIHelper.SKIP:
            self.address = address 
        if address_2 is not APIHelper.SKIP:
            self.address_2 = address_2 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if zip is not APIHelper.SKIP:
            self.zip = zip 
        if country is not APIHelper.SKIP:
            self.country = country 

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
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        address = dictionary.get("address") if dictionary.get("address") else APIHelper.SKIP
        address_2 = dictionary.get("address_2") if dictionary.get("address_2") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        zip = dictionary.get("zip") if dictionary.get("zip") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   phone,
                   address,
                   address_2,
                   city,
                   state,
                   zip,
                   country,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!r}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!r}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!r}, '
                f'address={(self.address if hasattr(self, "address") else None)!r}, '
                f'address_2={(self.address_2 if hasattr(self, "address_2") else None)!r}, '
                f'city={(self.city if hasattr(self, "city") else None)!r}, '
                f'state={(self.state if hasattr(self, "state") else None)!r}, '
                f'zip={(self.zip if hasattr(self, "zip") else None)!r}, '
                f'country={(self.country if hasattr(self, "country") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!s}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!s}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!s}, '
                f'address={(self.address if hasattr(self, "address") else None)!s}, '
                f'address_2={(self.address_2 if hasattr(self, "address_2") else None)!s}, '
                f'city={(self.city if hasattr(self, "city") else None)!s}, '
                f'state={(self.state if hasattr(self, "state") else None)!s}, '
                f'zip={(self.zip if hasattr(self, "zip") else None)!s}, '
                f'country={(self.country if hasattr(self, "country") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
