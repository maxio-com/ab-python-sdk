# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_invoice_payment_application import CreateInvoicePaymentApplication


class CreateMultiInvoicePayment(object):

    """Implementation of the 'Create Multi Invoice Payment' model.

    TODO: type model description here.

    Attributes:
        memo (str): A description to be attached to the payment.
        details (str): Additional information related to the payment method
            (eg. Check #).
        method (InvoicePaymentMethodType): The type of payment method used.
        amount (str | float): Dollar amount of the sum of the invoices payment
            (eg. "10.50" => $10.50).
        received_on (str): Date reflecting when the payment was received from
            a customer. Must be in the past.
        applications (List[CreateInvoicePaymentApplication]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "applications": 'applications',
        "memo": 'memo',
        "details": 'details',
        "method": 'method',
        "received_on": 'received_on'
    }

    _optionals = [
        'memo',
        'details',
        'method',
        'received_on',
    ]

    def __init__(self,
                 amount=None,
                 applications=None,
                 memo=APIHelper.SKIP,
                 details=APIHelper.SKIP,
                 method='other',
                 received_on=APIHelper.SKIP):
        """Constructor for the CreateMultiInvoicePayment class"""

        # Initialize members of the class
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if details is not APIHelper.SKIP:
            self.details = details 
        self.method = method 
        self.amount = amount 
        if received_on is not APIHelper.SKIP:
            self.received_on = received_on 
        self.applications = applications 

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
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateMultiInvoicePaymentAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else None
        applications = None
        if dictionary.get('applications') is not None:
            applications = [CreateInvoicePaymentApplication.from_dictionary(x) for x in dictionary.get('applications')]
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        method = dictionary.get("method") if dictionary.get("method") else 'other'
        received_on = dictionary.get("received_on") if dictionary.get("received_on") else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   applications,
                   memo,
                   details,
                   method,
                   received_on)

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
            return UnionTypeLookUp.get('CreateMultiInvoicePaymentAmount').validate(dictionary.amount) \
                and APIHelper.is_valid_type(value=dictionary.applications, type_callable=lambda value: CreateInvoicePaymentApplication.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return UnionTypeLookUp.get('CreateMultiInvoicePaymentAmount').validate(dictionary.get('amount')) \
            and APIHelper.is_valid_type(value=dictionary.get('applications'), type_callable=lambda value: CreateInvoicePaymentApplication.validate(value))
