# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupBankAccount(object):

    """Implementation of the 'Subscription Group Bank Account' model.

    TODO: type model description here.

    Attributes:
        bank_name (str): (Required when creating a subscription with ACH or
            GoCardless) The name of the bank where the customer’s account
            resides
        bank_account_number (str): (Required when creating a subscription with
            ACH. Required when creating a subscription with GoCardless and
            bank_iban is blank) The customerʼs bank account number
        bank_routing_number (str): (Required when creating a subscription with
            ACH. Optional when creating a subscription with GoCardless). The
            routing number of the bank. It becomes bank_code while passing via
            GoCardless API
        bank_iban (str): (Optional when creating a subscription with
            GoCardless). International Bank Account Number. Alternatively,
            local bank details can be provided
        bank_branch_code (str): (Optional when creating a subscription with
            GoCardless) Branch code. Alternatively, an IBAN can be provided
        bank_account_type (BankAccountType): Defaults to checking
        bank_account_holder_type (BankAccountHolderType): Defaults to
            personal
        payment_type (PaymentType): TODO: type description here.
        billing_address (str): TODO: type description here.
        billing_city (str): TODO: type description here.
        billing_state (str): TODO: type description here.
        billing_zip (str): TODO: type description here.
        billing_country (str): TODO: type description here.
        chargify_token (str): TODO: type description here.
        current_vault (BankAccountVault): The vault that stores the payment
            profile with the provided vault_token.
        gateway_handle (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_name": 'bank_name',
        "bank_account_number": 'bank_account_number',
        "bank_routing_number": 'bank_routing_number',
        "bank_iban": 'bank_iban',
        "bank_branch_code": 'bank_branch_code',
        "bank_account_type": 'bank_account_type',
        "bank_account_holder_type": 'bank_account_holder_type',
        "payment_type": 'payment_type',
        "billing_address": 'billing_address',
        "billing_city": 'billing_city',
        "billing_state": 'billing_state',
        "billing_zip": 'billing_zip',
        "billing_country": 'billing_country',
        "chargify_token": 'chargify_token',
        "current_vault": 'current_vault',
        "gateway_handle": 'gateway_handle'
    }

    _optionals = [
        'bank_name',
        'bank_account_number',
        'bank_routing_number',
        'bank_iban',
        'bank_branch_code',
        'bank_account_type',
        'bank_account_holder_type',
        'payment_type',
        'billing_address',
        'billing_city',
        'billing_state',
        'billing_zip',
        'billing_country',
        'chargify_token',
        'current_vault',
        'gateway_handle',
    ]

    def __init__(self,
                 bank_name=APIHelper.SKIP,
                 bank_account_number=APIHelper.SKIP,
                 bank_routing_number=APIHelper.SKIP,
                 bank_iban=APIHelper.SKIP,
                 bank_branch_code=APIHelper.SKIP,
                 bank_account_type=APIHelper.SKIP,
                 bank_account_holder_type=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 billing_city=APIHelper.SKIP,
                 billing_state=APIHelper.SKIP,
                 billing_zip=APIHelper.SKIP,
                 billing_country=APIHelper.SKIP,
                 chargify_token=APIHelper.SKIP,
                 current_vault=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the SubscriptionGroupBankAccount class"""

        # Initialize members of the class
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name 
        if bank_account_number is not APIHelper.SKIP:
            self.bank_account_number = bank_account_number 
        if bank_routing_number is not APIHelper.SKIP:
            self.bank_routing_number = bank_routing_number 
        if bank_iban is not APIHelper.SKIP:
            self.bank_iban = bank_iban 
        if bank_branch_code is not APIHelper.SKIP:
            self.bank_branch_code = bank_branch_code 
        if bank_account_type is not APIHelper.SKIP:
            self.bank_account_type = bank_account_type 
        if bank_account_holder_type is not APIHelper.SKIP:
            self.bank_account_holder_type = bank_account_holder_type 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
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
        if chargify_token is not APIHelper.SKIP:
            self.chargify_token = chargify_token 
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 

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
        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else APIHelper.SKIP
        bank_account_number = dictionary.get("bank_account_number") if dictionary.get("bank_account_number") else APIHelper.SKIP
        bank_routing_number = dictionary.get("bank_routing_number") if dictionary.get("bank_routing_number") else APIHelper.SKIP
        bank_iban = dictionary.get("bank_iban") if dictionary.get("bank_iban") else APIHelper.SKIP
        bank_branch_code = dictionary.get("bank_branch_code") if dictionary.get("bank_branch_code") else APIHelper.SKIP
        bank_account_type = dictionary.get("bank_account_type") if dictionary.get("bank_account_type") else APIHelper.SKIP
        bank_account_holder_type = dictionary.get("bank_account_holder_type") if dictionary.get("bank_account_holder_type") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if dictionary.get("billing_address") else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if dictionary.get("billing_city") else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if dictionary.get("billing_state") else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if dictionary.get("billing_zip") else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if dictionary.get("billing_country") else APIHelper.SKIP
        chargify_token = dictionary.get("chargify_token") if dictionary.get("chargify_token") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if dictionary.get("gateway_handle") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(bank_name,
                   bank_account_number,
                   bank_routing_number,
                   bank_iban,
                   bank_branch_code,
                   bank_account_type,
                   bank_account_holder_type,
                   payment_type,
                   billing_address,
                   billing_city,
                   billing_state,
                   billing_zip,
                   billing_country,
                   chargify_token,
                   current_vault,
                   gateway_handle,
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
