# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceEventType(object):

    """Implementation of the 'Invoice Event Type' enum.

    Invoice Event Type

    Attributes:
        ISSUE_INVOICE: The enum member of type str.
        APPLY_CREDIT_NOTE: The enum member of type str.
        CREATE_CREDIT_NOTE: The enum member of type str.
        APPLY_PAYMENT: The enum member of type str.
        APPLY_DEBIT_NOTE: The enum member of type str.
        CREATE_DEBIT_NOTE: The enum member of type str.
        REFUND_INVOICE: The enum member of type str.
        VOID_INVOICE: The enum member of type str.
        VOID_REMAINDER: The enum member of type str.
        BACKPORT_INVOICE: The enum member of type str.
        CHANGE_INVOICE_STATUS: The enum member of type str.
        CHANGE_INVOICE_COLLECTION_METHOD: The enum member of type str.
        REMOVE_PAYMENT: The enum member of type str.
        FAILED_PAYMENT: The enum member of type str.
        CHANGE_CHARGEBACK_STATUS: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['issue_invoice', 'apply_credit_note', 'create_credit_note', 'apply_payment', 'apply_debit_note', 'create_debit_note', 'refund_invoice', 'void_invoice', 'void_remainder', 'backport_invoice', 'change_invoice_status', 'change_invoice_collection_method', 'remove_payment', 'failed_payment', 'change_chargeback_status']
    ISSUE_INVOICE = 'issue_invoice'

    APPLY_CREDIT_NOTE = 'apply_credit_note'

    CREATE_CREDIT_NOTE = 'create_credit_note'

    APPLY_PAYMENT = 'apply_payment'

    APPLY_DEBIT_NOTE = 'apply_debit_note'

    CREATE_DEBIT_NOTE = 'create_debit_note'

    REFUND_INVOICE = 'refund_invoice'

    VOID_INVOICE = 'void_invoice'

    VOID_REMAINDER = 'void_remainder'

    BACKPORT_INVOICE = 'backport_invoice'

    CHANGE_INVOICE_STATUS = 'change_invoice_status'

    CHANGE_INVOICE_COLLECTION_METHOD = 'change_invoice_collection_method'

    REMOVE_PAYMENT = 'remove_payment'

    FAILED_PAYMENT = 'failed_payment'

    CHANGE_CHARGEBACK_STATUS = 'change_chargeback_status'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   