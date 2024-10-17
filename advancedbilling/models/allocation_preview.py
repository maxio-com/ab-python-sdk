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

    TODO: type model description here.

    Attributes:
        start_date (datetime): TODO: type description here.
        end_date (datetime): TODO: type description here.
        subtotal_in_cents (long|int): TODO: type description here.
        total_tax_in_cents (long|int): TODO: type description here.
        total_discount_in_cents (long|int): TODO: type description here.
        total_in_cents (long|int): TODO: type description here.
        direction (AllocationPreviewDirection): TODO: type description here.
        proration_scheme (str): TODO: type description here.
        line_items (List[AllocationPreviewLineItem]): TODO: type description
            here.
        accrue_charge (bool): TODO: type description here.
        allocations (List[AllocationPreviewItem]): TODO: type description here.
        period_type (str): TODO: type description here.
        existing_balance_in_cents (long|int): An integer representing the
            amount of the subscription's current balance

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
                 additional_properties={}):
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

        if dictionary is None:
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
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
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
                   dictionary)
