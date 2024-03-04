# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PrepaymentAggregatedError(object):

    """Implementation of the 'Prepayment Aggregated Error' model.

    TODO: type model description here.

    Attributes:
        amount_in_cents (List[str]): TODO: type description here.
        base (List[str]): TODO: type description here.
        external (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_in_cents": 'amount_in_cents',
        "base": 'base',
        "external": 'external'
    }

    _optionals = [
        'amount_in_cents',
        'base',
        'external',
    ]

    def __init__(self,
                 amount_in_cents=APIHelper.SKIP,
                 base=APIHelper.SKIP,
                 external=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the PrepaymentAggregatedError class"""

        # Initialize members of the class
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if base is not APIHelper.SKIP:
            self.base = base 
        if external is not APIHelper.SKIP:
            self.external = external 

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
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        base = dictionary.get("base") if dictionary.get("base") else APIHelper.SKIP
        external = dictionary.get("external") if dictionary.get("external") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(amount_in_cents,
                   base,
                   external,
                   dictionary)
