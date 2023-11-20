# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentMethodCreditCardType(object):

    """Implementation of the 'Payment Method Credit Card Type' model.

    TODO: type model description here.

    Attributes:
        card_brand (str): TODO: type description here.
        card_expiration (str): TODO: type description here.
        last_four (str): TODO: type description here.
        masked_card_number (str): TODO: type description here.
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_brand": 'card_brand',
        "card_expiration": 'card_expiration',
        "last_four": 'last_four',
        "masked_card_number": 'masked_card_number',
        "mtype": 'type'
    }

    _optionals = [
        'card_brand',
        'card_expiration',
        'last_four',
        'masked_card_number',
        'mtype',
    ]

    _nullables = [
        'last_four',
    ]

    def __init__(self,
                 card_brand=APIHelper.SKIP,
                 card_expiration=APIHelper.SKIP,
                 last_four=APIHelper.SKIP,
                 masked_card_number=APIHelper.SKIP,
                 mtype='credit_card'):
        """Constructor for the PaymentMethodCreditCardType class"""

        # Initialize members of the class
        if card_brand is not APIHelper.SKIP:
            self.card_brand = card_brand 
        if card_expiration is not APIHelper.SKIP:
            self.card_expiration = card_expiration 
        if last_four is not APIHelper.SKIP:
            self.last_four = last_four 
        if masked_card_number is not APIHelper.SKIP:
            self.masked_card_number = masked_card_number 
        self.mtype = mtype 

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
        card_brand = dictionary.get("card_brand") if dictionary.get("card_brand") else APIHelper.SKIP
        card_expiration = dictionary.get("card_expiration") if dictionary.get("card_expiration") else APIHelper.SKIP
        last_four = dictionary.get("last_four") if "last_four" in dictionary.keys() else APIHelper.SKIP
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'credit_card'
        # Return an object of this model
        return cls(card_brand,
                   card_expiration,
                   last_four,
                   masked_card_number,
                   mtype)

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
