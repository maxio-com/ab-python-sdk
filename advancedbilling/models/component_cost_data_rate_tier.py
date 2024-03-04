# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentCostDataRateTier(object):

    """Implementation of the 'Component Cost Data Rate Tier' model.

    TODO: type model description here.

    Attributes:
        starting_quantity (int): TODO: type description here.
        ending_quantity (int): TODO: type description here.
        quantity (str): TODO: type description here.
        unit_price (str): TODO: type description here.
        amount (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "starting_quantity": 'starting_quantity',
        "ending_quantity": 'ending_quantity',
        "quantity": 'quantity',
        "unit_price": 'unit_price',
        "amount": 'amount'
    }

    _optionals = [
        'starting_quantity',
        'ending_quantity',
        'quantity',
        'unit_price',
        'amount',
    ]

    _nullables = [
        'ending_quantity',
    ]

    def __init__(self,
                 starting_quantity=APIHelper.SKIP,
                 ending_quantity=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ComponentCostDataRateTier class"""

        # Initialize members of the class
        if starting_quantity is not APIHelper.SKIP:
            self.starting_quantity = starting_quantity 
        if ending_quantity is not APIHelper.SKIP:
            self.ending_quantity = ending_quantity 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if amount is not APIHelper.SKIP:
            self.amount = amount 

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
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        ending_quantity = dictionary.get("ending_quantity") if "ending_quantity" in dictionary.keys() else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(starting_quantity,
                   ending_quantity,
                   quantity,
                   unit_price,
                   amount,
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
