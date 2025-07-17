# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType


class FailedPaymentEventData(object):

    """Implementation of the 'Failed Payment Event Data' model.

    Example schema for an `failed_payment` event

    Attributes:
        amount_in_cents (int): The monetary value of the payment, expressed in
            cents.
        applied_amount (int): The monetary value of the payment, expressed in
            dollars.
        memo (str): The memo passed when the payment was created.
        payment_method (InvoicePaymentMethodType): The model property of type
            InvoicePaymentMethodType.
        transaction_id (int): The transaction ID of the failed payment.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_in_cents": 'amount_in_cents',
        "applied_amount": 'applied_amount',
        "payment_method": 'payment_method',
        "transaction_id": 'transaction_id',
        "memo": 'memo'
    }

    _optionals = [
        'memo',
    ]

    _nullables = [
        'memo',
    ]

    def __init__(self,
                 amount_in_cents=None,
                 applied_amount=None,
                 payment_method=None,
                 transaction_id=None,
                 memo=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the FailedPaymentEventData class"""

        # Initialize members of the class
        self.amount_in_cents = amount_in_cents 
        self.applied_amount = applied_amount 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        self.payment_method = payment_method 
        self.transaction_id = transaction_id 

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
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else None
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else None
        payment_method = dictionary.get("payment_method") if dictionary.get("payment_method") else None
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else None
        memo = dictionary.get("memo") if "memo" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount_in_cents,
                   applied_amount,
                   payment_method,
                   transaction_id,
                   memo,
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
            return APIHelper.is_valid_type(value=dictionary.amount_in_cents,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.payment_method,
                                            type_callable=lambda value: InvoicePaymentMethodType.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.transaction_id,
                                            type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('amount_in_cents'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_method'),
                                        type_callable=lambda value: InvoicePaymentMethodType.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_id'),
                                        type_callable=lambda value: isinstance(value, int))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount_in_cents={self.amount_in_cents!r}, '
                f'applied_amount={self.applied_amount!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'payment_method={self.payment_method!r}, '
                f'transaction_id={self.transaction_id!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount_in_cents={self.amount_in_cents!s}, '
                f'applied_amount={self.applied_amount!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'payment_method={self.payment_method!s}, '
                f'transaction_id={self.transaction_id!s}, '
                f'additional_properties={self.additional_properties!s})')
