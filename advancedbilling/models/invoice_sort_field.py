# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class InvoiceSortField(object):

    """Implementation of the 'Invoice Sort Field' enum.

    Attributes:
        STATUS: The enum member of type str.
        TOTAL_AMOUNT: The enum member of type str.
        DUE_AMOUNT: The enum member of type str.
        CREATED_AT: The enum member of type str.
        UPDATED_AT: The enum member of type str.
        ISSUE_DATE: The enum member of type str.
        DUE_DATE: The enum member of type str.
        NUMBER: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    STATUS = 'status'

    TOTAL_AMOUNT = 'total_amount'

    DUE_AMOUNT = 'due_amount'

    CREATED_AT = 'created_at'

    UPDATED_AT = 'updated_at'

    ISSUE_DATE = 'issue_date'

    DUE_DATE = 'due_date'

    NUMBER = 'number'

    @classmethod
    def from_value(cls, value, default=None):
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
