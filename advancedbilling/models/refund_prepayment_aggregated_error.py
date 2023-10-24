# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.prepayment_aggregated_error import PrepaymentAggregatedError


class RefundPrepaymentAggregatedError(object):

    """Implementation of the 'Refund Prepayment Aggregated Error' model.

    TODO: type model description here.

    Attributes:
        refund (PrepaymentAggregatedError): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "refund": 'refund'
    }

    _optionals = [
        'refund',
    ]

    def __init__(self,
                 refund=APIHelper.SKIP):
        """Constructor for the RefundPrepaymentAggregatedError class"""

        # Initialize members of the class
        if refund is not APIHelper.SKIP:
            self.refund = refund 

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
        refund = PrepaymentAggregatedError.from_dictionary(dictionary.get('refund')) if 'refund' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(refund)
