# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.deduct_service_credit import DeductServiceCredit


class DeductServiceCreditRequest(object):

    """Implementation of the 'Deduct Service Credit Request' model.

    TODO: type model description here.

    Attributes:
        deduction (DeductServiceCredit): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deduction": 'deduction'
    }

    def __init__(self,
                 deduction=None):
        """Constructor for the DeductServiceCreditRequest class"""

        # Initialize members of the class
        self.deduction = deduction 

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
        deduction = DeductServiceCredit.from_dictionary(dictionary.get('deduction')) if dictionary.get('deduction') else None
        # Return an object of this model
        return cls(deduction)
