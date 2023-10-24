# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentProfile(object):

    """Implementation of the 'Payment Profile' model.

    TODO: type model description here.

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
        current_vault (CurrentVault): The vault that stores the payment
            profile with the provided `vault_token`. Use `bogus` for testing.
        vault_token (str): The “token” provided by your vault storage for an
            already stored payment profile.
        billing_address (str): The current billing street address for the
            card.
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
        payment_type (PaymentType): TODO: type description here.
        disabled (bool): TODO: type description here.
        chargify_token (str): Token received after sending billing
            informations using chargify.js.
        site_gateway_setting_id (int): TODO: type description here.
        gateway_handle (str): An identifier of connected gateway.

    """

    # Create a mapping from Model property names to API property names
    _names = {
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
        "payment_type": 'payment_type',
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
        'payment_type',
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
        'gateway_handle',
    ]

    def __init__(self,
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
                 payment_type='credit_card',
                 disabled=APIHelper.SKIP,
                 chargify_token=APIHelper.SKIP,
                 site_gateway_setting_id=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP):
        """Constructor for the PaymentProfile class"""

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
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else 'credit_card'
        disabled = dictionary.get("disabled") if "disabled" in dictionary.keys() else APIHelper.SKIP
        chargify_token = dictionary.get("chargify_token") if dictionary.get("chargify_token") else APIHelper.SKIP
        site_gateway_setting_id = dictionary.get("site_gateway_setting_id") if dictionary.get("site_gateway_setting_id") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
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
                   payment_type,
                   disabled,
                   chargify_token,
                   site_gateway_setting_id,
                   gateway_handle)
