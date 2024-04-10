# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceStatus(object):

    """Implementation of the 'Invoice Status' enum.

    The current status of the invoice. See [Invoice
    Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494171#line
    -item-breakdowns) for more.

    Attributes:
        DRAFT: TODO: type description here.
        OPEN: TODO: type description here.
        PAID: TODO: type description here.
        PENDING: TODO: type description here.
        VOIDED: TODO: type description here.
        CANCELED: TODO: type description here.

    """
    _all_values = ['draft', 'open', 'paid', 'pending', 'voided', 'canceled']
    DRAFT = 'draft'

    OPEN = 'open'

    PAID = 'paid'

    PENDING = 'pending'

    VOIDED = 'voided'

    CANCELED = 'canceled'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   