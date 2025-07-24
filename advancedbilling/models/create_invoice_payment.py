# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class CreateInvoicePayment(object):

    """Implementation of the 'Create Invoice Payment' model.

    Attributes:
        amount (str | float | None): A string of the dollar amount to be
            refunded (eg. "10.50" => $10.50)
        memo (str): A description to be attached to the payment. Applicable
            only to `external` payments.
        method (InvoicePaymentMethodType): The type of payment method used.
            Defaults to other.
        details (str): Additional information related to the payment method
            (eg. Check #). Applicable only to `external` payments.
        payment_profile_id (int): The ID of the payment profile to be used for
            the payment.
        received_on (date): Date reflecting when the payment was received from
            a customer. Must be in the past. Applicable only to  `external`
            payments.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo',
        "method": 'method',
        "details": 'details',
        "payment_profile_id": 'payment_profile_id',
        "received_on": 'received_on'
    }

    _optionals = [
        'amount',
        'memo',
        'method',
        'details',
        'payment_profile_id',
        'received_on',
    ]

    def __init__(self,
                 amount=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 method=APIHelper.SKIP,
                 details=APIHelper.SKIP,
                 payment_profile_id=APIHelper.SKIP,
                 received_on=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateInvoicePayment class"""

        # Initialize members of the class
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if method is not APIHelper.SKIP:
            self.method = method 
        if details is not APIHelper.SKIP:
            self.details = details 
        if payment_profile_id is not APIHelper.SKIP:
            self.payment_profile_id = payment_profile_id 
        if received_on is not APIHelper.SKIP:
            self.received_on = received_on 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoicePaymentAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        method = dictionary.get("method") if dictionary.get("method") else APIHelper.SKIP
        details = dictionary.get("details") if dictionary.get("details") else APIHelper.SKIP
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else APIHelper.SKIP
        received_on = dateutil.parser.parse(dictionary.get('received_on')).date() if dictionary.get('received_on') else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount,
                   memo,
                   method,
                   details,
                   payment_profile_id,
                   received_on,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'method={(self.method if hasattr(self, "method") else None)!r}, '
                f'details={(self.details if hasattr(self, "details") else None)!r}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!r}, '
                f'received_on={(self.received_on if hasattr(self, "received_on") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'method={(self.method if hasattr(self, "method") else None)!s}, '
                f'details={(self.details if hasattr(self, "details") else None)!s}, '
                f'payment_profile_id={(self.payment_profile_id if hasattr(self, "payment_profile_id") else None)!s}, '
                f'received_on={(self.received_on if hasattr(self, "received_on") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
