# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoicePaymentMethod(object):

    """Implementation of the 'Invoice Payment Method' model.

    TODO: type model description here.

    Attributes:
        details (str): TODO: type description here.
        kind (str): TODO: type description here.
        memo (str): TODO: type description here.
        mtype (str): TODO: type description here.
        card_brand (str): TODO: type description here.
        card_expiration (str): TODO: type description here.
        last_four (str): TODO: type description here.
        masked_card_number (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "details": 'details',
        "kind": 'kind',
        "memo": 'memo',
        "mtype": 'type',
        "card_brand": 'card_brand',
        "card_expiration": 'card_expiration',
        "last_four": 'last_four',
        "masked_card_number": 'masked_card_number'
    }

    _optionals = [
        'details',
        'kind',
        'memo',
        'mtype',
        'card_brand',
        'card_expiration',
        'last_four',
        'masked_card_number',
    ]

    _nullables = [
        'last_four',
    ]

    def __init__(self,
                 details=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 card_brand=APIHelper.SKIP,
                 card_expiration=APIHelper.SKIP,
                 last_four=APIHelper.SKIP,
                 masked_card_number=APIHelper.SKIP):
        """Constructor for the InvoicePaymentMethod class"""

        # Initialize members of the class
        if details is not APIHelper.SKIP:
            self.details = details 
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if card_brand is not APIHelper.SKIP:
            self.card_brand = card_brand 
        if card_expiration is not APIHelper.SKIP:
            self.card_expiration = card_expiration 
        if last_four is not APIHelper.SKIP:
            self.last_four = last_four 
        if masked_card_number is not APIHelper.SKIP:
            self.masked_card_number = masked_card_number 

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
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        card_brand = dictionary.get("card_brand") if dictionary.get("card_brand") else APIHelper.SKIP
        card_expiration = dictionary.get("card_expiration") if dictionary.get("card_expiration") else APIHelper.SKIP
        last_four = dictionary.get("last_four") if "last_four" in dictionary.keys() else APIHelper.SKIP
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else APIHelper.SKIP
        # Return an object of this model
        return cls(details,
                   kind,
                   memo,
                   mtype,
                   card_brand,
                   card_expiration,
                   last_four,
                   masked_card_number)
