# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.service_credit import ServiceCredit


class ServiceCreditResponse(object):

    """Implementation of the 'Service Credit Response' model.

    TODO: type model description here.

    Attributes:
        service_credit (ServiceCredit): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_credit": 'service_credit'
    }

    def __init__(self,
                 service_credit=None,
                 additional_properties=None):
        """Constructor for the ServiceCreditResponse class"""

        # Initialize members of the class
        self.service_credit = service_credit 

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
        service_credit = ServiceCredit.from_dictionary(dictionary.get('service_credit')) if dictionary.get('service_credit') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(service_credit,
                   additional_properties)
