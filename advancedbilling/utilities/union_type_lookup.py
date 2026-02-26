
"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from __future__ import annotations

from typing import (
    Callable,
    ClassVar,
)

from apimatic_core.types.union_types.any_of import (
    AnyOf,
)
from apimatic_core.types.union_types.leaf_type import (
    LeafType,
)
from apimatic_core.types.union_types.one_of import (
    OneOf,
)
from apimatic_core.types.union_types.union_type_context import (
    UnionTypeContext as Context,
)

from advancedbilling.models.apple_pay_payment_profile import (
    ApplePayPaymentProfile,
)
from advancedbilling.models.apply_credit_note_event import (
    ApplyCreditNoteEvent,
)
from advancedbilling.models.apply_debit_note_event import (
    ApplyDebitNoteEvent,
)
from advancedbilling.models.apply_payment_event import (
    ApplyPaymentEvent,
)
from advancedbilling.models.backport_invoice_event import (
    BackportInvoiceEvent,
)
from advancedbilling.models.bank_account_payment_profile import (
    BankAccountPaymentProfile,
)
from advancedbilling.models.change_chargeback_status_event import (
    ChangeChargebackStatusEvent,
)
from advancedbilling.models.change_invoice_collection_method_event import (
    ChangeInvoiceCollectionMethodEvent,
)
from advancedbilling.models.change_invoice_status_event import (
    ChangeInvoiceStatusEvent,
)
from advancedbilling.models.component_allocation_change import (
    ComponentAllocationChange,
)
from advancedbilling.models.create_component_price_point import (
    CreateComponentPricePoint,
)
from advancedbilling.models.create_credit_note_event import (
    CreateCreditNoteEvent,
)
from advancedbilling.models.create_debit_note_event import (
    CreateDebitNoteEvent,
)
from advancedbilling.models.create_metafield import (
    CreateMetafield,
)
from advancedbilling.models.create_prepaid_usage_component_price_point import (
    CreatePrepaidUsageComponentPricePoint,
)
from advancedbilling.models.credit_account_balance_changed import (
    CreditAccountBalanceChanged,
)
from advancedbilling.models.credit_card_payment_profile import (
    CreditCardPaymentProfile,
)
from advancedbilling.models.custom_field_value_change import (
    CustomFieldValueChange,
)
from advancedbilling.models.customer_error import (
    CustomerError,
)
from advancedbilling.models.dunning_step_reached import (
    DunningStepReached,
)
from advancedbilling.models.failed_payment_event import (
    FailedPaymentEvent,
)
from advancedbilling.models.invoice_issued import (
    InvoiceIssued,
)
from advancedbilling.models.issue_invoice_event import (
    IssueInvoiceEvent,
)
from advancedbilling.models.item_price_point_changed import (
    ItemPricePointChanged,
)
from advancedbilling.models.metered_usage import (
    MeteredUsage,
)
from advancedbilling.models.payment_collection_method_changed import (
    PaymentCollectionMethodChanged,
)
from advancedbilling.models.payment_method_apple_pay import (
    PaymentMethodApplePay,
)
from advancedbilling.models.payment_method_bank_account import (
    PaymentMethodBankAccount,
)
from advancedbilling.models.payment_method_credit_card import (
    PaymentMethodCreditCard,
)
from advancedbilling.models.payment_method_external import (
    PaymentMethodExternal,
)
from advancedbilling.models.payment_method_paypal import (
    PaymentMethodPaypal,
)
from advancedbilling.models.payment_related_events import (
    PaymentRelatedEvents,
)
from advancedbilling.models.paypal_payment_profile import (
    PaypalPaymentProfile,
)
from advancedbilling.models.pending_cancellation_change import (
    PendingCancellationChange,
)
from advancedbilling.models.prepaid_subscription_balance_changed import (
    PrepaidSubscriptionBalanceChanged,
)
from advancedbilling.models.prepaid_usage import (
    PrepaidUsage,
)
from advancedbilling.models.prepayment_account_balance_changed import (
    PrepaymentAccountBalanceChanged,
)
from advancedbilling.models.proforma_invoice_issued import (
    ProformaInvoiceIssued,
)
from advancedbilling.models.refund_consolidated_invoice import (
    RefundConsolidatedInvoice,
)
from advancedbilling.models.refund_invoice import (
    RefundInvoice,
)
from advancedbilling.models.refund_invoice_event import (
    RefundInvoiceEvent,
)
from advancedbilling.models.refund_success import (
    RefundSuccess,
)
from advancedbilling.models.remove_payment_event import (
    RemovePaymentEvent,
)
from advancedbilling.models.resume_options import (
    ResumeOptions,
)
from advancedbilling.models.scheduled_renewal_item_request_body_component import (
    ScheduledRenewalItemRequestBodyComponent,
)
from advancedbilling.models.scheduled_renewal_item_request_body_product import (
    ScheduledRenewalItemRequestBodyProduct,
)
from advancedbilling.models.snap_day import (
    SnapDay,
)
from advancedbilling.models.subscription_group_members_array_error import (
    SubscriptionGroupMembersArrayError,
)
from advancedbilling.models.subscription_group_signup_event_data import (
    SubscriptionGroupSignupEventData,
)
from advancedbilling.models.subscription_group_single_error import (
    SubscriptionGroupSingleError,
)
from advancedbilling.models.subscription_product_change import (
    SubscriptionProductChange,
)
from advancedbilling.models.subscription_state_change import (
    SubscriptionStateChange,
)
from advancedbilling.models.update_metafield import (
    UpdateMetafield,
)
from advancedbilling.models.void_invoice_event import (
    VoidInvoiceEvent,
)
from advancedbilling.models.void_remainder_event import (
    VoidRemainderEvent,
)


class UnionTypeLookUp:
    """
    Provides lookup and factory methods for predefined union type templates.
    This class stores a mapping of template names to callables that construct
    union type instances. These templates are used to describe compatible
    data shapes by combining primitive or model-based types into a single
    resolved representation at runtime.

    Attributes:
        _templates (dict): A mapping of template names to factory callables
        that create configured union types.

    """

    _templates: ClassVar[dict[str, Callable]] = {
        "CloneComponentPricePointComponentId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "CloneComponentPricePointPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "UpdateComponentPricePointComponentId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "UpdateComponentPricePointPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ReadComponentPricePointComponentId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ReadComponentPricePointPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ArchiveComponentPricePointComponentId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ArchiveComponentPricePointPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "CreateProductPricePointProductId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ListProductPricePointsInputProductId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "UpdateProductPricePointProductId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "UpdateProductPricePointPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ReadProductPricePointProductId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ReadProductPricePointPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ArchiveProductPricePointProductId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ArchiveProductPricePointPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "CreateUsageSubscriptionIdOrReference": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "CreateUsageComponentId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ListUsagesInputSubscriptionIdOrReference": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "ListUsagesInputComponentId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "Invoice-Event": lambda: AnyOf(
            [
                LeafType(ApplyCreditNoteEvent,
                         Context.create(
                             discriminator_value="apply_credit_note",
                             discriminator="event_type",
                         )),
                LeafType(ApplyDebitNoteEvent,
                         Context.create(
                             discriminator_value="apply_debit_note",
                             discriminator="event_type",
                         )),
                LeafType(ApplyPaymentEvent,
                         Context.create(
                             discriminator_value="apply_payment",
                             discriminator="event_type",
                         )),
                LeafType(BackportInvoiceEvent,
                         Context.create(
                             discriminator_value="backport_invoice",
                             discriminator="event_type",
                         )),
                LeafType(ChangeChargebackStatusEvent,
                         Context.create(
                             discriminator_value="change_chargeback_status",
                             discriminator="event_type",
                         )),
                LeafType(ChangeInvoiceCollectionMethodEvent,
                         Context.create(
                             discriminator_value="change_invoice_collection_method",
                             discriminator="event_type",
                         )),
                LeafType(ChangeInvoiceStatusEvent,
                         Context.create(
                             discriminator_value="change_invoice_status",
                             discriminator="event_type",
                         )),
                LeafType(CreateCreditNoteEvent,
                         Context.create(
                             discriminator_value="create_credit_note",
                             discriminator="event_type",
                         )),
                LeafType(CreateDebitNoteEvent,
                         Context.create(
                             discriminator_value="create_debit_note",
                             discriminator="event_type",
                         )),
                LeafType(FailedPaymentEvent,
                         Context.create(
                             discriminator_value="failed_payment",
                             discriminator="event_type",
                         )),
                LeafType(IssueInvoiceEvent,
                         Context.create(
                             discriminator_value="issue_invoice",
                             discriminator="event_type",
                         )),
                LeafType(RefundInvoiceEvent,
                         Context.create(
                             discriminator_value="refund_invoice",
                             discriminator="event_type",
                         )),
                LeafType(RemovePaymentEvent,
                         Context.create(
                             discriminator_value="remove_payment",
                             discriminator="event_type",
                         )),
                LeafType(VoidInvoiceEvent,
                         Context.create(
                             discriminator_value="void_invoice",
                             discriminator="event_type",
                         )),
                LeafType(VoidRemainderEvent,
                         Context.create(
                             discriminator_value="void_remainder",
                             discriminator="event_type",
                         )),
            ],
            Context.create(
               is_array=True,
               is_optional=True,
            ),
        ),
        "AllocationQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "AllocationPreviousQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "AllocationPreviewItemQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "AllocationPreviewItemPreviousQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "Invoice-Event-Payment": lambda: AnyOf(
            [
                LeafType(PaymentMethodApplePay,
                         Context.create(
                             discriminator_value="apple_pay",
                             discriminator="type",
                         )),
                LeafType(PaymentMethodBankAccount,
                         Context.create(
                             discriminator_value="bank_account",
                             discriminator="type",
                         )),
                LeafType(PaymentMethodCreditCard,
                         Context.create(
                             discriminator_value="credit_card",
                             discriminator="type",
                         )),
                LeafType(PaymentMethodExternal,
                         Context.create(
                             discriminator_value="external",
                             discriminator="type",
                         )),
                LeafType(PaymentMethodPaypal,
                         Context.create(
                             discriminator_value="paypal_account",
                             discriminator="type",
                         )),
            ],
        ),
        "CalendarBillingSnapDay": lambda: OneOf(
            [
                LeafType(int),
                LeafType(SnapDay),
            ],
            Context.create(
               is_optional=True,
               is_nullable=True,
            ),
        ),
        "ComponentAllocationChangeAllocatedQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "ComponentPricePointAssignmentPricePoint": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CouponPayloadPercentage": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateAllocationPricePointId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
               is_nullable=True,
            ),
        ),
        "CreateComponentPricePointRequestPricePoint": lambda: AnyOf(
            [
                LeafType(CreateComponentPricePoint),
                LeafType(CreatePrepaidUsageComponentPricePoint),
            ],
        ),
        "CreateComponentPricePointsRequestPricePoints": lambda: AnyOf(
            [
                LeafType(CreateComponentPricePoint),
                LeafType(CreatePrepaidUsageComponentPricePoint),
            ],
            Context.create(
               is_array=True,
            ),
        ),
        "CreateInvoiceCouponPercentage": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceCouponAmount": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceCouponProductFamilyId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceItemQuantity": lambda: OneOf(
            [
                LeafType(float),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceItemUnitPrice": lambda: OneOf(
            [
                LeafType(float),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceItemProductId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceItemComponentId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceItemPricePointId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoiceItemProductPricePointId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateInvoicePaymentAmount": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateMetafieldsRequestMetafields": lambda: OneOf(
            [
                LeafType(CreateMetafield),
                LeafType(CreateMetafield,
                         Context.create(
                             is_array=True,
                         )),
            ],
        ),
        "CreateMultiInvoicePaymentAmount": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
        ),
        "CreateOrUpdateSegmentPriceUnitPrice": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
        ),
        "CreatePaymentProfileExpirationMonth": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreatePaymentProfileExpirationYear": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSegmentSegmentProperty1Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSegmentSegmentProperty2Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSegmentSegmentProperty3Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSegmentSegmentProperty4Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSubscriptionOfferId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSubscriptionComponentComponentId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSubscriptionComponentAllocatedQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CreateSubscriptionComponentPricePointId": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "CustomerErrorResponseErrors": lambda: OneOf(
            [
                LeafType(CustomerError),
                LeafType(str,
                         Context.create(
                             is_array=True,
                         )),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "DeductServiceCreditAmount": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
        ),
        "EBBComponentUnitPrice": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "EventEventSpecificData": lambda: OneOf(
            [
                LeafType(SubscriptionProductChange),
                LeafType(SubscriptionStateChange),
                LeafType(PaymentRelatedEvents),
                LeafType(RefundSuccess),
                LeafType(ComponentAllocationChange),
                LeafType(MeteredUsage),
                LeafType(PrepaidUsage),
                LeafType(DunningStepReached),
                LeafType(InvoiceIssued),
                LeafType(PendingCancellationChange),
                LeafType(PrepaidSubscriptionBalanceChanged),
                LeafType(ProformaInvoiceIssued),
                LeafType(SubscriptionGroupSignupEventData),
                LeafType(CreditAccountBalanceChanged),
                LeafType(PrepaymentAccountBalanceChanged),
                LeafType(PaymentCollectionMethodChanged),
                LeafType(ItemPricePointChanged),
                LeafType(CustomFieldValueChange),
            ],
            Context.create(
               is_nullable=True,
            ),
        ),
        "IssueServiceCreditAmount": lambda: OneOf(
            [
                LeafType(float),
                LeafType(str),
            ],
        ),
        "MetafieldEnum": lambda: OneOf(
            [
                LeafType(str),
                LeafType(str,
                         Context.create(
                             is_array=True,
                         )),
            ],
            Context.create(
               is_optional=True,
               is_nullable=True,
            ),
        ),
        "MeteredComponentUnitPrice": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "OnOffComponentUnitPrice": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
        ),
        "PaymentProfileAttributesExpirationMonth": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "PaymentProfileAttributesExpirationYear": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "Payment-Profile": lambda: AnyOf(
            [
                LeafType(ApplePayPaymentProfile,
                         Context.create(
                             discriminator_value="apple_pay",
                             discriminator="payment_type",
                         )),
                LeafType(BankAccountPaymentProfile,
                         Context.create(
                             discriminator_value="bank_account",
                             discriminator="payment_type",
                         )),
                LeafType(CreditCardPaymentProfile,
                         Context.create(
                             discriminator_value="credit_card",
                             discriminator="payment_type",
                         )),
                LeafType(PaypalPaymentProfile,
                         Context.create(
                             discriminator_value="paypal_account",
                             discriminator="payment_type",
                         )),
            ],
        ),
        "PrepaidUsageComponentUnitPrice": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "PriceStartingQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
        ),
        "PriceEndingQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
               is_nullable=True,
            ),
        ),
        "PriceUnitPrice": lambda: OneOf(
            [
                LeafType(float),
                LeafType(str),
            ],
        ),
        "QuantityBasedComponentUnitPrice": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "ReactivateSubscriptionRequestResume": lambda: OneOf(
            [
                LeafType(bool),
                LeafType(ResumeOptions),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "RefundConsolidatedInvoiceSegmentUids": lambda: OneOf(
            [
                LeafType(str,
                         Context.create(
                             is_array=True,
                         )),
                LeafType(str),
            ],
        ),
        "RefundInvoiceRequestRefund": lambda: AnyOf(
            [
                LeafType(RefundInvoice),
                LeafType(RefundConsolidatedInvoice),
            ],
        ),
        "RefundPrepaymentAmount": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
            ],
        ),
        "RenewalPreviewComponentComponentId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "RenewalPreviewComponentPricePointId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "ScheduledRenewalConfigurationItemRequestRenewalConfigurationItem": lambda: OneOf(
            [
                LeafType(ScheduledRenewalItemRequestBodyComponent),
                LeafType(ScheduledRenewalItemRequestBodyProduct),
            ],
        ),
        "ScheduledRenewalProductPricePointPriceInCents": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
        ),
        "ScheduledRenewalProductPricePointInterval": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
        ),
        "ScheduledRenewalUpdateRequestRenewalConfigurationItem": lambda: OneOf(
            [
                LeafType(ScheduledRenewalItemRequestBodyComponent),
                LeafType(ScheduledRenewalItemRequestBodyProduct),
            ],
        ),
        "SegmentSegmentProperty1Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SegmentSegmentProperty2Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SegmentSegmentProperty3Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SegmentSegmentProperty4Value": lambda: OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionSnapDay": lambda: OneOf(
            [
                LeafType(int),
                LeafType(SnapDay),
            ],
            Context.create(
               is_optional=True,
               is_nullable=True,
            ),
        ),
        "SubscriptionComponentAllocatedQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionCustomPricePriceInCents": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
        ),
        "SubscriptionCustomPriceInterval": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
        ),
        "SubscriptionCustomPriceTrialPriceInCents": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionCustomPriceTrialInterval": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionCustomPriceInitialChargeInCents": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionCustomPriceExpirationInterval": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionGroupCreateErrorResponseErrors": lambda: OneOf(
            [
                LeafType(SubscriptionGroupMembersArrayError),
                LeafType(SubscriptionGroupSingleError),
                LeafType(str),
            ],
        ),
        "SubscriptionGroupCreditCardFullNumber": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionGroupCreditCardExpirationMonth": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionGroupCreditCardExpirationYear": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionGroupSignupComponentComponentId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionGroupSignupComponentAllocatedQuantity": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionGroupSignupComponentUnitBalance": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "SubscriptionGroupSignupComponentPricePointId": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "UpdateMetafieldsRequestMetafields": lambda: OneOf(
            [
                LeafType(UpdateMetafield),
                LeafType(UpdateMetafield,
                         Context.create(
                             is_array=True,
                         )),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "UpdatePriceEndingQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "UpdatePriceUnitPrice": lambda: OneOf(
            [
                LeafType(float),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "UpdatePriceStartingQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "UpdateSubscriptionSnapDay": lambda: OneOf(
            [
                LeafType(int),
                LeafType(SnapDay),
            ],
            Context.create(
               is_optional=True,
               is_nullable=True,
            ),
        ),
        "UpdateSubscriptionNetTerms": lambda: OneOf(
            [
                LeafType(str),
                LeafType(int),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "UsageQuantity": lambda: OneOf(
            [
                LeafType(int),
                LeafType(str),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
    }

    @staticmethod
    def get(name):
        """
        Retrieve and construct a union type template by name.

        Args:
            name (str): The key identifying the template to resolve.

        Returns:
            Any: A new instance of the union type defined for the given name.

        Raises:
            KeyError: If no template exists for the specified name.

        """
        return UnionTypeLookUp._templates[name]()
