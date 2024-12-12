# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class EventKey(object):

    """Implementation of the 'Event Key' enum.

    TODO: type enum description here.

    Attributes:
        PAYMENT_SUCCESS: TODO: type description here.
        PAYMENT_FAILURE: TODO: type description here.
        SIGNUP_SUCCESS: TODO: type description here.
        SIGNUP_FAILURE: TODO: type description here.
        DELAYED_SIGNUP_CREATION_SUCCESS: TODO: type description here.
        DELAYED_SIGNUP_CREATION_FAILURE: TODO: type description here.
        BILLING_DATE_CHANGE: TODO: type description here.
        EXPIRATION_DATE_CHANGE: TODO: type description here.
        RENEWAL_SUCCESS: TODO: type description here.
        RENEWAL_FAILURE: TODO: type description here.
        SUBSCRIPTION_STATE_CHANGE: TODO: type description here.
        SUBSCRIPTION_PRODUCT_CHANGE: TODO: type description here.
        PENDING_CANCELLATION_CHANGE: TODO: type description here.
        EXPIRING_CARD: TODO: type description here.
        CUSTOMER_UPDATE: TODO: type description here.
        CUSTOMER_CREATE: TODO: type description here.
        CUSTOMER_DELETE: TODO: type description here.
        COMPONENT_ALLOCATION_CHANGE: TODO: type description here.
        METERED_USAGE: TODO: type description here.
        PREPAID_USAGE: TODO: type description here.
        UPGRADE_DOWNGRADE_SUCCESS: TODO: type description here.
        UPGRADE_DOWNGRADE_FAILURE: TODO: type description here.
        STATEMENT_CLOSED: TODO: type description here.
        STATEMENT_SETTLED: TODO: type description here.
        SUBSCRIPTION_CARD_UPDATE: TODO: type description here.
        SUBSCRIPTION_GROUP_CARD_UPDATE: TODO: type description here.
        SUBSCRIPTION_BANK_ACCOUNT_UPDATE: TODO: type description here.
        REFUND_SUCCESS: TODO: type description here.
        REFUND_FAILURE: TODO: type description here.
        UPCOMING_RENEWAL_NOTICE: TODO: type description here.
        TRIAL_END_NOTICE: TODO: type description here.
        DUNNING_STEP_REACHED: TODO: type description here.
        INVOICE_ISSUED: TODO: type description here.
        PREPAID_SUBSCRIPTION_BALANCE_CHANGED: TODO: type description here.
        SUBSCRIPTION_GROUP_SIGNUP_SUCCESS: TODO: type description here.
        SUBSCRIPTION_GROUP_SIGNUP_FAILURE: TODO: type description here.
        DIRECT_DEBIT_PAYMENT_PAID_OUT: TODO: type description here.
        DIRECT_DEBIT_PAYMENT_REJECTED: TODO: type description here.
        DIRECT_DEBIT_PAYMENT_PENDING: TODO: type description here.
        PENDING_PAYMENT_CREATED: TODO: type description here.
        PENDING_PAYMENT_FAILED: TODO: type description here.
        PENDING_PAYMENT_COMPLETED: TODO: type description here.
        PROFORMA_INVOICE_ISSUED: TODO: type description here.
        SUBSCRIPTION_PREPAYMENT_ACCOUNT_BALANCE_CHANGED: TODO: type
            description here.
        SUBSCRIPTION_SERVICE_CREDIT_ACCOUNT_BALANCE_CHANGED: TODO: type
            description here.
        CUSTOM_FIELD_VALUE_CHANGE: TODO: type description here.
        ITEM_PRICE_POINT_CHANGED: TODO: type description here.
        RENEWAL_SUCCESS_RECREATED: TODO: type description here.
        RENEWAL_FAILURE_RECREATED: TODO: type description here.
        PAYMENT_SUCCESS_RECREATED: TODO: type description here.
        PAYMENT_FAILURE_RECREATED: TODO: type description here.
        SUBSCRIPTION_DELETION: TODO: type description here.
        SUBSCRIPTION_GROUP_BANK_ACCOUNT_UPDATE: TODO: type description here.
        SUBSCRIPTION_PAYPAL_ACCOUNT_UPDATE: TODO: type description here.
        SUBSCRIPTION_GROUP_PAYPAL_ACCOUNT_UPDATE: TODO: type description here.
        SUBSCRIPTION_CUSTOMER_CHANGE: TODO: type description here.
        ACCOUNT_TRANSACTION_CHANGED: TODO: type description here.
        GO_CARDLESS_PAYMENT_PAID_OUT: TODO: type description here.
        GO_CARDLESS_PAYMENT_REJECTED: TODO: type description here.
        GO_CARDLESS_PAYMENT_PENDING: TODO: type description here.
        STRIPE_DIRECT_DEBIT_PAYMENT_PAID_OUT: TODO: type description here.
        STRIPE_DIRECT_DEBIT_PAYMENT_REJECTED: TODO: type description here.
        STRIPE_DIRECT_DEBIT_PAYMENT_PENDING: TODO: type description here.
        MAXIO_PAYMENTS_DIRECT_DEBIT_PAYMENT_PAID_OUT: TODO: type description
            here.
        MAXIO_PAYMENTS_DIRECT_DEBIT_PAYMENT_REJECTED: TODO: type description
            here.
        MAXIO_PAYMENTS_DIRECT_DEBIT_PAYMENT_PENDING: TODO: type description
            here.
        INVOICE_IN_COLLECTIONS_CANCELED: TODO: type description here.
        SUBSCRIPTION_ADDED_TO_GROUP: TODO: type description here.
        SUBSCRIPTION_REMOVED_FROM_GROUP: TODO: type description here.
        CHARGEBACK_OPENED: TODO: type description here.
        CHARGEBACK_LOST: TODO: type description here.
        CHARGEBACK_ACCEPTED: TODO: type description here.
        CHARGEBACK_CLOSED: TODO: type description here.
        CHARGEBACK_WON: TODO: type description here.
        PAYMENT_COLLECTION_METHOD_CHANGED: TODO: type description here.
        COMPONENT_BILLING_DATE_CHANGED: TODO: type description here.
        SUBSCRIPTION_TERM_RENEWAL_SCHEDULED: TODO: type description here.
        SUBSCRIPTION_TERM_RENEWAL_PENDING: TODO: type description here.
        SUBSCRIPTION_TERM_RENEWAL_ACTIVATED: TODO: type description here.
        SUBSCRIPTION_TERM_RENEWAL_REMOVED: TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['payment_success', 'payment_failure', 'signup_success', 'signup_failure', 'delayed_signup_creation_success', 'delayed_signup_creation_failure', 'billing_date_change', 'expiration_date_change', 'renewal_success', 'renewal_failure', 'subscription_state_change', 'subscription_product_change', 'pending_cancellation_change', 'expiring_card', 'customer_update', 'customer_create', 'customer_delete', 'component_allocation_change', 'metered_usage', 'prepaid_usage', 'upgrade_downgrade_success', 'upgrade_downgrade_failure', 'statement_closed', 'statement_settled', 'subscription_card_update', 'subscription_group_card_update', 'subscription_bank_account_update', 'refund_success', 'refund_failure', 'upcoming_renewal_notice', 'trial_end_notice', 'dunning_step_reached', 'invoice_issued', 'prepaid_subscription_balance_changed', 'subscription_group_signup_success', 'subscription_group_signup_failure', 'direct_debit_payment_paid_out', 'direct_debit_payment_rejected', 'direct_debit_payment_pending', 'pending_payment_created', 'pending_payment_failed', 'pending_payment_completed', 'proforma_invoice_issued', 'subscription_prepayment_account_balance_changed', 'subscription_service_credit_account_balance_changed', 'custom_field_value_change', 'item_price_point_changed', 'renewal_success_recreated', 'renewal_failure_recreated', 'payment_success_recreated', 'payment_failure_recreated', 'subscription_deletion', 'subscription_group_bank_account_update', 'subscription_paypal_account_update', 'subscription_group_paypal_account_update', 'subscription_customer_change', 'account_transaction_changed', 'go_cardless_payment_paid_out', 'go_cardless_payment_rejected', 'go_cardless_payment_pending', 'stripe_direct_debit_payment_paid_out', 'stripe_direct_debit_payment_rejected', 'stripe_direct_debit_payment_pending', 'maxio_payments_direct_debit_payment_paid_out', 'maxio_payments_direct_debit_payment_rejected', 'maxio_payments_direct_debit_payment_pending', 'invoice_in_collections_canceled', 'subscription_added_to_group', 'subscription_removed_from_group', 'chargeback_opened', 'chargeback_lost', 'chargeback_accepted', 'chargeback_closed', 'chargeback_won', 'payment_collection_method_changed', 'component_billing_date_changed', 'subscription_term_renewal_scheduled', 'subscription_term_renewal_pending', 'subscription_term_renewal_activated', 'subscription_term_renewal_removed']
    PAYMENT_SUCCESS = 'payment_success'

    PAYMENT_FAILURE = 'payment_failure'

    SIGNUP_SUCCESS = 'signup_success'

    SIGNUP_FAILURE = 'signup_failure'

    DELAYED_SIGNUP_CREATION_SUCCESS = 'delayed_signup_creation_success'

    DELAYED_SIGNUP_CREATION_FAILURE = 'delayed_signup_creation_failure'

    BILLING_DATE_CHANGE = 'billing_date_change'

    EXPIRATION_DATE_CHANGE = 'expiration_date_change'

    RENEWAL_SUCCESS = 'renewal_success'

    RENEWAL_FAILURE = 'renewal_failure'

    SUBSCRIPTION_STATE_CHANGE = 'subscription_state_change'

    SUBSCRIPTION_PRODUCT_CHANGE = 'subscription_product_change'

    PENDING_CANCELLATION_CHANGE = 'pending_cancellation_change'

    EXPIRING_CARD = 'expiring_card'

    CUSTOMER_UPDATE = 'customer_update'

    CUSTOMER_CREATE = 'customer_create'

    CUSTOMER_DELETE = 'customer_delete'

    COMPONENT_ALLOCATION_CHANGE = 'component_allocation_change'

    METERED_USAGE = 'metered_usage'

    PREPAID_USAGE = 'prepaid_usage'

    UPGRADE_DOWNGRADE_SUCCESS = 'upgrade_downgrade_success'

    UPGRADE_DOWNGRADE_FAILURE = 'upgrade_downgrade_failure'

    STATEMENT_CLOSED = 'statement_closed'

    STATEMENT_SETTLED = 'statement_settled'

    SUBSCRIPTION_CARD_UPDATE = 'subscription_card_update'

    SUBSCRIPTION_GROUP_CARD_UPDATE = 'subscription_group_card_update'

    SUBSCRIPTION_BANK_ACCOUNT_UPDATE = 'subscription_bank_account_update'

    REFUND_SUCCESS = 'refund_success'

    REFUND_FAILURE = 'refund_failure'

    UPCOMING_RENEWAL_NOTICE = 'upcoming_renewal_notice'

    TRIAL_END_NOTICE = 'trial_end_notice'

    DUNNING_STEP_REACHED = 'dunning_step_reached'

    INVOICE_ISSUED = 'invoice_issued'

    PREPAID_SUBSCRIPTION_BALANCE_CHANGED = 'prepaid_subscription_balance_changed'

    SUBSCRIPTION_GROUP_SIGNUP_SUCCESS = 'subscription_group_signup_success'

    SUBSCRIPTION_GROUP_SIGNUP_FAILURE = 'subscription_group_signup_failure'

    DIRECT_DEBIT_PAYMENT_PAID_OUT = 'direct_debit_payment_paid_out'

    DIRECT_DEBIT_PAYMENT_REJECTED = 'direct_debit_payment_rejected'

    DIRECT_DEBIT_PAYMENT_PENDING = 'direct_debit_payment_pending'

    PENDING_PAYMENT_CREATED = 'pending_payment_created'

    PENDING_PAYMENT_FAILED = 'pending_payment_failed'

    PENDING_PAYMENT_COMPLETED = 'pending_payment_completed'

    PROFORMA_INVOICE_ISSUED = 'proforma_invoice_issued'

    SUBSCRIPTION_PREPAYMENT_ACCOUNT_BALANCE_CHANGED = 'subscription_prepayment_account_balance_changed'

    SUBSCRIPTION_SERVICE_CREDIT_ACCOUNT_BALANCE_CHANGED = 'subscription_service_credit_account_balance_changed'

    CUSTOM_FIELD_VALUE_CHANGE = 'custom_field_value_change'

    ITEM_PRICE_POINT_CHANGED = 'item_price_point_changed'

    RENEWAL_SUCCESS_RECREATED = 'renewal_success_recreated'

    RENEWAL_FAILURE_RECREATED = 'renewal_failure_recreated'

    PAYMENT_SUCCESS_RECREATED = 'payment_success_recreated'

    PAYMENT_FAILURE_RECREATED = 'payment_failure_recreated'

    SUBSCRIPTION_DELETION = 'subscription_deletion'

    SUBSCRIPTION_GROUP_BANK_ACCOUNT_UPDATE = 'subscription_group_bank_account_update'

    SUBSCRIPTION_PAYPAL_ACCOUNT_UPDATE = 'subscription_paypal_account_update'

    SUBSCRIPTION_GROUP_PAYPAL_ACCOUNT_UPDATE = 'subscription_group_paypal_account_update'

    SUBSCRIPTION_CUSTOMER_CHANGE = 'subscription_customer_change'

    ACCOUNT_TRANSACTION_CHANGED = 'account_transaction_changed'

    GO_CARDLESS_PAYMENT_PAID_OUT = 'go_cardless_payment_paid_out'

    GO_CARDLESS_PAYMENT_REJECTED = 'go_cardless_payment_rejected'

    GO_CARDLESS_PAYMENT_PENDING = 'go_cardless_payment_pending'

    STRIPE_DIRECT_DEBIT_PAYMENT_PAID_OUT = 'stripe_direct_debit_payment_paid_out'

    STRIPE_DIRECT_DEBIT_PAYMENT_REJECTED = 'stripe_direct_debit_payment_rejected'

    STRIPE_DIRECT_DEBIT_PAYMENT_PENDING = 'stripe_direct_debit_payment_pending'

    MAXIO_PAYMENTS_DIRECT_DEBIT_PAYMENT_PAID_OUT = 'maxio_payments_direct_debit_payment_paid_out'

    MAXIO_PAYMENTS_DIRECT_DEBIT_PAYMENT_REJECTED = 'maxio_payments_direct_debit_payment_rejected'

    MAXIO_PAYMENTS_DIRECT_DEBIT_PAYMENT_PENDING = 'maxio_payments_direct_debit_payment_pending'

    INVOICE_IN_COLLECTIONS_CANCELED = 'invoice_in_collections_canceled'

    SUBSCRIPTION_ADDED_TO_GROUP = 'subscription_added_to_group'

    SUBSCRIPTION_REMOVED_FROM_GROUP = 'subscription_removed_from_group'

    CHARGEBACK_OPENED = 'chargeback_opened'

    CHARGEBACK_LOST = 'chargeback_lost'

    CHARGEBACK_ACCEPTED = 'chargeback_accepted'

    CHARGEBACK_CLOSED = 'chargeback_closed'

    CHARGEBACK_WON = 'chargeback_won'

    PAYMENT_COLLECTION_METHOD_CHANGED = 'payment_collection_method_changed'

    COMPONENT_BILLING_DATE_CHANGED = 'component_billing_date_changed'

    SUBSCRIPTION_TERM_RENEWAL_SCHEDULED = 'subscription_term_renewal_scheduled'

    SUBSCRIPTION_TERM_RENEWAL_PENDING = 'subscription_term_renewal_pending'

    SUBSCRIPTION_TERM_RENEWAL_ACTIVATED = 'subscription_term_renewal_activated'

    SUBSCRIPTION_TERM_RENEWAL_REMOVED = 'subscription_term_renewal_removed'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   