# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payment_type import PaymentType


class CreditCardPaymentProfile(object):

    """Implementation of the 'Credit Card Payment Profile' model.

    Attributes:
        id (int): The Chargify-assigned ID of the stored card. This value can
            be used as an input to payment_profile_id when creating a
            subscription, in order to re-use a stored payment profile for the
            same customer.
        first_name (str): The first name of the card holder.
        last_name (str): The last name of the card holder.
        masked_card_number (str): A string representation of the credit card
            number with all but the last 4 digits masked with X’s (i.e.
            ‘XXXX-XXXX-XXXX-1234’).
        card_type (CardType): The type of card used.
        expiration_month (int): An integer representing the expiration month
            of the card(1 – 12).
        expiration_year (int): An integer representing the 4-digit expiration
            year of the card(i.e. ‘2012’).
        customer_id (int): The Chargify-assigned id for the customer record to
            which the card belongs.
        current_vault (CreditCardVault): The vault that stores the payment
            profile with the provided `vault_token`. Use `bogus` for testing.
        vault_token (str): The “token” provided by your vault storage for an
            already stored payment profile.
        billing_address (str): The current billing street address for the card.
        billing_city (str): The current billing address city for the card.
        billing_state (str): The current billing address state for the card.
        billing_zip (str): The current billing address zip code for the card.
        billing_country (str): The current billing address country for the
            card.
        customer_vault_token (str): (only for Authorize.Net CIM storage): the
            customerProfileId for the owner of the customerPaymentProfileId
            provided as the vault_token.
        billing_address_2 (str): The current billing street address, second
            line, for the card.
        payment_type (PaymentType): The model property of type PaymentType.
        disabled (bool): The model property of type bool.
        chargify_token (str): Token received after sending billing information
            using chargify.js. This token will only be received if passed as a
            sole attribute of credit_card_attributes (i.e.
            tok_9g6hw85pnpt6knmskpwp4ttt)
        site_gateway_setting_id (int): The model property of type int.
        gateway_handle (str): An identifier of connected gateway.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": 'payment_type',
        "id": 'id',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "masked_card_number": 'masked_card_number',
        "card_type": 'card_type',
        "expiration_month": 'expiration_month',
        "expiration_year": 'expiration_year',
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
        "disabled": 'disabled',
        "chargify_token": 'chargify_token',
        "site_gateway_setting_id": 'site_gateway_setting_id',
        "gateway_handle": 'gateway_handle'
    }

    _optionals = [
        'id',
        'first_name',
        'last_name',
        'masked_card_number',
        'card_type',
        'expiration_month',
        'expiration_year',
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
        'disabled',
        'chargify_token',
        'site_gateway_setting_id',
        'gateway_handle',
    ]

    _nullables = [
        'vault_token',
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
                 payment_type='credit_card',
                 id=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 masked_card_number=APIHelper.SKIP,
                 card_type=APIHelper.SKIP,
                 expiration_month=APIHelper.SKIP,
                 expiration_year=APIHelper.SKIP,
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
                 disabled=APIHelper.SKIP,
                 chargify_token=APIHelper.SKIP,
                 site_gateway_setting_id=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreditCardPaymentProfile class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if masked_card_number is not APIHelper.SKIP:
            self.masked_card_number = masked_card_number 
        if card_type is not APIHelper.SKIP:
            self.card_type = card_type 
        if expiration_month is not APIHelper.SKIP:
            self.expiration_month = expiration_month 
        if expiration_year is not APIHelper.SKIP:
            self.expiration_year = expiration_year 
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
        self.payment_type = payment_type 
        if disabled is not APIHelper.SKIP:
            self.disabled = disabled 
        if chargify_token is not APIHelper.SKIP:
            self.chargify_token = chargify_token 
        if site_gateway_setting_id is not APIHelper.SKIP:
            self.site_gateway_setting_id = site_gateway_setting_id 
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
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else 'credit_card'
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else APIHelper.SKIP
        card_type = dictionary.get("card_type") if dictionary.get("card_type") else APIHelper.SKIP
        expiration_month = dictionary.get("expiration_month") if dictionary.get("expiration_month") else APIHelper.SKIP
        expiration_year = dictionary.get("expiration_year") if dictionary.get("expiration_year") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        vault_token = dictionary.get("vault_token") if "vault_token" in dictionary.keys() else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if "billing_address" in dictionary.keys() else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if "billing_city" in dictionary.keys() else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if "billing_state" in dictionary.keys() else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if "billing_zip" in dictionary.keys() else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if "billing_country" in dictionary.keys() else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if "customer_vault_token" in dictionary.keys() else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if "billing_address_2" in dictionary.keys() else APIHelper.SKIP
        disabled = dictionary.get("disabled") if "disabled" in dictionary.keys() else APIHelper.SKIP
        chargify_token = dictionary.get("chargify_token") if dictionary.get("chargify_token") else APIHelper.SKIP
        site_gateway_setting_id = dictionary.get("site_gateway_setting_id") if "site_gateway_setting_id" in dictionary.keys() else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payment_type,
                   id,
                   first_name,
                   last_name,
                   masked_card_number,
                   card_type,
                   expiration_month,
                   expiration_year,
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
                   disabled,
                   chargify_token,
                   site_gateway_setting_id,
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
            return APIHelper.is_valid_type(value=dictionary.payment_type,
                                           type_callable=lambda value: PaymentType.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('payment_type'),
                                       type_callable=lambda value: PaymentType.validate(value))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'first_name={self.first_name!r}, '
                f'last_name={self.last_name!r}, '
                f'masked_card_number={self.masked_card_number!r}, '
                f'card_type={self.card_type!r}, '
                f'expiration_month={self.expiration_month!r}, '
                f'expiration_year={self.expiration_year!r}, '
                f'customer_id={self.customer_id!r}, '
                f'current_vault={self.current_vault!r}, '
                f'vault_token={self.vault_token!r}, '
                f'billing_address={self.billing_address!r}, '
                f'billing_city={self.billing_city!r}, '
                f'billing_state={self.billing_state!r}, '
                f'billing_zip={self.billing_zip!r}, '
                f'billing_country={self.billing_country!r}, '
                f'customer_vault_token={self.customer_vault_token!r}, '
                f'billing_address_2={self.billing_address_2!r}, '
                f'payment_type={self.payment_type!r}, '
                f'disabled={self.disabled!r}, '
                f'chargify_token={self.chargify_token!r}, '
                f'site_gateway_setting_id={self.site_gateway_setting_id!r}, '
                f'gateway_handle={self.gateway_handle!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'first_name={self.first_name!s}, '
                f'last_name={self.last_name!s}, '
                f'masked_card_number={self.masked_card_number!s}, '
                f'card_type={self.card_type!s}, '
                f'expiration_month={self.expiration_month!s}, '
                f'expiration_year={self.expiration_year!s}, '
                f'customer_id={self.customer_id!s}, '
                f'current_vault={self.current_vault!s}, '
                f'vault_token={self.vault_token!s}, '
                f'billing_address={self.billing_address!s}, '
                f'billing_city={self.billing_city!s}, '
                f'billing_state={self.billing_state!s}, '
                f'billing_zip={self.billing_zip!s}, '
                f'billing_country={self.billing_country!s}, '
                f'customer_vault_token={self.customer_vault_token!s}, '
                f'billing_address_2={self.billing_address_2!s}, '
                f'payment_type={self.payment_type!s}, '
                f'disabled={self.disabled!s}, '
                f'chargify_token={self.chargify_token!s}, '
                f'site_gateway_setting_id={self.site_gateway_setting_id!s}, '
                f'gateway_handle={self.gateway_handle!s}, '
                f'additional_properties={self.additional_properties!s})')
