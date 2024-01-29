# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.prepayment import Prepayment


class PrepaymentsResponse(object):

    """Implementation of the 'Prepayments Response' model.

    TODO: type model description here.

    Attributes:
        prepayments (List[Prepayment]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepayments": 'prepayments'
    }

    _optionals = [
        'prepayments',
    ]

    def __init__(self,
                 prepayments=APIHelper.SKIP):
        """Constructor for the PrepaymentsResponse class"""

        # Initialize members of the class
        if prepayments is not APIHelper.SKIP:
            self.prepayments = prepayments 

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
        prepayments = None
        if dictionary.get('prepayments') is not None:
            prepayments = [Prepayment.from_dictionary(x) for x in dictionary.get('prepayments')]
        else:
            prepayments = APIHelper.SKIP
        # Return an object of this model
        return cls(prepayments)
