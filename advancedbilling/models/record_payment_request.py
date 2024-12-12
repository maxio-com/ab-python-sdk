# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.create_payment import CreatePayment


class RecordPaymentRequest(object):

    """Implementation of the 'Record Payment Request' model.

    TODO: type model description here.

    Attributes:
        payment (CreatePayment): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment'
    }

    def __init__(self,
                 payment=None,
                 additional_properties=None):
        """Constructor for the RecordPaymentRequest class"""

        # Initialize members of the class
        self.payment = payment 

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
        payment = CreatePayment.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payment,
                   additional_properties)
