# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RefundInvoice(object):

    """Implementation of the 'Refund Invoice' model.

    Refund an invoice or a segment of a consolidated invoice.

    Attributes:
        amount (str): The amount to be refunded in decimal format as a string.
            Example: "10.50". Must not exceed the remaining refundable balance
            of the payment.
        memo (str): A description that will be attached to the refund
        payment_id (int): The ID of the payment to be refunded
        external (bool): Flag that marks refund as external (no money is
            returned to the customer). Defaults to `false`.
        apply_credit (bool): If set to true, creates credit and applies it to
            an invoice. Defaults to `false`.
        void_invoice (bool): If `apply_credit` set to false and refunding full
            amount, if `void_invoice` set to true, invoice will be voided
            after refund. Defaults to `false`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "memo": 'memo',
        "payment_id": 'payment_id',
        "external": 'external',
        "apply_credit": 'apply_credit',
        "void_invoice": 'void_invoice'
    }

    _optionals = [
        'external',
        'apply_credit',
        'void_invoice',
    ]

    def __init__(self,
                 amount=None,
                 memo=None,
                 payment_id=None,
                 external=APIHelper.SKIP,
                 apply_credit=APIHelper.SKIP,
                 void_invoice=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the RefundInvoice class"""

        # Initialize members of the class
        self.amount = amount 
        self.memo = memo 
        self.payment_id = payment_id 
        if external is not APIHelper.SKIP:
            self.external = external 
        if apply_credit is not APIHelper.SKIP:
            self.apply_credit = apply_credit 
        if void_invoice is not APIHelper.SKIP:
            self.void_invoice = void_invoice 

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
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        payment_id = dictionary.get("payment_id") if dictionary.get("payment_id") else None
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        apply_credit = dictionary.get("apply_credit") if "apply_credit" in dictionary.keys() else APIHelper.SKIP
        void_invoice = dictionary.get("void_invoice") if "void_invoice" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount,
                   memo,
                   payment_id,
                   external,
                   apply_credit,
                   void_invoice,
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
            return APIHelper.is_valid_type(value=dictionary.amount,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.memo,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.payment_id,
                                            type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('amount'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_id'),
                                        type_callable=lambda value: isinstance(value, int))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount={self.amount!r}, '
                f'memo={self.memo!r}, '
                f'payment_id={self.payment_id!r}, '
                f'external={(self.external if hasattr(self, "external") else None)!r}, '
                f'apply_credit={(self.apply_credit if hasattr(self, "apply_credit") else None)!r}, '
                f'void_invoice={(self.void_invoice if hasattr(self, "void_invoice") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount={self.amount!s}, '
                f'memo={self.memo!s}, '
                f'payment_id={self.payment_id!s}, '
                f'external={(self.external if hasattr(self, "external") else None)!s}, '
                f'apply_credit={(self.apply_credit if hasattr(self, "apply_credit") else None)!s}, '
                f'void_invoice={(self.void_invoice if hasattr(self, "void_invoice") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
