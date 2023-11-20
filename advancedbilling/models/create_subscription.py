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
from advancedbilling.models.custom_price_used_for_subscription_create_update import CustomPriceUsedForSubscriptionCreateUpdate
from advancedbilling.models.customer_attributes import CustomerAttributes
from advancedbilling.models.payment_profile_attributes import PaymentProfileAttributes
from advancedbilling.models.upsert_prepaid_configuration import UpsertPrepaidConfiguration


class CreateSubscription(object):

    """Implementation of the 'Create Subscription' model.

    TODO: type model description here.

    Attributes:
        product_handle (str): The API Handle of the product for which you are
            creating a subscription. Required, unless a `product_id` is given
            instead.
        product_id (str): The Product ID of the product for which you are
            creating a subscription. The product ID is not currently
            published, so we recommend using the API Handle instead.
        product_price_point_handle (str): The user-friendly API handle of a
            product's particular price point.
        product_price_point_id (str): The ID of the particular price point on
            the product.
        custom_price (CustomPriceUsedForSubscriptionCreateUpdate): (Optional)
            Used in place of `product_price_point_id` to define a custom price
            point unique to the subscription
        coupon_code (str): (deprecated) The coupon code of the single coupon
            currently applied to the subscription. See coupon_codes instead as
            subscriptions can now have more than one coupon.
        coupon_codes (List[str]): An array for all the coupons attached to the
            subscription.
        payment_collection_method (PaymentCollectionMethod): The type of
            payment collection to be used in the subscription. For legacy
            Statements Architecture valid options are - `invoice`,
            `automatic`. For current Relationship Invoicing Architecture valid
            options are - `remittance`, `automatic`, `prepaid`.
        receives_invoice_emails (str): (Optional) Default: True - Whether or
            not this subscription is set to receive emails related to this
            subscription.
        net_terms (str): (Optional) Default: null The number of days after
            renewal (on invoice billing) that a subscription is due. A value
            between 0 (due immediately) and 180.
        customer_id (int): The ID of an existing customer within Chargify.
            Required, unless a `customer_reference` or a set of
            `customer_attributes` is given.
        next_billing_at (str): (Optional) Set this attribute to a future
            date/time to sync imported subscriptions to your existing renewal
            schedule. See the notes on “Date/Time Format” in our [subscription
            import
            documentation](https://maxio-chargify.zendesk.com/hc/en-us/articles
            /5404863655821#date-format). If you provide a next_billing_at
            timestamp that is in the future, no trial or initial charges will
            be applied when you create the subscription. In fact, no payment
            will be captured at all. The first payment will be captured,
            according to the prices defined by the product, near the time
            specified by next_billing_at. If you do not provide a value for
            next_billing_at, any trial and/or initial charges will be assessed
            and charged at the time of subscription creation. If the card
            cannot be successfully charged, the subscription will not be
            created. See further notes in the section on Importing
            Subscriptions.
        initial_billing_at (str): (Optional) Set this attribute to a future
            date/time to create a subscription in the "Awaiting Signup" state,
            rather than "Active" or "Trialing". See the notes on “Date/Time
            Format” in our [subscription import
            documentation](https://maxio-chargify.zendesk.com/hc/en-us/articles
            /5404863655821#date-format). In the "Awaiting Signup" state, a
            subscription behaves like any other. It can be canceled, allocated
            to, had its billing date changed. etc. When the initial_billing_at
            date hits, the subscription will transition to the expected state.
            If the product has a trial, the subscription will enter a trial,
            otherwise it will go active. Setup fees will be respected either
            before or after the trial, as configured on the price point. If
            the payment is due at the initial_billing_at and it fails the
            subscription will be immediately canceled. See further notes in
            the section on Delayed Signups.
        stored_credential_transaction_id (int): For European sites subject to
            PSD2 and using 3D Secure, this can be used to reference a previous
            transaction for the customer. This will ensure the card will be
            charged successfully at renewal.
        sales_rep_id (int): TODO: type description here.
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
            subscription itelf.
        customer_attributes (CustomerAttributes): TODO: type description
            here.
        payment_profile_attributes (PaymentProfileAttributes): alias to
            credit_card_attributes
        credit_card_attributes (PaymentProfileAttributes): Credit Card data to
            create a new Subscription. Interchangeable with
            `payment_profile_attributes` property.
        bank_account_attributes (BankAccountAttributes): TODO: type
            description here.
        components (List[CreateSubscriptionComponent] | None): (Optional) An
            array of component ids and quantities to be added to the
            subscription. See
            [Components](https://maxio-chargify.zendesk.com/hc/en-us/articles/5
            405020625677) for more information.
        calendar_billing (CalendarBilling): (Optional). Cannot be used when
            also specifying next_billing_at
        metafields (Dict[str, str]): (Optional) A set of key/value pairs
            representing custom fields and their values. Metafields will be
            created “on-the-fly” in your site for a given key, if they have
            not been created yet.
        customer_reference (str): The reference value (provided by your app)
            of an existing customer within Chargify. Required, unless a
            `customer_id` or a set of `customer_attributes` is given.
        group (GroupSettings | bool | None): TODO: type description here.
        ref (str): A valid referral code. (optional, see
            [Referrals](https://maxio-chargify.zendesk.com/hc/en-us/articles/54
            05420204045-Referrals-Reference#how-to-obtain-referral-codes) for
            more details). If supplied, must be valid, or else subscription
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
        expires_at (str): Timestamp giving the expiration date of this
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
        product_change_delayed (bool): (Optional, used only for Delayed
            Product Change When set to true, indicates that a changed value
            for product_handle should schedule the product change to the next
            subscription renewal.
        offer_id (str | int | None): Use in place of passing product and
            component information to set up the subscription with an existing
            offer. May be either the Chargify id of the offer or its handle
            prefixed with `handle:`.er
        prepaid_subscription_configuration (UpsertPrepaidConfiguration): TODO:
            type description here.
        previous_billing_at (str): Providing a previous_billing_at that is in
            the past will set the current_period_starts_at when the
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
        canceled_at (str): TODO: type description here.
        activated_at (str): TODO: type description here.
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
        "prepaid_subscription_configuration": 'prepaid_subscription_configuration',
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
        'prepaid_subscription_configuration',
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
        'dunning_communication_delay_enabled',
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
                 payment_collection_method='automatic',
                 receives_invoice_emails=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 next_billing_at=APIHelper.SKIP,
                 initial_billing_at=APIHelper.SKIP,
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
                 prepaid_subscription_configuration=APIHelper.SKIP,
                 previous_billing_at=APIHelper.SKIP,
                 import_mrr=APIHelper.SKIP,
                 canceled_at=APIHelper.SKIP,
                 activated_at=APIHelper.SKIP,
                 agreement_acceptance=APIHelper.SKIP,
                 ach_agreement=APIHelper.SKIP,
                 dunning_communication_delay_enabled=False,
                 dunning_communication_delay_time_zone=APIHelper.SKIP,
                 skip_billing_manifest_taxes=False):
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
        self.payment_collection_method = payment_collection_method 
        if receives_invoice_emails is not APIHelper.SKIP:
            self.receives_invoice_emails = receives_invoice_emails 
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if next_billing_at is not APIHelper.SKIP:
            self.next_billing_at = next_billing_at 
        if initial_billing_at is not APIHelper.SKIP:
            self.initial_billing_at = initial_billing_at 
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
            self.expires_at = expires_at 
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
        if prepaid_subscription_configuration is not APIHelper.SKIP:
            self.prepaid_subscription_configuration = prepaid_subscription_configuration 
        if previous_billing_at is not APIHelper.SKIP:
            self.previous_billing_at = previous_billing_at 
        if import_mrr is not APIHelper.SKIP:
            self.import_mrr = import_mrr 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = canceled_at 
        if activated_at is not APIHelper.SKIP:
            self.activated_at = activated_at 
        if agreement_acceptance is not APIHelper.SKIP:
            self.agreement_acceptance = agreement_acceptance 
        if ach_agreement is not APIHelper.SKIP:
            self.ach_agreement = ach_agreement 
        self.dunning_communication_delay_enabled = dunning_communication_delay_enabled 
        if dunning_communication_delay_time_zone is not APIHelper.SKIP:
            self.dunning_communication_delay_time_zone = dunning_communication_delay_time_zone 
        self.skip_billing_manifest_taxes = skip_billing_manifest_taxes 

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
        product_price_point_handle = dictionary.get("product_price_point_handle") if dictionary.get("product_price_point_handle") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        custom_price = CustomPriceUsedForSubscriptionCreateUpdate.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        coupon_code = dictionary.get("coupon_code") if dictionary.get("coupon_code") else APIHelper.SKIP
        coupon_codes = dictionary.get("coupon_codes") if dictionary.get("coupon_codes") else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else 'automatic'
        receives_invoice_emails = dictionary.get("receives_invoice_emails") if dictionary.get("receives_invoice_emails") else APIHelper.SKIP
        net_terms = dictionary.get("net_terms") if dictionary.get("net_terms") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        next_billing_at = dictionary.get("next_billing_at") if dictionary.get("next_billing_at") else APIHelper.SKIP
        initial_billing_at = dictionary.get("initial_billing_at") if dictionary.get("initial_billing_at") else APIHelper.SKIP
        stored_credential_transaction_id = dictionary.get("stored_credential_transaction_id") if dictionary.get("stored_credential_transaction_id") else APIHelper.SKIP
        sales_rep_id = dictionary.get("sales_rep_id") if dictionary.get("sales_rep_id") else APIHelper.SKIP
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        customer_attributes = CustomerAttributes.from_dictionary(dictionary.get('customer_attributes')) if 'customer_attributes' in dictionary.keys() else APIHelper.SKIP
        payment_profile_attributes = PaymentProfileAttributes.from_dictionary(dictionary.get('payment_profile_attributes')) if 'payment_profile_attributes' in dictionary.keys() else APIHelper.SKIP
        credit_card_attributes = PaymentProfileAttributes.from_dictionary(dictionary.get('credit_card_attributes')) if 'credit_card_attributes' in dictionary.keys() else APIHelper.SKIP
        bank_account_attributes = BankAccountAttributes.from_dictionary(dictionary.get('bank_account_attributes')) if 'bank_account_attributes' in dictionary.keys() else APIHelper.SKIP
        components = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionComponents'), dictionary.get('components'), False) if dictionary.get('components') is not None else APIHelper.SKIP
        calendar_billing = CalendarBilling.from_dictionary(dictionary.get('calendar_billing')) if 'calendar_billing' in dictionary.keys() else APIHelper.SKIP
        metafields = dictionary.get("metafields") if dictionary.get("metafields") else APIHelper.SKIP
        customer_reference = dictionary.get("customer_reference") if dictionary.get("customer_reference") else APIHelper.SKIP
        group = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionGroup2'), dictionary.get('group'), False) if dictionary.get('group') is not None else APIHelper.SKIP
        ref = dictionary.get("ref") if dictionary.get("ref") else APIHelper.SKIP
        cancellation_message = dictionary.get("cancellation_message") if dictionary.get("cancellation_message") else APIHelper.SKIP
        cancellation_method = dictionary.get("cancellation_method") if dictionary.get("cancellation_method") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        expires_at = dictionary.get("expires_at") if dictionary.get("expires_at") else APIHelper.SKIP
        expiration_tracks_next_billing_change = dictionary.get("expiration_tracks_next_billing_change") if dictionary.get("expiration_tracks_next_billing_change") else APIHelper.SKIP
        agreement_terms = dictionary.get("agreement_terms") if dictionary.get("agreement_terms") else APIHelper.SKIP
        authorizer_first_name = dictionary.get("authorizer_first_name") if dictionary.get("authorizer_first_name") else APIHelper.SKIP
        authorizer_last_name = dictionary.get("authorizer_last_name") if dictionary.get("authorizer_last_name") else APIHelper.SKIP
        calendar_billing_first_charge = dictionary.get("calendar_billing_first_charge") if dictionary.get("calendar_billing_first_charge") else APIHelper.SKIP
        reason_code = dictionary.get("reason_code") if dictionary.get("reason_code") else APIHelper.SKIP
        product_change_delayed = dictionary.get("product_change_delayed") if "product_change_delayed" in dictionary.keys() else APIHelper.SKIP
        offer_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSubscriptionOfferId'), dictionary.get('offer_id'), False) if dictionary.get('offer_id') is not None else APIHelper.SKIP
        prepaid_subscription_configuration = UpsertPrepaidConfiguration.from_dictionary(dictionary.get('prepaid_subscription_configuration')) if 'prepaid_subscription_configuration' in dictionary.keys() else APIHelper.SKIP
        previous_billing_at = dictionary.get("previous_billing_at") if dictionary.get("previous_billing_at") else APIHelper.SKIP
        import_mrr = dictionary.get("import_mrr") if "import_mrr" in dictionary.keys() else APIHelper.SKIP
        canceled_at = dictionary.get("canceled_at") if dictionary.get("canceled_at") else APIHelper.SKIP
        activated_at = dictionary.get("activated_at") if dictionary.get("activated_at") else APIHelper.SKIP
        agreement_acceptance = AgreementAcceptance.from_dictionary(dictionary.get('agreement_acceptance')) if 'agreement_acceptance' in dictionary.keys() else APIHelper.SKIP
        ach_agreement = ACHAgreement.from_dictionary(dictionary.get('ach_agreement')) if 'ach_agreement' in dictionary.keys() else APIHelper.SKIP
        dunning_communication_delay_enabled = dictionary.get("dunning_communication_delay_enabled") if dictionary.get("dunning_communication_delay_enabled") else False
        dunning_communication_delay_time_zone = dictionary.get("dunning_communication_delay_time_zone") if "dunning_communication_delay_time_zone" in dictionary.keys() else APIHelper.SKIP
        skip_billing_manifest_taxes = dictionary.get("skip_billing_manifest_taxes") if dictionary.get("skip_billing_manifest_taxes") else False
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
                   prepaid_subscription_configuration,
                   previous_billing_at,
                   import_mrr,
                   canceled_at,
                   activated_at,
                   agreement_acceptance,
                   ach_agreement,
                   dunning_communication_delay_enabled,
                   dunning_communication_delay_time_zone,
                   skip_billing_manifest_taxes)
