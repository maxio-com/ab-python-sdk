# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateCustomer(object):

    """Implementation of the 'Create Customer' model.

    TODO: type model description here.

    Attributes:
        first_name (str): TODO: type description here.
        last_name (str): TODO: type description here.
        email (str): TODO: type description here.
        cc_emails (str): TODO: type description here.
        organization (str): TODO: type description here.
        reference (str): TODO: type description here.
        address (str): TODO: type description here.
        address_2 (str): TODO: type description here.
        city (str): TODO: type description here.
        state (str): TODO: type description here.
        zip (str): TODO: type description here.
        country (str): TODO: type description here.
        phone (str): TODO: type description here.
        locale (str): Set a specific language on a customer record.
        vat_number (str): TODO: type description here.
        tax_exempt (bool): TODO: type description here.
        tax_exempt_reason (str): TODO: type description here.
        parent_id (int): The parent ID in Chargify if applicable. Parent is
            another Customer object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'first_name',
        "last_name": 'last_name',
        "email": 'email',
        "cc_emails": 'cc_emails',
        "organization": 'organization',
        "reference": 'reference',
        "address": 'address',
        "address_2": 'address_2',
        "city": 'city',
        "state": 'state',
        "zip": 'zip',
        "country": 'country',
        "phone": 'phone',
        "locale": 'locale',
        "vat_number": 'vat_number',
        "tax_exempt": 'tax_exempt',
        "tax_exempt_reason": 'tax_exempt_reason',
        "parent_id": 'parent_id'
    }

    _optionals = [
        'cc_emails',
        'organization',
        'reference',
        'address',
        'address_2',
        'city',
        'state',
        'zip',
        'country',
        'phone',
        'locale',
        'vat_number',
        'tax_exempt',
        'tax_exempt_reason',
        'parent_id',
    ]

    _nullables = [
        'parent_id',
    ]

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 email=None,
                 cc_emails=APIHelper.SKIP,
                 organization=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 address_2=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 zip=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 locale=APIHelper.SKIP,
                 vat_number=APIHelper.SKIP,
                 tax_exempt=APIHelper.SKIP,
                 tax_exempt_reason=APIHelper.SKIP,
                 parent_id=APIHelper.SKIP):
        """Constructor for the CreateCustomer class"""

        # Initialize members of the class
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email 
        if cc_emails is not APIHelper.SKIP:
            self.cc_emails = cc_emails 
        if organization is not APIHelper.SKIP:
            self.organization = organization 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
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
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if locale is not APIHelper.SKIP:
            self.locale = locale 
        if vat_number is not APIHelper.SKIP:
            self.vat_number = vat_number 
        if tax_exempt is not APIHelper.SKIP:
            self.tax_exempt = tax_exempt 
        if tax_exempt_reason is not APIHelper.SKIP:
            self.tax_exempt_reason = tax_exempt_reason 
        if parent_id is not APIHelper.SKIP:
            self.parent_id = parent_id 

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
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else None
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else None
        email = dictionary.get("email") if dictionary.get("email") else None
        cc_emails = dictionary.get("cc_emails") if dictionary.get("cc_emails") else APIHelper.SKIP
        organization = dictionary.get("organization") if dictionary.get("organization") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        address = dictionary.get("address") if dictionary.get("address") else APIHelper.SKIP
        address_2 = dictionary.get("address_2") if dictionary.get("address_2") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        zip = dictionary.get("zip") if dictionary.get("zip") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        locale = dictionary.get("locale") if dictionary.get("locale") else APIHelper.SKIP
        vat_number = dictionary.get("vat_number") if dictionary.get("vat_number") else APIHelper.SKIP
        tax_exempt = dictionary.get("tax_exempt") if "tax_exempt" in dictionary.keys() else APIHelper.SKIP
        tax_exempt_reason = dictionary.get("tax_exempt_reason") if dictionary.get("tax_exempt_reason") else APIHelper.SKIP
        parent_id = dictionary.get("parent_id") if "parent_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   email,
                   cc_emails,
                   organization,
                   reference,
                   address,
                   address_2,
                   city,
                   state,
                   zip,
                   country,
                   phone,
                   locale,
                   vat_number,
                   tax_exempt,
                   tax_exempt_reason,
                   parent_id)
