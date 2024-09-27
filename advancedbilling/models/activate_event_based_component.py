# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.billing_schedule import BillingSchedule
from advancedbilling.models.component_custom_price import ComponentCustomPrice


class ActivateEventBasedComponent(object):

    """Implementation of the 'Activate Event-Based Component' model.

    TODO: type model description here.

    Attributes:
        price_point_id (int): The Chargify id of the price point
        billing_schedule (BillingSchedule): This attribute is particularly
            useful when you need to align billing events for different
            components on distinct schedules within a subscription. Please
            note this only works for site with Multifrequency enabled
        custom_price (ComponentCustomPrice): Create or update custom pricing
            unique to the subscription. Used in place of `price_point_id`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price_point_id": 'price_point_id',
        "billing_schedule": 'billing_schedule',
        "custom_price": 'custom_price'
    }

    _optionals = [
        'price_point_id',
        'billing_schedule',
        'custom_price',
    ]

    def __init__(self,
                 price_point_id=APIHelper.SKIP,
                 billing_schedule=APIHelper.SKIP,
                 custom_price=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ActivateEventBasedComponent class"""

        # Initialize members of the class
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if billing_schedule is not APIHelper.SKIP:
            self.billing_schedule = billing_schedule 
        if custom_price is not APIHelper.SKIP:
            self.custom_price = custom_price 

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
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        billing_schedule = BillingSchedule.from_dictionary(dictionary.get('billing_schedule')) if 'billing_schedule' in dictionary.keys() else APIHelper.SKIP
        custom_price = ComponentCustomPrice.from_dictionary(dictionary.get('custom_price')) if 'custom_price' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(price_point_id,
                   billing_schedule,
                   custom_price,
                   dictionary)