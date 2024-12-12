# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreatePrepaymentMethod(object):

    """Implementation of the 'Create Prepayment Method' enum.

    :- When the `method` specified is `"credit_card_on_file"`, the prepayment
    amount will be collected using the default credit card payment profile and
    applied to the prepayment account balance. This is especially useful for
    manual replenishment of prepaid subscriptions.

    Attributes:
        CHECK: TODO: type description here.
        CASH: TODO: type description here.
        MONEY_ORDER: TODO: type description here.
        ACH: TODO: type description here.
        PAYPAL_ACCOUNT: TODO: type description here.
        CREDIT_CARD: TODO: type description here.
        CREDIT_CARD_ON_FILE: TODO: type description here.
        OTHER: TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    CHECK = 'check'

    CASH = 'cash'

    MONEY_ORDER = 'money_order'

    ACH = 'ach'

    PAYPAL_ACCOUNT = 'paypal_account'

    CREDIT_CARD = 'credit_card'

    CREDIT_CARD_ON_FILE = 'credit_card_on_file'

    OTHER = 'other'

