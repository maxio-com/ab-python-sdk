# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.event_key import EventKey


class Event(object):

    """Implementation of the 'Event' model.

    Attributes:
        id (int): The model property of type int.
        key (EventKey): The model property of type EventKey.
        message (str): The model property of type str.
        subscription_id (int): The model property of type int.
        customer_id (int): The model property of type int.
        created_at (datetime): The model property of type datetime.
        event_specific_data (SubscriptionProductChange |
            SubscriptionStateChange | PaymentRelatedEvents | RefundSuccess |
            ComponentAllocationChange | MeteredUsage | PrepaidUsage |
            DunningStepReached | InvoiceIssued | PendingCancellationChange |
            PrepaidSubscriptionBalanceChanged | ProformaInvoiceIssued |
            SubscriptionGroupSignupEventData | CreditAccountBalanceChanged |
            PrepaymentAccountBalanceChanged | PaymentCollectionMethodChanged |
            ItemPricePointChanged | CustomFieldValueChange | None): The schema
            varies based on the event key. The key-to-event data mapping is as
            follows:  * `subscription_product_change` -
            SubscriptionProductChange * `subscription_state_change` -
            SubscriptionStateChange * `signup_success`,
            `delayed_signup_creation_success`, `payment_success`,
            `payment_failure`, `renewal_success`, `renewal_failure`,
            `chargeback_lost`, `chargeback_accepted`, `chargeback_closed` -
            PaymentRelatedEvents * `refund_success` - RefundSuccess *
            `component_allocation_change` - ComponentAllocationChange *
            `metered_usage` - MeteredUsage * `prepaid_usage` - PrepaidUsage *
            `dunning_step_reached` - DunningStepReached * `invoice_issued` -
            InvoiceIssued * `pending_cancellation_change` -
            PendingCancellationChange * `prepaid_subscription_balance_changed`
            - PrepaidSubscriptionBalanceChanged *
            `subscription_group_signup_success` and
            `subscription_group_signup_failure` -
            SubscriptionGroupSignupEventData * `proforma_invoice_issued` -
            ProformaInvoiceIssued *
            `subscription_prepayment_account_balance_changed` -
            PrepaymentAccountBalanceChanged *
            `payment_collection_method_changed` -
            PaymentCollectionMethodChanged *
            `subscription_service_credit_account_balance_changed` -
            CreditAccountBalanceChanged * `item_price_point_changed` -
            ItemPricePointChanged * `custom_field_value_change` -
            CustomFieldValueChange * The rest, that is
            `delayed_signup_creation_failure`, `billing_date_change`,
            `expiration_date_change`, `expiring_card`,  `customer_update`,
            `customer_create`, `customer_delete`, `upgrade_downgrade_success`,
            `upgrade_downgrade_failure`,  `statement_closed`,
            `statement_settled`, `subscription_card_update`,
            `subscription_group_card_update`, 
            `subscription_bank_account_update`, `refund_failure`,
            `upcoming_renewal_notice`, `trial_end_notice`, 
            `direct_debit_payment_paid_out`, `direct_debit_payment_rejected`,
            `direct_debit_payment_pending`, `pending_payment_created`, 
            `pending_payment_failed`, `pending_payment_completed`,  don't have
            event_specific_data defined, `renewal_success_recreated`,
            `renewal_failure_recreated`, `payment_success_recreated`,
            `payment_failure_recreated`, `subscription_deletion`,
            `subscription_group_bank_account_update`,
            `subscription_paypal_account_update`,
            `subscription_group_paypal_account_update`,
            `subscription_customer_change`, `account_transaction_changed`,
            `go_cardless_payment_paid_out`, `go_cardless_payment_rejected`,
            `go_cardless_payment_pending`,
            `stripe_direct_debit_payment_paid_out`,
            `stripe_direct_debit_payment_rejected`,
            `stripe_direct_debit_payment_pending`,
            `maxio_payments_direct_debit_payment_paid_out`,
            `maxio_payments_direct_debit_payment_rejected`,
            `maxio_payments_direct_debit_payment_pending`,
            `invoice_in_collections_canceled`, `subscription_added_to_group`,
            `subscription_removed_from_group`, `chargeback_opened`,
            `chargeback_lost`, `chargeback_accepted`, `chargeback_closed`,
            `chargeback_won`, `payment_collection_method_changed`,
            `component_billing_date_changed`,
            `subscription_term_renewal_scheduled`,
            `subscription_term_renewal_pending`,
            `subscription_term_renewal_activated`,
            `subscription_term_renewal_removed`  they map to `null` instead.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "key": 'key',
        "message": 'message',
        "subscription_id": 'subscription_id',
        "customer_id": 'customer_id',
        "created_at": 'created_at',
        "event_specific_data": 'event_specific_data'
    }

    _nullables = [
        'subscription_id',
        'customer_id',
        'event_specific_data',
    ]

    def __init__(self,
                 id=None,
                 key=None,
                 message=None,
                 subscription_id=None,
                 customer_id=None,
                 created_at=None,
                 event_specific_data=None,
                 additional_properties=None):
        """Constructor for the Event class"""

        # Initialize members of the class
        self.id = id 
        self.key = key 
        self.message = message 
        self.subscription_id = subscription_id 
        self.customer_id = customer_id 
        self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        self.event_specific_data = event_specific_data 

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
        id = dictionary.get("id") if dictionary.get("id") else None
        key = dictionary.get("key") if dictionary.get("key") else None
        message = dictionary.get("message") if dictionary.get("message") else None
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        event_specific_data = APIHelper.deserialize_union_type(UnionTypeLookUp.get('EventEventSpecificData'), dictionary.get('event_specific_data'), False) if dictionary.get('event_specific_data') is not None else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   key,
                   message,
                   subscription_id,
                   customer_id,
                   created_at,
                   event_specific_data,
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.id,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.key,
                                            type_callable=lambda value: EventKey.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.message,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.subscription_id,
                                            type_callable=lambda value: isinstance(value, int),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.customer_id,
                                            type_callable=lambda value: isinstance(value, int),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.created_at,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and UnionTypeLookUp.get('EventEventSpecificData').validate(dictionary.event_specific_data).is_valid

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('id'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('key'),
                                        type_callable=lambda value: EventKey.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('message'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('subscription_id'),
                                        type_callable=lambda value: isinstance(value, int),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('customer_id'),
                                        type_callable=lambda value: isinstance(value, int),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('created_at'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and UnionTypeLookUp.get('EventEventSpecificData').validate(dictionary.get('event_specific_data')).is_valid

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'key={self.key!r}, '
                f'message={self.message!r}, '
                f'subscription_id={self.subscription_id!r}, '
                f'customer_id={self.customer_id!r}, '
                f'created_at={self.created_at!r}, '
                f'event_specific_data={self.event_specific_data!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'key={self.key!s}, '
                f'message={self.message!s}, '
                f'subscription_id={self.subscription_id!s}, '
                f'customer_id={self.customer_id!s}, '
                f'created_at={self.created_at!s}, '
                f'event_specific_data={self.event_specific_data!s}, '
                f'additional_properties={self.additional_properties!s})')
