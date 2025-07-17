# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod


class PaymentMethodCreditCard(object):

    """Implementation of the 'Payment Method Credit Card' model.

    Attributes:
        card_brand (str): The model property of type str.
        card_expiration (str): The model property of type str.
        last_four (str): The model property of type str.
        masked_card_number (str): The model property of type str.
        mtype (InvoiceEventPaymentMethod): The model property of type
            InvoiceEventPaymentMethod.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_brand": 'card_brand',
        "masked_card_number": 'masked_card_number',
        "mtype": 'type',
        "card_expiration": 'card_expiration',
        "last_four": 'last_four'
    }

    _optionals = [
        'card_expiration',
        'last_four',
    ]

    _nullables = [
        'last_four',
    ]

    def __init__(self,
                 card_brand=None,
                 masked_card_number=None,
                 mtype=None,
                 card_expiration=APIHelper.SKIP,
                 last_four=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PaymentMethodCreditCard class"""

        # Initialize members of the class
        self.card_brand = card_brand 
        if card_expiration is not APIHelper.SKIP:
            self.card_expiration = card_expiration 
        if last_four is not APIHelper.SKIP:
            self.last_four = last_four 
        self.masked_card_number = masked_card_number 
        self.mtype = mtype 

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
        card_brand = dictionary.get("card_brand") if dictionary.get("card_brand") else None
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        card_expiration = dictionary.get("card_expiration") if dictionary.get("card_expiration") else APIHelper.SKIP
        last_four = dictionary.get("last_four") if "last_four" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(card_brand,
                   masked_card_number,
                   mtype,
                   card_expiration,
                   last_four,
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
            return APIHelper.is_valid_type(value=dictionary.card_brand,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.masked_card_number,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.mtype,
                                            type_callable=lambda value: InvoiceEventPaymentMethod.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('card_brand'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('masked_card_number'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('type'),
                                        type_callable=lambda value: InvoiceEventPaymentMethod.validate(value))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'card_brand={self.card_brand!r}, '
                f'card_expiration={(self.card_expiration if hasattr(self, "card_expiration") else None)!r}, '
                f'last_four={(self.last_four if hasattr(self, "last_four") else None)!r}, '
                f'masked_card_number={self.masked_card_number!r}, '
                f'mtype={self.mtype!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'card_brand={self.card_brand!s}, '
                f'card_expiration={(self.card_expiration if hasattr(self, "card_expiration") else None)!s}, '
                f'last_four={(self.last_four if hasattr(self, "last_four") else None)!s}, '
                f'masked_card_number={self.masked_card_number!s}, '
                f'mtype={self.mtype!s}, '
                f'additional_properties={self.additional_properties!s})')
