# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CancellationMethod(object):

    """Implementation of the 'Cancellation Method' enum.

    The process used to cancel the subscription, if the subscription has been
    canceled. It is nil if the subscription's state is not canceled.

    Attributes:
        MERCHANT_UI: The enum member of type str.
        MERCHANT_API: The enum member of type str.
        DUNNING: The enum member of type str.
        BILLING_PORTAL: The enum member of type str.
        UNKNOWN: The enum member of type str.
        IMPORTED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    MERCHANT_UI = 'merchant_ui'

    MERCHANT_API = 'merchant_api'

    DUNNING = 'dunning'

    BILLING_PORTAL = 'billing_portal'

    UNKNOWN = 'unknown'

    IMPORTED = 'imported'

