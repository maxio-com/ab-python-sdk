# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class FailedPaymentAction(object):

    """Implementation of the 'Failed Payment Action' enum.

    Action taken when payment for an invoice fails:
    - `leave_open_invoice` - prepayments and credits applied to invoice;
    invoice status set to "open"; email sent to the customer for the issued
    invoice (if setting applies); payment failure recorded in the invoice
    history. This is the default option.
    - `rollback_to_pending` - prepayments and credits not applied; invoice
    remains in "pending" status; no email sent to the customer; payment
    failure recorded in the invoice history.
    - `initiate_dunning` - prepayments and credits applied to the invoice;
    invoice status set to "open"; email sent to the customer for the issued
    invoice (if setting applies); payment failure recorded in the invoice
    history; subscription will  most likely go into "past_due" or "canceled"
    state (depending upon net terms and dunning settings).

    Attributes:
        LEAVE_OPEN_INVOICE: The enum member of type str.
        ROLLBACK_TO_PENDING: The enum member of type str.
        INITIATE_DUNNING: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    LEAVE_OPEN_INVOICE = 'leave_open_invoice'

    ROLLBACK_TO_PENDING = 'rollback_to_pending'

    INITIATE_DUNNING = 'initiate_dunning'

