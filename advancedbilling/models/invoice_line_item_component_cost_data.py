# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_cost_data import ComponentCostData


class InvoiceLineItemComponentCostData(object):

    """Implementation of the 'Invoice Line Item Component Cost Data' model.

    TODO: type model description here.

    Attributes:
        rates (List[ComponentCostData]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rates": 'rates'
    }

    _optionals = [
        'rates',
    ]

    def __init__(self,
                 rates=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoiceLineItemComponentCostData class"""

        # Initialize members of the class
        if rates is not APIHelper.SKIP:
            self.rates = rates 

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
        rates = None
        if dictionary.get('rates') is not None:
            rates = [ComponentCostData.from_dictionary(x) for x in dictionary.get('rates')]
        else:
            rates = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(rates,
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
