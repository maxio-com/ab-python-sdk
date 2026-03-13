"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class CreatePayment(object):
    """Implementation of the 'Create Payment' model.

    Attributes:
        amount (str): The model property of type str.
        memo (str): The model property of type str.
        payment_details (str): The model property of type str.
        payment_method (InvoicePaymentMethodType): The type of payment method used.
            Defaults to other.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": "amount",
        "memo": "memo",
        "payment_details": "payment_details",
        "payment_method": "payment_method",
    }

    def __init__(
        self,
        amount=None,
        memo=None,
        payment_details=None,
        payment_method=None,
        additional_properties=None):
        """Initialize a CreatePayment instance."""
        # Initialize members of the class
        self.amount = amount
        self.memo = memo
        self.payment_details = payment_details
        self.payment_method = payment_method

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

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
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else None
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else None
        payment_details =\
            dictionary.get("payment_details")\
            if dictionary.get("payment_details")\
                else None
        payment_method =\
            dictionary.get("payment_method")\
            if dictionary.get("payment_method")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(amount,
                   memo,
                   payment_details,
                   payment_method,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _amount=self.amount
        _memo=self.memo
        _payment_details=self.payment_details
        _payment_method=self.payment_method
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!r}, "
            f"memo={_memo!r}, "
            f"payment_details={_payment_details!r}, "
            f"payment_method={_payment_method!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _amount=self.amount
        _memo=self.memo
        _payment_details=self.payment_details
        _payment_method=self.payment_method
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!s}, "
            f"memo={_memo!s}, "
            f"payment_details={_payment_details!s}, "
            f"payment_method={_payment_method!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
