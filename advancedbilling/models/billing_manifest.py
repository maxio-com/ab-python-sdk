# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.billing_manifest_item import BillingManifestItem


class BillingManifest(object):

    """Implementation of the 'Billing Manifest' model.

    Attributes:
        line_items (List[BillingManifestItem]): The model property of type
            List[BillingManifestItem].
        total_in_cents (int): The model property of type int.
        total_discount_in_cents (int): The model property of type int.
        total_tax_in_cents (int): The model property of type int.
        subtotal_in_cents (int): The model property of type int.
        start_date (datetime): The model property of type datetime.
        end_date (datetime): The model property of type datetime.
        period_type (str): The model property of type str.
        existing_balance_in_cents (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "line_items": 'line_items',
        "total_in_cents": 'total_in_cents',
        "total_discount_in_cents": 'total_discount_in_cents',
        "total_tax_in_cents": 'total_tax_in_cents',
        "subtotal_in_cents": 'subtotal_in_cents',
        "start_date": 'start_date',
        "end_date": 'end_date',
        "period_type": 'period_type',
        "existing_balance_in_cents": 'existing_balance_in_cents'
    }

    _optionals = [
        'line_items',
        'total_in_cents',
        'total_discount_in_cents',
        'total_tax_in_cents',
        'subtotal_in_cents',
        'start_date',
        'end_date',
        'period_type',
        'existing_balance_in_cents',
    ]

    _nullables = [
        'start_date',
        'end_date',
        'period_type',
    ]

    def __init__(self,
                 line_items=APIHelper.SKIP,
                 total_in_cents=APIHelper.SKIP,
                 total_discount_in_cents=APIHelper.SKIP,
                 total_tax_in_cents=APIHelper.SKIP,
                 subtotal_in_cents=APIHelper.SKIP,
                 start_date=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 period_type=APIHelper.SKIP,
                 existing_balance_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the BillingManifest class"""

        # Initialize members of the class
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items 
        if total_in_cents is not APIHelper.SKIP:
            self.total_in_cents = total_in_cents 
        if total_discount_in_cents is not APIHelper.SKIP:
            self.total_discount_in_cents = total_discount_in_cents 
        if total_tax_in_cents is not APIHelper.SKIP:
            self.total_tax_in_cents = total_tax_in_cents 
        if subtotal_in_cents is not APIHelper.SKIP:
            self.subtotal_in_cents = subtotal_in_cents 
        if start_date is not APIHelper.SKIP:
            self.start_date = APIHelper.apply_datetime_converter(start_date, APIHelper.RFC3339DateTime) if start_date else None 
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.apply_datetime_converter(end_date, APIHelper.RFC3339DateTime) if end_date else None 
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
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [BillingManifestItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        total_in_cents = dictionary.get("total_in_cents") if dictionary.get("total_in_cents") else APIHelper.SKIP
        total_discount_in_cents = dictionary.get("total_discount_in_cents") if dictionary.get("total_discount_in_cents") else APIHelper.SKIP
        total_tax_in_cents = dictionary.get("total_tax_in_cents") if dictionary.get("total_tax_in_cents") else APIHelper.SKIP
        subtotal_in_cents = dictionary.get("subtotal_in_cents") if dictionary.get("subtotal_in_cents") else APIHelper.SKIP
        if 'start_date' in dictionary.keys():
            start_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_date")).datetime if dictionary.get("start_date") else None
        else:
            start_date = APIHelper.SKIP
        if 'end_date' in dictionary.keys():
            end_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_date")).datetime if dictionary.get("end_date") else None
        else:
            end_date = APIHelper.SKIP
        period_type = dictionary.get("period_type") if "period_type" in dictionary.keys() else APIHelper.SKIP
        existing_balance_in_cents = dictionary.get("existing_balance_in_cents") if dictionary.get("existing_balance_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(line_items,
                   total_in_cents,
                   total_discount_in_cents,
                   total_tax_in_cents,
                   subtotal_in_cents,
                   start_date,
                   end_date,
                   period_type,
                   existing_balance_in_cents,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!r}, '
                f'total_in_cents={(self.total_in_cents if hasattr(self, "total_in_cents") else None)!r}, '
                f'total_discount_in_cents={(self.total_discount_in_cents if hasattr(self, "total_discount_in_cents") else None)!r}, '
                f'total_tax_in_cents={(self.total_tax_in_cents if hasattr(self, "total_tax_in_cents") else None)!r}, '
                f'subtotal_in_cents={(self.subtotal_in_cents if hasattr(self, "subtotal_in_cents") else None)!r}, '
                f'start_date={(self.start_date if hasattr(self, "start_date") else None)!r}, '
                f'end_date={(self.end_date if hasattr(self, "end_date") else None)!r}, '
                f'period_type={(self.period_type if hasattr(self, "period_type") else None)!r}, '
                f'existing_balance_in_cents={(self.existing_balance_in_cents if hasattr(self, "existing_balance_in_cents") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'line_items={(self.line_items if hasattr(self, "line_items") else None)!s}, '
                f'total_in_cents={(self.total_in_cents if hasattr(self, "total_in_cents") else None)!s}, '
                f'total_discount_in_cents={(self.total_discount_in_cents if hasattr(self, "total_discount_in_cents") else None)!s}, '
                f'total_tax_in_cents={(self.total_tax_in_cents if hasattr(self, "total_tax_in_cents") else None)!s}, '
                f'subtotal_in_cents={(self.subtotal_in_cents if hasattr(self, "subtotal_in_cents") else None)!s}, '
                f'start_date={(self.start_date if hasattr(self, "start_date") else None)!s}, '
                f'end_date={(self.end_date if hasattr(self, "end_date") else None)!s}, '
                f'period_type={(self.period_type if hasattr(self, "period_type") else None)!s}, '
                f'existing_balance_in_cents={(self.existing_balance_in_cents if hasattr(self, "existing_balance_in_cents") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
