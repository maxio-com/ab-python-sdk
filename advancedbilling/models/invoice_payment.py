# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_payment_method import InvoicePaymentMethod


class InvoicePayment(object):

    """Implementation of the 'Invoice Payment' model.

    Attributes:
        transaction_time (datetime): The model property of type datetime.
        memo (str): The model property of type str.
        original_amount (str): The model property of type str.
        applied_amount (str): The model property of type str.
        payment_method (InvoicePaymentMethod): The model property of type
            InvoicePaymentMethod.
        transaction_id (int): The model property of type int.
        prepayment (bool): The model property of type bool.
        gateway_handle (str): The model property of type str.
        gateway_used (str): The model property of type str.
        gateway_transaction_id (str): The transaction ID for the payment as
            returned from the payment gateway
        received_on (date): Date reflecting when the payment was received from
            a customer. Must be in the past. Applicable only to  `external`
            payments.
        uid (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_time": 'transaction_time',
        "memo": 'memo',
        "original_amount": 'original_amount',
        "applied_amount": 'applied_amount',
        "payment_method": 'payment_method',
        "transaction_id": 'transaction_id',
        "prepayment": 'prepayment',
        "gateway_handle": 'gateway_handle',
        "gateway_used": 'gateway_used',
        "gateway_transaction_id": 'gateway_transaction_id',
        "received_on": 'received_on',
        "uid": 'uid'
    }

    _optionals = [
        'transaction_time',
        'memo',
        'original_amount',
        'applied_amount',
        'payment_method',
        'transaction_id',
        'prepayment',
        'gateway_handle',
        'gateway_used',
        'gateway_transaction_id',
        'received_on',
        'uid',
    ]

    _nullables = [
        'gateway_handle',
        'gateway_transaction_id',
        'received_on',
    ]

    def __init__(self,
                 transaction_time=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 original_amount=APIHelper.SKIP,
                 applied_amount=APIHelper.SKIP,
                 payment_method=APIHelper.SKIP,
                 transaction_id=APIHelper.SKIP,
                 prepayment=APIHelper.SKIP,
                 gateway_handle=APIHelper.SKIP,
                 gateway_used=APIHelper.SKIP,
                 gateway_transaction_id=APIHelper.SKIP,
                 received_on=APIHelper.SKIP,
                 uid=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoicePayment class"""

        # Initialize members of the class
        if transaction_time is not APIHelper.SKIP:
            self.transaction_time = APIHelper.apply_datetime_converter(transaction_time, APIHelper.RFC3339DateTime) if transaction_time else None 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if original_amount is not APIHelper.SKIP:
            self.original_amount = original_amount 
        if applied_amount is not APIHelper.SKIP:
            self.applied_amount = applied_amount 
        if payment_method is not APIHelper.SKIP:
            self.payment_method = payment_method 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if prepayment is not APIHelper.SKIP:
            self.prepayment = prepayment 
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle 
        if gateway_used is not APIHelper.SKIP:
            self.gateway_used = gateway_used 
        if gateway_transaction_id is not APIHelper.SKIP:
            self.gateway_transaction_id = gateway_transaction_id 
        if received_on is not APIHelper.SKIP:
            self.received_on = received_on 
        if uid is not APIHelper.SKIP:
            self.uid = uid 

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
        transaction_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_time")).datetime if dictionary.get("transaction_time") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        original_amount = dictionary.get("original_amount") if dictionary.get("original_amount") else APIHelper.SKIP
        applied_amount = dictionary.get("applied_amount") if dictionary.get("applied_amount") else APIHelper.SKIP
        payment_method = InvoicePaymentMethod.from_dictionary(dictionary.get('payment_method')) if 'payment_method' in dictionary.keys() else APIHelper.SKIP
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        prepayment = dictionary.get("prepayment") if "prepayment" in dictionary.keys() else APIHelper.SKIP
        gateway_handle = dictionary.get("gateway_handle") if "gateway_handle" in dictionary.keys() else APIHelper.SKIP
        gateway_used = dictionary.get("gateway_used") if dictionary.get("gateway_used") else APIHelper.SKIP
        gateway_transaction_id = dictionary.get("gateway_transaction_id") if "gateway_transaction_id" in dictionary.keys() else APIHelper.SKIP
        if 'received_on' in dictionary.keys():
            received_on = dateutil.parser.parse(dictionary.get('received_on')).date() if dictionary.get('received_on') else None
        else:
            received_on = APIHelper.SKIP
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(transaction_time,
                   memo,
                   original_amount,
                   applied_amount,
                   payment_method,
                   transaction_id,
                   prepayment,
                   gateway_handle,
                   gateway_used,
                   gateway_transaction_id,
                   received_on,
                   uid,
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
                f'transaction_time={(self.transaction_time if hasattr(self, "transaction_time") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'original_amount={(self.original_amount if hasattr(self, "original_amount") else None)!r}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!r}, '
                f'payment_method={(self.payment_method if hasattr(self, "payment_method") else None)!r}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!r}, '
                f'prepayment={(self.prepayment if hasattr(self, "prepayment") else None)!r}, '
                f'gateway_handle={(self.gateway_handle if hasattr(self, "gateway_handle") else None)!r}, '
                f'gateway_used={(self.gateway_used if hasattr(self, "gateway_used") else None)!r}, '
                f'gateway_transaction_id={(self.gateway_transaction_id if hasattr(self, "gateway_transaction_id") else None)!r}, '
                f'received_on={(self.received_on if hasattr(self, "received_on") else None)!r}, '
                f'uid={(self.uid if hasattr(self, "uid") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_time={(self.transaction_time if hasattr(self, "transaction_time") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'original_amount={(self.original_amount if hasattr(self, "original_amount") else None)!s}, '
                f'applied_amount={(self.applied_amount if hasattr(self, "applied_amount") else None)!s}, '
                f'payment_method={(self.payment_method if hasattr(self, "payment_method") else None)!s}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!s}, '
                f'prepayment={(self.prepayment if hasattr(self, "prepayment") else None)!s}, '
                f'gateway_handle={(self.gateway_handle if hasattr(self, "gateway_handle") else None)!s}, '
                f'gateway_used={(self.gateway_used if hasattr(self, "gateway_used") else None)!s}, '
                f'gateway_transaction_id={(self.gateway_transaction_id if hasattr(self, "gateway_transaction_id") else None)!s}, '
                f'received_on={(self.received_on if hasattr(self, "received_on") else None)!s}, '
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
