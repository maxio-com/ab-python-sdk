# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class IssueInvoiceEventData(object):

    """Implementation of the 'Issue Invoice Event Data' model.

    Example schema for an `issue_invoice` event

    Attributes:
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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "consolidation_level": 'consolidation_level',
        "from_status": 'from_status',
        "to_status": 'to_status',
        "due_amount": 'due_amount',
        "total_amount": 'total_amount'
    }

    _optionals = [
        'consolidation_level',
        'from_status',
        'to_status',
        'due_amount',
        'total_amount',
    ]

    def __init__(self,
                 consolidation_level=APIHelper.SKIP,
                 from_status=APIHelper.SKIP,
                 to_status=APIHelper.SKIP,
                 due_amount=APIHelper.SKIP,
                 total_amount=APIHelper.SKIP):
        """Constructor for the IssueInvoiceEventData class"""

        # Initialize members of the class
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
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else APIHelper.SKIP
        from_status = dictionary.get("from_status") if dictionary.get("from_status") else APIHelper.SKIP
        to_status = dictionary.get("to_status") if dictionary.get("to_status") else APIHelper.SKIP
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(consolidation_level,
                   from_status,
                   to_status,
                   due_amount,
                   total_amount)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
