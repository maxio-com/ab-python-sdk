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


class InvoiceIssued(object):
    """Implementation of the 'Invoice Issued' model.

    Attributes:
        uid (str): The model property of type str.
        number (str): The model property of type str.
        role (str): The model property of type str.
        due_date (date): The model property of type date.
        issue_date (str): Invoice issue date. Can be an empty string if value is
            missing.
        paid_date (str): Paid date. Can be an empty string if value is missing.
        due_amount (str): The model property of type str.
        paid_amount (str): The model property of type str.
        tax_amount (str): The model property of type str.
        refund_amount (str): The model property of type str.
        total_amount (str): The model property of type str.
        status_amount (str): The model property of type str.
        product_name (str): The model property of type str.
        consolidation_level (str): The model property of type str.
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
        "due_date": "due_date",
        "issue_date": "issue_date",
        "paid_date": "paid_date",
        "due_amount": "due_amount",
        "paid_amount": "paid_amount",
        "tax_amount": "tax_amount",
        "refund_amount": "refund_amount",
        "total_amount": "total_amount",
        "status_amount": "status_amount",
        "product_name": "product_name",
        "consolidation_level": "consolidation_level",
        "line_items": "line_items",
    }

    _nullables = [
        "due_date",
    ]

    def __init__(
        self,
        uid=None,
        number=None,
        role=None,
        due_date=None,
        issue_date=None,
        paid_date=None,
        due_amount=None,
        paid_amount=None,
        tax_amount=None,
        refund_amount=None,
        total_amount=None,
        status_amount=None,
        product_name=None,
        consolidation_level=None,
        line_items=None,
        additional_properties=None):
        """Initialize a InvoiceIssued instance."""
        # Initialize members of the class
        self.uid = uid
        self.number = number
        self.role = role
        self.due_date = due_date
        self.issue_date = issue_date
        self.paid_date = paid_date
        self.due_amount = due_amount
        self.paid_amount = paid_amount
        self.tax_amount = tax_amount
        self.refund_amount = refund_amount
        self.total_amount = total_amount
        self.status_amount = status_amount
        self.product_name = product_name
        self.consolidation_level = consolidation_level
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
        due_date = dateutil.parser.parse(
            dictionary.get("due_date")).date()\
            if dictionary.get("due_date") else None
        issue_date =\
            dictionary.get("issue_date")\
            if dictionary.get("issue_date")\
                else None
        paid_date =\
            dictionary.get("paid_date")\
            if dictionary.get("paid_date")\
                else None
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
        refund_amount =\
            dictionary.get("refund_amount")\
            if dictionary.get("refund_amount")\
                else None
        total_amount =\
            dictionary.get("total_amount")\
            if dictionary.get("total_amount")\
                else None
        status_amount =\
            dictionary.get("status_amount")\
            if dictionary.get("status_amount")\
                else None
        product_name =\
            dictionary.get("product_name")\
            if dictionary.get("product_name")\
                else None
        consolidation_level =\
            dictionary.get("consolidation_level")\
            if dictionary.get("consolidation_level")\
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
                   due_date,
                   issue_date,
                   paid_date,
                   due_amount,
                   paid_amount,
                   tax_amount,
                   refund_amount,
                   total_amount,
                   status_amount,
                   product_name,
                   consolidation_level,
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
                    value=dictionary.due_date,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        date,
                ),
                    is_value_nullable=True) \
                and APIHelper.is_valid_type(
                    value=dictionary.issue_date,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.paid_date,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
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
                    value=dictionary.refund_amount,
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
                    value=dictionary.status_amount,
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
                    value=dictionary.consolidation_level,
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
                value=dictionary.get("due_date"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ),
                is_value_nullable=True) \
            and APIHelper.is_valid_type(
                value=dictionary.get("issue_date"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("paid_date"),
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
                value=dictionary.get("refund_amount"),
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
                value=dictionary.get("status_amount"),
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
                value=dictionary.get("consolidation_level"),
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
        _due_date=self.due_date
        _issue_date=self.issue_date
        _paid_date=self.paid_date
        _due_amount=self.due_amount
        _paid_amount=self.paid_amount
        _tax_amount=self.tax_amount
        _refund_amount=self.refund_amount
        _total_amount=self.total_amount
        _status_amount=self.status_amount
        _product_name=self.product_name
        _consolidation_level=self.consolidation_level
        _line_items=self.line_items
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!r}, "
            f"number={_number!r}, "
            f"role={_role!r}, "
            f"due_date={_due_date!r}, "
            f"issue_date={_issue_date!r}, "
            f"paid_date={_paid_date!r}, "
            f"due_amount={_due_amount!r}, "
            f"paid_amount={_paid_amount!r}, "
            f"tax_amount={_tax_amount!r}, "
            f"refund_amount={_refund_amount!r}, "
            f"total_amount={_total_amount!r}, "
            f"status_amount={_status_amount!r}, "
            f"product_name={_product_name!r}, "
            f"consolidation_level={_consolidation_level!r}, "
            f"line_items={_line_items!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _uid=self.uid
        _number=self.number
        _role=self.role
        _due_date=self.due_date
        _issue_date=self.issue_date
        _paid_date=self.paid_date
        _due_amount=self.due_amount
        _paid_amount=self.paid_amount
        _tax_amount=self.tax_amount
        _refund_amount=self.refund_amount
        _total_amount=self.total_amount
        _status_amount=self.status_amount
        _product_name=self.product_name
        _consolidation_level=self.consolidation_level
        _line_items=self.line_items
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!s}, "
            f"number={_number!s}, "
            f"role={_role!s}, "
            f"due_date={_due_date!s}, "
            f"issue_date={_issue_date!s}, "
            f"paid_date={_paid_date!s}, "
            f"due_amount={_due_amount!s}, "
            f"paid_amount={_paid_amount!s}, "
            f"tax_amount={_tax_amount!s}, "
            f"refund_amount={_refund_amount!s}, "
            f"total_amount={_total_amount!s}, "
            f"status_amount={_status_amount!s}, "
            f"product_name={_product_name!s}, "
            f"consolidation_level={_consolidation_level!s}, "
            f"line_items={_line_items!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
