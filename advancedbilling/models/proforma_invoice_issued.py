"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from datetime import date

import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_line_item_event_data import (
    InvoiceLineItemEventData,
)


class ProformaInvoiceIssued(object):
    """Implementation of the 'Proforma Invoice Issued' model.

    Attributes:
        uid (str): The model property of type str.
        number (str): The model property of type str.
        role (str): The model property of type str.
        delivery_date (date): The model property of type date.
        created_at (datetime): The model property of type datetime.
        due_amount (str): The model property of type str.
        paid_amount (str): The model property of type str.
        tax_amount (str): The model property of type str.
        total_amount (str): The model property of type str.
        product_name (str): The model property of type str.
        line_items (List[InvoiceLineItemEventData]): The model property of type
            List[InvoiceLineItemEventData].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": "uid",
        "number": "number",
        "role": "role",
        "delivery_date": "delivery_date",
        "created_at": "created_at",
        "due_amount": "due_amount",
        "paid_amount": "paid_amount",
        "tax_amount": "tax_amount",
        "total_amount": "total_amount",
        "product_name": "product_name",
        "line_items": "line_items",
    }

    def __init__(
        self,
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
        line_items=None,
        additional_properties=None):
        """Initialize a ProformaInvoiceIssued instance."""
        # Initialize members of the class
        self.uid = uid
        self.number = number
        self.role = role
        self.delivery_date = delivery_date
        self.created_at =\
             APIHelper.apply_datetime_converter(
            created_at, APIHelper.RFC3339DateTime)\
             if created_at else None
        self.due_amount = due_amount
        self.paid_amount = paid_amount
        self.tax_amount = tax_amount
        self.total_amount = total_amount
        self.product_name = product_name
        self.line_items = line_items

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

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
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else None
        number =\
            dictionary.get("number")\
            if dictionary.get("number")\
                else None
        role =\
            dictionary.get("role")\
            if dictionary.get("role")\
                else None
        delivery_date = dateutil.parser.parse(
            dictionary.get("delivery_date")).date()\
            if dictionary.get("delivery_date") else None
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else None
        due_amount =\
            dictionary.get("due_amount")\
            if dictionary.get("due_amount")\
                else None
        paid_amount =\
            dictionary.get("paid_amount")\
            if dictionary.get("paid_amount")\
                else None
        tax_amount =\
            dictionary.get("tax_amount")\
            if dictionary.get("tax_amount")\
                else None
        total_amount =\
            dictionary.get("total_amount")\
            if dictionary.get("total_amount")\
                else None
        product_name =\
            dictionary.get("product_name")\
            if dictionary.get("product_name")\
                else None
        line_items = None
        if dictionary.get("line_items") is not None:
            line_items = [
                InvoiceLineItemEventData.from_dictionary(x)
                    for x in dictionary.get("line_items")
            ]

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

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
                   line_items,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                    value=dictionary.uid,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.number,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.role,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.delivery_date,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        date,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.created_at,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        APIHelper.RFC3339DateTime,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.due_amount,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.paid_amount,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.tax_amount,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.total_amount,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.product_name,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.line_items,
                    type_callable=lambda value:
                        InvoiceLineItemEventData.validate(value),
                    is_model_dict=True,
                    is_inner_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("uid"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("number"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("role"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("delivery_date"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("created_at"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("due_amount"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("paid_amount"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("tax_amount"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("total_amount"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("product_name"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("line_items"),
                type_callable=lambda value:
                    InvoiceLineItemEventData.validate(value),
                is_model_dict=True,
                is_inner_model_dict=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _uid=self.uid
        _number=self.number
        _role=self.role
        _delivery_date=self.delivery_date
        _created_at=self.created_at
        _due_amount=self.due_amount
        _paid_amount=self.paid_amount
        _tax_amount=self.tax_amount
        _total_amount=self.total_amount
        _product_name=self.product_name
        _line_items=self.line_items
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!r}, "
            f"number={_number!r}, "
            f"role={_role!r}, "
            f"delivery_date={_delivery_date!r}, "
            f"created_at={_created_at!r}, "
            f"due_amount={_due_amount!r}, "
            f"paid_amount={_paid_amount!r}, "
            f"tax_amount={_tax_amount!r}, "
            f"total_amount={_total_amount!r}, "
            f"product_name={_product_name!r}, "
            f"line_items={_line_items!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _uid=self.uid
        _number=self.number
        _role=self.role
        _delivery_date=self.delivery_date
        _created_at=self.created_at
        _due_amount=self.due_amount
        _paid_amount=self.paid_amount
        _tax_amount=self.tax_amount
        _total_amount=self.total_amount
        _product_name=self.product_name
        _line_items=self.line_items
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!s}, "
            f"number={_number!s}, "
            f"role={_role!s}, "
            f"delivery_date={_delivery_date!s}, "
            f"created_at={_created_at!s}, "
            f"due_amount={_due_amount!s}, "
            f"paid_amount={_paid_amount!s}, "
            f"tax_amount={_tax_amount!s}, "
            f"total_amount={_total_amount!s}, "
            f"product_name={_product_name!s}, "
            f"line_items={_line_items!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
