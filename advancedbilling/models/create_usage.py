# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.billing_schedule import BillingSchedule


class CreateUsage(object):

    """Implementation of the 'Create Usage' model.

    Attributes:
        quantity (float): integer by default or decimal number if fractional
            quantities are enabled for the component
        price_point_id (str): The model property of type str.
        memo (str): The model property of type str.
        billing_schedule (BillingSchedule): This attribute is particularly
            useful when you need to align billing events for different
            components on distinct schedules within a subscription. Please
            note this only works for site with Multifrequency enabled
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity": 'quantity',
        "price_point_id": 'price_point_id',
        "memo": 'memo',
        "billing_schedule": 'billing_schedule'
    }

    _optionals = [
        'quantity',
        'price_point_id',
        'memo',
        'billing_schedule',
    ]

    def __init__(self,
                 quantity=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 billing_schedule=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateUsage class"""

        # Initialize members of the class
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if billing_schedule is not APIHelper.SKIP:
            self.billing_schedule = billing_schedule 

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
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        billing_schedule = BillingSchedule.from_dictionary(dictionary.get('billing_schedule')) if 'billing_schedule' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(quantity,
                   price_point_id,
                   memo,
                   billing_schedule,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'billing_schedule={(self.billing_schedule if hasattr(self, "billing_schedule") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'billing_schedule={(self.billing_schedule if hasattr(self, "billing_schedule") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
