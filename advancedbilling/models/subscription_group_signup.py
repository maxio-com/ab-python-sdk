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

    Attributes:
        payment_profile_id (int): The model property of type int.
        payer_id (int): The model property of type int.
        payer_reference (str): The model property of type str.
        payment_collection_method (CollectionMethod): The type of payment
            collection to be used in the subscription. For legacy Statements
            Architecture valid options are - `invoice`, `automatic`. For
            current Relationship Invoicing Architecture valid options are -
            `remittance`, `automatic`, `prepaid`.
        payer_attributes (PayerAttributes): The model property of type
            PayerAttributes.
        credit_card_attributes (SubscriptionGroupCreditCard): The model
            property of type SubscriptionGroupCreditCard.
        bank_account_attributes (SubscriptionGroupBankAccount): The model
            property of type SubscriptionGroupBankAccount.
        subscriptions (List[SubscriptionGroupSignupItem]): The model property
            of type List[SubscriptionGroupSignupItem].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 payment_collection_method=APIHelper.SKIP,
                 payer_attributes=APIHelper.SKIP,
                 credit_card_attributes=APIHelper.SKIP,
                 bank_account_attributes=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupSignup class"""

        # Initialize members of the class
        if payment_profile_id is not APIHelper.SKIP:
            self.payment_profile_id = payment_profile_id 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_reference is not APIHelper.SKIP:
            self.payer_reference = payer_reference 
        if payment_collection_method is not APIHelper.SKIP:
            self.payment_collection_method = payment_collection_method 
        if payer_attributes is not APIHelper.SKIP:
            self.payer_attributes = payer_attributes 
        if credit_card_attributes is not APIHelper.SKIP:
            self.credit_card_attributes = credit_card_attributes 
        if bank_account_attributes is not APIHelper.SKIP:
            self.bank_account_attributes = bank_account_attributes 
        self.subscriptions = subscriptions 

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
        subscriptions = None
        if dictionary.get('subscriptions') is not None:
            subscriptions = [SubscriptionGroupSignupItem.from_dictionary(x) for x in dictionary.get('subscriptions')]
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        payer_id = dictionary.get("payer_id") if dictionary.get("payer_id") else APIHelper.SKIP
        payer_reference = dictionary.get("payer_reference") if dictionary.get("payer_reference") else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else APIHelper.SKIP
        payer_attributes = PayerAttributes.from_dictionary(dictionary.get('payer_attributes')) if 'payer_attributes' in dictionary.keys() else APIHelper.SKIP
        credit_card_attributes = SubscriptionGroupCreditCard.from_dictionary(dictionary.get('credit_card_attributes')) if 'credit_card_attributes' in dictionary.keys() else APIHelper.SKIP
        bank_account_attributes = SubscriptionGroupBankAccount.from_dictionary(dictionary.get('bank_account_attributes')) if 'bank_account_attributes' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(subscriptions,
                   payment_profile_id,
                   payer_id,
                   payer_reference,
                   payment_collection_method,
                   payer_attributes,
                   credit_card_attributes,
                   bank_account_attributes,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'payment_profile_id={self.payment_profile_id!r}, '
                f'payer_id={self.payer_id!r}, '
                f'payer_reference={self.payer_reference!r}, '
                f'payment_collection_method={self.payment_collection_method!r}, '
                f'payer_attributes={self.payer_attributes!r}, '
                f'credit_card_attributes={self.credit_card_attributes!r}, '
                f'bank_account_attributes={self.bank_account_attributes!r}, '
                f'subscriptions={self.subscriptions!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'payment_profile_id={self.payment_profile_id!s}, '
                f'payer_id={self.payer_id!s}, '
                f'payer_reference={self.payer_reference!s}, '
                f'payment_collection_method={self.payment_collection_method!s}, '
                f'payer_attributes={self.payer_attributes!s}, '
                f'credit_card_attributes={self.credit_card_attributes!s}, '
                f'bank_account_attributes={self.bank_account_attributes!s}, '
                f'subscriptions={self.subscriptions!s}, '
                f'additional_properties={self.additional_properties!s})')
