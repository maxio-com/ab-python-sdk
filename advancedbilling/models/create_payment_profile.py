# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreatePaymentProfile(object):

    """Implementation of the 'Create Payment Profile' model.

    TODO: type model description here.

    Attributes:
        chargify_token (str): Token received after sending billing
            informations using chargify.js.
        id (int): TODO: type description here.
        payment_type (PaymentType): TODO: type description here.
        first_name (str): First name on card or bank account. If omitted, the
            first_name from customer attributes will be used.
        last_name (str): Last name on card or bank account. If omitted, the
            last_name from customer attributes will be used.
        masked_card_number (str): TODO: type description here.
        full_number (str): The full credit card number
        card_type (CardType): The type of card used.
        expiration_month (int | str | None): (Optional when performing an
            Import via vault_token, required otherwise) The 1- or 2-digit
            credit card expiration month, as an integer or string, i.e. 5
        expiration_year (int | str | None): (Optional when performing a Import
            via vault_token, required otherwise) The 4-digit credit card
            expiration year, as an integer or string, i.e. 2012
        billing_address (str): The credit card or bank account billing street
            address (i.e. 123 Main St.). This value is merely passed through
            to the payment gateway.
        billing_address_2 (str): Second line of the customer’s billing address
            i.e. Apt. 100
        billing_city (str): The credit card or bank account billing address
            city (i.e. “Boston”). This value is merely passed through to the
            payment gateway.
        billing_state (str): The credit card or bank account billing address
            state (i.e. MA). This value is merely passed through to the
            payment gateway. This must conform to the
            [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes
            ) in order to be valid for tax locale purposes.
        billing_country (str): The credit card or bank account billing address
            country, required in [ISO_3166-1
            alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format
            (i.e. “US”). This value is merely passed through to the payment
            gateway. Some gateways require country codes in a specific format.
            Please check your gateway’s documentation. If creating an ACH
            subscription, only US is supported at this time.
        billing_zip (str): The credit card or bank account billing address zip
            code (i.e. 12345). This value is merely passed through to the
            payment gateway.
        current_vault (AllVaults): The vault that stores the payment profile
            with the provided `vault_token`. Use `bogus` for testing.
        vault_token (str): The “token” provided by your vault storage for an
            already stored payment profile
        customer_vault_token (str): (only for Authorize.Net CIM storage or
            Square) The customerProfileId for the owner of the
            customerPaymentProfileId provided as the vault_token
        customer_id (int): (Required when creating a new payment profile) The
            Chargify customer id.
        paypal_email (str): used by merchants that implemented BraintreeBlue
            javaScript libraries on their own. We recommend using Chargify.js
            instead.
        payment_method_nonce (str): used by merchants that implemented
            BraintreeBlue javaScript libraries on their own. We recommend
            using Chargify.js instead.
        gateway_handle (str): This attribute is only available if MultiGateway
            feature is enabled for your Site. This feature is in the Private
            Beta currently. gateway_handle is used to directly select a
            gateway where a payment profile will be stored in. Every connected
            gateway must have a unique gateway handle specified. Read
            [Multigateway
            description](https://chargify.zendesk.com/hc/en-us/articles/4407761
            759643#connecting-with-multiple-gateways) to learn more about new
            concepts that MultiGateway introduces and the default behavior
            when this attribute is not passed.
        cvv (str): The 3- or 4-digit Card Verification Value. This value is
            merely passed through to the payment gateway.
        bank_name (str): (Required when creating with ACH or GoCardless,
            optional with Stripe Direct Debit). The name of the bank where the
            customerʼs account resides
        bank_iban (str): (Optional when creating with GoCardless, required
            with Stripe Direct Debit). International Bank Account Number.
            Alternatively, local bank details can be provided
        bank_routing_number (str): (Required when creating with ACH. Optional
            when creating a subscription with GoCardless). The routing number
            of the bank. It becomes bank_code while passing via GoCardless
            API
        bank_account_number (str): (Required when creating with ACH,
            GoCardless, Stripe BECS or BACS Direct Debit, and bank_iban is
            blank) The customerʼs bank account number
        bank_branch_code (str): (Optional when creating with GoCardless,
            required with Stripe BECS or BACS Direct Debit) Branch/Sort code.
            Alternatively, an IBAN can be provided
        bank_account_type (BankAccountType): Defaults to checking
        bank_account_holder_type (BankAccountHolderType): Defaults to
            personal
        last_four (str): (Optional) Used for creating subscription with
            payment profile imported using vault_token, for proper display in
            Advanced Billing UI

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chargify_token": 'chargify_token',
        "id": 'id',
        "payment_type": 'payment_type',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "masked_card_number": 'masked_card_number',
        "full_number": 'full_number',
        "card_type": 'card_type',
        "expiration_month": 'expiration_month',
        "expiration_year": 'expiration_year',
        "billing_address": 'billing_address',
        "billing_address_2": 'billing_address_2',
        "billing_city": 'billing_city',
        "billing_state": 'billing_state',
        "billing_country": 'billing_country',
        "billing_zip": 'billing_zip',
        "current_vault": 'current_vault',
        "vault_token": 'vault_token',
        "customer_vault_token": 'customer_vault_token',
        "customer_id": 'customer_id',
        "paypal_email": 'paypal_email',
        "payment_method_nonce": 'payment_method_nonce',
        "gateway_handle": 'gateway_handle',
        "cvv": 'cvv',
        "bank_name": 'bank_name',
        "bank_iban": 'bank_iban',
        "bank_routing_number": 'bank_routing_number',
        "bank_account_number": 'bank_account_number',
        "bank_branch_code": 'bank_branch_code',
        "bank_account_type": 'bank_account_type',
        "bank_account_holder_type": 'bank_account_holder_type',
        "last_four": 'last_four'
    }

    _optionals = [
        'chargify_token',
        'id',
        'payment_type',
        'first_name',
        'last_name',
        'masked_card_number',
        'full_number',
        'card_type',
        'expiration_month',
        'expiration_year',
        'billing_address',
        'billing_address_2',
        'billing_city',
        'billing_state',
        'billing_country',
        'billing_zip',
        'current_vault',
        'vault_token',
        'customer_vault_token',
        'customer_id',
        'paypal_email',
        'payment_method_nonce',
        'gateway_handle',
        'cvv',
        'bank_name',
        'bank_iban',
        'bank_routing_number',
        'bank_account_number',
        'bank_branch_code',
        'bank_account_type',
        'bank_account_holder_type',
        'last_four',
    ]

    _nullables = [
        'billing_address_2',
    ]

    def __init__(self,
                 chargify_token=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 masked_card_number=APIHelper.SKIP,
                 full_number=APIHelper.SKIP,
                 card_type=APIHelper.SKIP,
                 expiration_month=APIHelper.SKIP,
                 expiration_year=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 billing_address_2=APIHelper.SKIP,
                 billing_city=APIHelper.SKIP,
                 billing_state=APIHelper.SKIP,
                 billing_country=APIHelper.SKIP,
                 billing_zip=APIHelper.SKIP,
                 current_vault=APIHelper.SKIP,
                 vault_token=APIHelper.SKIP,
                 customer_vault_token=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 paypal_email=APIHelper.SKIP,
                 payment_method_nonce=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 cvv=APIHelper.SKIP,
                 bank_name=APIHelper.SKIP,
                 bank_iban=APIHelper.SKIP,
                 bank_routing_number=APIHelper.SKIP,
                 bank_account_number=APIHelper.SKIP,
                 bank_branch_code=APIHelper.SKIP,
                 bank_account_type=APIHelper.SKIP,
                 bank_account_holder_type=APIHelper.SKIP,
                 last_four=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CreatePaymentProfile class"""

        # Initialize members of the class
        if chargify_token is not APIHelper.SKIP:
            self.chargify_token = chargify_token 
        if id is not APIHelper.SKIP:
            self.id = id 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if masked_card_number is not APIHelper.SKIP:
            self.masked_card_number = masked_card_number 
        if full_number is not APIHelper.SKIP:
            self.full_number = full_number 
        if card_type is not APIHelper.SKIP:
            self.card_type = card_type 
        if expiration_month is not APIHelper.SKIP:
            self.expiration_month = expiration_month 
        if expiration_year is not APIHelper.SKIP:
            self.expiration_year = expiration_year 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if billing_address_2 is not APIHelper.SKIP:
            self.billing_address_2 = billing_address_2 
        if billing_city is not APIHelper.SKIP:
            self.billing_city = billing_city 
        if billing_state is not APIHelper.SKIP:
            self.billing_state = billing_state 
        if billing_country is not APIHelper.SKIP:
            self.billing_country = billing_country 
        if billing_zip is not APIHelper.SKIP:
            self.billing_zip = billing_zip 
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault 
        if vault_token is not APIHelper.SKIP:
            self.vault_token = vault_token 
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if paypal_email is not APIHelper.SKIP:
            self.paypal_email = paypal_email 
        if payment_method_nonce is not APIHelper.SKIP:
            self.payment_method_nonce = payment_method_nonce 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 
        if cvv is not APIHelper.SKIP:
            self.cvv = cvv 
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name 
        if bank_iban is not APIHelper.SKIP:
            self.bank_iban = bank_iban 
        if bank_routing_number is not APIHelper.SKIP:
            self.bank_routing_number = bank_routing_number 
        if bank_account_number is not APIHelper.SKIP:
            self.bank_account_number = bank_account_number 
        if bank_branch_code is not APIHelper.SKIP:
            self.bank_branch_code = bank_branch_code 
        if bank_account_type is not APIHelper.SKIP:
            self.bank_account_type = bank_account_type 
        if bank_account_holder_type is not APIHelper.SKIP:
            self.bank_account_holder_type = bank_account_holder_type 
        if last_four is not APIHelper.SKIP:
            self.last_four = last_four 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        chargify_token = dictionary.get("chargify_token") if dictionary.get("chargify_token") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else APIHelper.SKIP
        full_number = dictionary.get("full_number") if dictionary.get("full_number") else APIHelper.SKIP
        card_type = dictionary.get("card_type") if dictionary.get("card_type") else APIHelper.SKIP
        expiration_month = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreatePaymentProfileExpirationMonth'), dictionary.get('expiration_month'), False) if dictionary.get('expiration_month') is not None else APIHelper.SKIP
        expiration_year = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreatePaymentProfileExpirationYear'), dictionary.get('expiration_year'), False) if dictionary.get('expiration_year') is not None else APIHelper.SKIP
        billing_address = dictionary.get("billing_address") if dictionary.get("billing_address") else APIHelper.SKIP
        billing_address_2 = dictionary.get("billing_address_2") if "billing_address_2" in dictionary.keys() else APIHelper.SKIP
        billing_city = dictionary.get("billing_city") if dictionary.get("billing_city") else APIHelper.SKIP
        billing_state = dictionary.get("billing_state") if dictionary.get("billing_state") else APIHelper.SKIP
        billing_country = dictionary.get("billing_country") if dictionary.get("billing_country") else APIHelper.SKIP
        billing_zip = dictionary.get("billing_zip") if dictionary.get("billing_zip") else APIHelper.SKIP
        current_vault = dictionary.get("current_vault") if dictionary.get("current_vault") else APIHelper.SKIP
        vault_token = dictionary.get("vault_token") if dictionary.get("vault_token") else APIHelper.SKIP
        customer_vault_token = dictionary.get("customer_vault_token") if dictionary.get("customer_vault_token") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        paypal_email = dictionary.get("paypal_email") if dictionary.get("paypal_email") else APIHelper.SKIP
        payment_method_nonce = dictionary.get("payment_method_nonce") if dictionary.get("payment_method_nonce") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if dictionary.get("gateway_handle") else APIHelper.SKIP
        cvv = dictionary.get("cvv") if dictionary.get("cvv") else APIHelper.SKIP
        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else APIHelper.SKIP
        bank_iban = dictionary.get("bank_iban") if dictionary.get("bank_iban") else APIHelper.SKIP
        bank_routing_number = dictionary.get("bank_routing_number") if dictionary.get("bank_routing_number") else APIHelper.SKIP
        bank_account_number = dictionary.get("bank_account_number") if dictionary.get("bank_account_number") else APIHelper.SKIP
        bank_branch_code = dictionary.get("bank_branch_code") if dictionary.get("bank_branch_code") else APIHelper.SKIP
        bank_account_type = dictionary.get("bank_account_type") if dictionary.get("bank_account_type") else APIHelper.SKIP
        bank_account_holder_type = dictionary.get("bank_account_holder_type") if dictionary.get("bank_account_holder_type") else APIHelper.SKIP
        last_four = dictionary.get("last_four") if dictionary.get("last_four") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(chargify_token,
                   id,
                   payment_type,
                   first_name,
                   last_name,
                   masked_card_number,
                   full_number,
                   card_type,
                   expiration_month,
                   expiration_year,
                   billing_address,
                   billing_address_2,
                   billing_city,
                   billing_state,
                   billing_country,
                   billing_zip,
                   current_vault,
                   vault_token,
                   customer_vault_token,
                   customer_id,
                   paypal_email,
                   payment_method_nonce,
                   gateway_handle,
                   cvv,
                   bank_name,
                   bank_iban,
                   bank_routing_number,
                   bank_account_number,
                   bank_branch_code,
                   bank_account_type,
                   bank_account_holder_type,
                   last_four,
                   dictionary)
