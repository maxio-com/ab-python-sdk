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
        payment_method (PaymentMethodApplePayType |
            PaymentMethodBankAccountType | PaymentMethodCreditCardType |
            PaymentMethodExternalType | PaymentMethodPaypalType | None): A
            nested data structure detailing the method of payment
        prepayment (bool): The flag that shows whether the original payment
            was a prepayment or not

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_id": 'transaction_id',
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "transaction_time": 'transaction_time',
        "payment_method": 'payment_method',
        "prepayment": 'prepayment'
    }

    _optionals = [
        'transaction_id',
        'memo',
        'original_amount',
        'applied_amount',
        'transaction_time',
        'payment_method',
        'prepayment',
    ]

    def __init__(self,
                 transaction_id=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 transaction_time=APIHelper.SKIP,
                 payment_method=APIHelper.SKIP,
                 prepayment=APIHelper.SKIP):
        """Constructor for the RemovePaymentEventData class"""

        # Initialize members of the class
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        if payment_method is not APIHelper.SKIP:
            self.payment_method = payment_method 
        if prepayment is not APIHelper.SKIP:
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
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        payment_method = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RemovePaymentEventDataPaymentMethod'), dictionary.get('payment_method'), False) if dictionary.get('payment_method') is not None else APIHelper.SKIP
        prepayment = dictionary.get("prepayment") if "prepayment" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(transaction_id,
                   memo,
                   original_amount,
                   applied_amount,
                   transaction_time,
                   payment_method,
                   prepayment)

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
