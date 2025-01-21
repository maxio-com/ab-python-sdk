# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class DunnerData(object):

    """Implementation of the 'Dunner Data' model.

    Attributes:
        state (str): The model property of type str.
        subscription_id (int): The model property of type int.
        revenue_at_risk_in_cents (int): The model property of type int.
        created_at (datetime): The model property of type datetime.
        attempts (int): The model property of type int.
        last_attempted_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "state": 'state',
        "subscription_id": 'subscription_id',
        "revenue_at_risk_in_cents": 'revenue_at_risk_in_cents',
        "created_at": 'created_at',
        "attempts": 'attempts',
        "last_attempted_at": 'last_attempted_at'
    }

    def __init__(self,
                 state=None,
                 subscription_id=None,
                 revenue_at_risk_in_cents=None,
                 created_at=None,
                 attempts=None,
                 last_attempted_at=None,
                 additional_properties=None):
        """Constructor for the DunnerData class"""

        # Initialize members of the class
        self.state = state 
        self.subscription_id = subscription_id 
        self.revenue_at_risk_in_cents = revenue_at_risk_in_cents 
        self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        self.attempts = attempts 
        self.last_attempted_at = APIHelper.apply_datetime_converter(last_attempted_at, APIHelper.RFC3339DateTime) if last_attempted_at else None 

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
        state = dictionary.get("state") if dictionary.get("state") else None
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        revenue_at_risk_in_cents = dictionary.get("revenue_at_risk_in_cents") if dictionary.get("revenue_at_risk_in_cents") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        attempts = dictionary.get("attempts") if dictionary.get("attempts") else None
        last_attempted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("last_attempted_at")).datetime if dictionary.get("last_attempted_at") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(state,
                   subscription_id,
                   revenue_at_risk_in_cents,
                   created_at,
                   attempts,
                   last_attempted_at,
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
            return APIHelper.is_valid_type(value=dictionary.state,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.subscription_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.revenue_at_risk_in_cents,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.created_at,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.attempts,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.last_attempted_at,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('state'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('subscription_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('revenue_at_risk_in_cents'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('created_at'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('attempts'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('last_attempted_at'),
                                        type_callable=lambda value: isinstance(value, str))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'state={self.state!r}, '
                f'subscription_id={self.subscription_id!r}, '
                f'revenue_at_risk_in_cents={self.revenue_at_risk_in_cents!r}, '
                f'created_at={self.created_at!r}, '
                f'attempts={self.attempts!r}, '
                f'last_attempted_at={self.last_attempted_at!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'state={self.state!s}, '
                f'subscription_id={self.subscription_id!s}, '
                f'revenue_at_risk_in_cents={self.revenue_at_risk_in_cents!s}, '
                f'created_at={self.created_at!s}, '
                f'attempts={self.attempts!s}, '
                f'last_attempted_at={self.last_attempted_at!s}, '
                f'additional_properties={self.additional_properties!s})')
