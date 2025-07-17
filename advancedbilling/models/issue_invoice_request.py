# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class IssueInvoiceRequest(object):

    """Implementation of the 'Issue Invoice Request' model.

    Attributes:
        on_failed_payment (FailedPaymentAction): Action taken when payment for
            an invoice fails: - `leave_open_invoice` - prepayments and credits
            applied to invoice; invoice status set to "open"; email sent to
            the customer for the issued invoice (if setting applies); payment
            failure recorded in the invoice history. This is the default
            option. - `rollback_to_pending` - prepayments and credits not
            applied; invoice remains in "pending" status; no email sent to the
            customer; payment failure recorded in the invoice history. -
            `initiate_dunning` - prepayments and credits applied to the
            invoice; invoice status set to "open"; email sent to the customer
            for the issued invoice (if setting applies); payment failure
            recorded in the invoice history; subscription will  most likely go
            into "past_due" or "canceled" state (depending upon net terms and
            dunning settings).
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "on_failed_payment": 'on_failed_payment'
    }

    _optionals = [
        'on_failed_payment',
    ]

    def __init__(self,
                 on_failed_payment='leave_open_invoice',
                 additional_properties=None):
        """Constructor for the IssueInvoiceRequest class"""

        # Initialize members of the class
        self.on_failed_payment = on_failed_payment 

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
        on_failed_payment = dictionary.get("on_failed_payment") if dictionary.get("on_failed_payment") else 'leave_open_invoice'
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(on_failed_payment,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'on_failed_payment={(self.on_failed_payment if hasattr(self, "on_failed_payment") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'on_failed_payment={(self.on_failed_payment if hasattr(self, "on_failed_payment") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
