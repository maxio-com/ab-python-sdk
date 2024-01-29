# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionIncludedCoupon(object):

    """Implementation of the 'Subscription Included Coupon' model.

    TODO: type model description here.

    Attributes:
        code (str): TODO: type description here.
        use_count (int): TODO: type description here.
        uses_allowed (int): TODO: type description here.
        expires_at (str): TODO: type description here.
        recurring (bool): TODO: type description here.
        amount_in_cents (long|int): TODO: type description here.
        percentage (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "use_count": 'use_count',
        "uses_allowed": 'uses_allowed',
        "expires_at": 'expires_at',
        "recurring": 'recurring',
        "amount_in_cents": 'amount_in_cents',
        "percentage": 'percentage'
    }

    _optionals = [
        'code',
        'use_count',
        'uses_allowed',
        'expires_at',
        'recurring',
        'amount_in_cents',
        'percentage',
    ]

    _nullables = [
        'expires_at',
        'amount_in_cents',
        'percentage',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 use_count=APIHelper.SKIP,
                 uses_allowed=APIHelper.SKIP,
                 expires_at=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 percentage=APIHelper.SKIP):
        """Constructor for the SubscriptionIncludedCoupon class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if use_count is not APIHelper.SKIP:
            self.use_count = use_count 
        if uses_allowed is not APIHelper.SKIP:
            self.uses_allowed = uses_allowed 
        if expires_at is not APIHelper.SKIP:
            self.expires_at = expires_at 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 

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
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        use_count = dictionary.get("use_count") if dictionary.get("use_count") else APIHelper.SKIP
        uses_allowed = dictionary.get("uses_allowed") if dictionary.get("uses_allowed") else APIHelper.SKIP
        expires_at = dictionary.get("expires_at") if "expires_at" in dictionary.keys() else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if "amount_in_cents" in dictionary.keys() else APIHelper.SKIP
        percentage = dictionary.get("percentage") if "percentage" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   use_count,
                   uses_allowed,
                   expires_at,
                   recurring,
                   amount_in_cents,
                   percentage)

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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
