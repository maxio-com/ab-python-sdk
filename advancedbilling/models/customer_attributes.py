# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CustomerAttributes(object):

    """Implementation of the 'Customer Attributes' model.

    Attributes:
        first_name (str): The first name of the customer. Required when
            creating a customer via attributes.
        last_name (str): The last name of the customer. Required when creating
            a customer via attributes.
        email (str): The email address of the customer. Required when creating
            a customer via attributes.
        cc_emails (str): A list of emails that should be cc’d on all customer
            communications. Optional.
        organization (str): The organization/company of the customer. Optional.
        reference (str): A customer “reference”, or unique identifier from
            your app, stored in Chargify. Can be used so that you may
            reference your customer’s within Chargify using the same unique
            value you use in your application. Optional.
        address (str): (Optional) The customer’s shipping street address (i.e.
            “123 Main St.”).
        address_2 (str): (Optional) Second line of the customer’s shipping
            address i.e. “Apt. 100”
        city (str): (Optional) The customer’s shipping address city (i.e.
            “Boston”).
        state (str): (Optional) The customer’s shipping address state (i.e.
            “MA”). This must conform to the
            [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes
            ) in order to be valid for tax locale purposes.
        zip (str): (Optional) The customer’s shipping address zip code (i.e.
            “12345”).
        country (str): (Optional) The customer shipping address country,
            required in [ISO_3166-1
            alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format
            (i.e. “US”).
        phone (str): (Optional) The phone number of the customer.
        verified (bool): The model property of type bool.
        tax_exempt (bool): (Optional) The tax_exempt status of the customer.
            Acceptable values are true or 1 for true and false or 0 for false.
        vat_number (str): (Optional) Supplying the VAT number allows EU
            customer’s to opt-out of the Value Added Tax assuming the merchant
            address and customer billing address are not within the same EU
            country. It’s important to omit the country code from the VAT
            number upon entry. Otherwise, taxes will be assessed upon the
            purchase.
        metafields (Dict[str, str]): (Optional) A set of key/value pairs
            representing custom fields and their values. Metafields will be
            created “on-the-fly” in your site for a given key, if they have
            not been created yet.
        parent_id (int): The parent ID in Chargify if applicable. Parent is
            another Customer object.
        salesforce_id (str): (Optional) The Salesforce ID of the customer.
        default_auto_renewal_profile_id (int): (Optional) The default
            auto-renewal profile ID for the customer
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
        "verified": 'verified',
        "tax_exempt": 'tax_exempt',
        "vat_number": 'vat_number',
        "metafields": 'metafields',
        "parent_id": 'parent_id',
        "salesforce_id": 'salesforce_id',
        "default_auto_renewal_profile_id": 'default_auto_renewal_profile_id'
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
        'verified',
        'tax_exempt',
        'vat_number',
        'metafields',
        'parent_id',
        'salesforce_id',
        'default_auto_renewal_profile_id',
    ]

    _nullables = [
        'address_2',
        'parent_id',
        'salesforce_id',
        'default_auto_renewal_profile_id',
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
                 verified=APIHelper.SKIP,
                 tax_exempt=APIHelper.SKIP,
                 vat_number=APIHelper.SKIP,
                 metafields=APIHelper.SKIP,
                 parent_id=APIHelper.SKIP,
                 salesforce_id=APIHelper.SKIP,
                 default_auto_renewal_profile_id=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CustomerAttributes class"""

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
        if verified is not APIHelper.SKIP:
            self.verified = verified 
        if tax_exempt is not APIHelper.SKIP:
            self.tax_exempt = tax_exempt 
        if vat_number is not APIHelper.SKIP:
            self.vat_number = vat_number 
        if metafields is not APIHelper.SKIP:
            self.metafields = metafields 
        if parent_id is not APIHelper.SKIP:
            self.parent_id = parent_id 
        if salesforce_id is not APIHelper.SKIP:
            self.salesforce_id = salesforce_id 
        if default_auto_renewal_profile_id is not APIHelper.SKIP:
            self.default_auto_renewal_profile_id = default_auto_renewal_profile_id 

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
        address_2 = dictionary.get("address_2") if "address_2" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        zip = dictionary.get("zip") if dictionary.get("zip") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        verified = dictionary.get("verified") if "verified" in dictionary.keys() else APIHelper.SKIP
        tax_exempt = dictionary.get("tax_exempt") if "tax_exempt" in dictionary.keys() else APIHelper.SKIP
        vat_number = dictionary.get("vat_number") if dictionary.get("vat_number") else APIHelper.SKIP
        metafields = dictionary.get("metafields") if dictionary.get("metafields") else APIHelper.SKIP
        parent_id = dictionary.get("parent_id") if "parent_id" in dictionary.keys() else APIHelper.SKIP
        salesforce_id = dictionary.get("salesforce_id") if "salesforce_id" in dictionary.keys() else APIHelper.SKIP
        default_auto_renewal_profile_id = dictionary.get("default_auto_renewal_profile_id") if "default_auto_renewal_profile_id" in dictionary.keys() else APIHelper.SKIP
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
                   verified,
                   tax_exempt,
                   vat_number,
                   metafields,
                   parent_id,
                   salesforce_id,
                   default_auto_renewal_profile_id,
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
                f'verified={(self.verified if hasattr(self, "verified") else None)!r}, '
                f'tax_exempt={(self.tax_exempt if hasattr(self, "tax_exempt") else None)!r}, '
                f'vat_number={(self.vat_number if hasattr(self, "vat_number") else None)!r}, '
                f'metafields={(self.metafields if hasattr(self, "metafields") else None)!r}, '
                f'parent_id={(self.parent_id if hasattr(self, "parent_id") else None)!r}, '
                f'salesforce_id={(self.salesforce_id if hasattr(self, "salesforce_id") else None)!r}, '
                f'default_auto_renewal_profile_id={(self.default_auto_renewal_profile_id if hasattr(self, "default_auto_renewal_profile_id") else None)!r}, '
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
                f'verified={(self.verified if hasattr(self, "verified") else None)!s}, '
                f'tax_exempt={(self.tax_exempt if hasattr(self, "tax_exempt") else None)!s}, '
                f'vat_number={(self.vat_number if hasattr(self, "vat_number") else None)!s}, '
                f'metafields={(self.metafields if hasattr(self, "metafields") else None)!s}, '
                f'parent_id={(self.parent_id if hasattr(self, "parent_id") else None)!s}, '
                f'salesforce_id={(self.salesforce_id if hasattr(self, "salesforce_id") else None)!s}, '
                f'default_auto_renewal_profile_id={(self.default_auto_renewal_profile_id if hasattr(self, "default_auto_renewal_profile_id") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
