# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.credit_card_attributes import CreditCardAttributes
from advancedbilling.models.subscription_custom_price import SubscriptionCustomPrice
from advancedbilling.models.update_subscription_component import UpdateSubscriptionComponent


class UpdateSubscription(object):

    """Implementation of the 'Update Subscription' model.

    TODO: type model description here.

    Attributes:
        credit_card_attributes (CreditCardAttributes): TODO: type description
            here.
        product_handle (str): Set to the handle of a different product to
            change the subscription's product
        product_id (int): Set to the id of a different product to change the
            subscription's product
        product_change_delayed (bool): TODO: type description here.
        next_product_id (str): Set to an empty string to cancel a delayed
            product change.
        next_product_price_point_id (str): TODO: type description here.
        snap_day (SnapDay | int | None): Use for subscriptions with product
            eligible for calendar billing only. Value can be 1-28 or 'end'.
        next_billing_at (str): TODO: type description here.
        payment_collection_method (str): TODO: type description here.
        receives_invoice_emails (bool): TODO: type description here.
        net_terms (str | int | None): TODO: type description here.
        stored_credential_transaction_id (int): TODO: type description here.
        reference (str): TODO: type description here.
        custom_price (SubscriptionCustomPrice): (Optional) Used in place of
            `product_price_point_id` to define a custom price point unique to
            the subscription
        components (List[UpdateSubscriptionComponent]): (Optional) An array of
            component ids and custom prices to be added to the subscription.
        dunning_communication_delay_enabled (bool): Enable Communication Delay
            feature, making sure no communication (email or SMS) is sent to
            the Customer between 9PM and 8AM in time zone set by the
            `dunning_communication_delay_time_zone` attribute.
        dunning_communication_delay_time_zone (str): Time zone for the Dunning
            Communication Delay feature.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credit_card_attributes": 'credit_card_attributes',
        "product_handle": 'product_handle',
        "product_id": 'product_id',
        "product_change_delayed": 'product_change_delayed',
        "next_product_id": 'next_product_id',
        "next_product_price_point_id": 'next_product_price_point_id',
        "snap_day": 'snap_day',
        "next_billing_at": 'next_billing_at',
        "payment_collection_method": 'payment_collection_method',
        "receives_invoice_emails": 'receives_invoice_emails',
        "net_terms": 'net_terms',
        "stored_credential_transaction_id": 'stored_credential_transaction_id',
        "reference": 'reference',
        "custom_price": 'custom_price',
        "components": 'components',
        "dunning_communication_delay_enabled": 'dunning_communication_delay_enabled',
        "dunning_communication_delay_time_zone": 'dunning_communication_delay_time_zone'
    }

    _optionals = [
        'credit_card_attributes',
        'product_handle',
        'product_id',
        'product_change_delayed',
        'next_product_id',
        'next_product_price_point_id',
        'snap_day',
        'next_billing_at',
        'payment_collection_method',
        'receives_invoice_emails',
        'net_terms',
        'stored_credential_transaction_id',
        'reference',
        'custom_price',
        'components',
        'dunning_communication_delay_enabled',
        'dunning_communication_delay_time_zone',
    ]

    _nullables = [
        'dunning_communication_delay_enabled',
        'dunning_communication_delay_time_zone',
    ]

    def __init__(self,
                 credit_card_attributes=APIHelper.SKIP,
                 product_handle=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_change_delayed=False,
                 next_product_id=APIHelper.SKIP,
                 next_product_price_point_id=APIHelper.SKIP,
                 snap_day=APIHelper.SKIP,
                 next_billing_at=APIHelper.SKIP,
                 payment_collection_method=APIHelper.SKIP,
                 receives_invoice_emails=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 stored_credential_transaction_id=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 custom_price=APIHelper.SKIP,
                 components=APIHelper.SKIP,
                 dunning_communication_delay_enabled=False,
                 dunning_communication_delay_time_zone=APIHelper.SKIP):
        """Constructor for the UpdateSubscription class"""

        # Initialize members of the class
        if credit_card_attributes is not APIHelper.SKIP:
            self.credit_card_attributes = credit_card_attributes 
        if product_handle is not APIHelper.SKIP:
            self.product_handle = product_handle 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        self.product_change_delayed = product_change_delayed 
        if next_product_id is not APIHelper.SKIP:
            self.next_product_id = next_product_id 
        if next_product_price_point_id is not APIHelper.SKIP:
            self.next_product_price_point_id = next_product_price_point_id 
        if snap_day is not APIHelper.SKIP:
            self.snap_day = snap_day 
        if next_billing_at is not APIHelper.SKIP:
            self.next_billing_at = next_billing_at 
        if payment_collection_method is not APIHelper.SKIP:
            self.payment_collection_method = payment_collection_method 
        if receives_invoice_emails is not APIHelper.SKIP:
            self.receives_invoice_emails = receives_invoice_emails 
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms 
        if stored_credential_transaction_id is not APIHelper.SKIP:
            self.stored_credential_transaction_id = stored_credential_transaction_id 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if custom_price is not APIHelper.SKIP:
            self.custom_price = custom_price 
        if components is not APIHelper.SKIP:
            self.components = components 
        self.dunning_communication_delay_enabled = dunning_communication_delay_enabled 
        if dunning_communication_delay_time_zone is not APIHelper.SKIP:
            self.dunning_communication_delay_time_zone = dunning_communication_delay_time_zone 

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
        credit_card_attributes = CreditCardAttributes.from_dictionary(dictionary.get('credit_card_attributes')) if 'credit_card_attributes' in dictionary.keys() else APIHelper.SKIP
        product_handle = dictionary.get("product_handle") if dictionary.get("product_handle") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_change_delayed = dictionary.get("product_change_delayed") if dictionary.get("product_change_delayed") else False
        next_product_id = dictionary.get("next_product_id") if dictionary.get("next_product_id") else APIHelper.SKIP
        next_product_price_point_id = dictionary.get("next_product_price_point_id") if dictionary.get("next_product_price_point_id") else APIHelper.SKIP
        snap_day = APIHelper.deserialize_union_type(UnionTypeLookUp.get('UpdateSubscriptionSnapDay'), dictionary.get('snap_day'), False) if dictionary.get('snap_day') is not None else APIHelper.SKIP
        next_billing_at = dictionary.get("next_billing_at") if dictionary.get("next_billing_at") else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else APIHelper.SKIP
        receives_invoice_emails = dictionary.get("receives_invoice_emails") if "receives_invoice_emails" in dictionary.keys() else APIHelper.SKIP
        net_terms = APIHelper.deserialize_union_type(UnionTypeLookUp.get('UpdateSubscriptionNetTerms'), dictionary.get('net_terms'), False) if dictionary.get('net_terms') is not None else APIHelper.SKIP
        stored_credential_transaction_id = dictionary.get("stored_credential_transaction_id") if dictionary.get("stored_credential_transaction_id") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        custom_price = SubscriptionCustomPrice.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        components = None
        if dictionary.get('components') is not None:
            components = [UpdateSubscriptionComponent.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        dunning_communication_delay_enabled = dictionary.get("dunning_communication_delay_enabled") if dictionary.get("dunning_communication_delay_enabled") else False
        dunning_communication_delay_time_zone = dictionary.get("dunning_communication_delay_time_zone") if "dunning_communication_delay_time_zone" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(credit_card_attributes,
                   product_handle,
                   product_id,
                   product_change_delayed,
                   next_product_id,
                   next_product_price_point_id,
                   snap_day,
                   next_billing_at,
                   payment_collection_method,
                   receives_invoice_emails,
                   net_terms,
                   stored_credential_transaction_id,
                   reference,
                   custom_price,
                   components,
                   dunning_communication_delay_enabled,
                   dunning_communication_delay_time_zone)
