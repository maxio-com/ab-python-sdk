# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.invoice_status import InvoiceStatus


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
            documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269
            909389-Invoice-Consolidation).
        from_status (InvoiceStatus): The status of the invoice before event
            occurrence. See [Invoice
            Statuses](https://maxio.zendesk.com/hc/en-us/articles/2425228782964
            5-Advanced-Billing-Invoices-Overview#invoice-statuses) for more.
        to_status (InvoiceStatus): The status of the invoice after event
            occurrence. See [Invoice
            Statuses](https://maxio.zendesk.com/hc/en-us/articles/2425228782964
            5-Advanced-Billing-Invoices-Overview#invoice-statuses) for more.
        due_amount (str): Amount due on the invoice, which is `total_amount -
            credit_amount - paid_amount`.
        total_amount (str): The invoice total, which is `subtotal_amount -
            discount_amount + tax_amount`.'
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "consolidation_level": 'consolidation_level',
        "from_status": 'from_status',
        "to_status": 'to_status',
        "due_amount": 'due_amount',
        "total_amount": 'total_amount'
    }

    def __init__(self,
                 consolidation_level=None,
                 from_status=None,
                 to_status=None,
                 due_amount=None,
                 total_amount=None,
                 additional_properties=None):
        """Constructor for the IssueInvoiceEventData class"""

        # Initialize members of the class
        self.consolidation_level = consolidation_level 
        self.from_status = from_status 
        self.to_status = to_status 
        self.due_amount = due_amount 
        self.total_amount = total_amount 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else None
        from_status = dictionary.get("from_status") if dictionary.get("from_status") else None
        to_status = dictionary.get("to_status") if dictionary.get("to_status") else None
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else None
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(consolidation_level,
                   from_status,
                   to_status,
                   due_amount,
                   total_amount,
                   additional_properties)

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
            return APIHelper.is_valid_type(value=dictionary.consolidation_level,
                                           type_callable=lambda value: InvoiceConsolidationLevel.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.from_status,
                                            type_callable=lambda value: InvoiceStatus.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.to_status,
                                            type_callable=lambda value: InvoiceStatus.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.due_amount,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.total_amount,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('consolidation_level'),
                                       type_callable=lambda value: InvoiceConsolidationLevel.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('from_status'),
                                        type_callable=lambda value: InvoiceStatus.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('to_status'),
                                        type_callable=lambda value: InvoiceStatus.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('due_amount'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('total_amount'),
                                        type_callable=lambda value: isinstance(value, str))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'consolidation_level={self.consolidation_level!r}, '
                f'from_status={self.from_status!r}, '
                f'to_status={self.to_status!r}, '
                f'due_amount={self.due_amount!r}, '
                f'total_amount={self.total_amount!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'consolidation_level={self.consolidation_level!s}, '
                f'from_status={self.from_status!s}, '
                f'to_status={self.to_status!s}, '
                f'due_amount={self.due_amount!s}, '
                f'total_amount={self.total_amount!s}, '
                f'additional_properties={self.additional_properties!s})')
