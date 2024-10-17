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

    TODO: type model description here.

    Attributes:
        transaction_time (datetime): TODO: type description here.
        memo (str): TODO: type description here.
        original_amount (str): TODO: type description here.
        applied_amount (str): TODO: type description here.
        payment_method (InvoicePaymentMethod): TODO: type description here.
        transaction_id (int): TODO: type description here.
        prepayment (bool): TODO: type description here.
        gateway_handle (str): TODO: type description here.
        gateway_used (str): TODO: type description here.
        gateway_transaction_id (str): The transaction ID for the payment as
            returned from the payment gateway
        received_on (date): Date reflecting when the payment was received from
            a customer. Must be in the past. Applicable only to  `external`
            payments.
        uid (str): TODO: type description here.

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
                 additional_properties={}):
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
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
