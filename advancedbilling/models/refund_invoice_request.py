# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RefundInvoiceRequest(object):

    """Implementation of the 'Refund Invoice Request' model.

    TODO: type model description here.

    Attributes:
        refund (RefundInvoice | RefundConsolidatedInvoice): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "refund": 'refund'
    }

    def __init__(self,
                 refund=None):
        """Constructor for the RefundInvoiceRequest class"""

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        refund = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RefundInvoiceRequestRefund'), dictionary.get('refund'), False) if dictionary.get('refund') is not None else None
        # Return an object of this model
        return cls(refund)

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if isinstance(dictionary, cls):
            return UnionTypeLookUp.get('RefundInvoiceRequestRefund').validate(dictionary.refund)

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('RefundInvoiceRequestRefund').validate(dictionary.get('refund'))
