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

    TODO: type model description here.

    Attributes:
        line_items (List[BillingManifestItem]): TODO: type description here.
        total_in_cents (long|int): TODO: type description here.
        total_discount_in_cents (long|int): TODO: type description here.
        total_tax_in_cents (long|int): TODO: type description here.
        subtotal_in_cents (long|int): TODO: type description here.
        start_date (datetime): TODO: type description here.
        end_date (datetime): TODO: type description here.
        period_type (str): TODO: type description here.
        existing_balance_in_cents (long|int): TODO: type description here.

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
                 additional_properties={}):
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
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [BillingManifestItem.from_dictionary(x) for x in dictionary.get('line_items')]
        else:
            line_items = APIHelper.SKIP
        total_in_cents = dictionary.get("total_in_cents") if dictionary.get("total_in_cents") else APIHelper.SKIP
        total_discount_in_cents = dictionary.get("total_discount_in_cents") if dictionary.get("total_discount_in_cents") else APIHelper.SKIP
        total_tax_in_cents = dictionary.get("total_tax_in_cents") if dictionary.get("total_tax_in_cents") else APIHelper.SKIP
        subtotal_in_cents = dictionary.get("subtotal_in_cents") if dictionary.get("subtotal_in_cents") else APIHelper.SKIP
        start_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_date")).datetime if dictionary.get("start_date") else APIHelper.SKIP
        end_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_date")).datetime if dictionary.get("end_date") else APIHelper.SKIP
        period_type = dictionary.get("period_type") if dictionary.get("period_type") else APIHelper.SKIP
        existing_balance_in_cents = dictionary.get("existing_balance_in_cents") if dictionary.get("existing_balance_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
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
                   dictionary)
