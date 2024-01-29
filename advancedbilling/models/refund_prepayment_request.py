# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.refund_prepayment import RefundPrepayment


class RefundPrepaymentRequest(object):

    """Implementation of the 'Refund Prepayment Request' model.

    TODO: type model description here.

    Attributes:
        refund (RefundPrepayment): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "refund": 'refund'
    }

    def __init__(self,
                 refund=None):
        """Constructor for the RefundPrepaymentRequest class"""

        # Initialize members of the class
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
        refund = RefundPrepayment.from_dictionary(dictionary.get('refund')) if dictionary.get('refund') else None
        # Return an object of this model
        return cls(refund)
