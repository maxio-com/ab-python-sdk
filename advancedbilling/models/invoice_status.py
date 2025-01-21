# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceStatus(object):

    """Implementation of the 'Invoice Status' enum.

    The current status of the invoice. See [Invoice
    Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanc
    ed-Billing-Invoices-Overview#invoice-statuses) for more.

    Attributes:
        DRAFT: The enum member of type str.
        OPEN: The enum member of type str.
        PAID: The enum member of type str.
        PENDING: The enum member of type str.
        VOIDED: The enum member of type str.
        CANCELED: The enum member of type str.
        PROCESSING: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['draft', 'open', 'paid', 'pending', 'voided', 'canceled', 'processing']
    DRAFT = 'draft'

    OPEN = 'open'

    PAID = 'paid'

    PENDING = 'pending'

    VOIDED = 'voided'

    CANCELED = 'canceled'

    PROCESSING = 'processing'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   