# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceCustomer(object):

    """Implementation of the 'Invoice Customer' model.

    Information about the customer who is owner or recipient the invoiced
    subscription.

    Attributes:
        chargify_id (int): TODO: type description here.
        first_name (str): TODO: type description here.
        last_name (str): TODO: type description here.
        organization (str): TODO: type description here.
        email (str): TODO: type description here.
        vat_number (str): TODO: type description here.
        reference (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify_id": 'chargify_id',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "organization": 'organization',
        "email": 'email',
        "vat_number": 'vat_number',
        "reference": 'reference'
    }

    _optionals = [
        'chargify_id',
        'first_name',
        'last_name',
        'organization',
        'email',
        'vat_number',
        'reference',
    ]

    _nullables = [
        'chargify_id',
        'organization',
        'vat_number',
        'reference',
    ]

    def __init__(self,
                 chargify_id=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 organization=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 vat_number=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoiceCustomer class"""

        # Initialize members of the class
        if chargify_id is not APIHelper.SKIP:
            self.chargify_id = chargify_id 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if organization is not APIHelper.SKIP:
            self.organization = organization 
        if email is not APIHelper.SKIP:
            self.email = email 
        if vat_number is not APIHelper.SKIP:
            self.vat_number = vat_number 
        if reference is not APIHelper.SKIP:
            self.reference = reference 

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
        chargify_id = dictionary.get("chargify_id") if "chargify_id" in dictionary.keys() else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        organization = dictionary.get("organization") if "organization" in dictionary.keys() else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        vat_number = dictionary.get("vat_number") if "vat_number" in dictionary.keys() else APIHelper.SKIP
        reference = dictionary.get("reference") if "reference" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(chargify_id,
                   first_name,
                   last_name,
                   organization,
                   email,
                   vat_number,
                   reference,
                   dictionary)

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
