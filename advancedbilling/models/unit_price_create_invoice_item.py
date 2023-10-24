# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UnitPriceCreateInvoiceItem(object):

    """Implementation of the 'UnitPrice_Create Invoice Item' model.

    The unit_price can contain up to 8 decimal places. i.e. 1.00 or 0.0012 or
    0.00000065. If you submit a value with more than 8 decimal places, we will
    round it down to the 8th decimal place.

    """

    # Create a mapping from Model property names to API property names
    _names = {

    }

    def __init__(self,
                 ):
        """Constructor for the UnitPriceCreateInvoiceItem class"""

        # Initialize members of the class

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
        # Return an object of this model
        return cls()

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
