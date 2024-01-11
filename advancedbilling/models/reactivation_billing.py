# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ReactivationBilling(object):

    """Implementation of the 'Reactivation Billing' model.

    These values are only applicable to subscriptions using calendar billing

    Attributes:
        reactivation_charge (ReactivationCharge): You may choose how to handle
            the reactivation charge for that subscription: 1) `prorated` A
            prorated charge for the product price will be attempted for to
            complete the period 2) `immediate` A full-price charge for the
            product price will be attempted immediately 3) `delayed` A
            full-price charge for the product price will be attempted at the
            next renewal

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reactivation_charge": 'reactivation_charge'
    }

    _optionals = [
        'reactivation_charge',
    ]

    def __init__(self,
                 reactivation_charge='prorated'):
        """Constructor for the ReactivationBilling class"""

        # Initialize members of the class
        self.reactivation_charge = reactivation_charge 

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
        reactivation_charge = dictionary.get("reactivation_charge") if dictionary.get("reactivation_charge") else 'prorated'
        # Return an object of this model
        return cls(reactivation_charge)

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
