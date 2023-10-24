# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionBankAccount(object):

    """Implementation of the 'Subscription Bank Account' model.

    TODO: type model description here.

    Attributes:
        bank_account_holder_type (str): Defaults to personal
        bank_account_type (str): Defaults to checking
        bank_name (str): The bank where the account resides
        billing_address (str): The current billing street address for the bank
            account
        billing_address_2 (str): The current billing street address, second
            line, for the bank account
        billing_city (str): The current billing address city for the bank
            account
        billing_state (str): The current billing address state for the bank
            account
        billing_zip (str): The current billing address zip code for the bank
            account
        billing_country (str): The current billing address country for the
            bank account
        current_vault (BankAccountVault): The vault that stores the payment
            profile with the provided vault_token.
        customer_id (int): The Chargify-assigned id for the customer record to
            which the bank account belongs
        customer_vault_token (str): (only for Authorize.Net CIM storage): the
            customerProfileId for the owner of the customerPaymentProfileId
            provided as the vault_token
        first_name (str): The first name of the bank account holder
        last_name (str): The last name of the bank account holder
        id (int): The Chargify-assigned ID of the stored bank account. This
            value can be used as an input to payment_profile_id when creating
            a subscription, in order to re-use a stored payment profile for
            the same customer
        masked_bank_account_number (str): A string representation of the
            stored bank account number with all but the last 4 digits marked
            with X’s (i.e. ‘XXXXXXX1111’)
        masked_bank_routing_number (str): A string representation of the
            stored bank routing number with all but the last 4 digits marked
            with X’s (i.e. ‘XXXXXXX1111’). payment_type will be bank_account
        vault_token (str): The “token” provided by your vault storage for an
            already stored payment profile
        chargify_token (str): Token received after sending billing
            informations using chargify.js. This token will only be received
            if passed as a sole attribute of credit_card_attributes (i.e.
            tok_9g6hw85pnpt6knmskpwp4ttt)
        site_gateway_setting_id (int): TODO: type description here.
        gateway_handle (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_account_holder_type": 'bank_account_holder_type',
        "bank_account_type": 'bank_account_type',
        "bank_name": 'bank_name',
        "billing_address": 'billing_address',
        "billing_address_2": 'billing_address_2',
        "billing_city": 'billing_city',
        "billing_state": 'billing_state',
        "billing_zip": 'billing_zip',
        "billing_country": 'billing_country',
        "current_vault": 'current_vault',
        "customer_id": 'customer_id',
        "customer_vault_token": 'customer_vault_token',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "id": 'id',
        "masked_bank_account_number": 'masked_bank_account_number',
        "masked_bank_routing_number": 'masked_bank_routing_number',
        "vault_token": 'vault_token',
        "chargify_token": 'chargify_token',
        "site_gateway_setting_id": 'site_gateway_setting_id',
        "gateway_handle": 'gateway_handle'
    }

    _optionals = [
        'bank_account_holder_type',
        'bank_account_type',
        'bank_name',
        'billing_address',
        'billing_address_2',
        'billing_city',
        'billing_state',
        'billing_zip',
        'billing_country',
        'current_vault',
        'customer_id',
        'customer_vault_token',
        'first_name',
        'last_name',
        'id',
        'masked_bank_account_number',
        'masked_bank_routing_number',
        'vault_token',
        'chargify_token',
        'site_gateway_setting_id',
        'gateway_handle',
    ]

    def __init__(self,
                 bank_account_holder_type=APIHelper.SKIP,
                 bank_account_type=APIHelper.SKIP,
                 bank_name=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 billing_address_2=APIHelper.SKIP,
                 billing_city=APIHelper.SKIP,
                 billing_state=APIHelper.SKIP,
                 billing_zip=APIHelper.SKIP,
                 billing_country=APIHelper.SKIP,
                 current_vault=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 customer_vault_token=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 masked_bank_account_number=APIHelper.SKIP,
                 masked_bank_routing_number=APIHelper.SKIP,
                 vault_token=APIHelper.SKIP,
                 chargify_token=APIHelper.SKIP,
                 site_gateway_setting_id=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP):
        """Constructor for the SubscriptionBankAccount class"""

        # Initialize members of the class
        if bank_account_holder_type is not APIHelper.SKIP:
            self.bank_account_holder_type = bank_account_holder_type 
        if bank_account_type is not APIHelper.SKIP:
            self.bank_account_type = bank_account_type 
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if billing_address_2 is not APIHelper.SKIP:
            self.billing_address_2 = billing_address_2 
        if billing_city is not APIHelper.SKIP:
            self.billing_city = billing_city 
        if billing_state is not APIHelper.SKIP:
            self.billing_state = billing_state 
        if billing_zip is not APIHelper.SKIP:
            self.billing_zip = billing_zip 
        if billing_country is not APIHelper.SKIP:
            self.billing_country = billing_country 
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if id is not APIHelper.SKIP:
            self.id = id 
        if masked_bank_account_number is not APIHelper.SKIP:
            self.masked_bank_account_number = masked_bank_account_number 
        if masked_bank_routing_number is not APIHelper.SKIP:
            self.masked_bank_routing_number = masked_bank_routing_number 
        if vault_token is not APIHelper.SKIP:
            self.vault_token = vault_token 
        if chargify_token is not APIHelper.SKIP:
            self.chargify_token = chargify_token 
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
        bank_account_holder_type = dictionary.get("bank_account_holder_type") if dictionary.get("bank_account_holder_type") else APIHelper.SKIP
        bank_account_type = dictionary.get("bank_account_type") if dictionary.get("bank_account_type") else APIHelper.SKIP
        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if dictionary.get("billing_address") else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if dictionary.get("billing_address_2") else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if dictionary.get("billing_city") else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if dictionary.get("billing_state") else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if dictionary.get("billing_zip") else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if dictionary.get("billing_country") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if dictionary.get("customer_vault_token") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        masked_bank_account_number = dictionary.get("masked_bank_account_number") if dictionary.get("masked_bank_account_number") else APIHelper.SKIP
        masked_bank_routing_number = dictionary.get("masked_bank_routing_number") if dictionary.get("masked_bank_routing_number") else APIHelper.SKIP
        vault_token = dictionary.get("vault_token") if dictionary.get("vault_token") else APIHelper.SKIP
        chargify_token = dictionary.get("chargify_token") if dictionary.get("chargify_token") else APIHelper.SKIP
        site_gateway_setting_id = dictionary.get("site_gateway_setting_id") if dictionary.get("site_gateway_setting_id") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if dictionary.get("gateway_handle") else APIHelper.SKIP
        # Return an object of this model
        return cls(bank_account_holder_type,
                   bank_account_type,
                   bank_name,
                   billing_address,
                   billing_address_2,
                   billing_city,
                   billing_state,
                   billing_zip,
                   billing_country,
                   current_vault,
                   customer_id,
                   customer_vault_token,
                   first_name,
                   last_name,
                   id,
                   masked_bank_account_number,
                   masked_bank_routing_number,
                   vault_token,
                   chargify_token,
                   site_gateway_setting_id,
                   gateway_handle)
