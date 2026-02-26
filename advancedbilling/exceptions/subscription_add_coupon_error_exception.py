"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.exceptions.api_exception import (
    APIException,
)


class SubscriptionAddCouponErrorException(APIException):
    def __init__(self, reason, response):
        """Initialize SubscriptionAddCouponErrorException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(SubscriptionAddCouponErrorException, self).__init__(reason, response)
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
        self.codes =\
            dictionary.get("codes")\
            if dictionary.get("codes")\
                else None
        self.coupon_code =\
            dictionary.get("coupon_code")\
            if dictionary.get("coupon_code")\
                else None
        self.coupon_codes =\
            dictionary.get("coupon_codes")\
            if dictionary.get("coupon_codes")\
                else None
        self.subscription =\
            dictionary.get("subscription")\
            if dictionary.get("subscription")\
                else None


    def __str__(self):
        """Return a human-readable string representation."""
        _codes=(
            self.codes
            if hasattr(self, "codes")
            else None
        )
        _coupon_code=(
            self.coupon_code
            if hasattr(self, "coupon_code")
            else None
        )
        _coupon_codes=(
            self.coupon_codes
            if hasattr(self, "coupon_codes")
            else None
        )
        _subscription=(
            self.subscription
            if hasattr(self, "subscription")
            else None
        )
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}, "
            f"codes={_codes!s}, "
            f"coupon_code={_coupon_code!s}, "
            f"coupon_codes={_coupon_codes!s}, "
            f"subscription={_subscription!s}, "
            f")"
        )
