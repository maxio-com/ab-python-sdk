# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod


class PaymentMethodBankAccount(object):

    """Implementation of the 'Payment Method Bank Account' model.

    Attributes:
        masked_account_number (str): The model property of type str.
        masked_routing_number (str): The model property of type str.
        mtype (InvoiceEventPaymentMethod): The model property of type
            InvoiceEventPaymentMethod.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "masked_account_number": 'masked_account_number',
        "masked_routing_number": 'masked_routing_number',
        "mtype": 'type'
    }

    def __init__(self,
                 masked_account_number=None,
                 masked_routing_number=None,
                 mtype=None,
                 additional_properties=None):
        """Constructor for the PaymentMethodBankAccount class"""

        # Initialize members of the class
        self.masked_account_number = masked_account_number 
        self.masked_routing_number = masked_routing_number 
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
        masked_account_number = dictionary.get("masked_account_number") if dictionary.get("masked_account_number") else None
        masked_routing_number = dictionary.get("masked_routing_number") if dictionary.get("masked_routing_number") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(masked_account_number,
                   masked_routing_number,
                   mtype,
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
            return APIHelper.is_valid_type(value=dictionary.masked_account_number,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.masked_routing_number,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.mtype,
                                            type_callable=lambda value: InvoiceEventPaymentMethod.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('masked_account_number'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('masked_routing_number'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('type'),
                                        type_callable=lambda value: InvoiceEventPaymentMethod.validate(value))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'masked_account_number={self.masked_account_number!r}, '
                f'masked_routing_number={self.masked_routing_number!r}, '
                f'mtype={self.mtype!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'masked_account_number={self.masked_account_number!s}, '
                f'masked_routing_number={self.masked_routing_number!s}, '
                f'mtype={self.mtype!s}, '
                f'additional_properties={self.additional_properties!s})')
