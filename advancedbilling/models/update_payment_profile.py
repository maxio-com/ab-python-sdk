# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdatePaymentProfile(object):

    """Implementation of the 'Update Payment Profile' model.

    TODO: type model description here.

    Attributes:
        first_name (str): The first name of the card holder.
        last_name (str): The last name of the card holder.
        full_number (str): The full credit card number
        card_type (CardType): The type of card used.
        expiration_month (str): (Optional when performing an Import via
            vault_token, required otherwise) The 1- or 2-digit credit card
            expiration month, as an integer or string, i.e. 5
        expiration_year (str): (Optional when performing a Import via
            vault_token, required otherwise) The 4-digit credit card
            expiration year, as an integer or string, i.e. 2012
        current_vault (AllVaults): The vault that stores the payment profile
            with the provided `vault_token`. Use `bogus` for testing.
        billing_address (str): The credit card or bank account billing street
            address (i.e. 123 Main St.). This value is merely passed through
            to the payment gateway.
        billing_city (str): The credit card or bank account billing address
            city (i.e. “Boston”). This value is merely passed through to the
            payment gateway.
        billing_state (str): The credit card or bank account billing address
            state (i.e. MA). This value is merely passed through to the
            payment gateway. This must conform to the
            [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes
            ) in order to be valid for tax locale purposes.
        billing_zip (str): The credit card or bank account billing address zip
            code (i.e. 12345). This value is merely passed through to the
            payment gateway.
        billing_country (str): The credit card or bank account billing address
            country, required in [ISO_3166-1
            alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format
            (i.e. “US”). This value is merely passed through to the payment
            gateway. Some gateways require country codes in a specific format.
            Please check your gateway’s documentation. If creating an ACH
            subscription, only US is supported at this time.
        billing_address_2 (str): Second line of the customer’s billing address
            i.e. Apt. 100
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'first_name',
        "last_name": 'last_name',
        "full_number": 'full_number',
        "card_type": 'card_type',
        "expiration_month": 'expiration_month',
        "expiration_year": 'expiration_year',
        "current_vault": 'current_vault',
        "billing_address": 'billing_address',
        "billing_city": 'billing_city',
        "billing_state": 'billing_state',
        "billing_zip": 'billing_zip',
        "billing_country": 'billing_country',
        "billing_address_2": 'billing_address_2'
    }

    _optionals = [
        'first_name',
        'last_name',
        'full_number',
        'card_type',
        'expiration_month',
        'expiration_year',
        'current_vault',
        'billing_address',
        'billing_city',
        'billing_state',
        'billing_zip',
        'billing_country',
        'billing_address_2',
    ]

    _nullables = [
        'billing_address_2',
    ]

    def __init__(self,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 full_number=APIHelper.SKIP,
                 card_type=APIHelper.SKIP,
                 expiration_month=APIHelper.SKIP,
                 expiration_year=APIHelper.SKIP,
                 current_vault=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 billing_city=APIHelper.SKIP,
                 billing_state=APIHelper.SKIP,
                 billing_zip=APIHelper.SKIP,
                 billing_country=APIHelper.SKIP,
                 billing_address_2=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the UpdatePaymentProfile class"""

        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if full_number is not APIHelper.SKIP:
            self.full_number = full_number 
        if card_type is not APIHelper.SKIP:
            self.card_type = card_type 
        if expiration_month is not APIHelper.SKIP:
            self.expiration_month = expiration_month 
        if expiration_year is not APIHelper.SKIP:
            self.expiration_year = expiration_year 
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if billing_city is not APIHelper.SKIP:
            self.billing_city = billing_city 
        if billing_state is not APIHelper.SKIP:
            self.billing_state = billing_state 
        if billing_zip is not APIHelper.SKIP:
            self.billing_zip = billing_zip 
        if billing_country is not APIHelper.SKIP:
            self.billing_country = billing_country 
        if billing_address_2 is not APIHelper.SKIP:
            self.billing_address_2 = billing_address_2 

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
        full_number = dictionary.get("full_number") if dictionary.get("full_number") else APIHelper.SKIP
        card_type = dictionary.get("card_type") if dictionary.get("card_type") else APIHelper.SKIP
        expiration_month = dictionary.get("expiration_month") if dictionary.get("expiration_month") else APIHelper.SKIP
        expiration_year = dictionary.get("expiration_year") if dictionary.get("expiration_year") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if dictionary.get("billing_address") else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if dictionary.get("billing_city") else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if dictionary.get("billing_state") else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if dictionary.get("billing_zip") else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if dictionary.get("billing_country") else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if "billing_address_2" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   full_number,
                   card_type,
                   expiration_month,
                   expiration_year,
                   current_vault,
                   billing_address,
                   billing_city,
                   billing_state,
                   billing_zip,
                   billing_country,
                   billing_address_2,
                   additional_properties)
