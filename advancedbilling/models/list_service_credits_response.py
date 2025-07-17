# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.service_credit_1 import ServiceCredit1


class ListServiceCreditsResponse(object):

    """Implementation of the 'List Service Credits Response' model.

    Attributes:
        service_credits (List[ServiceCredit1]): The model property of type
            List[ServiceCredit1].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_credits": 'service_credits'
    }

    _optionals = [
        'service_credits',
    ]

    def __init__(self,
                 service_credits=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListServiceCreditsResponse class"""

        # Initialize members of the class
        if service_credits is not APIHelper.SKIP:
            self.service_credits = service_credits 

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
        service_credits = None
        if dictionary.get('service_credits') is not None:
            service_credits = [ServiceCredit1.from_dictionary(x) for x in dictionary.get('service_credits')]
        else:
            service_credits = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(service_credits,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'service_credits={(self.service_credits if hasattr(self, "service_credits") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'service_credits={(self.service_credits if hasattr(self, "service_credits") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
