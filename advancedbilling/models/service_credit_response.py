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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_credit": 'service_credit'
    }

    def __init__(self,
                 service_credit=None,
                 additional_properties={}):
        """Constructor for the ServiceCreditResponse class"""

        # Initialize members of the class
        self.service_credit = service_credit 

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
        service_credit = ServiceCredit.from_dictionary(dictionary.get('service_credit')) if dictionary.get('service_credit') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(service_credit,
                   dictionary)
