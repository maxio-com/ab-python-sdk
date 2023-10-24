# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payer_attributes import PayerAttributes
from advancedbilling.models.subscription_group_bank_account import SubscriptionGroupBankAccount
from advancedbilling.models.subscription_group_credit_card import SubscriptionGroupCreditCard
from advancedbilling.models.subscription_group_signup_item import SubscriptionGroupSignupItem


class SubscriptionGroupSignup(object):

    """Implementation of the 'Subscription Group Signup' model.

    TODO: type model description here.

    Attributes:
        payment_profile_id (int): TODO: type description here.
        payer_id (int): TODO: type description here.
        payer_reference (str): TODO: type description here.
        payment_collection_method (PaymentCollectionMethod): The type of
            payment collection to be used in the subscription. For legacy
            Statements Architecture valid options are - `invoice`,
            `automatic`. For current Relationship Invoicing Architecture valid
            options are - `remittance`, `automatic`, `prepaid`.
        payer_attributes (PayerAttributes): TODO: type description here.
        credit_card_attributes (SubscriptionGroupCreditCard): TODO: type
            description here.
        bank_account_attributes (SubscriptionGroupBankAccount): TODO: type
            description here.
        subscriptions (List[SubscriptionGroupSignupItem]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscriptions": 'subscriptions',
        "payment_profile_id": 'payment_profile_id',
        "payer_id": 'payer_id',
        "payer_reference": 'payer_reference',
        "payment_collection_method": 'payment_collection_method',
        "payer_attributes": 'payer_attributes',
        "credit_card_attributes": 'credit_card_attributes',
        "bank_account_attributes": 'bank_account_attributes'
    }

    _optionals = [
        'payment_profile_id',
        'payer_id',
        'payer_reference',
        'payment_collection_method',
        'payer_attributes',
        'credit_card_attributes',
        'bank_account_attributes',
    ]

    def __init__(self,
                 subscriptions=None,
                 payment_profile_id=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_reference=APIHelper.SKIP,
                 payment_collection_method='automatic',
                 payer_attributes=APIHelper.SKIP,
                 credit_card_attributes=APIHelper.SKIP,
                 bank_account_attributes=APIHelper.SKIP):
        """Constructor for the SubscriptionGroupSignup class"""

        # Initialize members of the class
        if payment_profile_id is not APIHelper.SKIP:
            self.payment_profile_id = payment_profile_id 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_reference is not APIHelper.SKIP:
            self.payer_reference = payer_reference 
        self.payment_collection_method = payment_collection_method 
        if payer_attributes is not APIHelper.SKIP:
            self.payer_attributes = payer_attributes 
        if credit_card_attributes is not APIHelper.SKIP:
            self.credit_card_attributes = credit_card_attributes 
        if bank_account_attributes is not APIHelper.SKIP:
            self.bank_account_attributes = bank_account_attributes 
        self.subscriptions = subscriptions 

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
        subscriptions = None
        if dictionary.get('subscriptions') is not None:
            subscriptions = [SubscriptionGroupSignupItem.from_dictionary(x) for x in dictionary.get('subscriptions')]
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        payer_id = dictionary.get("payer_id") if dictionary.get("payer_id") else APIHelper.SKIP
        payer_reference = dictionary.get("payer_reference") if dictionary.get("payer_reference") else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else 'automatic'
        payer_attributes = PayerAttributes.from_dictionary(dictionary.get('payer_attributes')) if 'payer_attributes' in dictionary.keys() else APIHelper.SKIP
        credit_card_attributes = SubscriptionGroupCreditCard.from_dictionary(dictionary.get('credit_card_attributes')) if 'credit_card_attributes' in dictionary.keys() else APIHelper.SKIP
        bank_account_attributes = SubscriptionGroupBankAccount.from_dictionary(dictionary.get('bank_account_attributes')) if 'bank_account_attributes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(subscriptions,
                   payment_profile_id,
                   payer_id,
                   payer_reference,
                   payment_collection_method,
                   payer_attributes,
                   credit_card_attributes,
                   bank_account_attributes)
