# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoicePaymentMethod(object):

    """Implementation of the 'Invoice Payment Method' model.

    Attributes:
        details (str): The model property of type str.
        kind (str): The model property of type str.
        memo (str): The model property of type str.
        mtype (str): The model property of type str.
        card_brand (str): The model property of type str.
        card_expiration (str): The model property of type str.
        last_four (str): The model property of type str.
        masked_card_number (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 masked_card_number=APIHelper.SKIP,
                 additional_properties=None):
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

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
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
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(details,
                   kind,
                   memo,
                   mtype,
                   card_brand,
                   card_expiration,
                   last_four,
                   masked_card_number,
                   additional_properties)

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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'details={(self.details if hasattr(self, "details") else None)!r}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'card_brand={(self.card_brand if hasattr(self, "card_brand") else None)!r}, '
                f'card_expiration={(self.card_expiration if hasattr(self, "card_expiration") else None)!r}, '
                f'last_four={(self.last_four if hasattr(self, "last_four") else None)!r}, '
                f'masked_card_number={(self.masked_card_number if hasattr(self, "masked_card_number") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'details={(self.details if hasattr(self, "details") else None)!s}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'card_brand={(self.card_brand if hasattr(self, "card_brand") else None)!s}, '
                f'card_expiration={(self.card_expiration if hasattr(self, "card_expiration") else None)!s}, '
                f'last_four={(self.last_four if hasattr(self, "last_four") else None)!s}, '
                f'masked_card_number={(self.masked_card_number if hasattr(self, "masked_card_number") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
