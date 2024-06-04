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

    TODO: type model description here.

    Attributes:
        card_brand (str): TODO: type description here.
        card_expiration (str): TODO: type description here.
        last_four (str): TODO: type description here.
        masked_card_number (str): TODO: type description here.
        mtype (InvoiceEventPaymentMethod): TODO: type description here.

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
                 additional_properties={}):
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
        card_brand = dictionary.get("card_brand") if dictionary.get("card_brand") else None
        masked_card_number = dictionary.get("masked_card_number") if dictionary.get("masked_card_number") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        card_expiration = dictionary.get("card_expiration") if dictionary.get("card_expiration") else APIHelper.SKIP
        last_four = dictionary.get("last_four") if "last_four" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(card_brand,
                   masked_card_number,
                   mtype,
                   card_expiration,
                   last_four,
                   dictionary)

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
