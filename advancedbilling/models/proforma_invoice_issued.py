# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_line_item_event_data import InvoiceLineItemEventData
from datetime import date


class ProformaInvoiceIssued(object):

    """Implementation of the 'Proforma Invoice Issued' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        number (str): TODO: type description here.
        role (str): TODO: type description here.
        delivery_date (date): TODO: type description here.
        created_at (datetime): TODO: type description here.
        due_amount (str): TODO: type description here.
        paid_amount (str): TODO: type description here.
        tax_amount (str): TODO: type description here.
        total_amount (str): TODO: type description here.
        product_name (str): TODO: type description here.
        line_items (List[InvoiceLineItemEventData]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "number": 'number',
        "role": 'role',
        "delivery_date": 'delivery_date',
        "created_at": 'created_at',
        "due_amount": 'due_amount',
        "paid_amount": 'paid_amount',
        "tax_amount": 'tax_amount',
        "total_amount": 'total_amount',
        "product_name": 'product_name',
        "line_items": 'line_items'
    }

    def __init__(self,
                 uid=None,
                 number=None,
                 role=None,
                 delivery_date=None,
                 created_at=None,
                 due_amount=None,
                 paid_amount=None,
                 tax_amount=None,
                 total_amount=None,
                 product_name=None,
                 line_items=None):
        """Constructor for the ProformaInvoiceIssued class"""

        # Initialize members of the class
        self.uid = uid 
        self.number = number 
        self.role = role 
        self.delivery_date = delivery_date 
        self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        self.due_amount = due_amount 
        self.paid_amount = paid_amount 
        self.tax_amount = tax_amount 
        self.total_amount = total_amount 
        self.product_name = product_name 
        self.line_items = line_items 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        number = dictionary.get("number") if dictionary.get("number") else None
        role = dictionary.get("role") if dictionary.get("role") else None
        delivery_date = dateutil.parser.parse(dictionary.get('delivery_date')).date() if dictionary.get('delivery_date') else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        due_amount = dictionary.get("due_amount") if dictionary.get("due_amount") else None
        paid_amount = dictionary.get("paid_amount") if dictionary.get("paid_amount") else None
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else None
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else None
        product_name = dictionary.get("product_name") if dictionary.get("product_name") else None
        line_items = None
        if dictionary.get('line_items') is not None:
            line_items = [InvoiceLineItemEventData.from_dictionary(x) for x in dictionary.get('line_items')]
        # Return an object of this model
        return cls(uid,
                   number,
                   role,
                   delivery_date,
                   created_at,
                   due_amount,
                   paid_amount,
                   tax_amount,
                   total_amount,
                   product_name,
                   line_items)

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
            return APIHelper.is_valid_type(value=dictionary.uid, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.number, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.role, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.delivery_date, type_callable=lambda value: isinstance(value, date)) \
                and APIHelper.is_valid_type(value=dictionary.created_at, type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.due_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.paid_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.tax_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.total_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.product_name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.line_items, type_callable=lambda value: InvoiceLineItemEventData.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('uid'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('number'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('role'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('delivery_date'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('created_at'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('due_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('paid_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('tax_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('total_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('product_name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('line_items'), type_callable=lambda value: InvoiceLineItemEventData.validate(value))
