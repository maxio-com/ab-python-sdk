# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.ach_agreement import ACHAgreement
from advancedbilling.models.agreement_acceptance import AgreementAcceptance
from advancedbilling.models.bank_account_attributes import BankAccountAttributes
from advancedbilling.models.calendar_billing import CalendarBilling
from advancedbilling.models.create_subscription_component import CreateSubscriptionComponent
from advancedbilling.models.customer_attributes import CustomerAttributes
from advancedbilling.models.group_settings import GroupSettings
from advancedbilling.models.payment_profile_attributes import PaymentProfileAttributes
from advancedbilling.models.subscription_custom_price import SubscriptionCustomPrice
from advancedbilling.models.upsert_prepaid_configuration import UpsertPrepaidConfiguration


class CreateSubscription(object):

    """Implementation of the 'Create Subscription' model.

    Attributes:
        product_handle (str): The API Handle of the product for which you are
            creating a subscription. Required, unless a `product_id` is given
            instead.
        product_id (int): The Product ID of the product for which you are
            creating a subscription. The product ID is not currently
            published, so we recommend using the API Handle instead.
        product_price_point_handle (str): The user-friendly API handle of a
            product's particular price point.
        product_price_point_id (int): The ID of the particular price point on
            the product.
        custom_price (SubscriptionCustomPrice): (Optional) Used in place of
            `product_price_point_id` to define a custom price point unique to
            the subscription
        coupon_code (str): (deprecated) The coupon code of the single coupon
            currently applied to the subscription. See coupon_codes instead as
            subscriptions can now have more than one coupon.
        coupon_codes (List[str]): An array for all the coupons attached to the
            subscription.
        payment_collection_method (CollectionMethod): The type of payment
            collection to be used in the subscription. For legacy Statements
            Architecture valid options are - `invoice`, `automatic`. For
            current Relationship Invoicing Architecture valid options are -
            `remittance`, `automatic`, `prepaid`.
        receives_invoice_emails (str): (Optional) Default: True - Whether or
            not this subscription is set to receive emails related to this
            subscription.
        net_terms (str): (Optional) Default: null The number of days after
            renewal (on invoice billing) that a subscription is due. A value
            between 0 (due immediately) and 180.
        customer_id (int): The ID of an existing customer within Chargify.
            Required, unless a `customer_reference` or a set of
            `customer_attributes` is given.
        next_billing_at (datetime): (Optional) Set this attribute to a future
            date/time to sync imported subscriptions to your existing renewal
            schedule. See the notes on “Date/Time Format” in our [subscription
            import
            documentation](https://maxio.zendesk.com/hc/en-us/articles/24251489
            107213-Advanced-Billing-Subscription-Imports#date-format). If you
            provide a next_billing_at timestamp that is in the future, no
            trial or initial charges will be applied when you create the
            subscription. In fact, no payment will be captured at all. The
            first payment will be captured, according to the prices defined by
            the product, near the time specified by next_billing_at. If you do
            not provide a value for next_billing_at, any trial and/or initial
            charges will be assessed and charged at the time of subscription
            creation. If the card cannot be successfully charged, the
            subscription will not be created. See further notes in the section
            on Importing Subscriptions.
        initial_billing_at (datetime): (Optional) Set this attribute to a
            future date/time to create a subscription in the Awaiting Signup
            state, rather than Active or Trialing. You can omit the
            initial_billing_at date to activate the subscription immediately.
            In the Awaiting Signup state, a subscription behaves like any
            other. It can be canceled, allocated to, or have its billing date
            changed. etc. When the initial_billing_at date hits, the
            subscription will transition to the expected state. If the product
            has a trial, the subscription will enter a trial, otherwise it
            will go active. Setup fees will be respected either before or
            after the trial, as configured on the price point. If the payment
            is due at the initial_billing_at and it fails the subscription
            will be immediately canceled. See the [subscription
            import](https://maxio.zendesk.com/hc/en-us/articles/24251489107213-
            Advanced-Billing-Subscription-Imports#date-format) documentation
            for more information about Date/Time Formats.
        defer_signup (bool): (Optional) Set this attribute to true to create
            the subscription in the Awaiting Signup Date state. Use this when
            you want to create a subscription that has an unknown first 
            billing date. When the first billing date is known, update a
            subscription and set the `initial_billing_at` date. The
            subscription moves to the Awaiting Signup state with a scheduled
            initial billing date. You can omit the initial_billing_at date to
            activate the subscription immediately. See [Subscription
            States](https://maxio-chargify.zendesk.com/hc/en-us/articles/540422
            2005773-Subscription-States) for more information.
        stored_credential_transaction_id (int): For European sites subject to
            PSD2 and using 3D Secure, this can be used to reference a previous
            transaction for the customer. This will ensure the card will be
            charged successfully at renewal.
        sales_rep_id (int): The model property of type int.
        payment_profile_id (int): The Payment Profile ID of an existing card
            or bank account, which belongs to an existing customer to use for
            payment for this subscription. If the card, bank account, or
            customer does not exist already, or if you want to use a new
            (unstored) card or bank account for the subscription, use
            `payment_profile_attributes` instead to create a new payment
            profile along with the subscription. (This value is available on
            an existing subscription via the API as `credit_card` > id or
            `bank_account` > id)
        reference (str): The reference value (provided by your app) for the
            subscription itself.
        customer_attributes (CustomerAttributes): The model property of type
            CustomerAttributes.
        payment_profile_attributes (PaymentProfileAttributes): alias to
            credit_card_attributes
        credit_card_attributes (PaymentProfileAttributes): Credit Card data to
            create a new Subscription. Interchangeable with
            `payment_profile_attributes` property.
        bank_account_attributes (BankAccountAttributes): The model property of
            type BankAccountAttributes.
        components (List[CreateSubscriptionComponent]): (Optional) An array of
            component ids and quantities to be added to the subscription. See
            [Components](https://maxio.zendesk.com/hc/en-us/articles/2426114152
            2189-Components-Overview) for more information.
        calendar_billing (CalendarBilling): (Optional). Cannot be used when
            also specifying next_billing_at
        metafields (Dict[str, str]): (Optional) A set of key/value pairs
            representing custom fields and their values. Metafields will be
            created “on-the-fly” in your site for a given key, if they have
            not been created yet.
        customer_reference (str): The reference value (provided by your app)
            of an existing customer within Chargify. Required, unless a
            `customer_id` or a set of `customer_attributes` is given.
        group (GroupSettings): The model property of type GroupSettings.
        ref (str): A valid referral code. (optional, see
            [Referrals](https://maxio.zendesk.com/hc/en-us/articles/24286981223
            693-Referrals-Reference#how-to-obtain-referral-codes) for more
            details). If supplied, must be valid, or else subscription
            creation will fail.
        cancellation_message (str): (Optional) Can be used when canceling a
            subscription (via the HTTP DELETE method) to make a note about the
            reason for cancellation.
        cancellation_method (str): (Optional) Can be used when canceling a
            subscription (via the HTTP DELETE method) to make a note about how
            the subscription was canceled.
        currency (str): (Optional) If Multi-Currency is enabled and the
            currency is configured in Chargify, pass it at signup to create a
            subscription on a non-default currency. Note that you cannot
            update the currency of an existing subscription.
        expires_at (datetime): Timestamp giving the expiration date of this
            subscription (if any). You may manually change the expiration date
            at any point during a subscription period.
        expiration_tracks_next_billing_change (str): (Optional, default false)
            When set to true, and when next_billing_at is present, if the
            subscription expires, the expires_at will be shifted by the same
            amount of time as the difference between the old and new “next
            billing” dates.
        agreement_terms (str): (Optional) The ACH authorization agreement
            terms. If enabled, an email will be sent to the customer with a
            copy of the terms.
        authorizer_first_name (str): (Optional) The first name of the person
            authorizing the ACH agreement.
        authorizer_last_name (str): (Optional) The last name of the person
            authorizing the ACH agreement.
        calendar_billing_first_charge (str): (Optional) One of “prorated” (the
            default – the prorated product price will be charged immediately),
            “immediate” (the full product price will be charged immediately),
            or “delayed” (the full product price will be charged with the
            first scheduled renewal).
        reason_code (str): (Optional) Can be used when canceling a
            subscription (via the HTTP DELETE method) to indicate why a
            subscription was canceled.
        product_change_delayed (bool): (Optional) used only for Delayed
            Product Change When set to true, indicates that a changed value
            for product_handle should schedule the product change to the next
            subscription renewal.
        offer_id (str | int | None): Use in place of passing product and
            component information to set up the subscription with an existing
            offer. May be either the Chargify id of the offer or its handle
            prefixed with `handle:`.er
        prepaid_configuration (UpsertPrepaidConfiguration): The model property
            of type UpsertPrepaidConfiguration.
        previous_billing_at (datetime): Providing a previous_billing_at that
            is in the past will set the current_period_starts_at when the
            subscription is created. It will also set activated_at if not
            explicitly passed during the subscription import. Can only be used
            if next_billing_at is also passed. Using this option will allow
            you to set the period start for the subscription so mid period
            component allocations have the correct prorated amount.
        import_mrr (bool): Setting this attribute to true will cause the
            subscription's MRR to be added to your MRR analytics immediately.
            For this value to be honored, a next_billing_at must be present
            and set to a future date. This key/value will not be returned in
            the subscription response body.
        canceled_at (datetime): The model property of type datetime.
        activated_at (datetime): The model property of type datetime.
        agreement_acceptance (AgreementAcceptance): Required when creating a
            subscription with Maxio Payments.
        ach_agreement (ACHAgreement): (Optional) If passed, the proof of the
            authorized ACH agreement terms will be persisted.
        dunning_communication_delay_enabled (bool): Enable Communication Delay
            feature, making sure no communication (email or SMS) is sent to
            the Customer between 9PM and 8AM in time zone set by the
            `dunning_communication_delay_time_zone` attribute.
        dunning_communication_delay_time_zone (str): Time zone for the Dunning
            Communication Delay feature.
        skip_billing_manifest_taxes (bool): Valid only for the Subscription
            Preview endpoint. When set to `true` it skips calculating taxes
            for the current and next billing manifests.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_handle": 'product_handle',
        "product_id": 'product_id',
        "product_price_point_handle": 'product_price_point_handle',
        "product_price_point_id": 'product_price_point_id',
        "custom_price": 'custom_price',
        "coupon_code": 'coupon_code',
        "coupon_codes": 'coupon_codes',
        "payment_collection_method": 'payment_collection_method',
        "receives_invoice_emails": 'receives_invoice_emails',
        "net_terms": 'net_terms',
        "customer_id": 'customer_id',
        "next_billing_at": 'next_billing_at',
        "initial_billing_at": 'initial_billing_at',
        "defer_signup": 'defer_signup',
        "stored_credential_transaction_id": 'stored_credential_transaction_id',
        "sales_rep_id": 'sales_rep_id',
        "payment_profile_id": 'payment_profile_id',
        "reference": 'reference',
        "customer_attributes": 'customer_attributes',
        "payment_profile_attributes": 'payment_profile_attributes',
        "credit_card_attributes": 'credit_card_attributes',
        "bank_account_attributes": 'bank_account_attributes',
        "components": 'components',
        "calendar_billing": 'calendar_billing',
        "metafields": 'metafields',
        "customer_reference": 'customer_reference',
        "group": 'group',
        "ref": 'ref',
        "cancellation_message": 'cancellation_message',
        "cancellation_method": 'cancellation_method',
        "currency": 'currency',
        "expires_at": 'expires_at',
        "expiration_tracks_next_billing_change": 'expiration_tracks_next_billing_change',
        "agreement_terms": 'agreement_terms',
        "authorizer_first_name": 'authorizer_first_name',
        "authorizer_last_name": 'authorizer_last_name',
        "calendar_billing_first_charge": 'calendar_billing_first_charge',
        "reason_code": 'reason_code',
        "product_change_delayed": 'product_change_delayed',
        "offer_id": 'offer_id',
        "prepaid_configuration": 'prepaid_configuration',
        "previous_billing_at": 'previous_billing_at',
        "import_mrr": 'import_mrr',
        "canceled_at": 'canceled_at',
        "activated_at": 'activated_at',
        "agreement_acceptance": 'agreement_acceptance',
        "ach_agreement": 'ach_agreement',
        "dunning_communication_delay_enabled": 'dunning_communication_delay_enabled',
        "dunning_communication_delay_time_zone": 'dunning_communication_delay_time_zone',
        "skip_billing_manifest_taxes": 'skip_billing_manifest_taxes'
    }

    _optionals = [
        'product_handle',
        'product_id',
        'product_price_point_handle',
        'product_price_point_id',
        'custom_price',
        'coupon_code',
        'coupon_codes',
        'payment_collection_method',
        'receives_invoice_emails',
        'net_terms',
        'customer_id',
        'next_billing_at',
        'initial_billing_at',
        'defer_signup',
        'stored_credential_transaction_id',
        'sales_rep_id',
        'payment_profile_id',
        'reference',
        'customer_attributes',
        'payment_profile_attributes',
        'credit_card_attributes',
        'bank_account_attributes',
        'components',
        'calendar_billing',
        'metafields',
        'customer_reference',
        'group',
        'ref',
        'cancellation_message',
        'cancellation_method',
        'currency',
        'expires_at',
        'expiration_tracks_next_billing_change',
        'agreement_terms',
        'authorizer_first_name',
        'authorizer_last_name',
        'calendar_billing_first_charge',
        'reason_code',
        'product_change_delayed',
        'offer_id',
        'prepaid_configuration',
        'previous_billing_at',
        'import_mrr',
        'canceled_at',
        'activated_at',
        'agreement_acceptance',
        'ach_agreement',
        'dunning_communication_delay_enabled',
        'dunning_communication_delay_time_zone',
        'skip_billing_manifest_taxes',
    ]

    _nullables = [
        'dunning_communication_delay_time_zone',
    ]

    def __init__(self,
                 product_handle=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_price_point_handle=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 custom_price=APIHelper.SKIP,
                 coupon_code=APIHelper.SKIP,
                 coupon_codes=APIHelper.SKIP,
                 payment_collection_method=APIHelper.SKIP,
                 receives_invoice_emails=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 next_billing_at=APIHelper.SKIP,
                 initial_billing_at=APIHelper.SKIP,
                 defer_signup=False,
                 stored_credential_transaction_id=APIHelper.SKIP,
                 sales_rep_id=APIHelper.SKIP,
                 payment_profile_id=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 customer_attributes=APIHelper.SKIP,
                 payment_profile_attributes=APIHelper.SKIP,
                 credit_card_attributes=APIHelper.SKIP,
                 bank_account_attributes=APIHelper.SKIP,
                 components=APIHelper.SKIP,
                 calendar_billing=APIHelper.SKIP,
                 metafields=APIHelper.SKIP,
                 customer_reference=APIHelper.SKIP,
                 group=APIHelper.SKIP,
                 ref=APIHelper.SKIP,
                 cancellation_message=APIHelper.SKIP,
                 cancellation_method=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 expires_at=APIHelper.SKIP,
                 expiration_tracks_next_billing_change=APIHelper.SKIP,
                 agreement_terms=APIHelper.SKIP,
                 authorizer_first_name=APIHelper.SKIP,
                 authorizer_last_name=APIHelper.SKIP,
                 calendar_billing_first_charge=APIHelper.SKIP,
                 reason_code=APIHelper.SKIP,
                 product_change_delayed=APIHelper.SKIP,
                 offer_id=APIHelper.SKIP,
                 prepaid_configuration=APIHelper.SKIP,
                 previous_billing_at=APIHelper.SKIP,
                 import_mrr=APIHelper.SKIP,
                 canceled_at=APIHelper.SKIP,
                 activated_at=APIHelper.SKIP,
                 agreement_acceptance=APIHelper.SKIP,
                 ach_agreement=APIHelper.SKIP,
                 dunning_communication_delay_enabled=False,
                 dunning_communication_delay_time_zone=APIHelper.SKIP,
                 skip_billing_manifest_taxes=False,
                 additional_properties=None):
        """Constructor for the CreateSubscription class"""

        # Initialize members of the class
        if product_handle is not APIHelper.SKIP:
            self.product_handle = product_handle 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_price_point_handle is not APIHelper.SKIP:
            self.product_price_point_handle = product_price_point_handle 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if custom_price is not APIHelper.SKIP:
            self.custom_price = custom_price 
        if coupon_code is not APIHelper.SKIP:
            self.coupon_code = coupon_code 
        if coupon_codes is not APIHelper.SKIP:
            self.coupon_codes = coupon_codes 
        if payment_collection_method is not APIHelper.SKIP:
            self.payment_collection_method = payment_collection_method 
        if receives_invoice_emails is not APIHelper.SKIP:
            self.receives_invoice_emails = receives_invoice_emails 
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if next_billing_at is not APIHelper.SKIP:
            self.next_billing_at = APIHelper.apply_datetime_converter(next_billing_at, APIHelper.RFC3339DateTime) if next_billing_at else None 
        if initial_billing_at is not APIHelper.SKIP:
            self.initial_billing_at = APIHelper.apply_datetime_converter(initial_billing_at, APIHelper.RFC3339DateTime) if initial_billing_at else None 
        self.defer_signup = defer_signup 
        if stored_credential_transaction_id is not APIHelper.SKIP:
            self.stored_credential_transaction_id = stored_credential_transaction_id 
        if sales_rep_id is not APIHelper.SKIP:
            self.sales_rep_id = sales_rep_id 
        if payment_profile_id is not APIHelper.SKIP:
            self.payment_profile_id = payment_profile_id 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if customer_attributes is not APIHelper.SKIP:
            self.customer_attributes = customer_attributes 
        if payment_profile_attributes is not APIHelper.SKIP:
            self.payment_profile_attributes = payment_profile_attributes 
        if credit_card_attributes is not APIHelper.SKIP:
            self.credit_card_attributes = credit_card_attributes 
        if bank_account_attributes is not APIHelper.SKIP:
            self.bank_account_attributes = bank_account_attributes 
        if components is not APIHelper.SKIP:
            self.components = components 
        if calendar_billing is not APIHelper.SKIP:
            self.calendar_billing = calendar_billing 
        if metafields is not APIHelper.SKIP:
            self.metafields = metafields 
        if customer_reference is not APIHelper.SKIP:
            self.customer_reference = customer_reference 
        if group is not APIHelper.SKIP:
            self.group = group 
        if ref is not APIHelper.SKIP:
            self.ref = ref 
        if cancellation_message is not APIHelper.SKIP:
            self.cancellation_message = cancellation_message 
        if cancellation_method is not APIHelper.SKIP:
            self.cancellation_method = cancellation_method 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = APIHelper.apply_datetime_converter(expires_at, APIHelper.RFC3339DateTime) if expires_at else None 
        if expiration_tracks_next_billing_change is not APIHelper.SKIP:
            self.expiration_tracks_next_billing_change = expiration_tracks_next_billing_change 
        if agreement_terms is not APIHelper.SKIP:
            self.agreement_terms = agreement_terms 
        if authorizer_first_name is not APIHelper.SKIP:
            self.authorizer_first_name = authorizer_first_name 
        if authorizer_last_name is not APIHelper.SKIP:
            self.authorizer_last_name = authorizer_last_name 
        if calendar_billing_first_charge is not APIHelper.SKIP:
            self.calendar_billing_first_charge = calendar_billing_first_charge 
        if reason_code is not APIHelper.SKIP:
            self.reason_code = reason_code 
        if product_change_delayed is not APIHelper.SKIP:
            self.product_change_delayed = product_change_delayed 
        if offer_id is not APIHelper.SKIP:
            self.offer_id = offer_id 
        if prepaid_configuration is not APIHelper.SKIP:
            self.prepaid_configuration = prepaid_configuration 
        if previous_billing_at is not APIHelper.SKIP:
            self.previous_billing_at = APIHelper.apply_datetime_converter(previous_billing_at, APIHelper.RFC3339DateTime) if previous_billing_at else None 
        if import_mrr is not APIHelper.SKIP:
            self.import_mrr = import_mrr 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = APIHelper.apply_datetime_converter(canceled_at, APIHelper.RFC3339DateTime) if canceled_at else None 
        if activated_at is not APIHelper.SKIP:
            self.activated_at = APIHelper.apply_datetime_converter(activated_at, APIHelper.RFC3339DateTime) if activated_at else None 
        if agreement_acceptance is not APIHelper.SKIP:
            self.agreement_acceptance = agreement_acceptance 
        if ach_agreement is not APIHelper.SKIP:
            self.ach_agreement = ach_agreement 
        self.dunning_communication_delay_enabled = dunning_communication_delay_enabled 
        if dunning_communication_delay_time_zone is not APIHelper.SKIP:
            self.dunning_communication_delay_time_zone = dunning_communication_delay_time_zone 
        self.skip_billing_manifest_taxes = skip_billing_manifest_taxes 

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
        product_handle = dictionary.get("product_handle") if dictionary.get("product_handle") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_price_point_handle = dictionary.get("product_price_point_handle") if dictionary.get("product_price_point_handle") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        custom_price = SubscriptionCustomPrice.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        coupon_code = dictionary.get("coupon_code") if dictionary.get("coupon_code") else APIHelper.SKIP
        coupon_codes = dictionary.get("coupon_codes") if dictionary.get("coupon_codes") else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else APIHelper.SKIP
        receives_invoice_emails = dictionary.get("receives_invoice_emails") if dictionary.get("receives_invoice_emails") else APIHelper.SKIP
        net_terms = dictionary.get("net_terms") if dictionary.get("net_terms") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        next_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_billing_at")).datetime if dictionary.get("next_billing_at") else APIHelper.SKIP
        initial_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("initial_billing_at")).datetime if dictionary.get("initial_billing_at") else APIHelper.SKIP
        defer_signup = dictionary.get("defer_signup") if dictionary.get("defer_signup") else False
        stored_credential_transaction_id = dictionary.get("stored_credential_transaction_id") if dictionary.get("stored_credential_transaction_id") else APIHelper.SKIP
        sales_rep_id = dictionary.get("sales_rep_id") if dictionary.get("sales_rep_id") else APIHelper.SKIP
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        customer_attributes = CustomerAttributes.from_dictionary(dictionary.get('customer_attributes')) if 'customer_attributes' in dictionary.keys() else APIHelper.SKIP
        payment_profile_attributes = PaymentProfileAttributes.from_dictionary(dictionary.get('payment_profile_attributes')) if 'payment_profile_attributes' in dictionary.keys() else APIHelper.SKIP
        credit_card_attributes = PaymentProfileAttributes.from_dictionary(dictionary.get('credit_card_attributes')) if 'credit_card_attributes' in dictionary.keys() else APIHelper.SKIP
        bank_account_attributes = BankAccountAttributes.from_dictionary(dictionary.get('bank_account_attributes')) if 'bank_account_attributes' in dictionary.keys() else APIHelper.SKIP
        components = None
        if dictionary.get('components') is not None:
            components = [CreateSubscriptionComponent.from_dictionary(x) for x in dictionary.get('components')]
        else:
            components = APIHelper.SKIP
        calendar_billing = CalendarBilling.from_dictionary(dictionary.get('calendar_billing')) if 'calendar_billing' in dictionary.keys() else APIHelper.SKIP
        metafields = dictionary.get("metafields") if dictionary.get("metafields") else APIHelper.SKIP
        customer_reference = dictionary.get("customer_reference") if dictionary.get("customer_reference") else APIHelper.SKIP
        group = GroupSettings.from_dictionary(dictionary.get('group')) if 'group' in dictionary.keys() else APIHelper.SKIP
        ref = dictionary.get("ref") if dictionary.get("ref") else APIHelper.SKIP
        cancellation_message = dictionary.get("cancellation_message") if dictionary.get("cancellation_message") else APIHelper.SKIP
        cancellation_method = dictionary.get("cancellation_method") if dictionary.get("cancellation_method") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else APIHelper.SKIP
        expiration_tracks_next_billing_change = dictionary.get("expiration_tracks_next_billing_change") if dictionary.get("expiration_tracks_next_billing_change") else APIHelper.SKIP
        agreement_terms = dictionary.get("agreement_terms") if dictionary.get("agreement_terms") else APIHelper.SKIP
        authorizer_first_name = dictionary.get("authorizer_first_name") if dictionary.get("authorizer_first_name") else APIHelper.SKIP
        authorizer_last_name = dictionary.get("authorizer_last_name") if dictionary.get("authorizer_last_name") else APIHelper.SKIP
        calendar_billing_first_charge = dictionary.get("calendar_billing_first_charge") if dictionary.get("calendar_billing_first_charge") else APIHelper.SKIP
        reason_code = dictionary.get("reason_code") if dictionary.get("reason_code") else APIHelper.SKIP
        product_change_delayed = dictionary.get("product_change_delayed") if "product_change_delayed" in dictionary.keys() else APIHelper.SKIP
        offer_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionOfferId'), dictionary.get('offer_id'), False) if dictionary.get('offer_id') is not None else APIHelper.SKIP
        prepaid_configuration = UpsertPrepaidConfiguration.from_dictionary(dictionary.get('prepaid_configuration')) if 'prepaid_configuration' in dictionary.keys() else APIHelper.SKIP
        previous_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("previous_billing_at")).datetime if dictionary.get("previous_billing_at") else APIHelper.SKIP
        import_mrr = dictionary.get("import_mrr") if "import_mrr" in dictionary.keys() else APIHelper.SKIP
        canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else APIHelper.SKIP
        activated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("activated_at")).datetime if dictionary.get("activated_at") else APIHelper.SKIP
        agreement_acceptance = AgreementAcceptance.from_dictionary(dictionary.get('agreement_acceptance')) if 'agreement_acceptance' in dictionary.keys() else APIHelper.SKIP
        ach_agreement = ACHAgreement.from_dictionary(dictionary.get('ach_agreement')) if 'ach_agreement' in dictionary.keys() else APIHelper.SKIP
        dunning_communication_delay_enabled = dictionary.get("dunning_communication_delay_enabled") if dictionary.get("dunning_communication_delay_enabled") else False
        dunning_communication_delay_time_zone = dictionary.get("dunning_communication_delay_time_zone") if "dunning_communication_delay_time_zone" in dictionary.keys() else APIHelper.SKIP
        skip_billing_manifest_taxes = dictionary.get("skip_billing_manifest_taxes") if dictionary.get("skip_billing_manifest_taxes") else False
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(product_handle,
                   product_id,
                   product_price_point_handle,
                   product_price_point_id,
                   custom_price,
                   coupon_code,
                   coupon_codes,
                   payment_collection_method,
                   receives_invoice_emails,
                   net_terms,
                   customer_id,
                   next_billing_at,
                   initial_billing_at,
                   defer_signup,
                   stored_credential_transaction_id,
                   sales_rep_id,
                   payment_profile_id,
                   reference,
                   customer_attributes,
                   payment_profile_attributes,
                   credit_card_attributes,
                   bank_account_attributes,
                   components,
                   calendar_billing,
                   metafields,
                   customer_reference,
                   group,
                   ref,
                   cancellation_message,
                   cancellation_method,
                   currency,
                   expires_at,
                   expiration_tracks_next_billing_change,
                   agreement_terms,
                   authorizer_first_name,
                   authorizer_last_name,
                   calendar_billing_first_charge,
                   reason_code,
                   product_change_delayed,
                   offer_id,
                   prepaid_configuration,
                   previous_billing_at,
                   import_mrr,
                   canceled_at,
                   activated_at,
                   agreement_acceptance,
                   ach_agreement,
                   dunning_communication_delay_enabled,
                   dunning_communication_delay_time_zone,
                   skip_billing_manifest_taxes,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_handle={(self.product_handle if hasattr(self, "product_handle") else None)!r}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!r}, '
                f'product_price_point_handle={(self.product_price_point_handle if hasattr(self, "product_price_point_handle") else None)!r}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!r}, '
                f'custom_price={(self.custom_price if hasattr(self, "custom_price") else None)!r}, '
                f'coupon_code={(self.coupon_code if hasattr(self, "coupon_code") else None)!r}, '
                f'coupon_codes={(self.coupon_codes if hasattr(self, "coupon_codes") else None)!r}, '
                f'payment_collection_method={(self.payment_collection_method if hasattr(self, "payment_collection_method") else None)!r}, '
                f'receives_invoice_emails={(self.receives_invoice_emails if hasattr(self, "receives_invoice_emails") else None)!r}, '
                f'net_terms={(self.net_terms if hasattr(self, "net_terms") else None)!r}, '
                f'customer_id={(self.customer_id if hasattr(self, "customer_id") else None)!r}, '
                f'next_billing_at={(self.next_billing_at if hasattr(self, "next_billing_at") else None)!r}, '
                f'initial_billing_at={(self.initial_billing_at if hasattr(self, "initial_billing_at") else None)!r}, '
                f'defer_signup={(self.defer_signup if hasattr(self, "defer_signup") else None)!r}, '
                f'stored_credential_transaction_id={(self.stored_credential_transaction_id if hasattr(self, "stored_credential_transaction_id") else None)!r}, '
                f'sales_rep_id={(self.sales_rep_id if hasattr(self, "sales_rep_id") else None)!r}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!r}, '
                f'reference={(self.reference if hasattr(self, "reference") else None)!r}, '
                f'customer_attributes={(self.customer_attributes if hasattr(self, "customer_attributes") else None)!r}, '
                f'payment_profile_attributes={(self.payment_profile_attributes if hasattr(self, "payment_profile_attributes") else None)!r}, '
                f'credit_card_attributes={(self.credit_card_attributes if hasattr(self, "credit_card_attributes") else None)!r}, '
                f'bank_account_attributes={(self.bank_account_attributes if hasattr(self, "bank_account_attributes") else None)!r}, '
                f'components={(self.components if hasattr(self, "components") else None)!r}, '
                f'calendar_billing={(self.calendar_billing if hasattr(self, "calendar_billing") else None)!r}, '
                f'metafields={(self.metafields if hasattr(self, "metafields") else None)!r}, '
                f'customer_reference={(self.customer_reference if hasattr(self, "customer_reference") else None)!r}, '
                f'group={(self.group if hasattr(self, "group") else None)!r}, '
                f'ref={(self.ref if hasattr(self, "ref") else None)!r}, '
                f'cancellation_message={(self.cancellation_message if hasattr(self, "cancellation_message") else None)!r}, '
                f'cancellation_method={(self.cancellation_method if hasattr(self, "cancellation_method") else None)!r}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!r}, '
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!r}, '
                f'expiration_tracks_next_billing_change={(self.expiration_tracks_next_billing_change if hasattr(self, "expiration_tracks_next_billing_change") else None)!r}, '
                f'agreement_terms={(self.agreement_terms if hasattr(self, "agreement_terms") else None)!r}, '
                f'authorizer_first_name={(self.authorizer_first_name if hasattr(self, "authorizer_first_name") else None)!r}, '
                f'authorizer_last_name={(self.authorizer_last_name if hasattr(self, "authorizer_last_name") else None)!r}, '
                f'calendar_billing_first_charge={(self.calendar_billing_first_charge if hasattr(self, "calendar_billing_first_charge") else None)!r}, '
                f'reason_code={(self.reason_code if hasattr(self, "reason_code") else None)!r}, '
                f'product_change_delayed={(self.product_change_delayed if hasattr(self, "product_change_delayed") else None)!r}, '
                f'offer_id={(self.offer_id if hasattr(self, "offer_id") else None)!r}, '
                f'prepaid_configuration={(self.prepaid_configuration if hasattr(self, "prepaid_configuration") else None)!r}, '
                f'previous_billing_at={(self.previous_billing_at if hasattr(self, "previous_billing_at") else None)!r}, '
                f'import_mrr={(self.import_mrr if hasattr(self, "import_mrr") else None)!r}, '
                f'canceled_at={(self.canceled_at if hasattr(self, "canceled_at") else None)!r}, '
                f'activated_at={(self.activated_at if hasattr(self, "activated_at") else None)!r}, '
                f'agreement_acceptance={(self.agreement_acceptance if hasattr(self, "agreement_acceptance") else None)!r}, '
                f'ach_agreement={(self.ach_agreement if hasattr(self, "ach_agreement") else None)!r}, '
                f'dunning_communication_delay_enabled={(self.dunning_communication_delay_enabled if hasattr(self, "dunning_communication_delay_enabled") else None)!r}, '
                f'dunning_communication_delay_time_zone={(self.dunning_communication_delay_time_zone if hasattr(self, "dunning_communication_delay_time_zone") else None)!r}, '
                f'skip_billing_manifest_taxes={(self.skip_billing_manifest_taxes if hasattr(self, "skip_billing_manifest_taxes") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_handle={(self.product_handle if hasattr(self, "product_handle") else None)!s}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!s}, '
                f'product_price_point_handle={(self.product_price_point_handle if hasattr(self, "product_price_point_handle") else None)!s}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!s}, '
                f'custom_price={(self.custom_price if hasattr(self, "custom_price") else None)!s}, '
                f'coupon_code={(self.coupon_code if hasattr(self, "coupon_code") else None)!s}, '
                f'coupon_codes={(self.coupon_codes if hasattr(self, "coupon_codes") else None)!s}, '
                f'payment_collection_method={(self.payment_collection_method if hasattr(self, "payment_collection_method") else None)!s}, '
                f'receives_invoice_emails={(self.receives_invoice_emails if hasattr(self, "receives_invoice_emails") else None)!s}, '
                f'net_terms={(self.net_terms if hasattr(self, "net_terms") else None)!s}, '
                f'customer_id={(self.customer_id if hasattr(self, "customer_id") else None)!s}, '
                f'next_billing_at={(self.next_billing_at if hasattr(self, "next_billing_at") else None)!s}, '
                f'initial_billing_at={(self.initial_billing_at if hasattr(self, "initial_billing_at") else None)!s}, '
                f'defer_signup={(self.defer_signup if hasattr(self, "defer_signup") else None)!s}, '
                f'stored_credential_transaction_id={(self.stored_credential_transaction_id if hasattr(self, "stored_credential_transaction_id") else None)!s}, '
                f'sales_rep_id={(self.sales_rep_id if hasattr(self, "sales_rep_id") else None)!s}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!s}, '
                f'reference={(self.reference if hasattr(self, "reference") else None)!s}, '
                f'customer_attributes={(self.customer_attributes if hasattr(self, "customer_attributes") else None)!s}, '
                f'payment_profile_attributes={(self.payment_profile_attributes if hasattr(self, "payment_profile_attributes") else None)!s}, '
                f'credit_card_attributes={(self.credit_card_attributes if hasattr(self, "credit_card_attributes") else None)!s}, '
                f'bank_account_attributes={(self.bank_account_attributes if hasattr(self, "bank_account_attributes") else None)!s}, '
                f'components={(self.components if hasattr(self, "components") else None)!s}, '
                f'calendar_billing={(self.calendar_billing if hasattr(self, "calendar_billing") else None)!s}, '
                f'metafields={(self.metafields if hasattr(self, "metafields") else None)!s}, '
                f'customer_reference={(self.customer_reference if hasattr(self, "customer_reference") else None)!s}, '
                f'group={(self.group if hasattr(self, "group") else None)!s}, '
                f'ref={(self.ref if hasattr(self, "ref") else None)!s}, '
                f'cancellation_message={(self.cancellation_message if hasattr(self, "cancellation_message") else None)!s}, '
                f'cancellation_method={(self.cancellation_method if hasattr(self, "cancellation_method") else None)!s}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!s}, '
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!s}, '
                f'expiration_tracks_next_billing_change={(self.expiration_tracks_next_billing_change if hasattr(self, "expiration_tracks_next_billing_change") else None)!s}, '
                f'agreement_terms={(self.agreement_terms if hasattr(self, "agreement_terms") else None)!s}, '
                f'authorizer_first_name={(self.authorizer_first_name if hasattr(self, "authorizer_first_name") else None)!s}, '
                f'authorizer_last_name={(self.authorizer_last_name if hasattr(self, "authorizer_last_name") else None)!s}, '
                f'calendar_billing_first_charge={(self.calendar_billing_first_charge if hasattr(self, "calendar_billing_first_charge") else None)!s}, '
                f'reason_code={(self.reason_code if hasattr(self, "reason_code") else None)!s}, '
                f'product_change_delayed={(self.product_change_delayed if hasattr(self, "product_change_delayed") else None)!s}, '
                f'offer_id={(self.offer_id if hasattr(self, "offer_id") else None)!s}, '
                f'prepaid_configuration={(self.prepaid_configuration if hasattr(self, "prepaid_configuration") else None)!s}, '
                f'previous_billing_at={(self.previous_billing_at if hasattr(self, "previous_billing_at") else None)!s}, '
                f'import_mrr={(self.import_mrr if hasattr(self, "import_mrr") else None)!s}, '
                f'canceled_at={(self.canceled_at if hasattr(self, "canceled_at") else None)!s}, '
                f'activated_at={(self.activated_at if hasattr(self, "activated_at") else None)!s}, '
                f'agreement_acceptance={(self.agreement_acceptance if hasattr(self, "agreement_acceptance") else None)!s}, '
                f'ach_agreement={(self.ach_agreement if hasattr(self, "ach_agreement") else None)!s}, '
                f'dunning_communication_delay_enabled={(self.dunning_communication_delay_enabled if hasattr(self, "dunning_communication_delay_enabled") else None)!s}, '
                f'dunning_communication_delay_time_zone={(self.dunning_communication_delay_time_zone if hasattr(self, "dunning_communication_delay_time_zone") else None)!s}, '
                f'skip_billing_manifest_taxes={(self.skip_billing_manifest_taxes if hasattr(self, "skip_billing_manifest_taxes") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
