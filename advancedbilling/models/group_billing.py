# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class GroupBilling(object):

    """Implementation of the 'Group Billing' model.

    Optional attributes related to billing date and accrual. Note: Only
    applicable for new subscriptions.

    Attributes:
        accrue (bool): A flag indicating whether or not to accrue charges on
            the new subscription.
        align_date (bool): A flag indicating whether or not to align the
            billing date of the new subscription with the billing date of the
            primary subscription of the hierarchy's default subscription
            group. Required to be true if prorate is also true.
        prorate (bool): A flag indicating whether or not to prorate billing of
            the new subscription for the current period. A value of true is
            ignored unless align_date is also true.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accrue": 'accrue',
        "align_date": 'align_date',
        "prorate": 'prorate'
    }

    _optionals = [
        'accrue',
        'align_date',
        'prorate',
    ]

    def __init__(self,
                 accrue=False,
                 align_date=False,
                 prorate=False,
                 additional_properties=None):
        """Constructor for the GroupBilling class"""

        # Initialize members of the class
        self.accrue = accrue 
        self.align_date = align_date 
        self.prorate = prorate 

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
        accrue = dictionary.get("accrue") if dictionary.get("accrue") else False
        align_date = dictionary.get("align_date") if dictionary.get("align_date") else False
        prorate = dictionary.get("prorate") if dictionary.get("prorate") else False
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(accrue,
                   align_date,
                   prorate,
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
