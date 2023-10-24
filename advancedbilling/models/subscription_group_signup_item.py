# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.calendar_billing import CalendarBilling
from advancedbilling.models.custom_price_used_for_subscription_create_update import CustomPriceUsedForSubscriptionCreateUpdate
from advancedbilling.models.subscription_group_signup_component import SubscriptionGroupSignupComponent


class SubscriptionGroupSignupItem(object):

    """Implementation of the 'Subscription Group Signup Item' model.

    TODO: type model description here.

    Attributes:
        product_handle (str): The API Handle of the product for which you are
            creating a subscription. Required, unless a `product_id` is given
            instead.
        product_id (int): The Product ID of the product for which you are
            creating a subscription. You can pass either `product_id` or
            `product_handle`.
        product_price_point_id (int): The ID of the particular price point on
            the product.
        product_price_point_handle (str): The user-friendly API handle of a
            product's particular price point.
        offer_id (int): Use in place of passing product and component
            information to set up the subscription with an existing offer. May
            be either the Chargify ID of the offer or its handle prefixed with
            `handle:`
        reference (str): The reference value (provided by your app) for the
            subscription itelf.
        primary (bool): One of the subscriptions must be marked as primary in
            the group.
        currency (str): (Optional) If Multi-Currency is enabled and the
            currency is configured in Chargify, pass it at signup to create a
            subscription on a non-default currency. Note that you cannot
            update the currency of an existing subscription.
        coupon_codes (List[str]): An array for all the coupons attached to the
            subscription.
        components (List[SubscriptionGroupSignupComponent]): TODO: type
            description here.
        custom_price (CustomPriceUsedForSubscriptionCreateUpdate): (Optional)
            Used in place of `product_price_point_id` to define a custom price
            point unique to the subscription
        calendar_billing (CalendarBilling): (Optional). Cannot be used when
            also specifying next_billing_at
        metafields (Dict[str, str]): (Optional) A set of key/value pairs
            representing custom fields and their values. Metafields will be
            created “on-the-fly” in your site for a given key, if they have
            not been created yet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_handle": 'product_handle',
        "product_id": 'product_id',
        "product_price_point_id": 'product_price_point_id',
        "product_price_point_handle": 'product_price_point_handle',
        "offer_id": 'offer_id',
        "reference": 'reference',
        "primary": 'primary',
        "currency": 'currency',
        "coupon_codes": 'coupon_codes',
        "components": 'components',
        "custom_price": 'custom_price',
        "calendar_billing": 'calendar_billing',
        "metafields": 'metafields'
    }

    _optionals = [
        'product_handle',
        'product_id',
        'product_price_point_id',
        'product_price_point_handle',
        'offer_id',
        'reference',
        'primary',
        'currency',
        'coupon_codes',
        'components',
        'custom_price',
        'calendar_billing',
        'metafields',
    ]

    def __init__(self,
                 product_handle=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 product_price_point_handle=APIHelper.SKIP,
                 offer_id=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 primary=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 coupon_codes=APIHelper.SKIP,
                 components=APIHelper.SKIP,
                 custom_price=APIHelper.SKIP,
                 calendar_billing=APIHelper.SKIP,
                 metafields=APIHelper.SKIP):
        """Constructor for the SubscriptionGroupSignupItem class"""

        # Initialize members of the class
        if product_handle is not APIHelper.SKIP:
            self.product_handle = product_handle 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if product_price_point_handle is not APIHelper.SKIP:
            self.product_price_point_handle = product_price_point_handle 
        if offer_id is not APIHelper.SKIP:
            self.offer_id = offer_id 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if primary is not APIHelper.SKIP:
            self.primary = primary 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if coupon_codes is not APIHelper.SKIP:
            self.coupon_codes = coupon_codes 
        if components is not APIHelper.SKIP:
            self.components = components 
        if custom_price is not APIHelper.SKIP:
            self.custom_price = custom_price 
        if calendar_billing is not APIHelper.SKIP:
            self.calendar_billing = calendar_billing 
        if metafields is not APIHelper.SKIP:
            self.metafields = metafields 

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
        product_handle = dictionary.get("product_handle") if dictionary.get("product_handle") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        product_price_point_handle = dictionary.get("product_price_point_handle") if dictionary.get("product_price_point_handle") else APIHelper.SKIP
        offer_id = dictionary.get("offer_id") if dictionary.get("offer_id") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        primary = dictionary.get("primary") if "primary" in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        coupon_codes = dictionary.get("coupon_codes") if dictionary.get("coupon_codes") else APIHelper.SKIP
        components = None
        if dictionary.get('components') is not None:
            components = [SubscriptionGroupSignupComponent.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        custom_price = CustomPriceUsedForSubscriptionCreateUpdate.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        calendar_billing = CalendarBilling.from_dictionary(dictionary.get('calendar_billing')) if 'calendar_billing' in dictionary.keys() else APIHelper.SKIP
        metafields = dictionary.get("metafields") if dictionary.get("metafields") else APIHelper.SKIP
        # Return an object of this model
        return cls(product_handle,
                   product_id,
                   product_price_point_id,
                   product_price_point_handle,
                   offer_id,
                   reference,
                   primary,
                   currency,
                   coupon_codes,
                   components,
                   custom_price,
                   calendar_billing,
                   metafields)
