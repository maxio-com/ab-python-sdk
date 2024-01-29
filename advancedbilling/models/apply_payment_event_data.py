# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ApplyPaymentEventData(object):

    """Implementation of the 'Apply Payment Event Data' model.

    Example schema for an `apply_payment` event

    Attributes:
        memo (str): The payment memo
        original_amount (str): The full, original amount of the payment
            transaction as a string in full units. Incoming payments can be
            split amongst several invoices, which will result in a
            `applied_amount` less than the `original_amount`. Example: A
            $100.99 payment, of which $40.11 is applied to this invoice, will
            have an `original_amount` of `"100.99"`.
        applied_amount (str): The amount of the payment applied to this
            invoice. Incoming payments can be split amongst several invoices,
            which will result in a `applied_amount` less than the
            `original_amount`. Example: A $100.99 payment, of which $40.11 is
            applied to this invoice, will have an `applied_amount` of
            `"40.11"`.
        transaction_time (datetime): The time the payment was applied, in ISO
            8601 format, i.e. "2019-06-07T17:20:06Z"
        payment_method (PaymentMethodApplePayType |
            PaymentMethodBankAccountType | PaymentMethodCreditCardType |
            PaymentMethodExternalType | PaymentMethodPaypalType): A nested
            data structure detailing the method of payment
        transaction_id (int): The Chargify id of the original payment

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time',
        "payment_method": 'payment_method',
        "transaction_id": 'transaction_id'
    }

    _optionals = [
        'transaction_id',
    ]

    def __init__(self,
                 memo=None,
                 original_amount=None,
                 applied_amount=None,
                 transaction_time=None,
                 payment_method=None,
                 transaction_id=APIHelper.SKIP):
        """Constructor for the ApplyPaymentEventData class"""

        # Initialize members of the class
        self.memo = memo 
        self.original_amount = original_amount 
        self.applied_amount = applied_amount 
        self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        self.payment_method = payment_method 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 

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
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else None
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else None
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else None
        payment_method = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ApplyPaymentEventDataPaymentMethod'), dictionary.get('payment_method'), False) if dictionary.get('payment_method') is not None else None
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(memo,
                   original_amount,
                   applied_amount,
                   transaction_time,
                   payment_method,
                   transaction_id)

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.memo, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.original_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.transaction_time, type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and UnionTypeLookUp.get('ApplyPaymentEventDataPaymentMethod').validate(dictionary.payment_method)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('memo'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('original_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_time'), type_callable=lambda value: isinstance(value, str)) \
            and UnionTypeLookUp.get('ApplyPaymentEventDataPaymentMethod').validate(dictionary.get('payment_method'))
