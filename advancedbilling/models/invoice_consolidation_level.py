# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceConsolidationLevel(object):

    """Implementation of the 'Invoice Consolidation Level' enum.

    Consolidation level of the invoice, which is applicable to invoice
    consolidation.  It will hold one of the following values:
    * "none": A normal invoice with no consolidation.
    * "child": An invoice segment which has been combined into a consolidated
    invoice.
    * "parent": A consolidated invoice, whose contents are composed of invoice
    segments.
    "Parent" invoices do not have lines of their own, but they have subtotals
    and totals which aggregate the member invoice segments.
    See also the [invoice consolidation
    documentation](https://chargify.zendesk.com/hc/en-us/articles/4407746391835
    ).

    Attributes:
        NONE: TODO: type description here.
        CHILD: TODO: type description here.
        PARENT: TODO: type description here.

    """
    _all_values = ['none', 'child', 'parent']
    NONE = 'none'

    CHILD = 'child'

    PARENT = 'parent'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   