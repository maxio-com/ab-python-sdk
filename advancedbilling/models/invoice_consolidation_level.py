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
    documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-I
    nvoice-Consolidation).

    Attributes:
        NONE: The enum member of type str.
        CHILD: The enum member of type str.
        PARENT: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
   