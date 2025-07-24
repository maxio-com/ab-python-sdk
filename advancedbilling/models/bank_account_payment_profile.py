# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payment_type import PaymentType


class BankAccountPaymentProfile(object):

    """Implementation of the 'Bank Account Payment Profile' model.

    Attributes:
        id (int): The Chargify-assigned ID of the stored bank account. This
            value can be used as an input to payment_profile_id when creating
            a subscription, in order to re-use a stored payment profile for
            the same customer
        first_name (str): The first name of the bank account holder
        last_name (str): The last name of the bank account holder
        customer_id (int): The Chargify-assigned id for the customer record to
            which the bank account belongs
        current_vault (BankAccountVault): The vault that stores the payment
            profile with the provided vault_token. Use `bogus` for testing.
        vault_token (str): The “token” provided by your vault storage for an
            already stored payment profile
        billing_address (str): The current billing street address for the bank
            account
        billing_city (str): The current billing address city for the bank
            account
        billing_state (str): The current billing address state for the bank
            account
        billing_zip (str): The current billing address zip code for the bank
            account
        billing_country (str): The current billing address country for the
            bank account
        customer_vault_token (str): (only for Authorize.Net CIM storage): the
            customerProfileId for the owner of the customerPaymentProfileId
            provided as the vault_token.
        billing_address_2 (str): The current billing street address, second
            line, for the bank account
        bank_name (str): The bank where the account resides
        masked_bank_routing_number (str): A string representation of the
            stored bank routing number with all but the last 4 digits marked
            with X’s (i.e. ‘XXXXXXX1111’). payment_type will be bank_account
        masked_bank_account_number (str): A string representation of the
            stored bank account number with all but the last 4 digits marked
            with X’s (i.e. ‘XXXXXXX1111’)
        bank_account_type (BankAccountType): Defaults to checking
        bank_account_holder_type (BankAccountHolderType): Defaults to personal
        payment_type (PaymentType): The model property of type PaymentType.
        verified (bool): denotes whether a bank account has been verified by
            providing the amounts of two small deposits made into the account
        site_gateway_setting_id (int): The model property of type int.
        gateway_handle (str): The model property of type str.
        created_at (datetime): A timestamp indicating when this payment
            profile was created
        updated_at (datetime): A timestamp indicating when this payment
            profile was last updated
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "masked_bank_account_number": 'masked_bank_account_number',
        "payment_type": 'payment_type',
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
        "bank_account_type": 'bank_account_type',
        "bank_account_holder_type": 'bank_account_holder_type',
        "verified": 'verified',
        "site_gateway_setting_id": 'site_gateway_setting_id',
        "gateway_handle": 'gateway_handle',
        "created_at": 'created_at',
        "updated_at": 'updated_at'
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
        'bank_account_type',
        'bank_account_holder_type',
        'verified',
        'site_gateway_setting_id',
        'gateway_handle',
        'created_at',
        'updated_at',
    ]

    _nullables = [
        'billing_address',
        'billing_city',
        'billing_state',
        'billing_zip',
        'billing_country',
        'customer_vault_token',
        'billing_address_2',
        'site_gateway_setting_id',
        'gateway_handle',
    ]

    def __init__(self,
                 masked_bank_account_number=None,
                 payment_type='bank_account',
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
                 bank_account_type=APIHelper.SKIP,
                 bank_account_holder_type=APIHelper.SKIP,
                 verified=False,
                 site_gateway_setting_id=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the BankAccountPaymentProfile class"""

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
        self.masked_bank_account_number = masked_bank_account_number 
        if bank_account_type is not APIHelper.SKIP:
            self.bank_account_type = bank_account_type 
        if bank_account_holder_type is not APIHelper.SKIP:
            self.bank_account_holder_type = bank_account_holder_type 
        self.payment_type = payment_type 
        self.verified = verified 
        if site_gateway_setting_id is not APIHelper.SKIP:
            self.site_gateway_setting_id = site_gateway_setting_id 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 

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
        masked_bank_account_number = dictionary.get("masked_bank_account_number") if dictionary.get("masked_bank_account_number") else None
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else 'bank_account'
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        vault_token = dictionary.get("vault_token") if dictionary.get("vault_token") else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if "billing_address" in dictionary.keys() else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if "billing_city" in dictionary.keys() else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if "billing_state" in dictionary.keys() else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if "billing_zip" in dictionary.keys() else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if "billing_country" in dictionary.keys() else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if "customer_vault_token" in dictionary.keys() else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if "billing_address_2" in dictionary.keys() else APIHelper.SKIP
        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else APIHelper.SKIP
        masked_bank_routing_number = dictionary.get("masked_bank_routing_number") if dictionary.get("masked_bank_routing_number") else APIHelper.SKIP
        bank_account_type = dictionary.get("bank_account_type") if dictionary.get("bank_account_type") else APIHelper.SKIP
        bank_account_holder_type = dictionary.get("bank_account_holder_type") if dictionary.get("bank_account_holder_type") else APIHelper.SKIP
        verified = dictionary.get("verified") if dictionary.get("verified") else False
        site_gateway_setting_id = dictionary.get("site_gateway_setting_id") if "site_gateway_setting_id" in dictionary.keys() else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(masked_bank_account_number,
                   payment_type,
                   id,
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
                   bank_account_type,
                   bank_account_holder_type,
                   verified,
                   site_gateway_setting_id,
                   gateway_handle,
                   created_at,
                   updated_at,
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
            return APIHelper.is_valid_type(value=dictionary.masked_bank_account_number,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.payment_type,
                                            type_callable=lambda value: PaymentType.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('masked_bank_account_number'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_type'),
                                        type_callable=lambda value: PaymentType.validate(value))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!r}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!r}, '
                f'customer_id={(self.customer_id if hasattr(self, "customer_id") else None)!r}, '
                f'current_vault={(self.current_vault if hasattr(self, "current_vault") else None)!r}, '
                f'vault_token={(self.vault_token if hasattr(self, "vault_token") else None)!r}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!r}, '
                f'billing_city={(self.billing_city if hasattr(self, "billing_city") else None)!r}, '
                f'billing_state={(self.billing_state if hasattr(self, "billing_state") else None)!r}, '
                f'billing_zip={(self.billing_zip if hasattr(self, "billing_zip") else None)!r}, '
                f'billing_country={(self.billing_country if hasattr(self, "billing_country") else None)!r}, '
                f'customer_vault_token={(self.customer_vault_token if hasattr(self, "customer_vault_token") else None)!r}, '
                f'billing_address_2={(self.billing_address_2 if hasattr(self, "billing_address_2") else None)!r}, '
                f'bank_name={(self.bank_name if hasattr(self, "bank_name") else None)!r}, '
                f'masked_bank_routing_number={(self.masked_bank_routing_number if hasattr(self, "masked_bank_routing_number") else None)!r}, '
                f'masked_bank_account_number={self.masked_bank_account_number!r}, '
                f'bank_account_type={(self.bank_account_type if hasattr(self, "bank_account_type") else None)!r}, '
                f'bank_account_holder_type={(self.bank_account_holder_type if hasattr(self, "bank_account_holder_type") else None)!r}, '
                f'payment_type={self.payment_type!r}, '
                f'verified={(self.verified if hasattr(self, "verified") else None)!r}, '
                f'site_gateway_setting_id={(self.site_gateway_setting_id if hasattr(self, "site_gateway_setting_id") else None)!r}, '
                f'gateway_handle={(self.gateway_handle if hasattr(self, "gateway_handle") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!s}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!s}, '
                f'customer_id={(self.customer_id if hasattr(self, "customer_id") else None)!s}, '
                f'current_vault={(self.current_vault if hasattr(self, "current_vault") else None)!s}, '
                f'vault_token={(self.vault_token if hasattr(self, "vault_token") else None)!s}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!s}, '
                f'billing_city={(self.billing_city if hasattr(self, "billing_city") else None)!s}, '
                f'billing_state={(self.billing_state if hasattr(self, "billing_state") else None)!s}, '
                f'billing_zip={(self.billing_zip if hasattr(self, "billing_zip") else None)!s}, '
                f'billing_country={(self.billing_country if hasattr(self, "billing_country") else None)!s}, '
                f'customer_vault_token={(self.customer_vault_token if hasattr(self, "customer_vault_token") else None)!s}, '
                f'billing_address_2={(self.billing_address_2 if hasattr(self, "billing_address_2") else None)!s}, '
                f'bank_name={(self.bank_name if hasattr(self, "bank_name") else None)!s}, '
                f'masked_bank_routing_number={(self.masked_bank_routing_number if hasattr(self, "masked_bank_routing_number") else None)!s}, '
                f'masked_bank_account_number={self.masked_bank_account_number!s}, '
                f'bank_account_type={(self.bank_account_type if hasattr(self, "bank_account_type") else None)!s}, '
                f'bank_account_holder_type={(self.bank_account_holder_type if hasattr(self, "bank_account_holder_type") else None)!s}, '
                f'payment_type={self.payment_type!s}, '
                f'verified={(self.verified if hasattr(self, "verified") else None)!s}, '
                f'site_gateway_setting_id={(self.site_gateway_setting_id if hasattr(self, "site_gateway_setting_id") else None)!s}, '
                f'gateway_handle={(self.gateway_handle if hasattr(self, "gateway_handle") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
