# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_address import InvoiceAddress


class InvoiceSeller(object):

    """Implementation of the 'Invoice Seller' model.

    Information about the seller (merchant) listed on the masthead of the
    invoice.

    Attributes:
        name (str): The model property of type str.
        address (InvoiceAddress): The model property of type InvoiceAddress.
        phone (str): The model property of type str.
        logo_url (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "address": 'address',
        "phone": 'phone',
        "logo_url": 'logo_url'
    }

    _optionals = [
        'name',
        'address',
        'phone',
        'logo_url',
    ]

    _nullables = [
        'logo_url',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 logo_url=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceSeller class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if address is not APIHelper.SKIP:
            self.address = address 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if logo_url is not APIHelper.SKIP:
            self.logo_url = logo_url 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        address = InvoiceAddress.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        logo_url = dictionary.get("logo_url") if "logo_url" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   address,
                   phone,
                   logo_url,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'address={self.address!r}, '
                f'phone={self.phone!r}, '
                f'logo_url={self.logo_url!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'address={self.address!s}, '
                f'phone={self.phone!s}, '
                f'logo_url={self.logo_url!s}, '
                f'additional_properties={self.additional_properties!s})')
