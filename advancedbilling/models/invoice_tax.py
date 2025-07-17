# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_tax_breakout import InvoiceTaxBreakout
from advancedbilling.models.invoice_tax_component_breakout import InvoiceTaxComponentBreakout


class InvoiceTax(object):

    """Implementation of the 'Invoice Tax' model.

    Attributes:
        uid (str): The model property of type str.
        title (str): The model property of type str.
        description (str): The model property of type str.
        source_type (ProformaInvoiceTaxSourceType): The model property of type
            ProformaInvoiceTaxSourceType.
        source_id (int): The model property of type int.
        percentage (str): The model property of type str.
        taxable_amount (str): The model property of type str.
        tax_amount (str): The model property of type str.
        transaction_id (int): The model property of type int.
        line_item_breakouts (List[InvoiceTaxBreakout]): The model property of
            type List[InvoiceTaxBreakout].
        tax_component_breakouts (List[InvoiceTaxComponentBreakout]): The model
            property of type List[InvoiceTaxComponentBreakout].
        eu_vat (bool): The model property of type bool.
        mtype (str): The model property of type str.
        tax_exempt_amount (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "title": 'title',
        "description": 'description',
        "source_type": 'source_type',
        "source_id": 'source_id',
        "percentage": 'percentage',
        "taxable_amount": 'taxable_amount',
        "tax_amount": 'tax_amount',
        "transaction_id": 'transaction_id',
        "line_item_breakouts": 'line_item_breakouts',
        "tax_component_breakouts": 'tax_component_breakouts',
        "eu_vat": 'eu_vat',
        "mtype": 'type',
        "tax_exempt_amount": 'tax_exempt_amount'
    }

    _optionals = [
        'uid',
        'title',
        'description',
        'source_type',
        'source_id',
        'percentage',
        'taxable_amount',
        'tax_amount',
        'transaction_id',
        'line_item_breakouts',
        'tax_component_breakouts',
        'eu_vat',
        'mtype',
        'tax_exempt_amount',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 source_type=APIHelper.SKIP,
                 source_id=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 taxable_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 transaction_id=APIHelper.SKIP,
                 line_item_breakouts=APIHelper.SKIP,
                 tax_component_breakouts=APIHelper.SKIP,
                 eu_vat=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 tax_exempt_amount=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceTax class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if title is not APIHelper.SKIP:
            self.title = title 
        if description is not APIHelper.SKIP:
            self.description = description 
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type 
        if source_id is not APIHelper.SKIP:
            self.source_id = source_id 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if line_item_breakouts is not APIHelper.SKIP:
            self.line_item_breakouts = line_item_breakouts 
        if tax_component_breakouts is not APIHelper.SKIP:
            self.tax_component_breakouts = tax_component_breakouts 
        if eu_vat is not APIHelper.SKIP:
            self.eu_vat = eu_vat 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if tax_exempt_amount is not APIHelper.SKIP:
            self.tax_exempt_amount = tax_exempt_amount 

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        source_type = dictionary.get("source_type") if dictionary.get("source_type") else APIHelper.SKIP
        source_id = dictionary.get("source_id") if dictionary.get("source_id") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        taxable_amount = dictionary.get("taxable_amount") if dictionary.get("taxable_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        line_item_breakouts = None
        if dictionary.get('line_item_breakouts') is not None:
            line_item_breakouts = [InvoiceTaxBreakout.from_dictionary(x) for x in dictionary.get('line_item_breakouts')]
        else:
            line_item_breakouts = APIHelper.SKIP
        tax_component_breakouts = None
        if dictionary.get('tax_component_breakouts') is not None:
            tax_component_breakouts = [InvoiceTaxComponentBreakout.from_dictionary(x) for x in dictionary.get('tax_component_breakouts')]
        else:
            tax_component_breakouts = APIHelper.SKIP
        eu_vat = dictionary.get("eu_vat") if "eu_vat" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        tax_exempt_amount = dictionary.get("tax_exempt_amount") if dictionary.get("tax_exempt_amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   title,
                   description,
                   source_type,
                   source_id,
                   percentage,
                   taxable_amount,
                   tax_amount,
                   transaction_id,
                   line_item_breakouts,
                   tax_component_breakouts,
                   eu_vat,
                   mtype,
                   tax_exempt_amount,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!r}, '
                f'title={(self.title if hasattr(self, "title") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'source_type={(self.source_type if hasattr(self, "source_type") else None)!r}, '
                f'source_id={(self.source_id if hasattr(self, "source_id") else None)!r}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!r}, '
                f'taxable_amount={(self.taxable_amount if hasattr(self, "taxable_amount") else None)!r}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!r}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!r}, '
                f'line_item_breakouts={(self.line_item_breakouts if hasattr(self, "line_item_breakouts") else None)!r}, '
                f'tax_component_breakouts={(self.tax_component_breakouts if hasattr(self, "tax_component_breakouts") else None)!r}, '
                f'eu_vat={(self.eu_vat if hasattr(self, "eu_vat") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'tax_exempt_amount={(self.tax_exempt_amount if hasattr(self, "tax_exempt_amount") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'title={(self.title if hasattr(self, "title") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'source_type={(self.source_type if hasattr(self, "source_type") else None)!s}, '
                f'source_id={(self.source_id if hasattr(self, "source_id") else None)!s}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!s}, '
                f'taxable_amount={(self.taxable_amount if hasattr(self, "taxable_amount") else None)!s}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!s}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!s}, '
                f'line_item_breakouts={(self.line_item_breakouts if hasattr(self, "line_item_breakouts") else None)!s}, '
                f'tax_component_breakouts={(self.tax_component_breakouts if hasattr(self, "tax_component_breakouts") else None)!s}, '
                f'eu_vat={(self.eu_vat if hasattr(self, "eu_vat") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'tax_exempt_amount={(self.tax_exempt_amount if hasattr(self, "tax_exempt_amount") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
