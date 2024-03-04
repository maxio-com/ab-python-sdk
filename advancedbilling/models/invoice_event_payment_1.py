# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceEventPayment1(object):

    """Implementation of the 'Invoice Event Payment1' model.

    A nested data structure detailing the method of payment

    Attributes:
        mtype (str): TODO: type description here.
        masked_account_number (str): TODO: type description here.
        masked_routing_number (str): TODO: type description here.
        card_brand (str): TODO: type description here.
        card_expiration (str): TODO: type description here.
        last_four (str): TODO: type description here.
        masked_card_number (str): TODO: type description here.
        details (str): TODO: type description here.
        kind (str): TODO: type description here.
        memo (str): TODO: type description here.
        email (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "masked_account_number": 'masked_account_number',
        "masked_routing_number": 'masked_routing_number',
        "card_brand": 'card_brand',
        "masked_card_number": 'masked_card_number',
        "details": 'details',
        "kind": 'kind',
        "memo": 'memo',
        "email": 'email',
        "mtype": 'type',
        "card_expiration": 'card_expiration',
        "last_four": 'last_four'
    }

    _optionals = [
        'mtype',
        'card_expiration',
        'last_four',
    ]

    _nullables = [
        'last_four',
        'details',
        'memo',
    ]

    def __init__(self,
                 masked_account_number=None,
                 masked_routing_number=None,
                 card_brand=None,
                 masked_card_number=None,
                 details=None,
                 kind=None,
                 memo=None,
                 email=None,
                 mtype='Invoice Event Payment1',
                 card_expiration=APIHelper.SKIP,
                 last_four=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoiceEventPayment1 class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.masked_account_number = masked_account_number 
        self.masked_routing_number = masked_routing_number 
        self.card_brand = card_brand 
        if card_expiration is not APIHelper.SKIP:
            self.card_expiration = card_expiration 
        if last_four is not APIHelper.SKIP:
            self.last_four = last_four 
        self.masked_card_number = masked_card_number 
        self.details = details 
        self.kind = kind 
        self.memo = memo 
        self.email = email 

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
        masked_account_number = dictionary.get("masked_account_number") if dictionary.get("masked_account_number") else None
        masked_routing_number = dictionary.get("masked_routing_number") if dictionary.get("masked_routing_number") else None
        card_brand = dictionary.get("card_brand") if dictionary.get("card_brand") else None
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else None
        details = dictionary.get("details") if dictionary.get("details") else None
        kind = dictionary.get("kind") if dictionary.get("kind") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        email = dictionary.get("email") if dictionary.get("email") else None
        mtype = dictionary.get("type") if dictionary.get("type") else 'Invoice Event Payment1'
        card_expiration = dictionary.get("card_expiration") if dictionary.get("card_expiration") else APIHelper.SKIP
        last_four = dictionary.get("last_four") if "last_four" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(masked_account_number,
                   masked_routing_number,
                   card_brand,
                   masked_card_number,
                   details,
                   kind,
                   memo,
                   email,
                   mtype,
                   card_expiration,
                   last_four,
                   dictionary)
