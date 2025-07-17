# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PayerAttributes(object):

    """Implementation of the 'Payer Attributes' model.

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
        locale (str): The model property of type str.
        vat_number (str): The model property of type str.
        tax_exempt (bool): The model property of type bool.
        tax_exempt_reason (str): The model property of type str.
        metafields (Dict[str, str]): (Optional) A set of key/value pairs
            representing custom fields and their values. Metafields will be
            created “on-the-fly” in your site for a given key, if they have
            not been created yet.
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
        "metafields": 'metafields'
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
        'metafields',
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
                 metafields=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PayerAttributes class"""

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
        if metafields is not APIHelper.SKIP:
            self.metafields = metafields 

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
        metafields = dictionary.get("metafields") if dictionary.get("metafields") else APIHelper.SKIP
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
                   metafields,
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
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!r}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!r}, '
                f'email={(self.email if hasattr(self, "email") else None)!r}, '
                f'cc_emails={(self.cc_emails if hasattr(self, "cc_emails") else None)!r}, '
                f'organization={(self.organization if hasattr(self, "organization") else None)!r}, '
                f'reference={(self.reference if hasattr(self, "reference") else None)!r}, '
                f'address={(self.address if hasattr(self, "address") else None)!r}, '
                f'address_2={(self.address_2 if hasattr(self, "address_2") else None)!r}, '
                f'city={(self.city if hasattr(self, "city") else None)!r}, '
                f'state={(self.state if hasattr(self, "state") else None)!r}, '
                f'zip={(self.zip if hasattr(self, "zip") else None)!r}, '
                f'country={(self.country if hasattr(self, "country") else None)!r}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!r}, '
                f'locale={(self.locale if hasattr(self, "locale") else None)!r}, '
                f'vat_number={(self.vat_number if hasattr(self, "vat_number") else None)!r}, '
                f'tax_exempt={(self.tax_exempt if hasattr(self, "tax_exempt") else None)!r}, '
                f'tax_exempt_reason={(self.tax_exempt_reason if hasattr(self, "tax_exempt_reason") else None)!r}, '
                f'metafields={(self.metafields if hasattr(self, "metafields") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!s}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!s}, '
                f'email={(self.email if hasattr(self, "email") else None)!s}, '
                f'cc_emails={(self.cc_emails if hasattr(self, "cc_emails") else None)!s}, '
                f'organization={(self.organization if hasattr(self, "organization") else None)!s}, '
                f'reference={(self.reference if hasattr(self, "reference") else None)!s}, '
                f'address={(self.address if hasattr(self, "address") else None)!s}, '
                f'address_2={(self.address_2 if hasattr(self, "address_2") else None)!s}, '
                f'city={(self.city if hasattr(self, "city") else None)!s}, '
                f'state={(self.state if hasattr(self, "state") else None)!s}, '
                f'zip={(self.zip if hasattr(self, "zip") else None)!s}, '
                f'country={(self.country if hasattr(self, "country") else None)!s}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!s}, '
                f'locale={(self.locale if hasattr(self, "locale") else None)!s}, '
                f'vat_number={(self.vat_number if hasattr(self, "vat_number") else None)!s}, '
                f'tax_exempt={(self.tax_exempt if hasattr(self, "tax_exempt") else None)!s}, '
                f'tax_exempt_reason={(self.tax_exempt_reason if hasattr(self, "tax_exempt_reason") else None)!s}, '
                f'metafields={(self.metafields if hasattr(self, "metafields") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
