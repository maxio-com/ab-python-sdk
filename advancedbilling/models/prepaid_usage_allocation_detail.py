# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PrepaidUsageAllocationDetail(object):

    """Implementation of the 'Prepaid Usage Allocation Detail' model.

    TODO: type model description here.

    Attributes:
        allocation_id (int): TODO: type description here.
        charge_id (int): TODO: type description here.
        usage_quantity (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allocation_id": 'allocation_id',
        "charge_id": 'charge_id',
        "usage_quantity": 'usage_quantity'
    }

    _optionals = [
        'allocation_id',
        'charge_id',
        'usage_quantity',
    ]

    def __init__(self,
                 allocation_id=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 usage_quantity=APIHelper.SKIP):
        """Constructor for the PrepaidUsageAllocationDetail class"""

        # Initialize members of the class
        if allocation_id is not APIHelper.SKIP:
            self.allocation_id = allocation_id 
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id 
        if usage_quantity is not APIHelper.SKIP:
            self.usage_quantity = usage_quantity 

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
        allocation_id = dictionary.get("allocation_id") if dictionary.get("allocation_id") else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if dictionary.get("charge_id") else APIHelper.SKIP
        usage_quantity = dictionary.get("usage_quantity") if dictionary.get("usage_quantity") else APIHelper.SKIP
        # Return an object of this model
        return cls(allocation_id,
                   charge_id,
                   usage_quantity)

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
