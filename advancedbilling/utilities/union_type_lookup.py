# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.models.address_change import AddressChange
from advancedbilling.models.apply_credit_note_event_data import ApplyCreditNoteEventData
from advancedbilling.models.apply_debit_note_event_data import ApplyDebitNoteEventData
from advancedbilling.models.apply_payment_event_data import ApplyPaymentEventData
from advancedbilling.models.bank_account_payment_profile import BankAccountPaymentProfile
from advancedbilling.models.change_invoice_collection_method_event_data import ChangeInvoiceCollectionMethodEventData
from advancedbilling.models.component_allocation_change import ComponentAllocationChange
from advancedbilling.models.compounding_strategy import CompoundingStrategy
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.create_metafield import CreateMetafield
from advancedbilling.models.create_or_update_flat_amount_coupon import CreateOrUpdateFlatAmountCoupon
from advancedbilling.models.create_or_update_percentage_coupon import CreateOrUpdatePercentageCoupon
from advancedbilling.models.create_prepaid_usage_component_price_point import CreatePrepaidUsageComponentPricePoint
from advancedbilling.models.credit_account_balance_changed import CreditAccountBalanceChanged
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.custom_field_value_change import CustomFieldValueChange
from advancedbilling.models.customer_custom_fields_change import CustomerCustomFieldsChange
from advancedbilling.models.customer_error import CustomerError
from advancedbilling.models.customer_payer_change import CustomerPayerChange
from advancedbilling.models.dunning_step_reached import DunningStepReached
from advancedbilling.models.extended_interval_unit import ExtendedIntervalUnit
from advancedbilling.models.group_settings import GroupSettings
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.invoice_issued import InvoiceIssued
from advancedbilling.models.invoice_line_item_component_cost_data import InvoiceLineItemComponentCostData
from advancedbilling.models.invoice_pre_payment import InvoicePrePayment
from advancedbilling.models.issue_invoice_event_data import IssueInvoiceEventData
from advancedbilling.models.item_price_point_changed import ItemPricePointChanged
from advancedbilling.models.metered_usage import MeteredUsage
from advancedbilling.models.nested_subscription_group import NestedSubscriptionGroup
from advancedbilling.models.payment_collection_method_changed import PaymentCollectionMethodChanged
from advancedbilling.models.payment_for_allocation import PaymentForAllocation
from advancedbilling.models.payment_method_apple_pay import PaymentMethodApplePay
from advancedbilling.models.payment_method_bank_account import PaymentMethodBankAccount
from advancedbilling.models.payment_method_credit_card import PaymentMethodCreditCard
from advancedbilling.models.payment_method_external import PaymentMethodExternal
from advancedbilling.models.payment_method_paypal import PaymentMethodPaypal
from advancedbilling.models.payment_related_events import PaymentRelatedEvents
from advancedbilling.models.pending_cancellation_change import PendingCancellationChange
from advancedbilling.models.prepaid_subscription_balance_changed import PrepaidSubscriptionBalanceChanged
from advancedbilling.models.prepaid_usage import PrepaidUsage
from advancedbilling.models.prepayment_account_balance_changed import PrepaymentAccountBalanceChanged
from advancedbilling.models.price_point_type import PricePointType
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.proforma_invoice_issued import ProformaInvoiceIssued
from advancedbilling.models.refund_consolidated_invoice import RefundConsolidatedInvoice
from advancedbilling.models.refund_invoice import RefundInvoice
from advancedbilling.models.refund_invoice_event_data import RefundInvoiceEventData
from advancedbilling.models.refund_success import RefundSuccess
from advancedbilling.models.remove_payment_event_data import RemovePaymentEventData
from advancedbilling.models.resume_options import ResumeOptions
from advancedbilling.models.snap_day import SnapDay
from advancedbilling.models.subscription_group_members_array_error import SubscriptionGroupMembersArrayError
from advancedbilling.models.subscription_group_signup_failure import SubscriptionGroupSignupFailure
from advancedbilling.models.subscription_group_signup_success import SubscriptionGroupSignupSuccess
from advancedbilling.models.subscription_group_single_error import SubscriptionGroupSingleError
from advancedbilling.models.subscription_product_change import SubscriptionProductChange
from advancedbilling.models.subscription_state_change import SubscriptionStateChange
from advancedbilling.models.update_metafield import UpdateMetafield
from advancedbilling.models.void_invoice_event_data import VoidInvoiceEventData
from advancedbilling.models.void_remainder_event_data import VoidRemainderEventData
from apimatic_core.types.union_types.any_of import AnyOf
from apimatic_core.types.union_types.leaf_type import LeafType
from apimatic_core.types.union_types.one_of import OneOf
from apimatic_core.types.union_types.union_type_context import UnionTypeContext as Context


class UnionTypeLookUp:

    """The `UnionTypeLookUp` class serves as a utility class for 
    storing and managing type combinator templates.It acts as a container for the templates 
    used in handling various data types within the application.

    """
    _templates = {
        'CreateProductPricePointProductId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'ListProductPricePointsInputProductId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'UpdateProductPricePointProductId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'UpdateProductPricePointPricePointId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'ReadProductPricePointProductId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'ReadProductPricePointPricePointId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'ArchiveProductPricePointProductId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'ArchiveProductPricePointPricePointId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'CreateUsageComponentId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'ListUsagesInputComponentId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'AddSubscriptionToAGroupGroup': OneOf(
            [
                LeafType(GroupSettings),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'AllocationQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'AllocationPreviousQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'AllocationPayment': OneOf(
            [
                LeafType(PaymentForAllocation)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'AllocationPreviewItemQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'AllocationPreviewItemPreviousQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'Invoice-Event-Payment': AnyOf(
            [
                LeafType(PaymentMethodApplePay,
                         Context.create(
                             discriminator_value='apple_pay',
                             discriminator='type'
                         )),
                LeafType(PaymentMethodBankAccount,
                         Context.create(
                             discriminator_value='bank_account',
                             discriminator='type'
                         )),
                LeafType(PaymentMethodCreditCard,
                         Context.create(
                             discriminator_value='credit_card',
                             discriminator='type'
                         )),
                LeafType(PaymentMethodExternal,
                         Context.create(
                             discriminator_value='external',
                             discriminator='type'
                         )),
                LeafType(PaymentMethodPaypal,
                         Context.create(
                             discriminator_value='paypal_account',
                             discriminator='type'
                         ))
            ]
        ),
        'CalendarBillingSnapDay': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ComponentPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'ComponentAllocationChangeAllocatedQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ComponentPricePointIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'ComponentPricePointAssignmentPricePoint': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CouponCompoundingStrategy': AnyOf(
            [
                LeafType(CompoundingStrategy)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateAllocationPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'CreateComponentPricePointRequestPricePoint': AnyOf(
            [
                LeafType(CreateComponentPricePoint),
                LeafType(CreatePrepaidUsageComponentPricePoint)
            ]
        ),
        'CreateComponentPricePointsRequestPricePoints': AnyOf(
            [
                LeafType(CreateComponentPricePoint),
                LeafType(CreatePrepaidUsageComponentPricePoint)
            ],
            Context.create(
               is_array=True
            )
        ),
        'CreateInvoiceCouponPercentage': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceCouponAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceCouponProductFamilyId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemQuantity': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemUnitPrice': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemProductId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemComponentId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoiceItemProductPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateInvoicePaymentAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateMetafieldsRequestMetafields': OneOf(
            [
                LeafType(CreateMetafield),
                LeafType(CreateMetafield,
                         Context.create(
                             is_array=True
                         ))
            ]
        ),
        'CreateMultiInvoicePaymentAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'CreateOrUpdateCouponCoupon': OneOf(
            [
                LeafType(CreateOrUpdatePercentageCoupon),
                LeafType(CreateOrUpdateFlatAmountCoupon)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateOrUpdatePercentageCouponPercentage': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'CreateOrUpdateSegmentPriceUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'CreatePaymentProfileExpirationMonth': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreatePaymentProfileExpirationYear': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty1Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty2Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty3Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSegmentSegmentProperty4Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionOfferId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionComponentComponentId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionComponentAllocatedQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CreateSubscriptionComponentPricePointId': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'CustomerChangePayer': OneOf(
            [
                LeafType(CustomerPayerChange)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'CustomerChangeShippingAddress': OneOf(
            [
                LeafType(AddressChange)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'CustomerChangeBillingAddress': OneOf(
            [
                LeafType(AddressChange)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'CustomerChangeCustomFields': OneOf(
            [
                LeafType(CustomerCustomFieldsChange)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'CustomerErrorResponseErrors': OneOf(
            [
                LeafType(CustomerError),
                LeafType(str,
                         Context.create(
                             is_array=True
                         ))
            ],
            Context.create(
               is_optional=True
            )
        ),
        'DeductServiceCreditAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'EBBComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'EventEventSpecificData': OneOf(
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
                LeafType(SubscriptionGroupSignupSuccess),
                LeafType(SubscriptionGroupSignupFailure),
                LeafType(CreditAccountBalanceChanged),
                LeafType(PrepaymentAccountBalanceChanged),
                LeafType(PaymentCollectionMethodChanged),
                LeafType(ItemPricePointChanged),
                LeafType(CustomFieldValueChange)
            ],
            Context.create(
               is_nullable=True
            )
        ),
        'InvoiceEventEventData': AnyOf(
            [
                LeafType(ApplyCreditNoteEventData),
                LeafType(ApplyDebitNoteEventData),
                LeafType(ApplyPaymentEventData),
                LeafType(ChangeInvoiceCollectionMethodEventData),
                LeafType(IssueInvoiceEventData),
                LeafType(RefundInvoiceEventData),
                LeafType(RemovePaymentEventData),
                LeafType(VoidInvoiceEventData),
                LeafType(VoidRemainderEventData)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'InvoiceEventDataPaymentMethod': AnyOf(
            [
                LeafType(PaymentMethodApplePay),
                LeafType(PaymentMethodBankAccount),
                LeafType(PaymentMethodCreditCard),
                LeafType(PaymentMethodExternal),
                LeafType(PaymentMethodPaypal)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'InvoiceLineItemComponentCostData2': OneOf(
            [
                LeafType(InvoiceLineItemComponentCostData)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'IssueServiceCreditAmount': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ]
        ),
        'MetafieldEnum': OneOf(
            [
                LeafType(str),
                LeafType(str,
                         Context.create(
                             is_array=True
                         ))
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'MeteredComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'OnOffComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PaymentProfileAttributesExpirationMonth': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PaymentProfileAttributesExpirationYear': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PaymentProfileResponsePaymentProfile': OneOf(
            [
                LeafType(BankAccountPaymentProfile),
                LeafType(CreditCardPaymentProfile)
            ]
        ),
        'PrepaidUsageComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'PriceStartingQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ]
        ),
        'PriceEndingQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'PriceUnitPrice': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ]
        ),
        'ProductExpirationIntervalUnit': OneOf(
            [
                LeafType(ExtendedIntervalUnit)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'ProductTrialIntervalUnit': OneOf(
            [
                LeafType(IntervalUnit)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'QuantityBasedComponentUnitPrice': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'ReactivateSubscriptionRequestResume': OneOf(
            [
                LeafType(bool),
                LeafType(ResumeOptions)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RecordPaymentResponsePrepayment': OneOf(
            [
                LeafType(InvoicePrePayment)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'RefundSegmentUids': OneOf(
            [
                LeafType(str,
                         Context.create(
                             is_array=True
                         )),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RefundConsolidatedInvoiceSegmentUids': OneOf(
            [
                LeafType(str,
                         Context.create(
                             is_array=True
                         )),
                LeafType(str)
            ]
        ),
        'RefundInvoiceRequestRefund': AnyOf(
            [
                LeafType(RefundInvoice),
                LeafType(RefundConsolidatedInvoice)
            ]
        ),
        'RefundPrepaymentAmount': OneOf(
            [
                LeafType(str),
                LeafType(float)
            ]
        ),
        'RenewalPreviewComponentComponentId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'RenewalPreviewComponentPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SegmentSegmentProperty1Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SegmentSegmentProperty2Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SegmentSegmentProperty3Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SegmentSegmentProperty4Value': OneOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(int),
                LeafType(bool)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroup2': OneOf(
            [
                LeafType(NestedSubscriptionGroup)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'SubscriptionComponentAllocatedQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionComponentPricingScheme': OneOf(
            [
                LeafType(PricingScheme)
            ],
            Context.create(
               is_optional=True,
               is_nullable=True
            )
        ),
        'SubscriptionComponentPricePointType': OneOf(
            [
                LeafType(PricePointType)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionCustomPricePriceInCents': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ]
        ),
        'SubscriptionCustomPriceInterval': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ]
        ),
        'SubscriptionCustomPriceTrialPriceInCents': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionCustomPriceTrialInterval': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionCustomPriceInitialChargeInCents': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionCustomPriceExpirationInterval': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupCreateErrorResponseErrors': OneOf(
            [
                LeafType(SubscriptionGroupMembersArrayError),
                LeafType(SubscriptionGroupSingleError),
                LeafType(str)
            ]
        ),
        'SubscriptionGroupCreditCardFullNumber': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupCreditCardExpirationMonth': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupCreditCardExpirationYear': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentComponentId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentAllocatedQuantity': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentUnitBalance': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'SubscriptionGroupSignupComponentPricePointId': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UpdateMetafieldsRequestMetafields': OneOf(
            [
                LeafType(UpdateMetafield),
                LeafType(UpdateMetafield,
                         Context.create(
                             is_array=True
                         ))
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UpdatePriceEndingQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UpdatePriceUnitPrice': OneOf(
            [
                LeafType(float),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UpdatePriceStartingQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UpdateSubscriptionSnapDay': OneOf(
            [
                LeafType(SnapDay),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UpdateSubscriptionNetTerms': OneOf(
            [
                LeafType(str),
                LeafType(int)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'UsageQuantity': OneOf(
            [
                LeafType(int),
                LeafType(str)
            ],
            Context.create(
               is_optional=True
            )
        ),
        'VoidInvoiceEventDataCreditNoteAttributes': OneOf(
            [
                LeafType(CreditNote)
            ],
            Context.create(
               is_nullable=True
            )
        )
    }

    @staticmethod
    def get(name):
        return UnionTypeLookUp._templates[name]

