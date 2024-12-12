# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentForAllocation(object):

    """Implementation of the 'Payment for Allocation' model.

    Information for captured payment, if applicable

    Attributes:
        id (int): TODO: type description here.
        amount_in_cents (long|int): TODO: type description here.
        success (bool): TODO: type description here.
        memo (str): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "amount_in_cents": 'amount_in_cents',
        "success": 'success',
        "memo": 'memo'
    }

    _optionals = [
        'id',
        'amount_in_cents',
        'success',
        'memo',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 success=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PaymentForAllocation class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if success is not APIHelper.SKIP:
            self.success = success 
        if memo is not APIHelper.SKIP:
            self.memo = memo 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        success = dictionary.get("success") if "success" in dictionary.keys() else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   amount_in_cents,
                   success,
                   memo,
                   additional_properties)

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
