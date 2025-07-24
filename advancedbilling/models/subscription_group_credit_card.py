# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupCreditCard(object):

    """Implementation of the 'Subscription Group Credit Card' model.

    Attributes:
        chargify_token (str): The model property of type str.
        vault_token (str): The model property of type str.
        current_vault (CreditCardVault): The vault that stores the payment
            profile with the provided `vault_token`. Use `bogus` for testing.
        gateway_handle (str): The model property of type str.
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        billing_address (str): The model property of type str.
        billing_address_2 (str): The model property of type str.
        billing_city (str): The model property of type str.
        billing_state (str): The model property of type str.
        billing_zip (str): The model property of type str.
        billing_country (str): The model property of type str.
        full_number (str | int | None): The model property of type str | int |
            None.
        expiration_month (str | int | None): The model property of type str |
            int | None.
        expiration_year (str | int | None): The model property of type str |
            int | None.
        last_four (str): The model property of type str.
        card_type (CardType): The type of card used.
        customer_vault_token (str): The model property of type str.
        cvv (str): The model property of type str.
        payment_type (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify_token": 'chargify_token',
        "vault_token": 'vault_token',
        "current_vault": 'current_vault',
        "gateway_handle": 'gateway_handle',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "billing_address": 'billing_address',
        "billing_address_2": 'billing_address_2',
        "billing_city": 'billing_city',
        "billing_state": 'billing_state',
        "billing_zip": 'billing_zip',
        "billing_country": 'billing_country',
        "full_number": 'full_number',
        "expiration_month": 'expiration_month',
        "expiration_year": 'expiration_year',
        "last_four": 'last_four',
        "card_type": 'card_type',
        "customer_vault_token": 'customer_vault_token',
        "cvv": 'cvv',
        "payment_type": 'payment_type'
    }

    _optionals = [
        'chargify_token',
        'vault_token',
        'current_vault',
        'gateway_handle',
        'first_name',
        'last_name',
        'billing_address',
        'billing_address_2',
        'billing_city',
        'billing_state',
        'billing_zip',
        'billing_country',
        'full_number',
        'expiration_month',
        'expiration_year',
        'last_four',
        'card_type',
        'customer_vault_token',
        'cvv',
        'payment_type',
    ]

    def __init__(self,
                 chargify_token=APIHelper.SKIP,
                 vault_token=APIHelper.SKIP,
                 current_vault=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 billing_address_2=APIHelper.SKIP,
                 billing_city=APIHelper.SKIP,
                 billing_state=APIHelper.SKIP,
                 billing_zip=APIHelper.SKIP,
                 billing_country=APIHelper.SKIP,
                 full_number=APIHelper.SKIP,
                 expiration_month=APIHelper.SKIP,
                 expiration_year=APIHelper.SKIP,
                 last_four=APIHelper.SKIP,
                 card_type=APIHelper.SKIP,
                 customer_vault_token=APIHelper.SKIP,
                 cvv=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupCreditCard class"""

        # Initialize members of the class
        if chargify_token is not APIHelper.SKIP:
            self.chargify_token = chargify_token 
        if vault_token is not APIHelper.SKIP:
            self.vault_token = vault_token 
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
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
        if full_number is not APIHelper.SKIP:
            self.full_number = full_number 
        if expiration_month is not APIHelper.SKIP:
            self.expiration_month = expiration_month 
        if expiration_year is not APIHelper.SKIP:
            self.expiration_year = expiration_year 
        if last_four is not APIHelper.SKIP:
            self.last_four = last_four 
        if card_type is not APIHelper.SKIP:
            self.card_type = card_type 
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token 
        if cvv is not APIHelper.SKIP:
            self.cvv = cvv 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        chargify_token = dictionary.get("chargify_token") if dictionary.get("chargify_token") else APIHelper.SKIP
        vault_token = dictionary.get("vault_token") if dictionary.get("vault_token") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if dictionary.get("gateway_handle") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if dictionary.get("billing_address") else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if dictionary.get("billing_address_2") else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if dictionary.get("billing_city") else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if dictionary.get("billing_state") else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if dictionary.get("billing_zip") else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if dictionary.get("billing_country") else APIHelper.SKIP
        full_number = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupCreditCardFullNumber'), dictionary.get('full_number'), False) if dictionary.get('full_number') is not None else APIHelper.SKIP
        expiration_month = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupCreditCardExpirationMonth'), dictionary.get('expiration_month'), False) if dictionary.get('expiration_month') is not None else APIHelper.SKIP
        expiration_year = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionGroupCreditCardExpirationYear'), dictionary.get('expiration_year'), False) if dictionary.get('expiration_year') is not None else APIHelper.SKIP
        last_four = dictionary.get("last_four") if dictionary.get("last_four") else APIHelper.SKIP
        card_type = dictionary.get("card_type") if dictionary.get("card_type") else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if dictionary.get("customer_vault_token") else APIHelper.SKIP
        cvv = dictionary.get("cvv") if dictionary.get("cvv") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(chargify_token,
                   vault_token,
                   current_vault,
                   gateway_handle,
                   first_name,
                   last_name,
                   billing_address,
                   billing_address_2,
                   billing_city,
                   billing_state,
                   billing_zip,
                   billing_country,
                   full_number,
                   expiration_month,
                   expiration_year,
                   last_four,
                   card_type,
                   customer_vault_token,
                   cvv,
                   payment_type,
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
                f'chargify_token={(self.chargify_token if hasattr(self, "chargify_token") else None)!r}, '
                f'vault_token={(self.vault_token if hasattr(self, "vault_token") else None)!r}, '
                f'current_vault={(self.current_vault if hasattr(self, "current_vault") else None)!r}, '
                f'gateway_handle={(self.gateway_handle if hasattr(self, "gateway_handle") else None)!r}, '
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!r}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!r}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!r}, '
                f'billing_address_2={(self.billing_address_2 if hasattr(self, "billing_address_2") else None)!r}, '
                f'billing_city={(self.billing_city if hasattr(self, "billing_city") else None)!r}, '
                f'billing_state={(self.billing_state if hasattr(self, "billing_state") else None)!r}, '
                f'billing_zip={(self.billing_zip if hasattr(self, "billing_zip") else None)!r}, '
                f'billing_country={(self.billing_country if hasattr(self, "billing_country") else None)!r}, '
                f'full_number={(self.full_number if hasattr(self, "full_number") else None)!r}, '
                f'expiration_month={(self.expiration_month if hasattr(self, "expiration_month") else None)!r}, '
                f'expiration_year={(self.expiration_year if hasattr(self, "expiration_year") else None)!r}, '
                f'last_four={(self.last_four if hasattr(self, "last_four") else None)!r}, '
                f'card_type={(self.card_type if hasattr(self, "card_type") else None)!r}, '
                f'customer_vault_token={(self.customer_vault_token if hasattr(self, "customer_vault_token") else None)!r}, '
                f'cvv={(self.cvv if hasattr(self, "cvv") else None)!r}, '
                f'payment_type={(self.payment_type if hasattr(self, "payment_type") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'chargify_token={(self.chargify_token if hasattr(self, "chargify_token") else None)!s}, '
                f'vault_token={(self.vault_token if hasattr(self, "vault_token") else None)!s}, '
                f'current_vault={(self.current_vault if hasattr(self, "current_vault") else None)!s}, '
                f'gateway_handle={(self.gateway_handle if hasattr(self, "gateway_handle") else None)!s}, '
                f'first_name={(self.first_name if hasattr(self, "first_name") else None)!s}, '
                f'last_name={(self.last_name if hasattr(self, "last_name") else None)!s}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!s}, '
                f'billing_address_2={(self.billing_address_2 if hasattr(self, "billing_address_2") else None)!s}, '
                f'billing_city={(self.billing_city if hasattr(self, "billing_city") else None)!s}, '
                f'billing_state={(self.billing_state if hasattr(self, "billing_state") else None)!s}, '
                f'billing_zip={(self.billing_zip if hasattr(self, "billing_zip") else None)!s}, '
                f'billing_country={(self.billing_country if hasattr(self, "billing_country") else None)!s}, '
                f'full_number={(self.full_number if hasattr(self, "full_number") else None)!s}, '
                f'expiration_month={(self.expiration_month if hasattr(self, "expiration_month") else None)!s}, '
                f'expiration_year={(self.expiration_year if hasattr(self, "expiration_year") else None)!s}, '
                f'last_four={(self.last_four if hasattr(self, "last_four") else None)!s}, '
                f'card_type={(self.card_type if hasattr(self, "card_type") else None)!s}, '
                f'customer_vault_token={(self.customer_vault_token if hasattr(self, "customer_vault_token") else None)!s}, '
                f'cvv={(self.cvv if hasattr(self, "cvv") else None)!s}, '
                f'payment_type={(self.payment_type if hasattr(self, "payment_type") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
