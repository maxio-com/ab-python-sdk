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
        DRAFT: TODO: type description here.
        OPEN: TODO: type description here.
        PAID: TODO: type description here.
        PENDING: TODO: type description here.
        VOIDED: TODO: type description here.
        CANCELED: TODO: type description here.
        PROCESSING: TODO: type description here.
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
   