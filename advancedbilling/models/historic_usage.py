# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class HistoricUsage(object):

    """Implementation of the 'Historic Usage' model.

    An optional object for Event Based Components, will be returned if
    provided `include=historic_usages` query param.

    Attributes:
        total_usage_quantity (float): Total usage of a component for billing
            period
        billing_period_starts_at (datetime): Start date of billing period
        billing_period_ends_at (datetime): End date of billing period

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_usage_quantity": 'total_usage_quantity',
        "billing_period_starts_at": 'billing_period_starts_at',
        "billing_period_ends_at": 'billing_period_ends_at'
    }

    _optionals = [
        'total_usage_quantity',
        'billing_period_starts_at',
        'billing_period_ends_at',
    ]

    def __init__(self,
                 total_usage_quantity=APIHelper.SKIP,
                 billing_period_starts_at=APIHelper.SKIP,
                 billing_period_ends_at=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the HistoricUsage class"""

        # Initialize members of the class
        if total_usage_quantity is not APIHelper.SKIP:
            self.total_usage_quantity = total_usage_quantity 
        if billing_period_starts_at is not APIHelper.SKIP:
            self.billing_period_starts_at = APIHelper.apply_datetime_converter(billing_period_starts_at, APIHelper.RFC3339DateTime) if billing_period_starts_at else None 
        if billing_period_ends_at is not APIHelper.SKIP:
            self.billing_period_ends_at = APIHelper.apply_datetime_converter(billing_period_ends_at, APIHelper.RFC3339DateTime) if billing_period_ends_at else None 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        total_usage_quantity = dictionary.get("total_usage_quantity") if dictionary.get("total_usage_quantity") else APIHelper.SKIP
        billing_period_starts_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("billing_period_starts_at")).datetime if dictionary.get("billing_period_starts_at") else APIHelper.SKIP
        billing_period_ends_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("billing_period_ends_at")).datetime if dictionary.get("billing_period_ends_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(total_usage_quantity,
                   billing_period_starts_at,
                   billing_period_ends_at,
                   dictionary)

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
