# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class BankAccountAttributes(object):

    """Implementation of the 'Bank Account Attributes' model.

    TODO: type model description here.

    Attributes:
        chargify_token (str): TODO: type description here.
        bank_name (str): (Required when creating a subscription with ACH or
            GoCardless) The name of the bank where the customer’s account
            resides
        bank_routing_number (str): (Required when creating a subscription with
            ACH. Optional when creating a subscription with GoCardless). The
            routing number of the bank. It becomes bank_code while passing via
            GoCardless API
        bank_account_number (str): (Required when creating a subscription with
            ACH. Required when creating a subscription with GoCardless and
            bank_iban is blank) The customerʼs bank account number
        bank_account_type (BankAccountType): Defaults to checking
        bank_branch_code (str): (Optional when creating a subscription with
            GoCardless) Branch code. Alternatively, an IBAN can be provided
        bank_iban (str): (Optional when creating a subscription with
            GoCardless). International Bank Account Number. Alternatively,
            local bank details can be provided
        bank_account_holder_type (BankAccountHolderType): Defaults to
            personal
        payment_type (PaymentType): TODO: type description here.
        current_vault (BankAccountVault): The vault that stores the payment
            profile with the provided vault_token.
        vault_token (str): TODO: type description here.
        customer_vault_token (str): (only for Authorize.Net CIM storage or
            Square) The customerProfileId for the owner of the
            customerPaymentProfileId provided as the vault_token

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify_token": 'chargify_token',
        "bank_name": 'bank_name',
        "bank_routing_number": 'bank_routing_number',
        "bank_account_number": 'bank_account_number',
        "bank_account_type": 'bank_account_type',
        "bank_branch_code": 'bank_branch_code',
        "bank_iban": 'bank_iban',
        "bank_account_holder_type": 'bank_account_holder_type',
        "payment_type": 'payment_type',
        "current_vault": 'current_vault',
        "vault_token": 'vault_token',
        "customer_vault_token": 'customer_vault_token'
    }

    _optionals = [
        'chargify_token',
        'bank_name',
        'bank_routing_number',
        'bank_account_number',
        'bank_account_type',
        'bank_branch_code',
        'bank_iban',
        'bank_account_holder_type',
        'payment_type',
        'current_vault',
        'vault_token',
        'customer_vault_token',
    ]

    def __init__(self,
                 chargify_token=APIHelper.SKIP,
                 bank_name=APIHelper.SKIP,
                 bank_routing_number=APIHelper.SKIP,
                 bank_account_number=APIHelper.SKIP,
                 bank_account_type=APIHelper.SKIP,
                 bank_branch_code=APIHelper.SKIP,
                 bank_iban=APIHelper.SKIP,
                 bank_account_holder_type=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 current_vault=APIHelper.SKIP,
                 vault_token=APIHelper.SKIP,
                 customer_vault_token=APIHelper.SKIP):
        """Constructor for the BankAccountAttributes class"""

        # Initialize members of the class
        if chargify_token is not APIHelper.SKIP:
            self.chargify_token = chargify_token 
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name 
        if bank_routing_number is not APIHelper.SKIP:
            self.bank_routing_number = bank_routing_number 
        if bank_account_number is not APIHelper.SKIP:
            self.bank_account_number = bank_account_number 
        if bank_account_type is not APIHelper.SKIP:
            self.bank_account_type = bank_account_type 
        if bank_branch_code is not APIHelper.SKIP:
            self.bank_branch_code = bank_branch_code 
        if bank_iban is not APIHelper.SKIP:
            self.bank_iban = bank_iban 
        if bank_account_holder_type is not APIHelper.SKIP:
            self.bank_account_holder_type = bank_account_holder_type 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault 
        if vault_token is not APIHelper.SKIP:
            self.vault_token = vault_token 
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token 

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
        chargify_token = dictionary.get("chargify_token") if dictionary.get("chargify_token") else APIHelper.SKIP
        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else APIHelper.SKIP
        bank_routing_number = dictionary.get("bank_routing_number") if dictionary.get("bank_routing_number") else APIHelper.SKIP
        bank_account_number = dictionary.get("bank_account_number") if dictionary.get("bank_account_number") else APIHelper.SKIP
        bank_account_type = dictionary.get("bank_account_type") if dictionary.get("bank_account_type") else APIHelper.SKIP
        bank_branch_code = dictionary.get("bank_branch_code") if dictionary.get("bank_branch_code") else APIHelper.SKIP
        bank_iban = dictionary.get("bank_iban") if dictionary.get("bank_iban") else APIHelper.SKIP
        bank_account_holder_type = dictionary.get("bank_account_holder_type") if dictionary.get("bank_account_holder_type") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        vault_token = dictionary.get("vault_token") if dictionary.get("vault_token") else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if dictionary.get("customer_vault_token") else APIHelper.SKIP
        # Return an object of this model
        return cls(chargify_token,
                   bank_name,
                   bank_routing_number,
                   bank_account_number,
                   bank_account_type,
                   bank_branch_code,
                   bank_iban,
                   bank_account_holder_type,
                   payment_type,
                   current_vault,
                   vault_token,
                   customer_vault_token)

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
