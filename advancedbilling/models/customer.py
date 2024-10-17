# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Customer(object):

    """Implementation of the 'Customer' model.

    TODO: type model description here.

    Attributes:
        first_name (str): The first name of the customer
        last_name (str): The last name of the customer
        email (str): The email address of the customer
        cc_emails (str): A comma-separated list of emails that should be cc’d
            on all customer communications (i.e. “joe@example.com,
            sue@example.com”)
        organization (str): The organization of the customer. If no value,
            `null` or empty string is provided, `organization` will be
            populated with the customer's first and last name, separated with
            a space.
        reference (str): The unique identifier used within your own
            application for this customer
        id (int): The customer ID in Chargify
        created_at (datetime): The timestamp in which the customer object was
            created in Chargify
        updated_at (datetime): The timestamp in which the customer object was
            last edited
        address (str): The customer’s shipping street address (i.e. “123 Main
            St.”)
        address_2 (str): Second line of the customer’s shipping address i.e.
            “Apt. 100”
        city (str): The customer’s shipping address city (i.e. “Boston”)
        state (str): The customer’s shipping address state (i.e. “MA”)
        state_name (str): The customer's full name of state
        zip (str): The customer’s shipping address zip code (i.e. “12345”)
        country (str): The customer shipping address country
        country_name (str): The customer's full name of country
        phone (str): The phone number of the customer
        verified (bool): Is the customer verified to use ACH as a payment
            method.
        portal_customer_created_at (datetime): The timestamp of when the
            Billing Portal entry was created at for the customer
        portal_invite_last_sent_at (datetime): The timestamp of when the
            Billing Portal invite was last sent at
        portal_invite_last_accepted_at (datetime): The timestamp of when the
            Billing Portal invite was last accepted
        tax_exempt (bool): The tax exempt status for the customer. Acceptable
            values are true or 1 for true and false or 0 for false.
        vat_number (str): The VAT business identification number for the
            customer. This number is used to determine VAT tax opt out rules.
            It is not validated when added or updated on a customer record.
            Instead, it is validated via VIES before calculating taxes. Only
            valid business identification numbers will allow for VAT opt out.
        parent_id (int): The parent ID in Chargify if applicable. Parent is
            another Customer object.
        locale (str): The locale for the customer to identify language-region
        default_subscription_group_uid (str): TODO: type description here.
        salesforce_id (str): The Salesforce ID for the customer
        tax_exempt_reason (str): The Tax Exemption Reason Code for the customer
        default_auto_renewal_profile_id (int): The default auto-renewal
            profile ID for the customer

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'first_name',
        "last_name": 'last_name',
        "email": 'email',
        "cc_emails": 'cc_emails',
        "organization": 'organization',
        "reference": 'reference',
        "id": 'id',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "address": 'address',
        "address_2": 'address_2',
        "city": 'city',
        "state": 'state',
        "state_name": 'state_name',
        "zip": 'zip',
        "country": 'country',
        "country_name": 'country_name',
        "phone": 'phone',
        "verified": 'verified',
        "portal_customer_created_at": 'portal_customer_created_at',
        "portal_invite_last_sent_at": 'portal_invite_last_sent_at',
        "portal_invite_last_accepted_at": 'portal_invite_last_accepted_at',
        "tax_exempt": 'tax_exempt',
        "vat_number": 'vat_number',
        "parent_id": 'parent_id',
        "locale": 'locale',
        "default_subscription_group_uid": 'default_subscription_group_uid',
        "salesforce_id": 'salesforce_id',
        "tax_exempt_reason": 'tax_exempt_reason',
        "default_auto_renewal_profile_id": 'default_auto_renewal_profile_id'
    }

    _optionals = [
        'first_name',
        'last_name',
        'email',
        'cc_emails',
        'organization',
        'reference',
        'id',
        'created_at',
        'updated_at',
        'address',
        'address_2',
        'city',
        'state',
        'state_name',
        'zip',
        'country',
        'country_name',
        'phone',
        'verified',
        'portal_customer_created_at',
        'portal_invite_last_sent_at',
        'portal_invite_last_accepted_at',
        'tax_exempt',
        'vat_number',
        'parent_id',
        'locale',
        'default_subscription_group_uid',
        'salesforce_id',
        'tax_exempt_reason',
        'default_auto_renewal_profile_id',
    ]

    _nullables = [
        'cc_emails',
        'organization',
        'reference',
        'address',
        'address_2',
        'city',
        'state',
        'state_name',
        'zip',
        'country',
        'country_name',
        'phone',
        'verified',
        'portal_customer_created_at',
        'portal_invite_last_sent_at',
        'portal_invite_last_accepted_at',
        'vat_number',
        'parent_id',
        'locale',
        'default_subscription_group_uid',
        'salesforce_id',
        'tax_exempt_reason',
        'default_auto_renewal_profile_id',
    ]

    def __init__(self,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 cc_emails=APIHelper.SKIP,
                 organization=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 address_2=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 state_name=APIHelper.SKIP,
                 zip=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 country_name=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 verified=APIHelper.SKIP,
                 portal_customer_created_at=APIHelper.SKIP,
                 portal_invite_last_sent_at=APIHelper.SKIP,
                 portal_invite_last_accepted_at=APIHelper.SKIP,
                 tax_exempt=APIHelper.SKIP,
                 vat_number=APIHelper.SKIP,
                 parent_id=APIHelper.SKIP,
                 locale=APIHelper.SKIP,
                 default_subscription_group_uid=APIHelper.SKIP,
                 salesforce_id=APIHelper.SKIP,
                 tax_exempt_reason=APIHelper.SKIP,
                 default_auto_renewal_profile_id=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the Customer class"""

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
        if id is not APIHelper.SKIP:
            self.id = id 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if address is not APIHelper.SKIP:
            self.address = address 
        if address_2 is not APIHelper.SKIP:
            self.address_2 = address_2 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if state_name is not APIHelper.SKIP:
            self.state_name = state_name 
        if zip is not APIHelper.SKIP:
            self.zip = zip 
        if country is not APIHelper.SKIP:
            self.country = country 
        if country_name is not APIHelper.SKIP:
            self.country_name = country_name 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if verified is not APIHelper.SKIP:
            self.verified = verified 
        if portal_customer_created_at is not APIHelper.SKIP:
            self.portal_customer_created_at = APIHelper.apply_datetime_converter(portal_customer_created_at, APIHelper.RFC3339DateTime) if portal_customer_created_at else None 
        if portal_invite_last_sent_at is not APIHelper.SKIP:
            self.portal_invite_last_sent_at = APIHelper.apply_datetime_converter(portal_invite_last_sent_at, APIHelper.RFC3339DateTime) if portal_invite_last_sent_at else None 
        if portal_invite_last_accepted_at is not APIHelper.SKIP:
            self.portal_invite_last_accepted_at = APIHelper.apply_datetime_converter(portal_invite_last_accepted_at, APIHelper.RFC3339DateTime) if portal_invite_last_accepted_at else None 
        if tax_exempt is not APIHelper.SKIP:
            self.tax_exempt = tax_exempt 
        if vat_number is not APIHelper.SKIP:
            self.vat_number = vat_number 
        if parent_id is not APIHelper.SKIP:
            self.parent_id = parent_id 
        if locale is not APIHelper.SKIP:
            self.locale = locale 
        if default_subscription_group_uid is not APIHelper.SKIP:
            self.default_subscription_group_uid = default_subscription_group_uid 
        if salesforce_id is not APIHelper.SKIP:
            self.salesforce_id = salesforce_id 
        if tax_exempt_reason is not APIHelper.SKIP:
            self.tax_exempt_reason = tax_exempt_reason 
        if default_auto_renewal_profile_id is not APIHelper.SKIP:
            self.default_auto_renewal_profile_id = default_auto_renewal_profile_id 

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
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        cc_emails = dictionary.get("cc_emails") if "cc_emails" in dictionary.keys() else APIHelper.SKIP
        organization = dictionary.get("organization") if "organization" in dictionary.keys() else APIHelper.SKIP
        reference = dictionary.get("reference") if "reference" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        address = dictionary.get("address") if "address" in dictionary.keys() else APIHelper.SKIP
        address_2 = dictionary.get("address_2") if "address_2" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get("city") if "city" in dictionary.keys() else APIHelper.SKIP
        state = dictionary.get("state") if "state" in dictionary.keys() else APIHelper.SKIP
        state_name = dictionary.get("state_name") if "state_name" in dictionary.keys() else APIHelper.SKIP
        zip = dictionary.get("zip") if "zip" in dictionary.keys() else APIHelper.SKIP
        country = dictionary.get("country") if "country" in dictionary.keys() else APIHelper.SKIP
        country_name = dictionary.get("country_name") if "country_name" in dictionary.keys() else APIHelper.SKIP
        phone = dictionary.get("phone") if "phone" in dictionary.keys() else APIHelper.SKIP
        verified = dictionary.get("verified") if "verified" in dictionary.keys() else APIHelper.SKIP
        if 'portal_customer_created_at' in dictionary.keys():
            portal_customer_created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("portal_customer_created_at")).datetime if dictionary.get("portal_customer_created_at") else None
        else:
            portal_customer_created_at = APIHelper.SKIP
        if 'portal_invite_last_sent_at' in dictionary.keys():
            portal_invite_last_sent_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("portal_invite_last_sent_at")).datetime if dictionary.get("portal_invite_last_sent_at") else None
        else:
            portal_invite_last_sent_at = APIHelper.SKIP
        if 'portal_invite_last_accepted_at' in dictionary.keys():
            portal_invite_last_accepted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("portal_invite_last_accepted_at")).datetime if dictionary.get("portal_invite_last_accepted_at") else None
        else:
            portal_invite_last_accepted_at = APIHelper.SKIP
        tax_exempt = dictionary.get("tax_exempt") if "tax_exempt" in dictionary.keys() else APIHelper.SKIP
        vat_number = dictionary.get("vat_number") if "vat_number" in dictionary.keys() else APIHelper.SKIP
        parent_id = dictionary.get("parent_id") if "parent_id" in dictionary.keys() else APIHelper.SKIP
        locale = dictionary.get("locale") if "locale" in dictionary.keys() else APIHelper.SKIP
        default_subscription_group_uid = dictionary.get("default_subscription_group_uid") if "default_subscription_group_uid" in dictionary.keys() else APIHelper.SKIP
        salesforce_id = dictionary.get("salesforce_id") if "salesforce_id" in dictionary.keys() else APIHelper.SKIP
        tax_exempt_reason = dictionary.get("tax_exempt_reason") if "tax_exempt_reason" in dictionary.keys() else APIHelper.SKIP
        default_auto_renewal_profile_id = dictionary.get("default_auto_renewal_profile_id") if "default_auto_renewal_profile_id" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   email,
                   cc_emails,
                   organization,
                   reference,
                   id,
                   created_at,
                   updated_at,
                   address,
                   address_2,
                   city,
                   state,
                   state_name,
                   zip,
                   country,
                   country_name,
                   phone,
                   verified,
                   portal_customer_created_at,
                   portal_invite_last_sent_at,
                   portal_invite_last_accepted_at,
                   tax_exempt,
                   vat_number,
                   parent_id,
                   locale,
                   default_subscription_group_uid,
                   salesforce_id,
                   tax_exempt_reason,
                   default_auto_renewal_profile_id,
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
