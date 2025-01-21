# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.bank_account_payment_profile import BankAccountPaymentProfile
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.nested_subscription_group import NestedSubscriptionGroup
from advancedbilling.models.prepaid_configuration import PrepaidConfiguration
from advancedbilling.models.product import Product
from advancedbilling.models.subscription_included_coupon import SubscriptionIncludedCoupon


class Subscription(object):

    """Implementation of the 'Subscription' model.

    Attributes:
        id (int): The subscription unique id within Chargify.
        state (SubscriptionState): The state of a subscription. * **Live
            States**     * `active` - A normal, active subscription. It is not
            in a trial and is paid and up to date.     * `assessing` - An
            internal (transient) state that indicates a subscription is in the
            middle of periodic assessment. Do not base any access decisions in
            your app on this state, as it may not always be exposed.     *
            `pending` - An internal (transient) state that indicates a
            subscription is in the creation process. Do not base any access
            decisions in your app on this state, as it may not always be
            exposed.     * `trialing` - A subscription in trialing state has a
            valid trial subscription. This type of subscription may transition
            to active once payment is received when the trial has ended.
            Otherwise, it may go to a Problem or End of Life state.     *
            `paused` - An internal state that indicates that your account with
            Advanced Billing is in arrears. * **Problem States**     *
            `past_due` - Indicates that the most recent payment has failed,
            and payment is past due for this subscription. If you have enabled
            our automated dunning, this subscription will be in the dunning
            process (additional status and callbacks from the dunning process
            will be available in the future). If you are handling dunning and
            payment updates yourself, you will want to use this state to
            initiate a payment update from your customers.     *
            `soft_failure` - Indicates that normal assessment/processing of
            the subscription has failed for a reason that cannot be fixed by
            the Customer. For example, a Soft Fail may result from a timeout
            at the gateway or incorrect credentials on your part. The
            subscriptions should be retried automatically. An interface is
            being built for you to review problems resulting from these events
            to take manual action when needed.     * `unpaid` - Indicates an
            unpaid subscription. A subscription is marked unpaid if the retry
            period expires and you have configured your
            [Dunning](https://maxio.zendesk.com/hc/en-us/articles/2428707658356
            5-Dunning-Overview) settings to have a Final Action of `mark the
            subscription unpaid`. * **End of Life States**     * `canceled` -
            Indicates a canceled subscription. This may happen at your request
            (via the API or the web interface) or due to the expiration of the
            [Dunning](https://maxio.zendesk.com/hc/en-us/articles/2428707658356
            5-Dunning-Overview) process without payment. See the
            [Reactivation](https://maxio.zendesk.com/hc/en-us/articles/24252109
            503629-Reactivating-and-Resuming) documentation for info on how to
            restart a canceled subscription.     While a subscription is
            canceled, its period will not advance, it will not accrue any new
            charges, and Advanced Billing will not attempt to collect the
            overdue balance.     * `expired` - Indicates a subscription that
            has expired due to running its normal life cycle. Some products
            may be configured to have an expiration period. An expired
            subscription then is one that stayed active until it fulfilled its
            full period.     * `failed_to_create` - Indicates that signup has
            failed. (You may see this state in a signup_failure webhook.)    
            * `on_hold` - Indicates that a subscription’s billing has been
            temporarily stopped. While it is expected that the subscription
            will resume and return to active status, this is still treated as
            an “End of Life” state because the customer is not paying for
            services during this time.     * `suspended` - Indicates that a
            prepaid subscription has used up all their prepayment balance. If
            a prepayment is applied, it will return to an active state.     *
            `trial_ended` - A subscription in a trial_ended state is a
            subscription that completed a no-obligation trial and did not have
            a card on file at the expiration of the trial period. See [Product
            Pricing – No Obligation
            Trials](https://maxio.zendesk.com/hc/en-us/articles/24261076617869-
            Product-Editing) for more details.  See [Subscription
            States](https://maxio.zendesk.com/hc/en-us/articles/24252119027853-
            Subscription-States) for more info about subscription states and
            state transitions.
        balance_in_cents (int): Gives the current outstanding subscription
            balance in the number of cents.
        total_revenue_in_cents (int): Gives the total revenue from the
            subscription in the number of cents.
        product_price_in_cents (int): (Added Nov 5 2013) The recurring amount
            of the product (and version),currently subscribed. NOTE: this may
            differ from the current price of,the product, if you’ve changed
            the price of the product but haven’t,moved this subscription to a
            newer version.
        product_version_number (int): The version of the product for the
            subscription. Note that this is a deprecated field kept for
            backwards-compatibility.
        current_period_ends_at (datetime): Timestamp relating to the end of
            the current (recurring) period (i.e.,when the next regularly
            scheduled attempted charge will occur)
        next_assessment_at (datetime): Timestamp that indicates when capture
            of payment will be tried or,retried. This value will usually track
            the current_period_ends_at, but,will diverge if a renewal payment
            fails and must be retried. In that,case, the
            current_period_ends_at will advance to the end of the next,period
            (time doesn’t stop because a payment was missed) but
            the,next_assessment_at will be scheduled for the auto-retry time
            (i.e. 24,hours in the future, in some cases)
        trial_started_at (datetime): Timestamp for when the trial period (if
            any) began
        trial_ended_at (datetime): Timestamp for when the trial period (if
            any) ended
        activated_at (datetime): Timestamp for when the subscription began
            (i.e. when it came out of trial, or when it began in the case of
            no trial)
        expires_at (datetime): Timestamp giving the expiration date of this
            subscription (if any)
        created_at (datetime): The creation date for this subscription
        updated_at (datetime): The date of last update for this subscription
        cancellation_message (str): Seller-provided reason for, or note about,
            the cancellation.
        cancellation_method (CancellationMethod): The process used to cancel
            the subscription, if the subscription has been canceled. It is nil
            if the subscription's state is not canceled.
        cancel_at_end_of_period (bool): Whether or not the subscription will
            (or has) canceled at the end of the period.
        canceled_at (datetime): The timestamp of the most recent cancellation
        current_period_started_at (datetime): Timestamp relating to the start
            of the current (recurring) period
        previous_state (SubscriptionState): Only valid for webhook payloads
            The previous state for webhooks that have indicated a change in
            state. For normal API calls, this will always be the same as the
            state (current state)
        signup_payment_id (int): The ID of the transaction that generated the
            revenue
        signup_revenue (str): The revenue, formatted as a string of decimal
            separated dollars and,cents, from the subscription signup ($50.00
            would be formatted as,50.00)
        delayed_cancel_at (datetime): Timestamp for when the subscription is
            currently set to cancel.
        coupon_code (str): (deprecated) The coupon code of the single coupon
            currently applied to the subscription. See coupon_codes instead as
            subscriptions can now have more than one coupon.
        snap_day (str): The day of the month that the subscription will charge
            according to calendar billing rules, if used.
        payment_collection_method (CollectionMethod): The type of payment
            collection to be used in the subscription. For legacy Statements
            Architecture valid options are - `invoice`, `automatic`. For
            current Relationship Invoicing Architecture valid options are -
            `remittance`, `automatic`, `prepaid`.
        customer (Customer): The model property of type Customer.
        product (Product): The model property of type Product.
        credit_card (CreditCardPaymentProfile): The model property of type
            CreditCardPaymentProfile.
        group (NestedSubscriptionGroup): The model property of type
            NestedSubscriptionGroup.
        bank_account (BankAccountPaymentProfile): The model property of type
            BankAccountPaymentProfile.
        payment_type (str): The payment profile type for the active profile on
            file.
        referral_code (str): The subscription's unique code that can be given
            to referrals.
        next_product_id (int): If a delayed product change is scheduled, the
            ID of the product that the subscription will be changed to at the
            next renewal.
        next_product_handle (str): If a delayed product change is scheduled,
            the handle of the product that the subscription will be changed to
            at the next renewal.
        coupon_use_count (int): (deprecated) How many times the subscription's
            single coupon has been used. This field has no replacement for
            multiple coupons.
        coupon_uses_allowed (int): (deprecated) How many times the
            subscription's single coupon may be used. This field has no
            replacement for multiple coupons.
        reason_code (str): If the subscription is canceled, this is their
            churn code.
        automatically_resume_at (datetime): The date the subscription is
            scheduled to automatically resume from the on_hold state.
        coupon_codes (List[str]): An array for all the coupons attached to the
            subscription.
        offer_id (int): The ID of the offer associated with the subscription.
        payer_id (int): On Relationship Invoicing, the ID of the individual
            paying for the subscription. Defaults to the Customer ID unless
            the 'Customer Hierarchies & WhoPays' feature is enabled.
        current_billing_amount_in_cents (int): The balance in cents plus the
            estimated renewal amount in cents. Returned ONLY for
            readSubscription operation as it's compute intensive operation.
        product_price_point_id (int): The product price point currently
            subscribed to.
        product_price_point_type (PricePointType): Price point type. We expose
            the following types: 1. **default**: a price point that is marked
            as a default price for a certain product. 2. **custom**: a custom
            price point. 3. **catalog**: a price point that is **not** marked
            as a default price for a certain product and is **not** a custom
            one.
        next_product_price_point_id (int): If a delayed product change is
            scheduled, the ID of the product price point that the subscription
            will be changed to at the next renewal.
        net_terms (int): On Relationship Invoicing, the number of days before
            a renewal invoice is due.
        stored_credential_transaction_id (int): For European sites subject to
            PSD2 and using 3D Secure, this can be used to reference a previous
            transaction for the customer. This will ensure the card will be
            charged successfully at renewal.
        reference (str): The reference value (provided by your app) for the
            subscription itelf.
        on_hold_at (datetime): The timestamp of the most recent on hold action.
        prepaid_dunning (bool): Boolean representing whether the subscription
            is prepaid and currently in dunning. Only returned for
            Relationship Invoicing sites with the feature enabled
        coupons (List[SubscriptionIncludedCoupon]): Additional coupon data. To
            use this data you also have to include the following param in the
            request`include[]=coupons`. Only in Read Subscription Endpoint.
        dunning_communication_delay_enabled (bool): Enable Communication Delay
            feature, making sure no communication (email or SMS) is sent to
            the Customer between 9PM and 8AM in time zone set by the
            `dunning_communication_delay_time_zone` attribute.
        dunning_communication_delay_time_zone (str): Time zone for the Dunning
            Communication Delay feature.
        receives_invoice_emails (bool): The model property of type bool.
        locale (str): The model property of type str.
        currency (str): The model property of type str.
        scheduled_cancellation_at (datetime): The model property of type
            datetime.
        credit_balance_in_cents (int): The model property of type int.
        prepayment_balance_in_cents (int): The model property of type int.
        prepaid_configuration (PrepaidConfiguration): The model property of
            type PrepaidConfiguration.
        self_service_page_token (str): Returned only for list/read
            Subscription operation when `include[]=self_service_page_token`
            parameter is provided.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "state": 'state',
        "balance_in_cents": 'balance_in_cents',
        "total_revenue_in_cents": 'total_revenue_in_cents',
        "product_price_in_cents": 'product_price_in_cents',
        "product_version_number": 'product_version_number',
        "current_period_ends_at": 'current_period_ends_at',
        "next_assessment_at": 'next_assessment_at',
        "trial_started_at": 'trial_started_at',
        "trial_ended_at": 'trial_ended_at',
        "activated_at": 'activated_at',
        "expires_at": 'expires_at',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "cancellation_message": 'cancellation_message',
        "cancellation_method": 'cancellation_method',
        "cancel_at_end_of_period": 'cancel_at_end_of_period',
        "canceled_at": 'canceled_at',
        "current_period_started_at": 'current_period_started_at',
        "previous_state": 'previous_state',
        "signup_payment_id": 'signup_payment_id',
        "signup_revenue": 'signup_revenue',
        "delayed_cancel_at": 'delayed_cancel_at',
        "coupon_code": 'coupon_code',
        "snap_day": 'snap_day',
        "payment_collection_method": 'payment_collection_method',
        "customer": 'customer',
        "product": 'product',
        "credit_card": 'credit_card',
        "group": 'group',
        "bank_account": 'bank_account',
        "payment_type": 'payment_type',
        "referral_code": 'referral_code',
        "next_product_id": 'next_product_id',
        "next_product_handle": 'next_product_handle',
        "coupon_use_count": 'coupon_use_count',
        "coupon_uses_allowed": 'coupon_uses_allowed',
        "reason_code": 'reason_code',
        "automatically_resume_at": 'automatically_resume_at',
        "coupon_codes": 'coupon_codes',
        "offer_id": 'offer_id',
        "payer_id": 'payer_id',
        "current_billing_amount_in_cents": 'current_billing_amount_in_cents',
        "product_price_point_id": 'product_price_point_id',
        "product_price_point_type": 'product_price_point_type',
        "next_product_price_point_id": 'next_product_price_point_id',
        "net_terms": 'net_terms',
        "stored_credential_transaction_id": 'stored_credential_transaction_id',
        "reference": 'reference',
        "on_hold_at": 'on_hold_at',
        "prepaid_dunning": 'prepaid_dunning',
        "coupons": 'coupons',
        "dunning_communication_delay_enabled": 'dunning_communication_delay_enabled',
        "dunning_communication_delay_time_zone": 'dunning_communication_delay_time_zone',
        "receives_invoice_emails": 'receives_invoice_emails',
        "locale": 'locale',
        "currency": 'currency',
        "scheduled_cancellation_at": 'scheduled_cancellation_at',
        "credit_balance_in_cents": 'credit_balance_in_cents',
        "prepayment_balance_in_cents": 'prepayment_balance_in_cents',
        "prepaid_configuration": 'prepaid_configuration',
        "self_service_page_token": 'self_service_page_token'
    }

    _optionals = [
        'id',
        'state',
        'balance_in_cents',
        'total_revenue_in_cents',
        'product_price_in_cents',
        'product_version_number',
        'current_period_ends_at',
        'next_assessment_at',
        'trial_started_at',
        'trial_ended_at',
        'activated_at',
        'expires_at',
        'created_at',
        'updated_at',
        'cancellation_message',
        'cancellation_method',
        'cancel_at_end_of_period',
        'canceled_at',
        'current_period_started_at',
        'previous_state',
        'signup_payment_id',
        'signup_revenue',
        'delayed_cancel_at',
        'coupon_code',
        'snap_day',
        'payment_collection_method',
        'customer',
        'product',
        'credit_card',
        'group',
        'bank_account',
        'payment_type',
        'referral_code',
        'next_product_id',
        'next_product_handle',
        'coupon_use_count',
        'coupon_uses_allowed',
        'reason_code',
        'automatically_resume_at',
        'coupon_codes',
        'offer_id',
        'payer_id',
        'current_billing_amount_in_cents',
        'product_price_point_id',
        'product_price_point_type',
        'next_product_price_point_id',
        'net_terms',
        'stored_credential_transaction_id',
        'reference',
        'on_hold_at',
        'prepaid_dunning',
        'coupons',
        'dunning_communication_delay_enabled',
        'dunning_communication_delay_time_zone',
        'receives_invoice_emails',
        'locale',
        'currency',
        'scheduled_cancellation_at',
        'credit_balance_in_cents',
        'prepayment_balance_in_cents',
        'prepaid_configuration',
        'self_service_page_token',
    ]

    _nullables = [
        'current_period_ends_at',
        'next_assessment_at',
        'trial_started_at',
        'trial_ended_at',
        'activated_at',
        'expires_at',
        'cancellation_message',
        'cancellation_method',
        'cancel_at_end_of_period',
        'canceled_at',
        'current_period_started_at',
        'delayed_cancel_at',
        'coupon_code',
        'snap_day',
        'group',
        'payment_type',
        'referral_code',
        'next_product_id',
        'next_product_handle',
        'coupon_use_count',
        'coupon_uses_allowed',
        'reason_code',
        'automatically_resume_at',
        'offer_id',
        'payer_id',
        'next_product_price_point_id',
        'net_terms',
        'stored_credential_transaction_id',
        'reference',
        'on_hold_at',
        'dunning_communication_delay_time_zone',
        'receives_invoice_emails',
        'locale',
        'scheduled_cancellation_at',
        'prepaid_configuration',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 balance_in_cents=APIHelper.SKIP,
                 total_revenue_in_cents=APIHelper.SKIP,
                 product_price_in_cents=APIHelper.SKIP,
                 product_version_number=APIHelper.SKIP,
                 current_period_ends_at=APIHelper.SKIP,
                 next_assessment_at=APIHelper.SKIP,
                 trial_started_at=APIHelper.SKIP,
                 trial_ended_at=APIHelper.SKIP,
                 activated_at=APIHelper.SKIP,
                 expires_at=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 cancellation_message=APIHelper.SKIP,
                 cancellation_method=APIHelper.SKIP,
                 cancel_at_end_of_period=APIHelper.SKIP,
                 canceled_at=APIHelper.SKIP,
                 current_period_started_at=APIHelper.SKIP,
                 previous_state=APIHelper.SKIP,
                 signup_payment_id=APIHelper.SKIP,
                 signup_revenue=APIHelper.SKIP,
                 delayed_cancel_at=APIHelper.SKIP,
                 coupon_code=APIHelper.SKIP,
                 snap_day=APIHelper.SKIP,
                 payment_collection_method=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 product=APIHelper.SKIP,
                 credit_card=APIHelper.SKIP,
                 group=APIHelper.SKIP,
                 bank_account=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 referral_code=APIHelper.SKIP,
                 next_product_id=APIHelper.SKIP,
                 next_product_handle=APIHelper.SKIP,
                 coupon_use_count=APIHelper.SKIP,
                 coupon_uses_allowed=APIHelper.SKIP,
                 reason_code=APIHelper.SKIP,
                 automatically_resume_at=APIHelper.SKIP,
                 coupon_codes=APIHelper.SKIP,
                 offer_id=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 current_billing_amount_in_cents=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 product_price_point_type=APIHelper.SKIP,
                 next_product_price_point_id=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 stored_credential_transaction_id=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 on_hold_at=APIHelper.SKIP,
                 prepaid_dunning=APIHelper.SKIP,
                 coupons=APIHelper.SKIP,
                 dunning_communication_delay_enabled=APIHelper.SKIP,
                 dunning_communication_delay_time_zone=APIHelper.SKIP,
                 receives_invoice_emails=APIHelper.SKIP,
                 locale=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 scheduled_cancellation_at=APIHelper.SKIP,
                 credit_balance_in_cents=APIHelper.SKIP,
                 prepayment_balance_in_cents=APIHelper.SKIP,
                 prepaid_configuration=APIHelper.SKIP,
                 self_service_page_token=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Subscription class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if state is not APIHelper.SKIP:
            self.state = state 
        if balance_in_cents is not APIHelper.SKIP:
            self.balance_in_cents = balance_in_cents 
        if total_revenue_in_cents is not APIHelper.SKIP:
            self.total_revenue_in_cents = total_revenue_in_cents 
        if product_price_in_cents is not APIHelper.SKIP:
            self.product_price_in_cents = product_price_in_cents 
        if product_version_number is not APIHelper.SKIP:
            self.product_version_number = product_version_number 
        if current_period_ends_at is not APIHelper.SKIP:
            self.current_period_ends_at = APIHelper.apply_datetime_converter(current_period_ends_at, APIHelper.RFC3339DateTime) if current_period_ends_at else None 
        if next_assessment_at is not APIHelper.SKIP:
            self.next_assessment_at = APIHelper.apply_datetime_converter(next_assessment_at, APIHelper.RFC3339DateTime) if next_assessment_at else None 
        if trial_started_at is not APIHelper.SKIP:
            self.trial_started_at = APIHelper.apply_datetime_converter(trial_started_at, APIHelper.RFC3339DateTime) if trial_started_at else None 
        if trial_ended_at is not APIHelper.SKIP:
            self.trial_ended_at = APIHelper.apply_datetime_converter(trial_ended_at, APIHelper.RFC3339DateTime) if trial_ended_at else None 
        if activated_at is not APIHelper.SKIP:
            self.activated_at = APIHelper.apply_datetime_converter(activated_at, APIHelper.RFC3339DateTime) if activated_at else None 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = APIHelper.apply_datetime_converter(expires_at, APIHelper.RFC3339DateTime) if expires_at else None 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if cancellation_message is not APIHelper.SKIP:
            self.cancellation_message = cancellation_message 
        if cancellation_method is not APIHelper.SKIP:
            self.cancellation_method = cancellation_method 
        if cancel_at_end_of_period is not APIHelper.SKIP:
            self.cancel_at_end_of_period = cancel_at_end_of_period 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = APIHelper.apply_datetime_converter(canceled_at, APIHelper.RFC3339DateTime) if canceled_at else None 
        if current_period_started_at is not APIHelper.SKIP:
            self.current_period_started_at = APIHelper.apply_datetime_converter(current_period_started_at, APIHelper.RFC3339DateTime) if current_period_started_at else None 
        if previous_state is not APIHelper.SKIP:
            self.previous_state = previous_state 
        if signup_payment_id is not APIHelper.SKIP:
            self.signup_payment_id = signup_payment_id 
        if signup_revenue is not APIHelper.SKIP:
            self.signup_revenue = signup_revenue 
        if delayed_cancel_at is not APIHelper.SKIP:
            self.delayed_cancel_at = APIHelper.apply_datetime_converter(delayed_cancel_at, APIHelper.RFC3339DateTime) if delayed_cancel_at else None 
        if coupon_code is not APIHelper.SKIP:
            self.coupon_code = coupon_code 
        if snap_day is not APIHelper.SKIP:
            self.snap_day = snap_day 
        if payment_collection_method is not APIHelper.SKIP:
            self.payment_collection_method = payment_collection_method 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if product is not APIHelper.SKIP:
            self.product = product 
        if credit_card is not APIHelper.SKIP:
            self.credit_card = credit_card 
        if group is not APIHelper.SKIP:
            self.group = group 
        if bank_account is not APIHelper.SKIP:
            self.bank_account = bank_account 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
        if referral_code is not APIHelper.SKIP:
            self.referral_code = referral_code 
        if next_product_id is not APIHelper.SKIP:
            self.next_product_id = next_product_id 
        if next_product_handle is not APIHelper.SKIP:
            self.next_product_handle = next_product_handle 
        if coupon_use_count is not APIHelper.SKIP:
            self.coupon_use_count = coupon_use_count 
        if coupon_uses_allowed is not APIHelper.SKIP:
            self.coupon_uses_allowed = coupon_uses_allowed 
        if reason_code is not APIHelper.SKIP:
            self.reason_code = reason_code 
        if automatically_resume_at is not APIHelper.SKIP:
            self.automatically_resume_at = APIHelper.apply_datetime_converter(automatically_resume_at, APIHelper.RFC3339DateTime) if automatically_resume_at else None 
        if coupon_codes is not APIHelper.SKIP:
            self.coupon_codes = coupon_codes 
        if offer_id is not APIHelper.SKIP:
            self.offer_id = offer_id 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if current_billing_amount_in_cents is not APIHelper.SKIP:
            self.current_billing_amount_in_cents = current_billing_amount_in_cents 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if product_price_point_type is not APIHelper.SKIP:
            self.product_price_point_type = product_price_point_type 
        if next_product_price_point_id is not APIHelper.SKIP:
            self.next_product_price_point_id = next_product_price_point_id 
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms 
        if stored_credential_transaction_id is not APIHelper.SKIP:
            self.stored_credential_transaction_id = stored_credential_transaction_id 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if on_hold_at is not APIHelper.SKIP:
            self.on_hold_at = APIHelper.apply_datetime_converter(on_hold_at, APIHelper.RFC3339DateTime) if on_hold_at else None 
        if prepaid_dunning is not APIHelper.SKIP:
            self.prepaid_dunning = prepaid_dunning 
        if coupons is not APIHelper.SKIP:
            self.coupons = coupons 
        if dunning_communication_delay_enabled is not APIHelper.SKIP:
            self.dunning_communication_delay_enabled = dunning_communication_delay_enabled 
        if dunning_communication_delay_time_zone is not APIHelper.SKIP:
            self.dunning_communication_delay_time_zone = dunning_communication_delay_time_zone 
        if receives_invoice_emails is not APIHelper.SKIP:
            self.receives_invoice_emails = receives_invoice_emails 
        if locale is not APIHelper.SKIP:
            self.locale = locale 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if scheduled_cancellation_at is not APIHelper.SKIP:
            self.scheduled_cancellation_at = APIHelper.apply_datetime_converter(scheduled_cancellation_at, APIHelper.RFC3339DateTime) if scheduled_cancellation_at else None 
        if credit_balance_in_cents is not APIHelper.SKIP:
            self.credit_balance_in_cents = credit_balance_in_cents 
        if prepayment_balance_in_cents is not APIHelper.SKIP:
            self.prepayment_balance_in_cents = prepayment_balance_in_cents 
        if prepaid_configuration is not APIHelper.SKIP:
            self.prepaid_configuration = prepaid_configuration 
        if self_service_page_token is not APIHelper.SKIP:
            self.self_service_page_token = self_service_page_token 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        balance_in_cents = dictionary.get("balance_in_cents") if dictionary.get("balance_in_cents") else APIHelper.SKIP
        total_revenue_in_cents = dictionary.get("total_revenue_in_cents") if dictionary.get("total_revenue_in_cents") else APIHelper.SKIP
        product_price_in_cents = dictionary.get("product_price_in_cents") if dictionary.get("product_price_in_cents") else APIHelper.SKIP
        product_version_number = dictionary.get("product_version_number") if dictionary.get("product_version_number") else APIHelper.SKIP
        if 'current_period_ends_at' in dictionary.keys():
            current_period_ends_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("current_period_ends_at")).datetime if dictionary.get("current_period_ends_at") else None
        else:
            current_period_ends_at = APIHelper.SKIP
        if 'next_assessment_at' in dictionary.keys():
            next_assessment_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_assessment_at")).datetime if dictionary.get("next_assessment_at") else None
        else:
            next_assessment_at = APIHelper.SKIP
        if 'trial_started_at' in dictionary.keys():
            trial_started_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("trial_started_at")).datetime if dictionary.get("trial_started_at") else None
        else:
            trial_started_at = APIHelper.SKIP
        if 'trial_ended_at' in dictionary.keys():
            trial_ended_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("trial_ended_at")).datetime if dictionary.get("trial_ended_at") else None
        else:
            trial_ended_at = APIHelper.SKIP
        if 'activated_at' in dictionary.keys():
            activated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("activated_at")).datetime if dictionary.get("activated_at") else None
        else:
            activated_at = APIHelper.SKIP
        if 'expires_at' in dictionary.keys():
            expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else None
        else:
            expires_at = APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        cancellation_message = dictionary.get("cancellation_message") if "cancellation_message" in dictionary.keys() else APIHelper.SKIP
        cancellation_method = dictionary.get("cancellation_method") if "cancellation_method" in dictionary.keys() else APIHelper.SKIP
        cancel_at_end_of_period = dictionary.get("cancel_at_end_of_period") if "cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        if 'canceled_at' in dictionary.keys():
            canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else None
        else:
            canceled_at = APIHelper.SKIP
        if 'current_period_started_at' in dictionary.keys():
            current_period_started_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("current_period_started_at")).datetime if dictionary.get("current_period_started_at") else None
        else:
            current_period_started_at = APIHelper.SKIP
        previous_state = dictionary.get("previous_state") if dictionary.get("previous_state") else APIHelper.SKIP
        signup_payment_id = dictionary.get("signup_payment_id") if dictionary.get("signup_payment_id") else APIHelper.SKIP
        signup_revenue = dictionary.get("signup_revenue") if dictionary.get("signup_revenue") else APIHelper.SKIP
        if 'delayed_cancel_at' in dictionary.keys():
            delayed_cancel_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("delayed_cancel_at")).datetime if dictionary.get("delayed_cancel_at") else None
        else:
            delayed_cancel_at = APIHelper.SKIP
        coupon_code = dictionary.get("coupon_code") if "coupon_code" in dictionary.keys() else APIHelper.SKIP
        snap_day = dictionary.get("snap_day") if "snap_day" in dictionary.keys() else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else APIHelper.SKIP
        customer = Customer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        product = Product.from_dictionary(dictionary.get('product')) if 'product' in dictionary.keys() else APIHelper.SKIP
        credit_card = CreditCardPaymentProfile.from_dictionary(dictionary.get('credit_card')) if 'credit_card' in dictionary.keys() else APIHelper.SKIP
        if 'group' in dictionary.keys():
            group = NestedSubscriptionGroup.from_dictionary(dictionary.get('group')) if dictionary.get('group') else None
        else:
            group = APIHelper.SKIP
        bank_account = BankAccountPaymentProfile.from_dictionary(dictionary.get('bank_account')) if 'bank_account' in dictionary.keys() else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if "payment_type" in dictionary.keys() else APIHelper.SKIP
        referral_code = dictionary.get("referral_code") if "referral_code" in dictionary.keys() else APIHelper.SKIP
        next_product_id = dictionary.get("next_product_id") if "next_product_id" in dictionary.keys() else APIHelper.SKIP
        next_product_handle = dictionary.get("next_product_handle") if "next_product_handle" in dictionary.keys() else APIHelper.SKIP
        coupon_use_count = dictionary.get("coupon_use_count") if "coupon_use_count" in dictionary.keys() else APIHelper.SKIP
        coupon_uses_allowed = dictionary.get("coupon_uses_allowed") if "coupon_uses_allowed" in dictionary.keys() else APIHelper.SKIP
        reason_code = dictionary.get("reason_code") if "reason_code" in dictionary.keys() else APIHelper.SKIP
        if 'automatically_resume_at' in dictionary.keys():
            automatically_resume_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("automatically_resume_at")).datetime if dictionary.get("automatically_resume_at") else None
        else:
            automatically_resume_at = APIHelper.SKIP
        coupon_codes = dictionary.get("coupon_codes") if dictionary.get("coupon_codes") else APIHelper.SKIP
        offer_id = dictionary.get("offer_id") if "offer_id" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("payer_id") if "payer_id" in dictionary.keys() else APIHelper.SKIP
        current_billing_amount_in_cents = dictionary.get("current_billing_amount_in_cents") if dictionary.get("current_billing_amount_in_cents") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        product_price_point_type = dictionary.get("product_price_point_type") if dictionary.get("product_price_point_type") else APIHelper.SKIP
        next_product_price_point_id = dictionary.get("next_product_price_point_id") if "next_product_price_point_id" in dictionary.keys() else APIHelper.SKIP
        net_terms = dictionary.get("net_terms") if "net_terms" in dictionary.keys() else APIHelper.SKIP
        stored_credential_transaction_id = dictionary.get("stored_credential_transaction_id") if "stored_credential_transaction_id" in dictionary.keys() else APIHelper.SKIP
        reference = dictionary.get("reference") if "reference" in dictionary.keys() else APIHelper.SKIP
        if 'on_hold_at' in dictionary.keys():
            on_hold_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("on_hold_at")).datetime if dictionary.get("on_hold_at") else None
        else:
            on_hold_at = APIHelper.SKIP
        prepaid_dunning = dictionary.get("prepaid_dunning") if "prepaid_dunning" in dictionary.keys() else APIHelper.SKIP
        coupons = None
        if dictionary.get('coupons') is not None:
            coupons = [SubscriptionIncludedCoupon.from_dictionary(x) for x in dictionary.get('coupons')]
        else:
            coupons = APIHelper.SKIP
        dunning_communication_delay_enabled = dictionary.get("dunning_communication_delay_enabled") if "dunning_communication_delay_enabled" in dictionary.keys() else APIHelper.SKIP
        dunning_communication_delay_time_zone = dictionary.get("dunning_communication_delay_time_zone") if "dunning_communication_delay_time_zone" in dictionary.keys() else APIHelper.SKIP
        receives_invoice_emails = dictionary.get("receives_invoice_emails") if "receives_invoice_emails" in dictionary.keys() else APIHelper.SKIP
        locale = dictionary.get("locale") if "locale" in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        if 'scheduled_cancellation_at' in dictionary.keys():
            scheduled_cancellation_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("scheduled_cancellation_at")).datetime if dictionary.get("scheduled_cancellation_at") else None
        else:
            scheduled_cancellation_at = APIHelper.SKIP
        credit_balance_in_cents = dictionary.get("credit_balance_in_cents") if dictionary.get("credit_balance_in_cents") else APIHelper.SKIP
        prepayment_balance_in_cents = dictionary.get("prepayment_balance_in_cents") if dictionary.get("prepayment_balance_in_cents") else APIHelper.SKIP
        if 'prepaid_configuration' in dictionary.keys():
            prepaid_configuration = PrepaidConfiguration.from_dictionary(dictionary.get('prepaid_configuration')) if dictionary.get('prepaid_configuration') else None
        else:
            prepaid_configuration = APIHelper.SKIP
        self_service_page_token = dictionary.get("self_service_page_token") if dictionary.get("self_service_page_token") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   state,
                   balance_in_cents,
                   total_revenue_in_cents,
                   product_price_in_cents,
                   product_version_number,
                   current_period_ends_at,
                   next_assessment_at,
                   trial_started_at,
                   trial_ended_at,
                   activated_at,
                   expires_at,
                   created_at,
                   updated_at,
                   cancellation_message,
                   cancellation_method,
                   cancel_at_end_of_period,
                   canceled_at,
                   current_period_started_at,
                   previous_state,
                   signup_payment_id,
                   signup_revenue,
                   delayed_cancel_at,
                   coupon_code,
                   snap_day,
                   payment_collection_method,
                   customer,
                   product,
                   credit_card,
                   group,
                   bank_account,
                   payment_type,
                   referral_code,
                   next_product_id,
                   next_product_handle,
                   coupon_use_count,
                   coupon_uses_allowed,
                   reason_code,
                   automatically_resume_at,
                   coupon_codes,
                   offer_id,
                   payer_id,
                   current_billing_amount_in_cents,
                   product_price_point_id,
                   product_price_point_type,
                   next_product_price_point_id,
                   net_terms,
                   stored_credential_transaction_id,
                   reference,
                   on_hold_at,
                   prepaid_dunning,
                   coupons,
                   dunning_communication_delay_enabled,
                   dunning_communication_delay_time_zone,
                   receives_invoice_emails,
                   locale,
                   currency,
                   scheduled_cancellation_at,
                   credit_balance_in_cents,
                   prepayment_balance_in_cents,
                   prepaid_configuration,
                   self_service_page_token,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'state={self.state!r}, '
                f'balance_in_cents={self.balance_in_cents!r}, '
                f'total_revenue_in_cents={self.total_revenue_in_cents!r}, '
                f'product_price_in_cents={self.product_price_in_cents!r}, '
                f'product_version_number={self.product_version_number!r}, '
                f'current_period_ends_at={self.current_period_ends_at!r}, '
                f'next_assessment_at={self.next_assessment_at!r}, '
                f'trial_started_at={self.trial_started_at!r}, '
                f'trial_ended_at={self.trial_ended_at!r}, '
                f'activated_at={self.activated_at!r}, '
                f'expires_at={self.expires_at!r}, '
                f'created_at={self.created_at!r}, '
                f'updated_at={self.updated_at!r}, '
                f'cancellation_message={self.cancellation_message!r}, '
                f'cancellation_method={self.cancellation_method!r}, '
                f'cancel_at_end_of_period={self.cancel_at_end_of_period!r}, '
                f'canceled_at={self.canceled_at!r}, '
                f'current_period_started_at={self.current_period_started_at!r}, '
                f'previous_state={self.previous_state!r}, '
                f'signup_payment_id={self.signup_payment_id!r}, '
                f'signup_revenue={self.signup_revenue!r}, '
                f'delayed_cancel_at={self.delayed_cancel_at!r}, '
                f'coupon_code={self.coupon_code!r}, '
                f'snap_day={self.snap_day!r}, '
                f'payment_collection_method={self.payment_collection_method!r}, '
                f'customer={self.customer!r}, '
                f'product={self.product!r}, '
                f'credit_card={self.credit_card!r}, '
                f'group={self.group!r}, '
                f'bank_account={self.bank_account!r}, '
                f'payment_type={self.payment_type!r}, '
                f'referral_code={self.referral_code!r}, '
                f'next_product_id={self.next_product_id!r}, '
                f'next_product_handle={self.next_product_handle!r}, '
                f'coupon_use_count={self.coupon_use_count!r}, '
                f'coupon_uses_allowed={self.coupon_uses_allowed!r}, '
                f'reason_code={self.reason_code!r}, '
                f'automatically_resume_at={self.automatically_resume_at!r}, '
                f'coupon_codes={self.coupon_codes!r}, '
                f'offer_id={self.offer_id!r}, '
                f'payer_id={self.payer_id!r}, '
                f'current_billing_amount_in_cents={self.current_billing_amount_in_cents!r}, '
                f'product_price_point_id={self.product_price_point_id!r}, '
                f'product_price_point_type={self.product_price_point_type!r}, '
                f'next_product_price_point_id={self.next_product_price_point_id!r}, '
                f'net_terms={self.net_terms!r}, '
                f'stored_credential_transaction_id={self.stored_credential_transaction_id!r}, '
                f'reference={self.reference!r}, '
                f'on_hold_at={self.on_hold_at!r}, '
                f'prepaid_dunning={self.prepaid_dunning!r}, '
                f'coupons={self.coupons!r}, '
                f'dunning_communication_delay_enabled={self.dunning_communication_delay_enabled!r}, '
                f'dunning_communication_delay_time_zone={self.dunning_communication_delay_time_zone!r}, '
                f'receives_invoice_emails={self.receives_invoice_emails!r}, '
                f'locale={self.locale!r}, '
                f'currency={self.currency!r}, '
                f'scheduled_cancellation_at={self.scheduled_cancellation_at!r}, '
                f'credit_balance_in_cents={self.credit_balance_in_cents!r}, '
                f'prepayment_balance_in_cents={self.prepayment_balance_in_cents!r}, '
                f'prepaid_configuration={self.prepaid_configuration!r}, '
                f'self_service_page_token={self.self_service_page_token!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'state={self.state!s}, '
                f'balance_in_cents={self.balance_in_cents!s}, '
                f'total_revenue_in_cents={self.total_revenue_in_cents!s}, '
                f'product_price_in_cents={self.product_price_in_cents!s}, '
                f'product_version_number={self.product_version_number!s}, '
                f'current_period_ends_at={self.current_period_ends_at!s}, '
                f'next_assessment_at={self.next_assessment_at!s}, '
                f'trial_started_at={self.trial_started_at!s}, '
                f'trial_ended_at={self.trial_ended_at!s}, '
                f'activated_at={self.activated_at!s}, '
                f'expires_at={self.expires_at!s}, '
                f'created_at={self.created_at!s}, '
                f'updated_at={self.updated_at!s}, '
                f'cancellation_message={self.cancellation_message!s}, '
                f'cancellation_method={self.cancellation_method!s}, '
                f'cancel_at_end_of_period={self.cancel_at_end_of_period!s}, '
                f'canceled_at={self.canceled_at!s}, '
                f'current_period_started_at={self.current_period_started_at!s}, '
                f'previous_state={self.previous_state!s}, '
                f'signup_payment_id={self.signup_payment_id!s}, '
                f'signup_revenue={self.signup_revenue!s}, '
                f'delayed_cancel_at={self.delayed_cancel_at!s}, '
                f'coupon_code={self.coupon_code!s}, '
                f'snap_day={self.snap_day!s}, '
                f'payment_collection_method={self.payment_collection_method!s}, '
                f'customer={self.customer!s}, '
                f'product={self.product!s}, '
                f'credit_card={self.credit_card!s}, '
                f'group={self.group!s}, '
                f'bank_account={self.bank_account!s}, '
                f'payment_type={self.payment_type!s}, '
                f'referral_code={self.referral_code!s}, '
                f'next_product_id={self.next_product_id!s}, '
                f'next_product_handle={self.next_product_handle!s}, '
                f'coupon_use_count={self.coupon_use_count!s}, '
                f'coupon_uses_allowed={self.coupon_uses_allowed!s}, '
                f'reason_code={self.reason_code!s}, '
                f'automatically_resume_at={self.automatically_resume_at!s}, '
                f'coupon_codes={self.coupon_codes!s}, '
                f'offer_id={self.offer_id!s}, '
                f'payer_id={self.payer_id!s}, '
                f'current_billing_amount_in_cents={self.current_billing_amount_in_cents!s}, '
                f'product_price_point_id={self.product_price_point_id!s}, '
                f'product_price_point_type={self.product_price_point_type!s}, '
                f'next_product_price_point_id={self.next_product_price_point_id!s}, '
                f'net_terms={self.net_terms!s}, '
                f'stored_credential_transaction_id={self.stored_credential_transaction_id!s}, '
                f'reference={self.reference!s}, '
                f'on_hold_at={self.on_hold_at!s}, '
                f'prepaid_dunning={self.prepaid_dunning!s}, '
                f'coupons={self.coupons!s}, '
                f'dunning_communication_delay_enabled={self.dunning_communication_delay_enabled!s}, '
                f'dunning_communication_delay_time_zone={self.dunning_communication_delay_time_zone!s}, '
                f'receives_invoice_emails={self.receives_invoice_emails!s}, '
                f'locale={self.locale!s}, '
                f'currency={self.currency!s}, '
                f'scheduled_cancellation_at={self.scheduled_cancellation_at!s}, '
                f'credit_balance_in_cents={self.credit_balance_in_cents!s}, '
                f'prepayment_balance_in_cents={self.prepayment_balance_in_cents!s}, '
                f'prepaid_configuration={self.prepaid_configuration!s}, '
                f'self_service_page_token={self.self_service_page_token!s}, '
                f'additional_properties={self.additional_properties!s})')
