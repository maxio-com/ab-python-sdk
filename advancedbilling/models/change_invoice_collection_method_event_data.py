# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ChangeInvoiceCollectionMethodEventData(object):

    """Implementation of the 'Change Invoice Collection Method Event Data' model.

    Example schema for an `change_invoice_collection_method` event

    Attributes:
        from_collection_method (str): The previous collection method of the
            invoice.
        to_collection_method (str): The new collection method of the invoice.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "from_collection_method": 'from_collection_method',
        "to_collection_method": 'to_collection_method'
    }

    _optionals = [
        'from_collection_method',
        'to_collection_method',
    ]

    def __init__(self,
                 from_collection_method=APIHelper.SKIP,
                 to_collection_method=APIHelper.SKIP):
        """Constructor for the ChangeInvoiceCollectionMethodEventData class"""

        # Initialize members of the class
        if from_collection_method is not APIHelper.SKIP:
            self.from_collection_method = from_collection_method 
        if to_collection_method is not APIHelper.SKIP:
            self.to_collection_method = to_collection_method 

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
        from_collection_method = dictionary.get("from_collection_method") if dictionary.get("from_collection_method") else APIHelper.SKIP
        to_collection_method = dictionary.get("to_collection_method") if dictionary.get("to_collection_method") else APIHelper.SKIP
        # Return an object of this model
        return cls(from_collection_method,
                   to_collection_method)

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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
