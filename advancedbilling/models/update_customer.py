# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdateCustomer(object):

    """Implementation of the 'Update Customer' model.

    Attributes:
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        email (str): The model property of type str.
        cc_emails (str): The model property of type str.
        organization (str): The model property of type str.
        reference (str): The model property of type str.
        address (str): The model property of type str.
        address_2 (str): The model property of type str.
        city (str): The model property of type str.
        state (str): The model property of type str.
        zip (str): The model property of type str.
        country (str): The model property of type str.
        phone (str): The model property of type str.
        locale (str): Set a specific language on a customer record.
        vat_number (str): The model property of type str.
        tax_exempt (bool): The model property of type bool.
        tax_exempt_reason (str): The model property of type str.
        parent_id (int): The model property of type int.
        verified (bool): Is the customer verified to use ACH as a payment
            method. Available only on Authorize.Net gateway
        salesforce_id (str): The Salesforce ID of the customer
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
        "parent_id": 'parent_id',
        "verified": 'verified',
        "salesforce_id": 'salesforce_id'
    }

    _optionals = [
        'first_name',
        'last_name',
        'email',
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
        'verified',
        'salesforce_id',
    ]

    _nullables = [
        'parent_id',
        'verified',
        'salesforce_id',
    ]

    def __init__(self,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 email=APIHelper.SKIP,
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
                 parent_id=APIHelper.SKIP,
                 verified=APIHelper.SKIP,
                 salesforce_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the UpdateCustomer class"""

        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if email is not APIHelper.SKIP:
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
        if verified is not APIHelper.SKIP:
            self.verified = verified 
        if salesforce_id is not APIHelper.SKIP:
            self.salesforce_id = salesforce_id 

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
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
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
        verified = dictionary.get("verified") if "verified" in dictionary.keys() else APIHelper.SKIP
        salesforce_id = dictionary.get("salesforce_id") if "salesforce_id" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   parent_id,
                   verified,
                   salesforce_id,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'first_name={self.first_name!r}, '
                f'last_name={self.last_name!r}, '
                f'email={self.email!r}, '
                f'cc_emails={self.cc_emails!r}, '
                f'organization={self.organization!r}, '
                f'reference={self.reference!r}, '
                f'address={self.address!r}, '
                f'address_2={self.address_2!r}, '
                f'city={self.city!r}, '
                f'state={self.state!r}, '
                f'zip={self.zip!r}, '
                f'country={self.country!r}, '
                f'phone={self.phone!r}, '
                f'locale={self.locale!r}, '
                f'vat_number={self.vat_number!r}, '
                f'tax_exempt={self.tax_exempt!r}, '
                f'tax_exempt_reason={self.tax_exempt_reason!r}, '
                f'parent_id={self.parent_id!r}, '
                f'verified={self.verified!r}, '
                f'salesforce_id={self.salesforce_id!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'first_name={self.first_name!s}, '
                f'last_name={self.last_name!s}, '
                f'email={self.email!s}, '
                f'cc_emails={self.cc_emails!s}, '
                f'organization={self.organization!s}, '
                f'reference={self.reference!s}, '
                f'address={self.address!s}, '
                f'address_2={self.address_2!s}, '
                f'city={self.city!s}, '
                f'state={self.state!s}, '
                f'zip={self.zip!s}, '
                f'country={self.country!s}, '
                f'phone={self.phone!s}, '
                f'locale={self.locale!s}, '
                f'vat_number={self.vat_number!s}, '
                f'tax_exempt={self.tax_exempt!s}, '
                f'tax_exempt_reason={self.tax_exempt_reason!s}, '
                f'parent_id={self.parent_id!s}, '
                f'verified={self.verified!s}, '
                f'salesforce_id={self.salesforce_id!s}, '
                f'additional_properties={self.additional_properties!s})')
