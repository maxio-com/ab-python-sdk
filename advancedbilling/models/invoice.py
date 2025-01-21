# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_address import InvoiceAddress
from advancedbilling.models.invoice_avatax_details import InvoiceAvataxDetails
from advancedbilling.models.invoice_credit import InvoiceCredit
from advancedbilling.models.invoice_custom_field import InvoiceCustomField
from advancedbilling.models.invoice_customer import InvoiceCustomer
from advancedbilling.models.invoice_debit import InvoiceDebit
from advancedbilling.models.invoice_discount import InvoiceDiscount
from advancedbilling.models.invoice_display_settings import InvoiceDisplaySettings
from advancedbilling.models.invoice_line_item import InvoiceLineItem
from advancedbilling.models.invoice_payer import InvoicePayer
from advancedbilling.models.invoice_payment import InvoicePayment
from advancedbilling.models.invoice_previous_balance import InvoicePreviousBalance
from advancedbilling.models.invoice_refund import InvoiceRefund
from advancedbilling.models.invoice_seller import InvoiceSeller
from advancedbilling.models.invoice_tax import InvoiceTax


class Invoice(object):

    """Implementation of the 'Invoice' model.

    Attributes:
        id (int): The model property of type int.
        uid (str): Unique identifier for the invoice. It is generated
            automatically by Chargify and has the prefix "inv_" followed by
            alphanumeric characters.
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
        transaction_time (datetime): The model property of type datetime.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        issue_date (date): Date the invoice was issued to the customer.  This
            is the date that the invoice was made available for payment.  The
            format is `"YYYY-MM-DD"`.
        due_date (date): Date the invoice is due.  The format is
            `"YYYY-MM-DD"`.
        paid_date (date): Date the invoice became fully paid.  If partial
            payments are applied to the invoice, this date will not be present
            until payment has been made in full.  The format is `"YYYY-MM-DD"`.
        status (InvoiceStatus): The current status of the invoice. See
            [Invoice
            Statuses](https://maxio.zendesk.com/hc/en-us/articles/2425228782964
            5-Advanced-Billing-Invoices-Overview#invoice-statuses) for more.
        role (InvoiceRole): The model property of type InvoiceRole.
        parent_invoice_id (int): The model property of type int.
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
        consolidation_level (InvoiceConsolidationLevel): Consolidation level
            of the invoice, which is applicable to invoice consolidation.  It
            will hold one of the following values:  * "none": A normal invoice
            with no consolidation. * "child": An invoice segment which has
            been combined into a consolidated invoice. * "parent": A
            consolidated invoice, whose contents are composed of invoice
            segments.  "Parent" invoices do not have lines of their own, but
            they have subtotals and totals which aggregate the member invoice
            segments.  See also the [invoice consolidation
            documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269
            909389-Invoice-Consolidation).
        parent_invoice_uid (str): For invoices with `consolidation_level` of
            `child`, this specifies the UID of the parent (consolidated)
            invoice.
        subscription_group_id (int): The model property of type int.
        parent_invoice_number (int): For invoices with `consolidation_level`
            of `child`, this specifies the number of the parent (consolidated)
            invoice.
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
        payer (InvoicePayer): The model property of type InvoicePayer.
        recipient_emails (List[str]): The model property of type List[str].
        net_terms (int): The model property of type int.
        memo (str): The memo printed on invoices of any collection type.  This
            message is in control of the merchant.
        billing_address (InvoiceAddress): The invoice billing address.
        shipping_address (InvoiceAddress): The invoice shipping address.
        subtotal_amount (str): Subtotal of the invoice, which is the sum of
            all line items before discounts or taxes.
        discount_amount (str): Total discount applied to the invoice.
        tax_amount (str): Total tax on the invoice.
        total_amount (str): The invoice total, which is `subtotal_amount -
            discount_amount + tax_amount`.'
        credit_amount (str): The amount of credit (from credit notes) applied
            to this invoice.  Credits offset the amount due from the customer.
        debit_amount (str): The model property of type str.
        refund_amount (str): The model property of type str.
        paid_amount (str): The amount paid on the invoice by the customer.
        due_amount (str): Amount due on the invoice, which is `total_amount -
            credit_amount - paid_amount`.
        line_items (List[InvoiceLineItem]): Line items on the invoice.
        discounts (List[InvoiceDiscount]): The model property of type
            List[InvoiceDiscount].
        taxes (List[InvoiceTax]): The model property of type List[InvoiceTax].
        credits (List[InvoiceCredit]): The model property of type
            List[InvoiceCredit].
        debits (List[InvoiceDebit]): The model property of type
            List[InvoiceDebit].
        refunds (List[InvoiceRefund]): The model property of type
            List[InvoiceRefund].
        payments (List[InvoicePayment]): The model property of type
            List[InvoicePayment].
        custom_fields (List[InvoiceCustomField]): The model property of type
            List[InvoiceCustomField].
        display_settings (InvoiceDisplaySettings): The model property of type
            InvoiceDisplaySettings.
        avatax_details (InvoiceAvataxDetails): The model property of type
            InvoiceAvataxDetails.
        public_url (str): The public URL of the invoice
        previous_balance_data (InvoicePreviousBalance): The model property of
            type InvoicePreviousBalance.
        public_url_expires_on (date): The format is `"YYYY-MM-DD"`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "uid": 'uid',
        "site_id": 'site_id',
        "customer_id": 'customer_id',
        "subscription_id": 'subscription_id',
        "number": 'number',
        "sequence_number": 'sequence_number',
        "transaction_time": 'transaction_time',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "issue_date": 'issue_date',
        "due_date": 'due_date',
        "paid_date": 'paid_date',
        "status": 'status',
        "role": 'role',
        "parent_invoice_id": 'parent_invoice_id',
        "collection_method": 'collection_method',
        "payment_instructions": 'payment_instructions',
        "currency": 'currency',
        "consolidation_level": 'consolidation_level',
        "parent_invoice_uid": 'parent_invoice_uid',
        "subscription_group_id": 'subscription_group_id',
        "parent_invoice_number": 'parent_invoice_number',
        "group_primary_subscription_id": 'group_primary_subscription_id',
        "product_name": 'product_name',
        "product_family_name": 'product_family_name',
        "seller": 'seller',
        "customer": 'customer',
        "payer": 'payer',
        "recipient_emails": 'recipient_emails',
        "net_terms": 'net_terms',
        "memo": 'memo',
        "billing_address": 'billing_address',
        "shipping_address": 'shipping_address',
        "subtotal_amount": 'subtotal_amount',
        "discount_amount": 'discount_amount',
        "tax_amount": 'tax_amount',
        "total_amount": 'total_amount',
        "credit_amount": 'credit_amount',
        "debit_amount": 'debit_amount',
        "refund_amount": 'refund_amount',
        "paid_amount": 'paid_amount',
        "due_amount": 'due_amount',
        "line_items": 'line_items',
        "discounts": 'discounts',
        "taxes": 'taxes',
        "credits": 'credits',
        "debits": 'debits',
        "refunds": 'refunds',
        "payments": 'payments',
        "custom_fields": 'custom_fields',
        "display_settings": 'display_settings',
        "avatax_details": 'avatax_details',
        "public_url": 'public_url',
        "previous_balance_data": 'previous_balance_data',
        "public_url_expires_on": 'public_url_expires_on'
    }

    _optionals = [
        'id',
        'uid',
        'site_id',
        'customer_id',
        'subscription_id',
        'number',
        'sequence_number',
        'transaction_time',
        'created_at',
        'updated_at',
        'issue_date',
        'due_date',
        'paid_date',
        'status',
        'role',
        'parent_invoice_id',
        'collection_method',
        'payment_instructions',
        'currency',
        'consolidation_level',
        'parent_invoice_uid',
        'subscription_group_id',
        'parent_invoice_number',
        'group_primary_subscription_id',
        'product_name',
        'product_family_name',
        'seller',
        'customer',
        'payer',
        'recipient_emails',
        'net_terms',
        'memo',
        'billing_address',
        'shipping_address',
        'subtotal_amount',
        'discount_amount',
        'tax_amount',
        'total_amount',
        'credit_amount',
        'debit_amount',
        'refund_amount',
        'paid_amount',
        'due_amount',
        'line_items',
        'discounts',
        'taxes',
        'credits',
        'debits',
        'refunds',
        'payments',
        'custom_fields',
        'display_settings',
        'avatax_details',
        'public_url',
        'previous_balance_data',
        'public_url_expires_on',
    ]

    _nullables = [
        'paid_date',
        'parent_invoice_id',
        'parent_invoice_uid',
        'subscription_group_id',
        'parent_invoice_number',
        'group_primary_subscription_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 uid=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 sequence_number=APIHelper.SKIP,
                 transaction_time=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 due_date=APIHelper.SKIP,
                 paid_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 role=APIHelper.SKIP,
                 parent_invoice_id=APIHelper.SKIP,
                 collection_method=APIHelper.SKIP,
                 payment_instructions=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 consolidation_level=APIHelper.SKIP,
                 parent_invoice_uid=APIHelper.SKIP,
                 subscription_group_id=APIHelper.SKIP,
                 parent_invoice_number=APIHelper.SKIP,
                 group_primary_subscription_id=APIHelper.SKIP,
                 product_name=APIHelper.SKIP,
                 product_family_name=APIHelper.SKIP,
                 seller=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 payer=APIHelper.SKIP,
                 recipient_emails=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 shipping_address=APIHelper.SKIP,
                 subtotal_amount=APIHelper.SKIP,
                 discount_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 total_amount=APIHelper.SKIP,
                 credit_amount=APIHelper.SKIP,
                 debit_amount=APIHelper.SKIP,
                 refund_amount=APIHelper.SKIP,
                 paid_amount=APIHelper.SKIP,
                 due_amount=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 taxes=APIHelper.SKIP,
                 credits=APIHelper.SKIP,
                 debits=APIHelper.SKIP,
                 refunds=APIHelper.SKIP,
                 payments=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 display_settings=APIHelper.SKIP,
                 avatax_details=APIHelper.SKIP,
                 public_url=APIHelper.SKIP,
                 previous_balance_data=APIHelper.SKIP,
                 public_url_expires_on=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Invoice class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if uid is not APIHelper.SKIP:
            self.uid = uid 
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
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
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
        if role is not APIHelper.SKIP:
            self.role = role 
        if parent_invoice_id is not APIHelper.SKIP:
            self.parent_invoice_id = parent_invoice_id 
        if collection_method is not APIHelper.SKIP:
            self.collection_method = collection_method 
        if payment_instructions is not APIHelper.SKIP:
            self.payment_instructions = payment_instructions 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if consolidation_level is not APIHelper.SKIP:
            self.consolidation_level = consolidation_level 
        if parent_invoice_uid is not APIHelper.SKIP:
            self.parent_invoice_uid = parent_invoice_uid 
        if subscription_group_id is not APIHelper.SKIP:
            self.subscription_group_id = subscription_group_id 
        if parent_invoice_number is not APIHelper.SKIP:
            self.parent_invoice_number = parent_invoice_number 
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
        if memo is not APIHelper.SKIP:
            self.memo = memo 
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
        if total_amount is not APIHelper.SKIP:
            self.total_amount = total_amount 
        if credit_amount is not APIHelper.SKIP:
            self.credit_amount = credit_amount 
        if debit_amount is not APIHelper.SKIP:
            self.debit_amount = debit_amount 
        if refund_amount is not APIHelper.SKIP:
            self.refund_amount = refund_amount 
        if paid_amount is not APIHelper.SKIP:
            self.paid_amount = paid_amount 
        if due_amount is not APIHelper.SKIP:
            self.due_amount = due_amount 
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        if taxes is not APIHelper.SKIP:
            self.taxes = taxes 
        if credits is not APIHelper.SKIP:
            self.credits = credits 
        if debits is not APIHelper.SKIP:
            self.debits = debits 
        if refunds is not APIHelper.SKIP:
            self.refunds = refunds 
        if payments is not APIHelper.SKIP:
            self.payments = payments 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if display_settings is not APIHelper.SKIP:
            self.display_settings = display_settings 
        if avatax_details is not APIHelper.SKIP:
            self.avatax_details = avatax_details 
        if public_url is not APIHelper.SKIP:
            self.public_url = public_url 
        if previous_balance_data is not APIHelper.SKIP:
            self.previous_balance_data = previous_balance_data 
        if public_url_expires_on is not APIHelper.SKIP:
            self.public_url_expires_on = public_url_expires_on 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        sequence_number = dictionary.get("sequence_number") if dictionary.get("sequence_number") else APIHelper.SKIP
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        issue_date = dateutil.parser.parse(dictionary.get('issue_date')).date() if dictionary.get('issue_date') else APIHelper.SKIP
        due_date = dateutil.parser.parse(dictionary.get('due_date')).date() if dictionary.get('due_date') else APIHelper.SKIP
        if 'paid_date' in dictionary.keys():
            paid_date = dateutil.parser.parse(dictionary.get('paid_date')).date() if dictionary.get('paid_date') else None
        else:
            paid_date = APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        parent_invoice_id = dictionary.get("parent_invoice_id") if "parent_invoice_id" in dictionary.keys() else APIHelper.SKIP
        collection_method = dictionary.get("collection_method") if dictionary.get("collection_method") else APIHelper.SKIP
        payment_instructions = dictionary.get("payment_instructions") if dictionary.get("payment_instructions") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else APIHelper.SKIP
        parent_invoice_uid = dictionary.get("parent_invoice_uid") if "parent_invoice_uid" in dictionary.keys() else APIHelper.SKIP
        subscription_group_id = dictionary.get("subscription_group_id") if "subscription_group_id" in dictionary.keys() else APIHelper.SKIP
        parent_invoice_number = dictionary.get("parent_invoice_number") if "parent_invoice_number" in dictionary.keys() else APIHelper.SKIP
        group_primary_subscription_id = dictionary.get("group_primary_subscription_id") if "group_primary_subscription_id" in dictionary.keys() else APIHelper.SKIP
        product_name = dictionary.get("product_name") if dictionary.get("product_name") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
        seller = InvoiceSeller.from_dictionary(dictionary.get('seller')) if 'seller' in dictionary.keys() else APIHelper.SKIP
        customer = InvoiceCustomer.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        payer = InvoicePayer.from_dictionary(dictionary.get('payer')) if 'payer' in dictionary.keys() else APIHelper.SKIP
        recipient_emails = dictionary.get("recipient_emails") if dictionary.get("recipient_emails") else APIHelper.SKIP
        net_terms = dictionary.get("net_terms") if dictionary.get("net_terms") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        billing_address = InvoiceAddress.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        shipping_address = InvoiceAddress.from_dictionary(dictionary.get('shipping_address')) if 'shipping_address' in dictionary.keys() else APIHelper.SKIP
        subtotal_amount = dictionary.get("subtotal_amount") if dictionary.get("subtotal_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        credit_amount = dictionary.get("credit_amount") if dictionary.get("credit_amount") else APIHelper.SKIP
        debit_amount = dictionary.get("debit_amount") if dictionary.get("debit_amount") else APIHelper.SKIP
        refund_amount = dictionary.get("refund_amount") if dictionary.get("refund_amount") else APIHelper.SKIP
        paid_amount = dictionary.get("paid_amount") if dictionary.get("paid_amount") else APIHelper.SKIP
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [InvoiceLineItem.from_dictionary(x) for x in dictionary.get('line_items')]
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
        debits = None
        if dictionary.get('debits') is not None:
            debits = [InvoiceDebit.from_dictionary(x) for x in dictionary.get('debits')]
        else:
            debits = APIHelper.SKIP
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
        avatax_details = InvoiceAvataxDetails.from_dictionary(dictionary.get('avatax_details')) if 'avatax_details' in dictionary.keys() else APIHelper.SKIP
        public_url = dictionary.get("public_url") if dictionary.get("public_url") else APIHelper.SKIP
        previous_balance_data = InvoicePreviousBalance.from_dictionary(dictionary.get('previous_balance_data')) if 'previous_balance_data' in dictionary.keys() else APIHelper.SKIP
        public_url_expires_on = dateutil.parser.parse(dictionary.get('public_url_expires_on')).date() if dictionary.get('public_url_expires_on') else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   uid,
                   site_id,
                   customer_id,
                   subscription_id,
                   number,
                   sequence_number,
                   transaction_time,
                   created_at,
                   updated_at,
                   issue_date,
                   due_date,
                   paid_date,
                   status,
                   role,
                   parent_invoice_id,
                   collection_method,
                   payment_instructions,
                   currency,
                   consolidation_level,
                   parent_invoice_uid,
                   subscription_group_id,
                   parent_invoice_number,
                   group_primary_subscription_id,
                   product_name,
                   product_family_name,
                   seller,
                   customer,
                   payer,
                   recipient_emails,
                   net_terms,
                   memo,
                   billing_address,
                   shipping_address,
                   subtotal_amount,
                   discount_amount,
                   tax_amount,
                   total_amount,
                   credit_amount,
                   debit_amount,
                   refund_amount,
                   paid_amount,
                   due_amount,
                   line_items,
                   discounts,
                   taxes,
                   credits,
                   debits,
                   refunds,
                   payments,
                   custom_fields,
                   display_settings,
                   avatax_details,
                   public_url,
                   previous_balance_data,
                   public_url_expires_on,
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

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'uid={self.uid!r}, '
                f'site_id={self.site_id!r}, '
                f'customer_id={self.customer_id!r}, '
                f'subscription_id={self.subscription_id!r}, '
                f'number={self.number!r}, '
                f'sequence_number={self.sequence_number!r}, '
                f'transaction_time={self.transaction_time!r}, '
                f'created_at={self.created_at!r}, '
                f'updated_at={self.updated_at!r}, '
                f'issue_date={self.issue_date!r}, '
                f'due_date={self.due_date!r}, '
                f'paid_date={self.paid_date!r}, '
                f'status={self.status!r}, '
                f'role={self.role!r}, '
                f'parent_invoice_id={self.parent_invoice_id!r}, '
                f'collection_method={self.collection_method!r}, '
                f'payment_instructions={self.payment_instructions!r}, '
                f'currency={self.currency!r}, '
                f'consolidation_level={self.consolidation_level!r}, '
                f'parent_invoice_uid={self.parent_invoice_uid!r}, '
                f'subscription_group_id={self.subscription_group_id!r}, '
                f'parent_invoice_number={self.parent_invoice_number!r}, '
                f'group_primary_subscription_id={self.group_primary_subscription_id!r}, '
                f'product_name={self.product_name!r}, '
                f'product_family_name={self.product_family_name!r}, '
                f'seller={self.seller!r}, '
                f'customer={self.customer!r}, '
                f'payer={self.payer!r}, '
                f'recipient_emails={self.recipient_emails!r}, '
                f'net_terms={self.net_terms!r}, '
                f'memo={self.memo!r}, '
                f'billing_address={self.billing_address!r}, '
                f'shipping_address={self.shipping_address!r}, '
                f'subtotal_amount={self.subtotal_amount!r}, '
                f'discount_amount={self.discount_amount!r}, '
                f'tax_amount={self.tax_amount!r}, '
                f'total_amount={self.total_amount!r}, '
                f'credit_amount={self.credit_amount!r}, '
                f'debit_amount={self.debit_amount!r}, '
                f'refund_amount={self.refund_amount!r}, '
                f'paid_amount={self.paid_amount!r}, '
                f'due_amount={self.due_amount!r}, '
                f'line_items={self.line_items!r}, '
                f'discounts={self.discounts!r}, '
                f'taxes={self.taxes!r}, '
                f'credits={self.credits!r}, '
                f'debits={self.debits!r}, '
                f'refunds={self.refunds!r}, '
                f'payments={self.payments!r}, '
                f'custom_fields={self.custom_fields!r}, '
                f'display_settings={self.display_settings!r}, '
                f'avatax_details={self.avatax_details!r}, '
                f'public_url={self.public_url!r}, '
                f'previous_balance_data={self.previous_balance_data!r}, '
                f'public_url_expires_on={self.public_url_expires_on!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'uid={self.uid!s}, '
                f'site_id={self.site_id!s}, '
                f'customer_id={self.customer_id!s}, '
                f'subscription_id={self.subscription_id!s}, '
                f'number={self.number!s}, '
                f'sequence_number={self.sequence_number!s}, '
                f'transaction_time={self.transaction_time!s}, '
                f'created_at={self.created_at!s}, '
                f'updated_at={self.updated_at!s}, '
                f'issue_date={self.issue_date!s}, '
                f'due_date={self.due_date!s}, '
                f'paid_date={self.paid_date!s}, '
                f'status={self.status!s}, '
                f'role={self.role!s}, '
                f'parent_invoice_id={self.parent_invoice_id!s}, '
                f'collection_method={self.collection_method!s}, '
                f'payment_instructions={self.payment_instructions!s}, '
                f'currency={self.currency!s}, '
                f'consolidation_level={self.consolidation_level!s}, '
                f'parent_invoice_uid={self.parent_invoice_uid!s}, '
                f'subscription_group_id={self.subscription_group_id!s}, '
                f'parent_invoice_number={self.parent_invoice_number!s}, '
                f'group_primary_subscription_id={self.group_primary_subscription_id!s}, '
                f'product_name={self.product_name!s}, '
                f'product_family_name={self.product_family_name!s}, '
                f'seller={self.seller!s}, '
                f'customer={self.customer!s}, '
                f'payer={self.payer!s}, '
                f'recipient_emails={self.recipient_emails!s}, '
                f'net_terms={self.net_terms!s}, '
                f'memo={self.memo!s}, '
                f'billing_address={self.billing_address!s}, '
                f'shipping_address={self.shipping_address!s}, '
                f'subtotal_amount={self.subtotal_amount!s}, '
                f'discount_amount={self.discount_amount!s}, '
                f'tax_amount={self.tax_amount!s}, '
                f'total_amount={self.total_amount!s}, '
                f'credit_amount={self.credit_amount!s}, '
                f'debit_amount={self.debit_amount!s}, '
                f'refund_amount={self.refund_amount!s}, '
                f'paid_amount={self.paid_amount!s}, '
                f'due_amount={self.due_amount!s}, '
                f'line_items={self.line_items!s}, '
                f'discounts={self.discounts!s}, '
                f'taxes={self.taxes!s}, '
                f'credits={self.credits!s}, '
                f'debits={self.debits!s}, '
                f'refunds={self.refunds!s}, '
                f'payments={self.payments!s}, '
                f'custom_fields={self.custom_fields!s}, '
                f'display_settings={self.display_settings!s}, '
                f'avatax_details={self.avatax_details!s}, '
                f'public_url={self.public_url!s}, '
                f'previous_balance_data={self.previous_balance_data!s}, '
                f'public_url_expires_on={self.public_url_expires_on!s}, '
                f'additional_properties={self.additional_properties!s})')
