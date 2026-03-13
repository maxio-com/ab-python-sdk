"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.exceptions.api_exception import (
    APIException,
)


class CustomerErrorResponseException(APIException):
    def __init__(self, reason, response):
        """Initialize CustomerErrorResponseException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(CustomerErrorResponseException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populate the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        self.errors = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("CustomerErrorResponseErrors"),
            dictionary.get("errors"),
            False)\
            if dictionary.get("errors") is not None\
            else None


    def __str__(self):
        """Return a human-readable string representation."""
        _errors=(
            self.errors
            if hasattr(self, "errors")
            else None
        )
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}, "
            f"errors={_errors!s}, "
            f")"
        )
