# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
from advancedbilling.exceptions.api_exception import APIException


class SubscriptionAddCouponErrorException(APIException):
    def __init__(self, reason, response):
        """Constructor for the SubscriptionAddCouponErrorException class

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
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.codes = dictionary.get("codes") if dictionary.get("codes") else None
        self.coupon_code = dictionary.get("coupon_code") if dictionary.get("coupon_code") else None
        self.coupon_codes = dictionary.get("coupon_codes") if dictionary.get("coupon_codes") else None
        self.subscription = dictionary.get("subscription") if dictionary.get("subscription") else None

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'codes={self.codes!s}, '
                f'coupon_code={self.coupon_code!s}, '
                f'coupon_codes={self.coupon_codes!s}, '
                f'subscription={self.subscription!s})')
