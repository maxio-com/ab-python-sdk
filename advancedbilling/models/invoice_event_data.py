# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.applied_credit_note_data import AppliedCreditNoteData
from advancedbilling.models.credit_note_1 import CreditNote1


class InvoiceEventData(object):

    """Implementation of the 'Invoice Event Data' model.

    The event data is the data that, when combined with the command, results
    in the output invoice found in the invoice field.

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
        role (str): The role of the credit note (e.g. 'general')
        consolidated_invoice (bool): Shows whether it was applied to
            consolidated invoice or not
        applied_credit_notes (List[AppliedCreditNoteData]): List of credit
            notes applied to children invoices (if consolidated invoice)
        debit_note_number (str): A unique, identifying string that appears on
            the debit note and in places it is referenced.
        debit_note_uid (str): Unique identifier for the debit note. It is
            generated automatically by Chargify and has the prefix "db_"
            followed by alphanumeric characters.
        payment_method (PaymentMethodApplePay | PaymentMethodBankAccount |
            PaymentMethodCreditCard | PaymentMethodExternal |
            PaymentMethodPaypal | None): A nested data structure detailing the
            method of payment
        transaction_id (int): The Chargify id of the original payment
        parent_invoice_number (int): TODO: type description here.
        remaining_prepayment_amount (str): TODO: type description here.
        prepayment (bool): The flag that shows whether the original payment
            was a prepayment or not
        external (bool): TODO: type description here.
        from_collection_method (str): The previous collection method of the
            invoice.
        to_collection_method (str): The new collection method of the invoice.
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
        from_status (InvoiceStatus): The status of the invoice before event
            occurence. See [Invoice
            Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494
            171#line-item-breakdowns) for more.
        to_status (InvoiceStatus): The status of the invoice after event
            occurence. See [Invoice
            Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494
            171#line-item-breakdowns) for more.
        due_amount (str): Amount due on the invoice, which is `total_amount -
            credit_amount - paid_amount`.
        total_amount (str): The invoice total, which is `subtotal_amount -
            discount_amount + tax_amount`.'
        apply_credit (bool): If true, credit was created and applied it to the
            invoice.
        credit_note_attributes (CreditNote1): TODO: type description here.
        payment_id (int): The ID of the payment transaction to be refunded.
        refund_amount (str): The amount of the refund.
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
        "role": 'role',
        "consolidated_invoice": 'consolidated_invoice',
        "applied_credit_notes": 'applied_credit_notes',
        "debit_note_number": 'debit_note_number',
        "debit_note_uid": 'debit_note_uid',
        "payment_method": 'payment_method',
        "transaction_id": 'transaction_id',
        "parent_invoice_number": 'parent_invoice_number',
        "remaining_prepayment_amount": 'remaining_prepayment_amount',
        "prepayment": 'prepayment',
        "external": 'external',
        "from_collection_method": 'from_collection_method',
        "to_collection_method": 'to_collection_method',
        "consolidation_level": 'consolidation_level',
        "from_status": 'from_status',
        "to_status": 'to_status',
        "due_amount": 'due_amount',
        "total_amount": 'total_amount',
        "apply_credit": 'apply_credit',
        "credit_note_attributes": 'credit_note_attributes',
        "payment_id": 'payment_id',
        "refund_amount": 'refund_amount',
        "refund_id": 'refund_id',
        "is_advance_invoice": 'is_advance_invoice',
        "reason": 'reason'
    }

    _optionals = [
        'uid',
        'credit_note_number',
        'credit_note_uid',
        'original_amount',
        'applied_amount',
        'transaction_time',
        'memo',
        'role',
        'consolidated_invoice',
        'applied_credit_notes',
        'debit_note_number',
        'debit_note_uid',
        'payment_method',
        'transaction_id',
        'parent_invoice_number',
        'remaining_prepayment_amount',
        'prepayment',
        'external',
        'from_collection_method',
        'to_collection_method',
        'consolidation_level',
        'from_status',
        'to_status',
        'due_amount',
        'total_amount',
        'apply_credit',
        'credit_note_attributes',
        'payment_id',
        'refund_amount',
        'refund_id',
        'is_advance_invoice',
        'reason',
    ]

    _nullables = [
        'parent_invoice_number',
        'remaining_prepayment_amount',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 credit_note_number=APIHelper.SKIP,
                 credit_note_uid=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 transaction_time=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 role=APIHelper.SKIP,
                 consolidated_invoice=APIHelper.SKIP,
                 applied_credit_notes=APIHelper.SKIP,
                 debit_note_number=APIHelper.SKIP,
                 debit_note_uid=APIHelper.SKIP,
                 payment_method=APIHelper.SKIP,
                 transaction_id=APIHelper.SKIP,
                 parent_invoice_number=APIHelper.SKIP,
                 remaining_prepayment_amount=APIHelper.SKIP,
                 prepayment=APIHelper.SKIP,
                 external=APIHelper.SKIP,
                 from_collection_method=APIHelper.SKIP,
                 to_collection_method=APIHelper.SKIP,
                 consolidation_level=APIHelper.SKIP,
                 from_status=APIHelper.SKIP,
                 to_status=APIHelper.SKIP,
                 due_amount=APIHelper.SKIP,
                 total_amount=APIHelper.SKIP,
                 apply_credit=APIHelper.SKIP,
                 credit_note_attributes=APIHelper.SKIP,
                 payment_id=APIHelper.SKIP,
                 refund_amount=APIHelper.SKIP,
                 refund_id=APIHelper.SKIP,
                 is_advance_invoice=APIHelper.SKIP,
                 reason=APIHelper.SKIP):
        """Constructor for the InvoiceEventData class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if credit_note_number is not APIHelper.SKIP:
            self.credit_note_number = credit_note_number 
        if credit_note_uid is not APIHelper.SKIP:
            self.credit_note_uid = credit_note_uid 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if role is not APIHelper.SKIP:
            self.role = role 
        if consolidated_invoice is not APIHelper.SKIP:
            self.consolidated_invoice = consolidated_invoice 
        if applied_credit_notes is not APIHelper.SKIP:
            self.applied_credit_notes = applied_credit_notes 
        if debit_note_number is not APIHelper.SKIP:
            self.debit_note_number = debit_note_number 
        if debit_note_uid is not APIHelper.SKIP:
            self.debit_note_uid = debit_note_uid 
        if payment_method is not APIHelper.SKIP:
            self.payment_method = payment_method 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if parent_invoice_number is not APIHelper.SKIP:
            self.parent_invoice_number = parent_invoice_number 
        if remaining_prepayment_amount is not APIHelper.SKIP:
            self.remaining_prepayment_amount = remaining_prepayment_amount 
        if prepayment is not APIHelper.SKIP:
            self.prepayment = prepayment 
        if external is not APIHelper.SKIP:
            self.external = external 
        if from_collection_method is not APIHelper.SKIP:
            self.from_collection_method = from_collection_method 
        if to_collection_method is not APIHelper.SKIP:
            self.to_collection_method = to_collection_method 
        if consolidation_level is not APIHelper.SKIP:
            self.consolidation_level = consolidation_level 
        if from_status is not APIHelper.SKIP:
            self.from_status = from_status 
        if to_status is not APIHelper.SKIP:
            self.to_status = to_status 
        if due_amount is not APIHelper.SKIP:
            self.due_amount = due_amount 
        if total_amount is not APIHelper.SKIP:
            self.total_amount = total_amount 
        if apply_credit is not APIHelper.SKIP:
            self.apply_credit = apply_credit 
        if credit_note_attributes is not APIHelper.SKIP:
            self.credit_note_attributes = credit_note_attributes 
        if payment_id is not APIHelper.SKIP:
            self.payment_id = payment_id 
        if refund_amount is not APIHelper.SKIP:
            self.refund_amount = refund_amount 
        if refund_id is not APIHelper.SKIP:
            self.refund_id = refund_id 
        if is_advance_invoice is not APIHelper.SKIP:
            self.is_advance_invoice = is_advance_invoice 
        if reason is not APIHelper.SKIP:
            self.reason = reason 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        credit_note_number = dictionary.get("credit_note_number") if dictionary.get("credit_note_number") else APIHelper.SKIP
        credit_note_uid = dictionary.get("credit_note_uid") if dictionary.get("credit_note_uid") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        consolidated_invoice = dictionary.get("consolidated_invoice") if "consolidated_invoice" in dictionary.keys() else APIHelper.SKIP
        applied_credit_notes = None
        if dictionary.get('applied_credit_notes') is not None:
            applied_credit_notes = [AppliedCreditNoteData.from_dictionary(x) for x in dictionary.get('applied_credit_notes')]
        else:
            applied_credit_notes = APIHelper.SKIP
        debit_note_number = dictionary.get("debit_note_number") if dictionary.get("debit_note_number") else APIHelper.SKIP
        debit_note_uid = dictionary.get("debit_note_uid") if dictionary.get("debit_note_uid") else APIHelper.SKIP
        payment_method = APIHelper.deserialize_union_type(UnionTypeLookUp.get('InvoiceEventDataPaymentMethod'), dictionary.get('payment_method'), False) if dictionary.get('payment_method') is not None else APIHelper.SKIP
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        parent_invoice_number = dictionary.get("parent_invoice_number") if "parent_invoice_number" in dictionary.keys() else APIHelper.SKIP
        remaining_prepayment_amount = dictionary.get("remaining_prepayment_amount") if "remaining_prepayment_amount" in dictionary.keys() else APIHelper.SKIP
        prepayment = dictionary.get("prepayment") if "prepayment" in dictionary.keys() else APIHelper.SKIP
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        from_collection_method = dictionary.get("from_collection_method") if dictionary.get("from_collection_method") else APIHelper.SKIP
        to_collection_method = dictionary.get("to_collection_method") if dictionary.get("to_collection_method") else APIHelper.SKIP
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else APIHelper.SKIP
        from_status = dictionary.get("from_status") if dictionary.get("from_status") else APIHelper.SKIP
        to_status = dictionary.get("to_status") if dictionary.get("to_status") else APIHelper.SKIP
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        apply_credit = dictionary.get("apply_credit") if "apply_credit" in dictionary.keys() else APIHelper.SKIP
        credit_note_attributes = CreditNote1.from_dictionary(dictionary.get('credit_note_attributes')) if 'credit_note_attributes' in dictionary.keys() else APIHelper.SKIP
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else APIHelper.SKIP
        refund_amount = dictionary.get("refund_amount") if dictionary.get("refund_amount") else APIHelper.SKIP
        refund_id = dictionary.get("refund_id") if dictionary.get("refund_id") else APIHelper.SKIP
        is_advance_invoice = dictionary.get("is_advance_invoice") if "is_advance_invoice" in dictionary.keys() else APIHelper.SKIP
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   credit_note_number,
                   credit_note_uid,
                   original_amount,
                   applied_amount,
                   transaction_time,
                   memo,
                   role,
                   consolidated_invoice,
                   applied_credit_notes,
                   debit_note_number,
                   debit_note_uid,
                   payment_method,
                   transaction_id,
                   parent_invoice_number,
                   remaining_prepayment_amount,
                   prepayment,
                   external,
                   from_collection_method,
                   to_collection_method,
                   consolidation_level,
                   from_status,
                   to_status,
                   due_amount,
                   total_amount,
                   apply_credit,
                   credit_note_attributes,
                   payment_id,
                   refund_amount,
                   refund_id,
                   is_advance_invoice,
                   reason)
