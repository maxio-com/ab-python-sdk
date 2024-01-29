# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceLineItemPricingDetail(object):

    """Implementation of the 'Invoice Line Item Pricing Detail' model.

    TODO: type model description here.

    Attributes:
        label (str): TODO: type description here.
        amount (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "label": 'label',
        "amount": 'amount'
    }

    _optionals = [
        'label',
        'amount',
    ]

    def __init__(self,
                 label=APIHelper.SKIP,
                 amount=APIHelper.SKIP):
        """Constructor for the InvoiceLineItemPricingDetail class"""

        # Initialize members of the class
        if label is not APIHelper.SKIP:
            self.label = label 
        if amount is not APIHelper.SKIP:
            self.amount = amount 

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
        label = dictionary.get("label") if dictionary.get("label") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(label,
                   amount)

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
