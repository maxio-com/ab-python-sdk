# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper
import maxioadvancedbillingformerlychargifyapi.exceptions.api_exception


class SubscriptionsAddCouponJson422ErrorException(maxioadvancedbillingformerlychargifyapi.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the SubscriptionsAddCouponJson422ErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(SubscriptionsAddCouponJson422ErrorException, self).__init__(reason, response)
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
        self.subscription = dictionary.get("subscription") if dictionary.get("subscription") else None
        self.coupon_codes = dictionary.get("coupon_codes") if dictionary.get("coupon_codes") else None
