# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_tax_breakout import InvoiceTaxBreakout


class ProformaInvoiceTax(object):

    """Implementation of the 'Proforma Invoice Tax' model.

    Attributes:
        uid (str): The model property of type str.
        title (str): The model property of type str.
        source_type (ProformaInvoiceTaxSourceType): The model property of type
            ProformaInvoiceTaxSourceType.
        percentage (str): The model property of type str.
        taxable_amount (str): The model property of type str.
        tax_amount (str): The model property of type str.
        line_item_breakouts (List[InvoiceTaxBreakout]): The model property of
            type List[InvoiceTaxBreakout].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "title": 'title',
        "source_type": 'source_type',
        "percentage": 'percentage',
        "taxable_amount": 'taxable_amount',
        "tax_amount": 'tax_amount',
        "line_item_breakouts": 'line_item_breakouts'
    }

    _optionals = [
        'uid',
        'title',
        'source_type',
        'percentage',
        'taxable_amount',
        'tax_amount',
        'line_item_breakouts',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 source_type=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 taxable_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 line_item_breakouts=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ProformaInvoiceTax class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if title is not APIHelper.SKIP:
            self.title = title 
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if line_item_breakouts is not APIHelper.SKIP:
            self.line_item_breakouts = line_item_breakouts 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        source_type = dictionary.get("source_type") if dictionary.get("source_type") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        taxable_amount = dictionary.get("taxable_amount") if dictionary.get("taxable_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        line_item_breakouts = None
        if dictionary.get('line_item_breakouts') is not None:
            line_item_breakouts = [InvoiceTaxBreakout.from_dictionary(x) for x in dictionary.get('line_item_breakouts')]
        else:
            line_item_breakouts = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   title,
                   source_type,
                   percentage,
                   taxable_amount,
                   tax_amount,
                   line_item_breakouts,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={self.uid!r}, '
                f'title={self.title!r}, '
                f'source_type={self.source_type!r}, '
                f'percentage={self.percentage!r}, '
                f'taxable_amount={self.taxable_amount!r}, '
                f'tax_amount={self.tax_amount!r}, '
                f'line_item_breakouts={self.line_item_breakouts!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={self.uid!s}, '
                f'title={self.title!s}, '
                f'source_type={self.source_type!s}, '
                f'percentage={self.percentage!s}, '
                f'taxable_amount={self.taxable_amount!s}, '
                f'tax_amount={self.tax_amount!s}, '
                f'line_item_breakouts={self.line_item_breakouts!s}, '
                f'additional_properties={self.additional_properties!s})')
