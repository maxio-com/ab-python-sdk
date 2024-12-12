# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payment_type import PaymentType


class PaypalPaymentProfile(object):

    """Implementation of the 'Paypal Payment Profile' model.

    TODO: type model description here.

    Attributes:
        id (int): The Chargify-assigned ID of the stored PayPal payment
            profile.
        first_name (str): The first name of the PayPal account holder
        last_name (str): The last name of the PayPal account holder
        customer_id (int): The Chargify-assigned id for the customer record to
            which the PayPal account belongs
        current_vault (PayPalVault): The vault that stores the payment profile
            with the provided vault_token.
        vault_token (str): The “token” provided by your vault storage for an
            already stored payment profile
        billing_address (str): The current billing street address for the
            PayPal account
        billing_city (str): The current billing address city for the PayPal
            account
        billing_state (str): The current billing address state for the PayPal
            account
        billing_zip (str): The current billing address zip code for the PayPal
            account
        billing_country (str): The current billing address country for the
            PayPal account
        customer_vault_token (str): TODO: type description here.
        billing_address_2 (str): The current billing street address, second
            line, for the PayPal account
        payment_type (PaymentType): TODO: type description here.
        site_gateway_setting_id (int): TODO: type description here.
        gateway_handle (str): TODO: type description here.
        paypal_email (str): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
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
        "site_gateway_setting_id": 'site_gateway_setting_id',
        "gateway_handle": 'gateway_handle',
        "paypal_email": 'paypal_email'
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
        'site_gateway_setting_id',
        'gateway_handle',
        'paypal_email',
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
                 payment_type='paypal_account',
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
                 site_gateway_setting_id=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 paypal_email=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PaypalPaymentProfile class"""

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
        self.payment_type = payment_type 
        if site_gateway_setting_id is not APIHelper.SKIP:
            self.site_gateway_setting_id = site_gateway_setting_id 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 
        if paypal_email is not APIHelper.SKIP:
            self.paypal_email = paypal_email 

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
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else 'paypal_account'
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
        site_gateway_setting_id = dictionary.get("site_gateway_setting_id") if "site_gateway_setting_id" in dictionary.keys() else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        paypal_email = dictionary.get("paypal_email") if dictionary.get("paypal_email") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payment_type,
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
                   site_gateway_setting_id,
                   gateway_handle,
                   paypal_email,
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
