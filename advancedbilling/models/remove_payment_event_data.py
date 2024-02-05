# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RemovePaymentEventData(object):

    """Implementation of the 'Remove Payment Event Data' model.

    Example schema for an `remove_payment` event

    Attributes:
        transaction_id (int): Transaction ID of the original payment that was
            removed
        memo (str): Memo of the original payment
        original_amount (str): Full amount of the original payment
        applied_amount (str): Applied amount of the original payment
        transaction_time (datetime): Transaction time of the original payment,
            in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
        payment_method (PaymentMethodApplePay | PaymentMethodBankAccount |
            PaymentMethodCreditCard | PaymentMethodExternal |
            PaymentMethodPaypal): A nested data structure detailing the method
            of payment
        prepayment (bool): The flag that shows whether the original payment
            was a prepayment or not

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_id": 'transaction_id',
        "memo": 'memo',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time',
        "payment_method": 'payment_method',
        "prepayment": 'prepayment',
        "original_amount": 'original_amount'
    }

    _optionals = [
        'original_amount',
    ]

    def __init__(self,
                 transaction_id=None,
                 memo=None,
                 applied_amount=None,
                 transaction_time=None,
                 payment_method=None,
                 prepayment=None,
                 original_amount=APIHelper.SKIP):
        """Constructor for the RemovePaymentEventData class"""

        # Initialize members of the class
        self.transaction_id = transaction_id 
        self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        self.applied_amount = applied_amount 
        self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        self.payment_method = payment_method 
        self.prepayment = prepayment 

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
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else None
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else None
        payment_method = APIHelper.deserialize_union_type(UnionTypeLookUp.get('Invoice-Event-Payment'), dictionary.get('payment_method'), False) if dictionary.get('payment_method') is not None else None
        prepayment = dictionary.get("prepayment") if "prepayment" in dictionary.keys() else None
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(transaction_id,
                   memo,
                   applied_amount,
                   transaction_time,
                   payment_method,
                   prepayment,
                   original_amount)

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
            return APIHelper.is_valid_type(value=dictionary.transaction_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.memo, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.applied_amount, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.transaction_time, type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and UnionTypeLookUp.get('Invoice-Event-Payment').validate(dictionary.payment_method).is_valid \
                and APIHelper.is_valid_type(value=dictionary.prepayment, type_callable=lambda value: isinstance(value, bool))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('transaction_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('applied_amount'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('transaction_time'), type_callable=lambda value: isinstance(value, str)) \
            and UnionTypeLookUp.get('Invoice-Event-Payment').validate(dictionary.get('payment_method')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('prepayment'), type_callable=lambda value: isinstance(value, bool))
