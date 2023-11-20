# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoicePayer(object):

    """Implementation of the 'Invoice Payer' model.

    TODO: type model description here.

    Attributes:
        chargify_id (int): TODO: type description here.
        first_name (str): TODO: type description here.
        last_name (str): TODO: type description here.
        organization (str): TODO: type description here.
        email (str): TODO: type description here.
        vat_number (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify_id": 'chargify_id',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "organization": 'organization',
        "email": 'email',
        "vat_number": 'vat_number'
    }

    _optionals = [
        'chargify_id',
        'first_name',
        'last_name',
        'organization',
        'email',
        'vat_number',
    ]

    _nullables = [
        'organization',
        'vat_number',
    ]

    def __init__(self,
                 chargify_id=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 organization=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 vat_number=APIHelper.SKIP):
        """Constructor for the InvoicePayer class"""

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
        chargify_id = dictionary.get("chargify_id") if dictionary.get("chargify_id") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        organization = dictionary.get("organization") if "organization" in dictionary.keys() else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        vat_number = dictionary.get("vat_number") if "vat_number" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(chargify_id,
                   first_name,
                   last_name,
                   organization,
                   email,
                   vat_number)
