# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.allocation_preview_item import AllocationPreviewItem
from advancedbilling.models.allocation_preview_line_item import AllocationPreviewLineItem


class AllocationPreview(object):

    """Implementation of the 'Allocation Preview' model.

    Attributes:
        start_date (datetime): The model property of type datetime.
        end_date (datetime): The model property of type datetime.
        subtotal_in_cents (int): The model property of type int.
        total_tax_in_cents (int): The model property of type int.
        total_discount_in_cents (int): The model property of type int.
        total_in_cents (int): The model property of type int.
        direction (AllocationPreviewDirection): The model property of type
            AllocationPreviewDirection.
        proration_scheme (str): The model property of type str.
        line_items (List[AllocationPreviewLineItem]): The model property of
            type List[AllocationPreviewLineItem].
        accrue_charge (bool): The model property of type bool.
        allocations (List[AllocationPreviewItem]): The model property of type
            List[AllocationPreviewItem].
        period_type (str): The model property of type str.
        existing_balance_in_cents (int): An integer representing the amount of
            the subscription's current balance
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_date": 'start_date',
        "end_date": 'end_date',
        "subtotal_in_cents": 'subtotal_in_cents',
        "total_tax_in_cents": 'total_tax_in_cents',
        "total_discount_in_cents": 'total_discount_in_cents',
        "total_in_cents": 'total_in_cents',
        "direction": 'direction',
        "proration_scheme": 'proration_scheme',
        "line_items": 'line_items',
        "accrue_charge": 'accrue_charge',
        "allocations": 'allocations',
        "period_type": 'period_type',
        "existing_balance_in_cents": 'existing_balance_in_cents'
    }

    _optionals = [
        'start_date',
        'end_date',
        'subtotal_in_cents',
        'total_tax_in_cents',
        'total_discount_in_cents',
        'total_in_cents',
        'direction',
        'proration_scheme',
        'line_items',
        'accrue_charge',
        'allocations',
        'period_type',
        'existing_balance_in_cents',
    ]

    def __init__(self,
                 start_date=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 subtotal_in_cents=APIHelper.SKIP,
                 total_tax_in_cents=APIHelper.SKIP,
                 total_discount_in_cents=APIHelper.SKIP,
                 total_in_cents=APIHelper.SKIP,
                 direction=APIHelper.SKIP,
                 proration_scheme=APIHelper.SKIP,
                 line_items=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 allocations=APIHelper.SKIP,
                 period_type=APIHelper.SKIP,
                 existing_balance_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the AllocationPreview class"""

        # Initialize members of the class
        if start_date is not APIHelper.SKIP:
            self.start_date = APIHelper.apply_datetime_converter(start_date, APIHelper.RFC3339DateTime) if start_date else None 
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.apply_datetime_converter(end_date, APIHelper.RFC3339DateTime) if end_date else None 
        if subtotal_in_cents is not APIHelper.SKIP:
            self.subtotal_in_cents = subtotal_in_cents 
        if total_tax_in_cents is not APIHelper.SKIP:
            self.total_tax_in_cents = total_tax_in_cents 
        if total_discount_in_cents is not APIHelper.SKIP:
            self.total_discount_in_cents = total_discount_in_cents 
        if total_in_cents is not APIHelper.SKIP:
            self.total_in_cents = total_in_cents 
        if direction is not APIHelper.SKIP:
            self.direction = direction 
        if proration_scheme is not APIHelper.SKIP:
            self.proration_scheme = proration_scheme 
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 
        if allocations is not APIHelper.SKIP:
            self.allocations = allocations 
        if period_type is not APIHelper.SKIP:
            self.period_type = period_type 
        if existing_balance_in_cents is not APIHelper.SKIP:
            self.existing_balance_in_cents = existing_balance_in_cents 

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
        start_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_date")).datetime if dictionary.get("start_date") else APIHelper.SKIP
        end_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_date")).datetime if dictionary.get("end_date") else APIHelper.SKIP
        subtotal_in_cents = dictionary.get("subtotal_in_cents") if dictionary.get("subtotal_in_cents") else APIHelper.SKIP
        total_tax_in_cents = dictionary.get("total_tax_in_cents") if dictionary.get("total_tax_in_cents") else APIHelper.SKIP
        total_discount_in_cents = dictionary.get("total_discount_in_cents") if dictionary.get("total_discount_in_cents") else APIHelper.SKIP
        total_in_cents = dictionary.get("total_in_cents") if dictionary.get("total_in_cents") else APIHelper.SKIP
        direction = dictionary.get("direction") if dictionary.get("direction") else APIHelper.SKIP
        proration_scheme = dictionary.get("proration_scheme") if dictionary.get("proration_scheme") else APIHelper.SKIP
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [AllocationPreviewLineItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        allocations = None
        if dictionary.get('allocations') is not None:
            allocations = [AllocationPreviewItem.from_dictionary(x) for x in dictionary.get('allocations')]
        else:
            allocations = APIHelper.SKIP
        period_type = dictionary.get("period_type") if dictionary.get("period_type") else APIHelper.SKIP
        existing_balance_in_cents = dictionary.get("existing_balance_in_cents") if dictionary.get("existing_balance_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(start_date,
                   end_date,
                   subtotal_in_cents,
                   total_tax_in_cents,
                   total_discount_in_cents,
                   total_in_cents,
                   direction,
                   proration_scheme,
                   line_items,
                   accrue_charge,
                   allocations,
                   period_type,
                   existing_balance_in_cents,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'start_date={(self.start_date if hasattr(self, "start_date") else None)!r}, '
                f'end_date={(self.end_date if hasattr(self, "end_date") else None)!r}, '
                f'subtotal_in_cents={(self.subtotal_in_cents if hasattr(self, "subtotal_in_cents") else None)!r}, '
                f'total_tax_in_cents={(self.total_tax_in_cents if hasattr(self, "total_tax_in_cents") else None)!r}, '
                f'total_discount_in_cents={(self.total_discount_in_cents if hasattr(self, "total_discount_in_cents") else None)!r}, '
                f'total_in_cents={(self.total_in_cents if hasattr(self, "total_in_cents") else None)!r}, '
                f'direction={(self.direction if hasattr(self, "direction") else None)!r}, '
                f'proration_scheme={(self.proration_scheme if hasattr(self, "proration_scheme") else None)!r}, '
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!r}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!r}, '
                f'allocations={(self.allocations if hasattr(self, "allocations") else None)!r}, '
                f'period_type={(self.period_type if hasattr(self, "period_type") else None)!r}, '
                f'existing_balance_in_cents={(self.existing_balance_in_cents if hasattr(self, "existing_balance_in_cents") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'start_date={(self.start_date if hasattr(self, "start_date") else None)!s}, '
                f'end_date={(self.end_date if hasattr(self, "end_date") else None)!s}, '
                f'subtotal_in_cents={(self.subtotal_in_cents if hasattr(self, "subtotal_in_cents") else None)!s}, '
                f'total_tax_in_cents={(self.total_tax_in_cents if hasattr(self, "total_tax_in_cents") else None)!s}, '
                f'total_discount_in_cents={(self.total_discount_in_cents if hasattr(self, "total_discount_in_cents") else None)!s}, '
                f'total_in_cents={(self.total_in_cents if hasattr(self, "total_in_cents") else None)!s}, '
                f'direction={(self.direction if hasattr(self, "direction") else None)!s}, '
                f'proration_scheme={(self.proration_scheme if hasattr(self, "proration_scheme") else None)!s}, '
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!s}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!s}, '
                f'allocations={(self.allocations if hasattr(self, "allocations") else None)!s}, '
                f'period_type={(self.period_type if hasattr(self, "period_type") else None)!s}, '
                f'existing_balance_in_cents={(self.existing_balance_in_cents if hasattr(self, "existing_balance_in_cents") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
