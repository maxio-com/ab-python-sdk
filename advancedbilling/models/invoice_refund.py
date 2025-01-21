# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceRefund(object):

    """Implementation of the 'Invoice Refund' model.

    Attributes:
        transaction_id (int): The model property of type int.
        payment_id (int): The model property of type int.
        memo (str): The model property of type str.
        original_amount (str): The model property of type str.
        applied_amount (str): The model property of type str.
        gateway_transaction_id (str): The transaction ID for the refund as
            returned from the payment gateway
        gateway_used (str): The model property of type str.
        gateway_handle (str): The model property of type str.
        ach_late_reject (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_id": 'transaction_id',
        "payment_id": 'payment_id',
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "gateway_transaction_id": 'gateway_transaction_id',
        "gateway_used": 'gateway_used',
        "gateway_handle": 'gateway_handle',
        "ach_late_reject": 'ach_late_reject'
    }

    _optionals = [
        'transaction_id',
        'payment_id',
        'memo',
        'original_amount',
        'applied_amount',
        'gateway_transaction_id',
        'gateway_used',
        'gateway_handle',
        'ach_late_reject',
    ]

    _nullables = [
        'gateway_transaction_id',
        'gateway_handle',
        'ach_late_reject',
    ]

    def __init__(self,
                 transaction_id=APIHelper.SKIP,
                 payment_id=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 gateway_transaction_id=APIHelper.SKIP,
                 gateway_used=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 ach_late_reject=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceRefund class"""

        # Initialize members of the class
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if payment_id is not APIHelper.SKIP:
            self.payment_id = payment_id 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if gateway_transaction_id is not APIHelper.SKIP:
            self.gateway_transaction_id = gateway_transaction_id 
        if gateway_used is not APIHelper.SKIP:
            self.gateway_used = gateway_used 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 
        if ach_late_reject is not APIHelper.SKIP:
            self.ach_late_reject = ach_late_reject 

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
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        gateway_transaction_id = dictionary.get("gateway_transaction_id") if "gateway_transaction_id" in dictionary.keys() else APIHelper.SKIP
        gateway_used = dictionary.get("gateway_used") if dictionary.get("gateway_used") else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        ach_late_reject = dictionary.get("ach_late_reject") if "ach_late_reject" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(transaction_id,
                   payment_id,
                   memo,
                   original_amount,
                   applied_amount,
                   gateway_transaction_id,
                   gateway_used,
                   gateway_handle,
                   ach_late_reject,
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
                f'transaction_id={self.transaction_id!r}, '
                f'payment_id={self.payment_id!r}, '
                f'memo={self.memo!r}, '
                f'original_amount={self.original_amount!r}, '
                f'applied_amount={self.applied_amount!r}, '
                f'gateway_transaction_id={self.gateway_transaction_id!r}, '
                f'gateway_used={self.gateway_used!r}, '
                f'gateway_handle={self.gateway_handle!r}, '
                f'ach_late_reject={self.ach_late_reject!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_id={self.transaction_id!s}, '
                f'payment_id={self.payment_id!s}, '
                f'memo={self.memo!s}, '
                f'original_amount={self.original_amount!s}, '
                f'applied_amount={self.applied_amount!s}, '
                f'gateway_transaction_id={self.gateway_transaction_id!s}, '
                f'gateway_used={self.gateway_used!s}, '
                f'gateway_handle={self.gateway_handle!s}, '
                f'ach_late_reject={self.ach_late_reject!s}, '
                f'additional_properties={self.additional_properties!s})')
