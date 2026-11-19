"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.exceptions.api_exception import (
    APIException,
)


class WalletErrorResponseException(APIException):
    def __init__(self, reason, response):
        """Initialize WalletErrorResponseException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(WalletErrorResponseException, self).__init__(reason, response)
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
        self.errors =\
            dictionary.get("errors")\
            if dictionary.get("errors")\
                else None
        self.code =\
            dictionary.get("code")\
            if dictionary.get("code")\
                else None
        self.invoice_uid =\
            dictionary.get("invoice_uid")\
            if dictionary.get("invoice_uid")\
                else None
        self.invoice_number =\
            dictionary.get("invoice_number")\
            if dictionary.get("invoice_number")\
                else None


    def __str__(self):
        """Return a human-readable string representation."""
        _errors=self.errors
        _code=self.code
        _invoice_uid=(
            self.invoice_uid
            if hasattr(self, "invoice_uid")
            else None
        )
        _invoice_number=(
            self.invoice_number
            if hasattr(self, "invoice_number")
            else None
        )
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}, "
            f"errors={_errors!s}, "
            f"code={_code!s}, "
            f"invoice_uid={_invoice_uid!s}, "
            f"invoice_number={_invoice_number!s}, "
            f")"
        )
