# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.renewal_preview_line_item import RenewalPreviewLineItem


class RenewalPreview(object):

    """Implementation of the 'Renewal Preview' model.

    Attributes:
        next_assessment_at (datetime): The timestamp for the subscription’s
            next renewal
        subtotal_in_cents (int): An integer representing the amount of the
            total pre-tax, pre-discount charges that will be assessed at the
            next renewal
        total_tax_in_cents (int): An integer representing the total tax
            charges that will be assessed at the next renewal
        total_discount_in_cents (int): An integer representing the amount of
            the coupon discounts that will be applied to the next renewal
        total_in_cents (int): An integer representing the total amount owed,
            less any discounts, that will be assessed at the next renewal
        existing_balance_in_cents (int): An integer representing the amount of
            the subscription’s current balance
        total_amount_due_in_cents (int): An integer representing the
            existing_balance_in_cents plus the total_in_cents
        uncalculated_taxes (bool): A boolean indicating whether or not
            additional taxes will be calculated at the time of renewal. This
            will be true if you are using Avalara and the address of the
            subscription is in one of your defined taxable regions.
        line_items (List[RenewalPreviewLineItem]): An array of objects
            representing the individual transactions that will be created at
            the next renewal
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "next_assessment_at": 'next_assessment_at',
        "subtotal_in_cents": 'subtotal_in_cents',
        "total_tax_in_cents": 'total_tax_in_cents',
        "total_discount_in_cents": 'total_discount_in_cents',
        "total_in_cents": 'total_in_cents',
        "existing_balance_in_cents": 'existing_balance_in_cents',
        "total_amount_due_in_cents": 'total_amount_due_in_cents',
        "uncalculated_taxes": 'uncalculated_taxes',
        "line_items": 'line_items'
    }

    _optionals = [
        'next_assessment_at',
        'subtotal_in_cents',
        'total_tax_in_cents',
        'total_discount_in_cents',
        'total_in_cents',
        'existing_balance_in_cents',
        'total_amount_due_in_cents',
        'uncalculated_taxes',
        'line_items',
    ]

    def __init__(self,
                 next_assessment_at=APIHelper.SKIP,
                 subtotal_in_cents=APIHelper.SKIP,
                 total_tax_in_cents=APIHelper.SKIP,
                 total_discount_in_cents=APIHelper.SKIP,
                 total_in_cents=APIHelper.SKIP,
                 existing_balance_in_cents=APIHelper.SKIP,
                 total_amount_due_in_cents=APIHelper.SKIP,
                 uncalculated_taxes=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the RenewalPreview class"""

        # Initialize members of the class
        if next_assessment_at is not APIHelper.SKIP:
            self.next_assessment_at = APIHelper.apply_datetime_converter(next_assessment_at, APIHelper.RFC3339DateTime) if next_assessment_at else None 
        if subtotal_in_cents is not APIHelper.SKIP:
            self.subtotal_in_cents = subtotal_in_cents 
        if total_tax_in_cents is not APIHelper.SKIP:
            self.total_tax_in_cents = total_tax_in_cents 
        if total_discount_in_cents is not APIHelper.SKIP:
            self.total_discount_in_cents = total_discount_in_cents 
        if total_in_cents is not APIHelper.SKIP:
            self.total_in_cents = total_in_cents 
        if existing_balance_in_cents is not APIHelper.SKIP:
            self.existing_balance_in_cents = existing_balance_in_cents 
        if total_amount_due_in_cents is not APIHelper.SKIP:
            self.total_amount_due_in_cents = total_amount_due_in_cents 
        if uncalculated_taxes is not APIHelper.SKIP:
            self.uncalculated_taxes = uncalculated_taxes 
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 

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
        next_assessment_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_assessment_at")).datetime if dictionary.get("next_assessment_at") else APIHelper.SKIP
        subtotal_in_cents = dictionary.get("subtotal_in_cents") if dictionary.get("subtotal_in_cents") else APIHelper.SKIP
        total_tax_in_cents = dictionary.get("total_tax_in_cents") if dictionary.get("total_tax_in_cents") else APIHelper.SKIP
        total_discount_in_cents = dictionary.get("total_discount_in_cents") if dictionary.get("total_discount_in_cents") else APIHelper.SKIP
        total_in_cents = dictionary.get("total_in_cents") if dictionary.get("total_in_cents") else APIHelper.SKIP
        existing_balance_in_cents = dictionary.get("existing_balance_in_cents") if dictionary.get("existing_balance_in_cents") else APIHelper.SKIP
        total_amount_due_in_cents = dictionary.get("total_amount_due_in_cents") if dictionary.get("total_amount_due_in_cents") else APIHelper.SKIP
        uncalculated_taxes = dictionary.get("uncalculated_taxes") if "uncalculated_taxes" in dictionary.keys() else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [RenewalPreviewLineItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(next_assessment_at,
                   subtotal_in_cents,
                   total_tax_in_cents,
                   total_discount_in_cents,
                   total_in_cents,
                   existing_balance_in_cents,
                   total_amount_due_in_cents,
                   uncalculated_taxes,
                   line_items,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'next_assessment_at={(self.next_assessment_at if hasattr(self, "next_assessment_at") else None)!r}, '
                f'subtotal_in_cents={(self.subtotal_in_cents if hasattr(self, "subtotal_in_cents") else None)!r}, '
                f'total_tax_in_cents={(self.total_tax_in_cents if hasattr(self, "total_tax_in_cents") else None)!r}, '
                f'total_discount_in_cents={(self.total_discount_in_cents if hasattr(self, "total_discount_in_cents") else None)!r}, '
                f'total_in_cents={(self.total_in_cents if hasattr(self, "total_in_cents") else None)!r}, '
                f'existing_balance_in_cents={(self.existing_balance_in_cents if hasattr(self, "existing_balance_in_cents") else None)!r}, '
                f'total_amount_due_in_cents={(self.total_amount_due_in_cents if hasattr(self, "total_amount_due_in_cents") else None)!r}, '
                f'uncalculated_taxes={(self.uncalculated_taxes if hasattr(self, "uncalculated_taxes") else None)!r}, '
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'next_assessment_at={(self.next_assessment_at if hasattr(self, "next_assessment_at") else None)!s}, '
                f'subtotal_in_cents={(self.subtotal_in_cents if hasattr(self, "subtotal_in_cents") else None)!s}, '
                f'total_tax_in_cents={(self.total_tax_in_cents if hasattr(self, "total_tax_in_cents") else None)!s}, '
                f'total_discount_in_cents={(self.total_discount_in_cents if hasattr(self, "total_discount_in_cents") else None)!s}, '
                f'total_in_cents={(self.total_in_cents if hasattr(self, "total_in_cents") else None)!s}, '
                f'existing_balance_in_cents={(self.existing_balance_in_cents if hasattr(self, "existing_balance_in_cents") else None)!s}, '
                f'total_amount_due_in_cents={(self.total_amount_due_in_cents if hasattr(self, "total_amount_due_in_cents") else None)!s}, '
                f'uncalculated_taxes={(self.uncalculated_taxes if hasattr(self, "uncalculated_taxes") else None)!s}, '
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
