# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class GetOneTimeTokenPaymentProfile(object):

    """Implementation of the 'Get One Time Token Payment Profile' model.

    TODO: type model description here.

    Attributes:
        id (str): TODO: type description here.
        first_name (str): TODO: type description here.
        last_name (str): TODO: type description here.
        masked_card_number (str): TODO: type description here.
        card_type (str): TODO: type description here.
        expiration_month (float): TODO: type description here.
        expiration_year (float): TODO: type description here.
        customer_id (str): TODO: type description here.
        current_vault (CurrentVault): The vault that stores the payment
            profile with the provided `vault_token`. Use `bogus` for testing.
        vault_token (str): TODO: type description here.
        billing_address (str): TODO: type description here.
        billing_address_2 (str): TODO: type description here.
        billing_city (str): TODO: type description here.
        billing_country (str): TODO: type description here.
        billing_state (str): TODO: type description here.
        billing_zip (str): TODO: type description here.
        payment_type (str): TODO: type description here.
        disabled (bool): TODO: type description here.
        site_gateway_setting_id (int): TODO: type description here.
        customer_vault_token (str): TODO: type description here.
        gateway_handle (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'first_name',
        "last_name": 'last_name',
        "masked_card_number": 'masked_card_number',
        "card_type": 'card_type',
        "expiration_month": 'expiration_month',
        "expiration_year": 'expiration_year',
        "current_vault": 'current_vault',
        "vault_token": 'vault_token',
        "billing_address": 'billing_address',
        "billing_city": 'billing_city',
        "billing_country": 'billing_country',
        "billing_state": 'billing_state',
        "billing_zip": 'billing_zip',
        "payment_type": 'payment_type',
        "disabled": 'disabled',
        "site_gateway_setting_id": 'site_gateway_setting_id',
        "id": 'id',
        "customer_id": 'customer_id',
        "billing_address_2": 'billing_address_2',
        "customer_vault_token": 'customer_vault_token',
        "gateway_handle": 'gateway_handle'
    }

    _optionals = [
        'id',
        'customer_id',
        'billing_address_2',
        'customer_vault_token',
        'gateway_handle',
    ]

    _nullables = [
        'id',
        'customer_id',
        'customer_vault_token',
        'gateway_handle',
    ]

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 masked_card_number=None,
                 card_type=None,
                 expiration_month=None,
                 expiration_year=None,
                 current_vault=None,
                 vault_token=None,
                 billing_address=None,
                 billing_city=None,
                 billing_country=None,
                 billing_state=None,
                 billing_zip=None,
                 payment_type=None,
                 disabled=None,
                 site_gateway_setting_id=None,
                 id=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 billing_address_2=APIHelper.SKIP,
                 customer_vault_token=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP):
        """Constructor for the GetOneTimeTokenPaymentProfile class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        self.first_name = first_name 
        self.last_name = last_name 
        self.masked_card_number = masked_card_number 
        self.card_type = card_type 
        self.expiration_month = expiration_month 
        self.expiration_year = expiration_year 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        self.current_vault = current_vault 
        self.vault_token = vault_token 
        self.billing_address = billing_address 
        if billing_address_2 is not APIHelper.SKIP:
            self.billing_address_2 = billing_address_2 
        self.billing_city = billing_city 
        self.billing_country = billing_country 
        self.billing_state = billing_state 
        self.billing_zip = billing_zip 
        self.payment_type = payment_type 
        self.disabled = disabled 
        self.site_gateway_setting_id = site_gateway_setting_id 
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 

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
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else None
        card_type = dictionary.get("card_type") if dictionary.get("card_type") else None
        expiration_month = dictionary.get("expiration_month") if dictionary.get("expiration_month") else None
        expiration_year = dictionary.get("expiration_year") if dictionary.get("expiration_year") else None
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else None
        vault_token = dictionary.get("vault_token") if dictionary.get("vault_token") else None
        billing_address = dictionary.get("billing_address") if dictionary.get("billing_address") else None
        billing_city = dictionary.get("billing_city") if dictionary.get("billing_city") else None
        billing_country = dictionary.get("billing_country") if dictionary.get("billing_country") else None
        billing_state = dictionary.get("billing_state") if dictionary.get("billing_state") else None
        billing_zip = dictionary.get("billing_zip") if dictionary.get("billing_zip") else None
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else None
        disabled = dictionary.get("disabled") if "disabled" in dictionary.keys() else None
        site_gateway_setting_id = dictionary.get("site_gateway_setting_id") if dictionary.get("site_gateway_setting_id") else None
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if "customer_id" in dictionary.keys() else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if dictionary.get("billing_address_2") else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if "customer_vault_token" in dictionary.keys() else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   masked_card_number,
                   card_type,
                   expiration_month,
                   expiration_year,
                   current_vault,
                   vault_token,
                   billing_address,
                   billing_city,
                   billing_country,
                   billing_state,
                   billing_zip,
                   payment_type,
                   disabled,
                   site_gateway_setting_id,
                   id,
                   customer_id,
                   billing_address_2,
                   customer_vault_token,
                   gateway_handle)
