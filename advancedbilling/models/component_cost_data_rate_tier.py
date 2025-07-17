# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentCostDataRateTier(object):

    """Implementation of the 'Component Cost Data Rate Tier' model.

    Attributes:
        starting_quantity (int): The model property of type int.
        ending_quantity (int): The model property of type int.
        quantity (str): The model property of type str.
        unit_price (str): The model property of type str.
        amount (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        starting_quantity = dictionary.get("starting_quantity") if dictionary.get("starting_quantity") else APIHelper.SKIP
        ending_quantity = dictionary.get("ending_quantity") if "ending_quantity" in dictionary.keys() else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(starting_quantity,
                   ending_quantity,
                   quantity,
                   unit_price,
                   amount,
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'starting_quantity={(self.starting_quantity if hasattr(self, "starting_quantity") else None)!r}, '
                f'ending_quantity={(self.ending_quantity if hasattr(self, "ending_quantity") else None)!r}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'unit_price={(self.unit_price if hasattr(self, "unit_price") else None)!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'starting_quantity={(self.starting_quantity if hasattr(self, "starting_quantity") else None)!s}, '
                f'ending_quantity={(self.ending_quantity if hasattr(self, "ending_quantity") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'unit_price={(self.unit_price if hasattr(self, "unit_price") else None)!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
