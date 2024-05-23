# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.applied_credit_note_data import AppliedCreditNoteData
from advancedbilling.models.billing_address import BillingAddress
from advancedbilling.models.chargeback_status import ChargebackStatus
from advancedbilling.models.credit_note_1 import CreditNote1
from advancedbilling.models.credit_note_application import CreditNoteApplication
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.invoice_credit import InvoiceCredit
from advancedbilling.models.invoice_custom_field import InvoiceCustomField
from advancedbilling.models.invoice_customer import InvoiceCustomer
from advancedbilling.models.invoice_discount import InvoiceDiscount
from advancedbilling.models.invoice_display_settings import InvoiceDisplaySettings
from advancedbilling.models.invoice_line_item_2 import InvoiceLineItem2
from advancedbilling.models.invoice_payer import InvoicePayer
from advancedbilling.models.invoice_payment import InvoicePayment
from advancedbilling.models.invoice_previous_balance import InvoicePreviousBalance
from advancedbilling.models.invoice_refund import InvoiceRefund
from advancedbilling.models.invoice_seller import InvoiceSeller
from advancedbilling.models.invoice_tax import InvoiceTax
from advancedbilling.models.origin_invoice import OriginInvoice
from advancedbilling.models.shipping_address import ShippingAddress


class ApplyCreditNoteEventData1(object):

    """Implementation of the 'Apply Credit Note Event Data1' model.

    Example schema for an `apply_credit_note` event

    Attributes:
        uid (str): Unique identifier for the credit note application. It is
            generated automatically by Chargify and has the prefix "cdt_"
            followed by alphanumeric characters.
        credit_note_number (str): A unique, identifying string that appears on
            the credit note and in places it is referenced.
        credit_note_uid (str): Unique identifier for the credit note. It is
            generated automatically by Chargify and has the prefix "cn_"
            followed by alphanumeric characters.
        original_amount (str): The full, original amount of the credit note.
        applied_amount (str): The amount of the credit note applied to
            invoice.
        transaction_time (datetime): The time the credit note was applied, in
            ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
        memo (str): The credit note memo.
        role (InvoiceRole2): The role of the credit note (e.g. 'general')
        consolidated_invoice (bool): Shows whether it was applied to
            consolidated invoice or not
        applied_credit_notes (List[AppliedCreditNoteData]): List of credit
            notes applied to children invoices (if consolidated invoice)
        debit_note_number (str): A unique, identifying string that appears on
            the debit note and in places it is referenced.
        debit_note_uid (str): Unique identifier for the debit note. It is
            generated automatically by Chargify and has the prefix "db_"
            followed by alphanumeric characters.
        consolidation_level (InvoiceConsolidationLevel): Consolidation level
            of the invoice, which is applicable to invoice consolidation.  It
            will hold one of the following values:  * "none": A normal invoice
            with no consolidation. * "child": An invoice segment which has
            been combined into a consolidated invoice. * "parent": A
            consolidated invoice, whose contents are composed of invoice
            segments.  "Parent" invoices do not have lines of their own, but
            they have subtotals and totals which aggregate the member invoice
            segments.  See also the [invoice consolidation
            documentation](https://chargify.zendesk.com/hc/en-us/articles/44077
            46391835).
        payment_method (PaymentMethodApplePay | PaymentMethodBankAccount |
            PaymentMethodCreditCard | PaymentMethodExternal |
            PaymentMethodPaypal): A nested data structure detailing the method
            of payment
        transaction_id (int): The Chargify id of the original payment
        parent_invoice_number (int): For invoices with `consolidation_level`
            of `child`, this specifies the number of the parent (consolidated)
            invoice.
        remaining_prepayment_amount (str): TODO: type description here.
        prepayment (bool): The flag that shows whether the original payment
            was a prepayment or not
        external (bool): TODO: type description here.
        id (long|int): TODO: type description here.
        site_id (int): ID of the site to which the invoice belongs.
        customer_id (int): ID of the customer to which the invoice belongs.
        subscription_id (int): ID of the subscription that generated the
            invoice.
        number (str): A unique, identifying string that appears on the invoice
            and in places the invoice is referenced.  While the UID is long
            and not appropriate to show to customers, the number is usually
            shorter and consumable by the customer and the merchant alike.
        sequence_number (int): A monotonically increasing number assigned to
            invoices as they are created.  This number is unique within a site
            and can be used to sort and order invoices.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        issue_date (date): Date the invoice was issued to the customer.  This
            is the date that the invoice was made available for payment.  The
            format is `"YYYY-MM-DD"`.
        due_date (date): Date the invoice is due.  The format is
            `"YYYY-MM-DD"`.
        paid_date (date): Date the invoice became fully paid.  If partial
            payments are applied to the invoice, this date will not be present
            until payment has been made in full.  The format is
            `"YYYY-MM-DD"`.
        status (InvoiceStatus): The current status of the invoice. See
            [Invoice
            Statuses](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405
            078794253-Introduction-to-Invoices#invoice-statuses) for more.
        parent_invoice_id (int): TODO: type description here.
        collection_method (CollectionMethod): The type of payment collection
            to be used in the subscription. For legacy Statements Architecture
            valid options are - `invoice`, `automatic`. For current
            Relationship Invoicing Architecture valid options are -
            `remittance`, `automatic`, `prepaid`.
        payment_instructions (str): A message that is printed on the invoice
            when it is marked for remittance collection. It is intended to
            describe to the customer how they may make payment, and is
            configured by the merchant.
        currency (str): The ISO 4217 currency code (3 character string)
            representing the currency of invoice transaction.
        parent_invoice_uid (str): For invoices with `consolidation_level` of
            `child`, this specifies the UID of the parent (consolidated)
            invoice.
        subscription_group_id (int): TODO: type description here.
        group_primary_subscription_id (int): For invoices with
            `consolidation_level` of `parent`, this specifies the ID of the
            subscription which was the primary subscription of the
            subscription group that generated the invoice.
        product_name (str): The name of the product subscribed when the
            invoice was generated.
        product_family_name (str): The name of the product family subscribed
            when the invoice was generated.
        seller (InvoiceSeller): Information about the seller (merchant) listed
            on the masthead of the invoice.
        customer (InvoiceCustomer): Information about the customer who is
            owner or recipient the invoiced subscription.
        payer (InvoicePayer): TODO: type description here.
        recipient_emails (List[str]): TODO: type description here.
        net_terms (int): TODO: type description here.
        billing_address (BillingAddress): TODO: type description here.
        shipping_address (ShippingAddress): TODO: type description here.
        subtotal_amount (str): Subtotal of the invoice, which is the sum of
            all line items before discounts or taxes.
        discount_amount (str): Total discount applied to the invoice.
        tax_amount (str): Total tax on the invoice.
        total_amount (str): The invoice total, which is `subtotal_amount -
            discount_amount + tax_amount`.'
        credit_amount (str): The amount of credit (from credit notes) applied
            to this invoice.  Credits offset the amount due from the
            customer.
        refund_amount (str): The amount of the refund.
        paid_amount (str): The amount paid on the invoice by the customer.
        due_amount (str): Amount due on the invoice, which is `total_amount -
            credit_amount - paid_amount`.
        line_items (List[InvoiceLineItem2]): Line items on the invoice.
        discounts (List[InvoiceDiscount]): TODO: type description here.
        taxes (List[InvoiceTax]): TODO: type description here.
        credits (List[InvoiceCredit]): TODO: type description here.
        refunds (List[InvoiceRefund]): TODO: type description here.
        payments (List[InvoicePayment]): TODO: type description here.
        custom_fields (List[InvoiceCustomField]): TODO: type description
            here.
        display_settings (InvoiceDisplaySettings): TODO: type description
            here.
        public_url (str): The public URL of the invoice
        previous_balance_data (InvoicePreviousBalance): TODO: type description
            here.
        chargeback_status (ChargebackStatus): TODO: type description here.
        from_collection_method (str): The previous collection method of the
            invoice.
        to_collection_method (str): The new collection method of the invoice.
        gateway_trans_id (str): Identifier for the transaction within the
            payment gateway.
        amount (str): The monetary value associated with the linked payment,
            expressed in dollars.
        from_status (object): TODO: type description here.
        to_status (object): TODO: type description here.
        applied_date (date): Credit notes are applied to invoices to offset
            invoiced amounts - they reduce the amount due. This field is the
            date the credit note became fully applied to invoices.  If the
            credit note has been partially applied, this field will not have a
            value until it has been fully applied.  The format is
            `"YYYY-MM-DD"`.
        remaining_amount (str): The amount of the credit note remaining to be
            applied to invoices, which is `total_amount - applied_amount`.
        applications (List[CreditNoteApplication]): TODO: type description
            here.
        origin_invoices (List[OriginInvoice]): An array of origin invoices for
            the credit note. Learn more about [Origin Invoice from our
            docs](https://chargify.zendesk.com/hc/en-us/articles/4407753036699#
            origin-invoices)
        origin_credit_note_uid (str): Unique identifier for the connected
            credit note. It is generated automatically by Chargify and has the
            prefix "cn_" followed by alphanumeric characters.  While the UID
            is long and not appropriate to show to customers, the number is
            usually shorter and consumable by the customer and the merchant
            alike.
        origin_credit_note_number (str): A unique, identifying string of the
            connected credit note.
        amount_in_cents (int): The monetary value of the payment, expressed in
            cents.
        apply_credit (bool): If true, credit was created and applied it to the
            invoice.
        credit_note_attributes (CreditNote1): TODO: type description here.
        payment_id (int): The ID of the payment transaction to be refunded.
        refund_id (int): The ID of the refund transaction.
        is_advance_invoice (bool): If true, the invoice is an advance
            invoice.
        reason (str): The reason for the void.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "credit_note_number": 'credit_note_number',
        "credit_note_uid": 'credit_note_uid',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time',
        "memo": 'memo',
        "debit_note_number": 'debit_note_number',
        "debit_note_uid": 'debit_note_uid',
        "consolidation_level": 'consolidation_level',
        "payment_method": 'payment_method',
        "transaction_id": 'transaction_id',
        "prepayment": 'prepayment',
        "total_amount": 'total_amount',
        "refund_amount": 'refund_amount',
        "due_amount": 'due_amount',
        "chargeback_status": 'chargeback_status',
        "from_collection_method": 'from_collection_method',
        "to_collection_method": 'to_collection_method',
        "from_status": 'from_status',
        "to_status": 'to_status',
        "amount_in_cents": 'amount_in_cents',
        "apply_credit": 'apply_credit',
        "credit_note_attributes": 'credit_note_attributes',
        "payment_id": 'payment_id',
        "refund_id": 'refund_id',
        "is_advance_invoice": 'is_advance_invoice',
        "reason": 'reason',
        "role": 'role',
        "consolidated_invoice": 'consolidated_invoice',
        "applied_credit_notes": 'applied_credit_notes',
        "parent_invoice_number": 'parent_invoice_number',
        "remaining_prepayment_amount": 'remaining_prepayment_amount',
        "external": 'external',
        "id": 'id',
        "site_id": 'site_id',
        "customer_id": 'customer_id',
        "subscription_id": 'subscription_id',
        "number": 'number',
        "sequence_number": 'sequence_number',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "issue_date": 'issue_date',
        "due_date": 'due_date',
        "paid_date": 'paid_date',
        "status": 'status',
        "parent_invoice_id": 'parent_invoice_id',
        "collection_method": 'collection_method',
        "payment_instructions": 'payment_instructions',
        "currency": 'currency',
        "parent_invoice_uid": 'parent_invoice_uid',
        "subscription_group_id": 'subscription_group_id',
        "group_primary_subscription_id": 'group_primary_subscription_id',
        "product_name": 'product_name',
        "product_family_name": 'product_family_name',
        "seller": 'seller',
        "customer": 'customer',
        "payer": 'payer',
        "recipient_emails": 'recipient_emails',
        "net_terms": 'net_terms',
        "billing_address": 'billing_address',
        "shipping_address": 'shipping_address',
        "subtotal_amount": 'subtotal_amount',
        "discount_amount": 'discount_amount',
        "tax_amount": 'tax_amount',
        "credit_amount": 'credit_amount',
        "paid_amount": 'paid_amount',
        "line_items": 'line_items',
        "discounts": 'discounts',
        "taxes": 'taxes',
        "credits": 'credits',
        "refunds": 'refunds',
        "payments": 'payments',
        "custom_fields": 'custom_fields',
        "display_settings": 'display_settings',
        "public_url": 'public_url',
        "previous_balance_data": 'previous_balance_data',
        "gateway_trans_id": 'gateway_trans_id',
        "amount": 'amount',
        "applied_date": 'applied_date',
        "remaining_amount": 'remaining_amount',
        "applications": 'applications',
        "origin_invoices": 'origin_invoices',
        "origin_credit_note_uid": 'origin_credit_note_uid',
        "origin_credit_note_number": 'origin_credit_note_number'
    }

    _optionals = [
        'role',
        'consolidated_invoice',
        'applied_credit_notes',
        'parent_invoice_number',
        'remaining_prepayment_amount',
        'external',
        'id',
        'site_id',
        'customer_id',
        'subscription_id',
        'number',
        'sequence_number',
        'created_at',
        'updated_at',
        'issue_date',
        'due_date',
        'paid_date',
        'status',
        'parent_invoice_id',
        'collection_method',
        'payment_instructions',
        'currency',
        'parent_invoice_uid',
        'subscription_group_id',
        'group_primary_subscription_id',
        'product_name',
        'product_family_name',
        'seller',
        'customer',
        'payer',
        'recipient_emails',
        'net_terms',
        'billing_address',
        'shipping_address',
        'subtotal_amount',
        'discount_amount',
        'tax_amount',
        'credit_amount',
        'paid_amount',
        'line_items',
        'discounts',
        'taxes',
        'credits',
        'refunds',
        'payments',
        'custom_fields',
        'display_settings',
        'public_url',
        'previous_balance_data',
        'gateway_trans_id',
        'amount',
        'applied_date',
        'remaining_amount',
        'applications',
        'origin_invoices',
        'origin_credit_note_uid',
        'origin_credit_note_number',
    ]

    _nullables = [
        'memo',
        'parent_invoice_number',
        'remaining_prepayment_amount',
        'paid_date',
        'parent_invoice_id',
        'parent_invoice_uid',
        'subscription_group_id',
        'group_primary_subscription_id',
    ]

    def __init__(self,
                 uid=None,
                 credit_note_number=None,
                 credit_note_uid=None,
                 original_amount=None,
                 applied_amount=None,
                 transaction_time=None,
                 memo=None,
                 debit_note_number=None,
                 debit_note_uid=None,
                 consolidation_level=None,
                 payment_method=None,
                 transaction_id=None,
                 prepayment=None,
                 total_amount=None,
                 refund_amount=None,
                 due_amount=None,
                 chargeback_status=None,
                 from_collection_method=None,
                 to_collection_method=None,
                 from_status=None,
                 to_status=None,
                 amount_in_cents=None,
                 apply_credit=None,
                 credit_note_attributes=None,
                 payment_id=None,
                 refund_id=None,
                 is_advance_invoice=None,
                 reason=None,
                 role=APIHelper.SKIP,
                 consolidated_invoice=APIHelper.SKIP,
                 applied_credit_notes=APIHelper.SKIP,
                 parent_invoice_number=APIHelper.SKIP,
                 remaining_prepayment_amount=APIHelper.SKIP,
                 external=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 sequence_number=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 due_date=APIHelper.SKIP,
                 paid_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 parent_invoice_id=APIHelper.SKIP,
                 collection_method=APIHelper.SKIP,
                 payment_instructions=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 parent_invoice_uid=APIHelper.SKIP,
                 subscription_group_id=APIHelper.SKIP,
                 group_primary_subscription_id=APIHelper.SKIP,
                 product_name=APIHelper.SKIP,
                 product_family_name=APIHelper.SKIP,
                 seller=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 payer=APIHelper.SKIP,
                 recipient_emails=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 shipping_address=APIHelper.SKIP,
                 subtotal_amount=APIHelper.SKIP,
                 discount_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 credit_amount=APIHelper.SKIP,
                 paid_amount=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 taxes=APIHelper.SKIP,
                 credits=APIHelper.SKIP,
                 refunds=APIHelper.SKIP,
                 payments=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 display_settings=APIHelper.SKIP,
                 public_url=APIHelper.SKIP,
                 previous_balance_data=APIHelper.SKIP,
                 gateway_trans_id=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 applied_date=APIHelper.SKIP,
                 remaining_amount=APIHelper.SKIP,
                 applications=APIHelper.SKIP,
                 origin_invoices=APIHelper.SKIP,
                 origin_credit_note_uid=APIHelper.SKIP,
                 origin_credit_note_number=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ApplyCreditNoteEventData1 class"""

        # Initialize members of the class
        self.uid = uid 
        self.credit_note_number = credit_note_number 
        self.credit_note_uid = credit_note_uid 
        self.original_amount = original_amount 
        self.applied_amount = applied_amount 
        self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        self.memo = memo 
        if role is not APIHelper.SKIP:
            self.role = role 
        if consolidated_invoice is not APIHelper.SKIP:
            self.consolidated_invoice = consolidated_invoice 
        if applied_credit_notes is not APIHelper.SKIP:
            self.applied_credit_notes = applied_credit_notes 
        self.debit_note_number = debit_note_number 
        self.debit_note_uid = debit_note_uid 
        self.consolidation_level = consolidation_level 
        self.payment_method = payment_method 
        self.transaction_id = transaction_id 
        if parent_invoice_number is not APIHelper.SKIP:
            self.parent_invoice_number = parent_invoice_number 
        if remaining_prepayment_amount is not APIHelper.SKIP:
            self.remaining_prepayment_amount = remaining_prepayment_amount 
        self.prepayment = prepayment 
        if external is not APIHelper.SKIP:
            self.external = external 
        if id is not APIHelper.SKIP:
            self.id = id 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if number is not APIHelper.SKIP:
            self.number = number 
        if sequence_number is not APIHelper.SKIP:
            self.sequence_number = sequence_number 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if issue_date is not APIHelper.SKIP:
            self.issue_date = issue_date 
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date 
        if paid_date is not APIHelper.SKIP:
            self.paid_date = paid_date 
        if status is not APIHelper.SKIP:
            self.status = status 
        if parent_invoice_id is not APIHelper.SKIP:
            self.parent_invoice_id = parent_invoice_id 
        if collection_method is not APIHelper.SKIP:
            self.collection_method = collection_method 
        if payment_instructions is not APIHelper.SKIP:
            self.payment_instructions = payment_instructions 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if parent_invoice_uid is not APIHelper.SKIP:
            self.parent_invoice_uid = parent_invoice_uid 
        if subscription_group_id is not APIHelper.SKIP:
            self.subscription_group_id = subscription_group_id 
        if group_primary_subscription_id is not APIHelper.SKIP:
            self.group_primary_subscription_id = group_primary_subscription_id 
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name 
        if product_family_name is not APIHelper.SKIP:
            self.product_family_name = product_family_name 
        if seller is not APIHelper.SKIP:
            self.seller = seller 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if payer is not APIHelper.SKIP:
            self.payer = payer 
        if recipient_emails is not APIHelper.SKIP:
            self.recipient_emails = recipient_emails 
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if shipping_address is not APIHelper.SKIP:
            self.shipping_address = shipping_address 
        if subtotal_amount is not APIHelper.SKIP:
            self.subtotal_amount = subtotal_amount 
        if discount_amount is not APIHelper.SKIP:
            self.discount_amount = discount_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        self.total_amount = total_amount 
        if credit_amount is not APIHelper.SKIP:
            self.credit_amount = credit_amount 
        self.refund_amount = refund_amount 
        if paid_amount is not APIHelper.SKIP:
            self.paid_amount = paid_amount 
        self.due_amount = due_amount 
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        if taxes is not APIHelper.SKIP:
            self.taxes = taxes 
        if credits is not APIHelper.SKIP:
            self.credits = credits 
        if refunds is not APIHelper.SKIP:
            self.refunds = refunds 
        if payments is not APIHelper.SKIP:
            self.payments = payments 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if display_settings is not APIHelper.SKIP:
            self.display_settings = display_settings 
        if public_url is not APIHelper.SKIP:
            self.public_url = public_url 
        if previous_balance_data is not APIHelper.SKIP:
            self.previous_balance_data = previous_balance_data 
        self.chargeback_status = chargeback_status 
        self.from_collection_method = from_collection_method 
        self.to_collection_method = to_collection_method 
        if gateway_trans_id is not APIHelper.SKIP:
            self.gateway_trans_id = gateway_trans_id 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        self.from_status = from_status 
        self.to_status = to_status 
        if applied_date is not APIHelper.SKIP:
            self.applied_date = applied_date 
        if remaining_amount is not APIHelper.SKIP:
            self.remaining_amount = remaining_amount 
        if applications is not APIHelper.SKIP:
            self.applications = applications 
        if origin_invoices is not APIHelper.SKIP:
            self.origin_invoices = origin_invoices 
        if origin_credit_note_uid is not APIHelper.SKIP:
            self.origin_credit_note_uid = origin_credit_note_uid 
        if origin_credit_note_number is not APIHelper.SKIP:
            self.origin_credit_note_number = origin_credit_note_number 
        self.amount_in_cents = amount_in_cents 
        self.apply_credit = apply_credit 
        self.credit_note_attributes = credit_note_attributes 
        self.payment_id = payment_id 
        self.refund_id = refund_id 
        self.is_advance_invoice = is_advance_invoice 
        self.reason = reason 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        credit_note_number = dictionary.get("credit_note_number") if dictionary.get("credit_note_number") else None
        credit_note_uid = dictionary.get("credit_note_uid") if dictionary.get("credit_note_uid") else None
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else None
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else None
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        debit_note_number = dictionary.get("debit_note_number") if dictionary.get("debit_note_number") else None
        debit_note_uid = dictionary.get("debit_note_uid") if dictionary.get("debit_note_uid") else None
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else None
        payment_method = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ApplyCreditNoteEventData1PaymentMethod'), dictionary.get('payment_method'), False) if dictionary.get('payment_method') is not None else None
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else None
        prepayment = dictionary.get("prepayment") if "prepayment" in dictionary.keys() else None
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else None
        refund_amount = dictionary.get("refund_amount") if dictionary.get("refund_amount") else None
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else None
        chargeback_status = dictionary.get("chargeback_status") if dictionary.get("chargeback_status") else None
        from_collection_method = dictionary.get("from_collection_method") if dictionary.get("from_collection_method") else None
        to_collection_method = dictionary.get("to_collection_method") if dictionary.get("to_collection_method") else None
        from_status = dictionary.get("from_status") if dictionary.get("from_status") else None
        to_status = dictionary.get("to_status") if dictionary.get("to_status") else None
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else None
        apply_credit = dictionary.get("apply_credit") if "apply_credit" in dictionary.keys() else None
        credit_note_attributes = CreditNote1.from_dictionary(dictionary.get('credit_note_attributes')) if dictionary.get('credit_note_attributes') else None
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else None
        refund_id = dictionary.get("refund_id") if dictionary.get("refund_id") else None
        is_advance_invoice = dictionary.get("is_advance_invoice") if "is_advance_invoice" in dictionary.keys() else None
        reason = dictionary.get("reason") if dictionary.get("reason") else None
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        consolidated_invoice = dictionary.get("consolidated_invoice") if "consolidated_invoice" in dictionary.keys() else APIHelper.SKIP
        applied_credit_notes = None
        if dictionary.get('applied_credit_notes') is not None:
            applied_credit_notes = [AppliedCreditNoteData.from_dictionary(x) for x in dictionary.get('applied_credit_notes')]
        else:
            applied_credit_notes = APIHelper.SKIP
        parent_invoice_number = dictionary.get("parent_invoice_number") if "parent_invoice_number" in dictionary.keys() else APIHelper.SKIP
        remaining_prepayment_amount = dictionary.get("remaining_prepayment_amount") if "remaining_prepayment_amount" in dictionary.keys() else APIHelper.SKIP
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        sequence_number = dictionary.get("sequence_number") if dictionary.get("sequence_number") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        issue_date = dateutil.parser.parse(dictionary.get('issue_date')).date() if dictionary.get('issue_date') else APIHelper.SKIP
        due_date = dateutil.parser.parse(dictionary.get('due_date')).date() if dictionary.get('due_date') else APIHelper.SKIP
        if 'paid_date' in dictionary.keys():
            paid_date = dateutil.parser.parse(dictionary.get('paid_date')).date() if dictionary.get('paid_date') else None
        else:
            paid_date = APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        parent_invoice_id = dictionary.get("parent_invoice_id") if "parent_invoice_id" in dictionary.keys() else APIHelper.SKIP
        collection_method = dictionary.get("collection_method") if dictionary.get("collection_method") else APIHelper.SKIP
        payment_instructions = dictionary.get("payment_instructions") if dictionary.get("payment_instructions") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        parent_invoice_uid = dictionary.get("parent_invoice_uid") if "parent_invoice_uid" in dictionary.keys() else APIHelper.SKIP
        subscription_group_id = dictionary.get("subscription_group_id") if "subscription_group_id" in dictionary.keys() else APIHelper.SKIP
        group_primary_subscription_id = dictionary.get("group_primary_subscription_id") if "group_primary_subscription_id" in dictionary.keys() else APIHelper.SKIP
        product_name = dictionary.get("product_name") if dictionary.get("product_name") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
        seller = InvoiceSeller.from_dictionary(dictionary.get('seller')) if 'seller' in dictionary.keys() else APIHelper.SKIP
        customer = InvoiceCustomer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        payer = InvoicePayer.from_dictionary(dictionary.get('payer')) if 'payer' in dictionary.keys() else APIHelper.SKIP
        recipient_emails = dictionary.get("recipient_emails") if dictionary.get("recipient_emails") else APIHelper.SKIP
        net_terms = dictionary.get("net_terms") if dictionary.get("net_terms") else APIHelper.SKIP
        billing_address = BillingAddress.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        shipping_address = ShippingAddress.from_dictionary(dictionary.get('shipping_address')) if 'shipping_address' in dictionary.keys() else APIHelper.SKIP
        subtotal_amount = dictionary.get("subtotal_amount") if dictionary.get("subtotal_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        credit_amount = dictionary.get("credit_amount") if dictionary.get("credit_amount") else APIHelper.SKIP
        paid_amount = dictionary.get("paid_amount") if dictionary.get("paid_amount") else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [InvoiceLineItem2.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        discounts = None
        if dictionary.get('discounts') is not None:
            discounts = [InvoiceDiscount.from_dictionary(x) for x in dictionary.get('discounts')]
        else:
            discounts = APIHelper.SKIP
        taxes = None
        if dictionary.get('taxes') is not None:
            taxes = [InvoiceTax.from_dictionary(x) for x in dictionary.get('taxes')]
        else:
            taxes = APIHelper.SKIP
        credits = None
        if dictionary.get('credits') is not None:
            credits = [InvoiceCredit.from_dictionary(x) for x in dictionary.get('credits')]
        else:
            credits = APIHelper.SKIP
        refunds = None
        if dictionary.get('refunds') is not None:
            refunds = [InvoiceRefund.from_dictionary(x) for x in dictionary.get('refunds')]
        else:
            refunds = APIHelper.SKIP
        payments = None
        if dictionary.get('payments') is not None:
            payments = [InvoicePayment.from_dictionary(x) for x in dictionary.get('payments')]
        else:
            payments = APIHelper.SKIP
        custom_fields = None
        if dictionary.get('custom_fields') is not None:
            custom_fields = [InvoiceCustomField.from_dictionary(x) for x in dictionary.get('custom_fields')]
        else:
            custom_fields = APIHelper.SKIP
        display_settings = InvoiceDisplaySettings.from_dictionary(dictionary.get('display_settings')) if 'display_settings' in dictionary.keys() else APIHelper.SKIP
        public_url = dictionary.get("public_url") if dictionary.get("public_url") else APIHelper.SKIP
        previous_balance_data = InvoicePreviousBalance.from_dictionary(dictionary.get('previous_balance_data')) if 'previous_balance_data' in dictionary.keys() else APIHelper.SKIP
        gateway_trans_id = dictionary.get("gateway_trans_id") if dictionary.get("gateway_trans_id") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        applied_date = dateutil.parser.parse(dictionary.get('applied_date')).date() if dictionary.get('applied_date') else APIHelper.SKIP
        remaining_amount = dictionary.get("remaining_amount") if dictionary.get("remaining_amount") else APIHelper.SKIP
        applications = None
        if dictionary.get('applications') is not None:
            applications = [CreditNoteApplication.from_dictionary(x) for x in dictionary.get('applications')]
        else:
            applications = APIHelper.SKIP
        origin_invoices = None
        if dictionary.get('origin_invoices') is not None:
            origin_invoices = [OriginInvoice.from_dictionary(x) for x in dictionary.get('origin_invoices')]
        else:
            origin_invoices = APIHelper.SKIP
        origin_credit_note_uid = dictionary.get("origin_credit_note_uid") if dictionary.get("origin_credit_note_uid") else APIHelper.SKIP
        origin_credit_note_number = dictionary.get("origin_credit_note_number") if dictionary.get("origin_credit_note_number") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(uid,
                   credit_note_number,
                   credit_note_uid,
                   original_amount,
                   applied_amount,
                   transaction_time,
                   memo,
                   debit_note_number,
                   debit_note_uid,
                   consolidation_level,
                   payment_method,
                   transaction_id,
                   prepayment,
                   total_amount,
                   refund_amount,
                   due_amount,
                   chargeback_status,
                   from_collection_method,
                   to_collection_method,
                   from_status,
                   to_status,
                   amount_in_cents,
                   apply_credit,
                   credit_note_attributes,
                   payment_id,
                   refund_id,
                   is_advance_invoice,
                   reason,
                   role,
                   consolidated_invoice,
                   applied_credit_notes,
                   parent_invoice_number,
                   remaining_prepayment_amount,
                   external,
                   id,
                   site_id,
                   customer_id,
                   subscription_id,
                   number,
                   sequence_number,
                   created_at,
                   updated_at,
                   issue_date,
                   due_date,
                   paid_date,
                   status,
                   parent_invoice_id,
                   collection_method,
                   payment_instructions,
                   currency,
                   parent_invoice_uid,
                   subscription_group_id,
                   group_primary_subscription_id,
                   product_name,
                   product_family_name,
                   seller,
                   customer,
                   payer,
                   recipient_emails,
                   net_terms,
                   billing_address,
                   shipping_address,
                   subtotal_amount,
                   discount_amount,
                   tax_amount,
                   credit_amount,
                   paid_amount,
                   line_items,
                   discounts,
                   taxes,
                   credits,
                   refunds,
                   payments,
                   custom_fields,
                   display_settings,
                   public_url,
                   previous_balance_data,
                   gateway_trans_id,
                   amount,
                   applied_date,
                   remaining_amount,
                   applications,
                   origin_invoices,
                   origin_credit_note_uid,
                   origin_credit_note_number,
                   dictionary)

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
            return APIHelper.is_valid_type(value=dictionary.uid, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.credit_note_number, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.credit_note_uid, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.original_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.transaction_time, type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.memo, type_callable=lambda value: isinstance(value, str), is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.debit_note_number, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.debit_note_uid, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.consolidation_level, type_callable=lambda value: InvoiceConsolidationLevel.validate(value)) \
                and UnionTypeLookUp.get('ApplyCreditNoteEventData1PaymentMethod').validate(dictionary.payment_method).is_valid \
                and APIHelper.is_valid_type(value=dictionary.transaction_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.prepayment, type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.total_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.refund_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.due_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.chargeback_status, type_callable=lambda value: ChargebackStatus.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.from_collection_method, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.to_collection_method, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.from_status, type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.to_status, type_callable=lambda value: isinstance(value, object)) \
                and APIHelper.is_valid_type(value=dictionary.amount_in_cents, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.apply_credit, type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.credit_note_attributes, type_callable=lambda value: CreditNote1.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.payment_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.refund_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.is_advance_invoice, type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.reason, type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('uid'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('credit_note_number'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('credit_note_uid'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('original_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_time'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'), type_callable=lambda value: isinstance(value, str), is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('debit_note_number'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('debit_note_uid'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('consolidation_level'), type_callable=lambda value: InvoiceConsolidationLevel.validate(value)) \
            and UnionTypeLookUp.get('ApplyCreditNoteEventData1PaymentMethod').validate(dictionary.get('payment_method')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('prepayment'), type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('total_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('refund_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('due_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('chargeback_status'), type_callable=lambda value: ChargebackStatus.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('from_collection_method'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('to_collection_method'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('from_status'), type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('to_status'), type_callable=lambda value: isinstance(value, object)) \
            and APIHelper.is_valid_type(value=dictionary.get('amount_in_cents'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('apply_credit'), type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('credit_note_attributes'), type_callable=lambda value: CreditNote1.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('refund_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('is_advance_invoice'), type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('reason'), type_callable=lambda value: isinstance(value, str))
