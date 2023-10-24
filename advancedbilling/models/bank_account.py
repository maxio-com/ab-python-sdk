# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class BankAccount(object):

    """Implementation of the 'Bank Account' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        first_name (str): TODO: type description here.
        last_name (str): TODO: type description here.
        customer_id (int): TODO: type description here.
        current_vault (BankAccountVault): The vault that stores the payment
            profile with the provided vault_token.
        vault_token (str): TODO: type description here.
        billing_address (str): TODO: type description here.
        billing_city (str): TODO: type description here.
        billing_state (str): TODO: type description here.
        billing_zip (str): TODO: type description here.
        billing_country (str): TODO: type description here.
        customer_vault_token (str): TODO: type description here.
        billing_address_2 (str): TODO: type description here.
        bank_name (str): TODO: type description here.
        masked_bank_routing_number (str): TODO: type description here.
        masked_bank_account_number (str): TODO: type description here.
        bank_account_type (str): TODO: type description here.
        bank_account_holder_type (str): TODO: type description here.
        payment_type (str): TODO: type description here.
        verified (bool): denotes whether a bank account has been verified by
            providing the amounts of two small deposits made into the account
        site_gateway_setting_id (int): TODO: type description here.
        gateway_handle (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "customer_id": 'customer_id',
        "current_vault": 'current_vault',
        "vault_token": 'vault_token',
        "billing_address": 'billing_address',
        "billing_city": 'billing_city',
        "billing_state": 'billing_state',
        "billing_zip": 'billing_zip',
        "billing_country": 'billing_country',
        "customer_vault_token": 'customer_vault_token',
        "billing_address_2": 'billing_address_2',
        "bank_name": 'bank_name',
        "masked_bank_routing_number": 'masked_bank_routing_number',
        "masked_bank_account_number": 'masked_bank_account_number',
        "bank_account_type": 'bank_account_type',
        "bank_account_holder_type": 'bank_account_holder_type',
        "payment_type": 'payment_type',
        "verified": 'verified',
        "site_gateway_setting_id": 'site_gateway_setting_id',
        "gateway_handle": 'gateway_handle'
    }

    _optionals = [
        'id',
        'first_name',
        'last_name',
        'customer_id',
        'current_vault',
        'vault_token',
        'billing_address',
        'billing_city',
        'billing_state',
        'billing_zip',
        'billing_country',
        'customer_vault_token',
        'billing_address_2',
        'bank_name',
        'masked_bank_routing_number',
        'masked_bank_account_number',
        'bank_account_type',
        'bank_account_holder_type',
        'payment_type',
        'verified',
        'site_gateway_setting_id',
        'gateway_handle',
    ]

    _nullables = [
        'customer_vault_token',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 current_vault=APIHelper.SKIP,
                 vault_token=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 billing_city=APIHelper.SKIP,
                 billing_state=APIHelper.SKIP,
                 billing_zip=APIHelper.SKIP,
                 billing_country=APIHelper.SKIP,
                 customer_vault_token=APIHelper.SKIP,
                 billing_address_2=APIHelper.SKIP,
                 bank_name=APIHelper.SKIP,
                 masked_bank_routing_number=APIHelper.SKIP,
                 masked_bank_account_number=APIHelper.SKIP,
                 bank_account_type=APIHelper.SKIP,
                 bank_account_holder_type=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 verified=False,
                 site_gateway_setting_id=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP):
        """Constructor for the BankAccount class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault 
        if vault_token is not APIHelper.SKIP:
            self.vault_token = vault_token 
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
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token 
        if billing_address_2 is not APIHelper.SKIP:
            self.billing_address_2 = billing_address_2 
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name 
        if masked_bank_routing_number is not APIHelper.SKIP:
            self.masked_bank_routing_number = masked_bank_routing_number 
        if masked_bank_account_number is not APIHelper.SKIP:
            self.masked_bank_account_number = masked_bank_account_number 
        if bank_account_type is not APIHelper.SKIP:
            self.bank_account_type = bank_account_type 
        if bank_account_holder_type is not APIHelper.SKIP:
            self.bank_account_holder_type = bank_account_holder_type 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
        self.verified = verified 
        if site_gateway_setting_id is not APIHelper.SKIP:
            self.site_gateway_setting_id = site_gateway_setting_id 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        vault_token = dictionary.get("vault_token") if dictionary.get("vault_token") else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if dictionary.get("billing_address") else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if dictionary.get("billing_city") else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if dictionary.get("billing_state") else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if dictionary.get("billing_zip") else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if dictionary.get("billing_country") else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if "customer_vault_token" in dictionary.keys() else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if dictionary.get("billing_address_2") else APIHelper.SKIP
        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else APIHelper.SKIP
        masked_bank_routing_number = dictionary.get("masked_bank_routing_number") if dictionary.get("masked_bank_routing_number") else APIHelper.SKIP
        masked_bank_account_number = dictionary.get("masked_bank_account_number") if dictionary.get("masked_bank_account_number") else APIHelper.SKIP
        bank_account_type = dictionary.get("bank_account_type") if dictionary.get("bank_account_type") else APIHelper.SKIP
        bank_account_holder_type = dictionary.get("bank_account_holder_type") if dictionary.get("bank_account_holder_type") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        verified = dictionary.get("verified") if dictionary.get("verified") else False
        site_gateway_setting_id = dictionary.get("site_gateway_setting_id") if dictionary.get("site_gateway_setting_id") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if dictionary.get("gateway_handle") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   first_name,
                   last_name,
                   customer_id,
                   current_vault,
                   vault_token,
                   billing_address,
                   billing_city,
                   billing_state,
                   billing_zip,
                   billing_country,
                   customer_vault_token,
                   billing_address_2,
                   bank_name,
                   masked_bank_routing_number,
                   masked_bank_account_number,
                   bank_account_type,
                   bank_account_holder_type,
                   payment_type,
                   verified,
                   site_gateway_setting_id,
                   gateway_handle)
