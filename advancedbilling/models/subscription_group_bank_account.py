# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupBankAccount(object):

    """Implementation of the 'Subscription Group Bank Account' model.

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
        bank_account_holder_type (BankAccountHolderType): Defaults to personal
        payment_type (PaymentType): The model property of type PaymentType.
        billing_address (str): The model property of type str.
        billing_city (str): The model property of type str.
        billing_state (str): The model property of type str.
        billing_zip (str): The model property of type str.
        billing_country (str): The model property of type str.
        chargify_token (str): The model property of type str.
        current_vault (BankAccountVault): The vault that stores the payment
            profile with the provided vault_token. Use `bogus` for testing.
        gateway_handle (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                f'bank_name={self.bank_name!r}, '
                f'bank_account_number={self.bank_account_number!r}, '
                f'bank_routing_number={self.bank_routing_number!r}, '
                f'bank_iban={self.bank_iban!r}, '
                f'bank_branch_code={self.bank_branch_code!r}, '
                f'bank_account_type={self.bank_account_type!r}, '
                f'bank_account_holder_type={self.bank_account_holder_type!r}, '
                f'payment_type={self.payment_type!r}, '
                f'billing_address={self.billing_address!r}, '
                f'billing_city={self.billing_city!r}, '
                f'billing_state={self.billing_state!r}, '
                f'billing_zip={self.billing_zip!r}, '
                f'billing_country={self.billing_country!r}, '
                f'chargify_token={self.chargify_token!r}, '
                f'current_vault={self.current_vault!r}, '
                f'gateway_handle={self.gateway_handle!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'bank_name={self.bank_name!s}, '
                f'bank_account_number={self.bank_account_number!s}, '
                f'bank_routing_number={self.bank_routing_number!s}, '
                f'bank_iban={self.bank_iban!s}, '
                f'bank_branch_code={self.bank_branch_code!s}, '
                f'bank_account_type={self.bank_account_type!s}, '
                f'bank_account_holder_type={self.bank_account_holder_type!s}, '
                f'payment_type={self.payment_type!s}, '
                f'billing_address={self.billing_address!s}, '
                f'billing_city={self.billing_city!s}, '
                f'billing_state={self.billing_state!s}, '
                f'billing_zip={self.billing_zip!s}, '
                f'billing_country={self.billing_country!s}, '
                f'chargify_token={self.chargify_token!s}, '
                f'current_vault={self.current_vault!s}, '
                f'gateway_handle={self.gateway_handle!s}, '
                f'additional_properties={self.additional_properties!s})')
