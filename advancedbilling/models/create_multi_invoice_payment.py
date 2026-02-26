"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_invoice_payment_application import (
    CreateInvoicePaymentApplication,
)


class CreateMultiInvoicePayment(object):
    """Implementation of the 'Create Multi Invoice Payment' model.

    Attributes:
        memo (str): A description to be attached to the payment.
        details (str): Additional information related to the payment method (eg.
            Check #).
        method (InvoicePaymentMethodType): The type of payment method used. Defaults
            to other.
        amount (str | float): Dollar amount of the sum of the invoices payment (eg.
            "10.50" => $10.50).
        received_on (str): Date reflecting when the payment was received from a
            customer. Must be in the past.
        applications (List[CreateInvoicePaymentApplication]): The model property of
            type List[CreateInvoicePaymentApplication].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": "amount",
        "applications": "applications",
        "memo": "memo",
        "details": "details",
        "method": "method",
        "received_on": "received_on",
    }

    _optionals = [
        "memo",
        "details",
        "method",
        "received_on",
    ]

    def __init__(
        self,
        amount=None,
        applications=None,
        memo=APIHelper.SKIP,
        details=APIHelper.SKIP,
        method=APIHelper.SKIP,
        received_on=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CreateMultiInvoicePayment instance."""
        # Initialize members of the class
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if details is not APIHelper.SKIP:
            self.details = details
        if method is not APIHelper.SKIP:
            self.method = method
        self.amount = amount
        if received_on is not APIHelper.SKIP:
            self.received_on = received_on
        self.applications = applications

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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        amount = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("CreateMultiInvoicePaymentAmount"),
            dictionary.get("amount"),
            False)\
            if dictionary.get("amount") is not None\
            else None
        applications = None
        if dictionary.get("applications") is not None:
            applications = [
                CreateInvoicePaymentApplication.from_dictionary(x)
                    for x in dictionary.get("applications")
            ]
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else APIHelper.SKIP
        details =\
            dictionary.get("details")\
            if dictionary.get("details")\
                else APIHelper.SKIP
        method =\
            dictionary.get("method")\
            if dictionary.get("method")\
                else APIHelper.SKIP
        received_on =\
            dictionary.get("received_on")\
            if dictionary.get("received_on")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(amount,
                   applications,
                   memo,
                   details,
                   method,
                   received_on,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if isinstance(dictionary, cls):
            return (UnionTypeLookUp.get("CreateMultiInvoicePaymentAmount")
                .validate(dictionary.amount).is_valid) \
                and APIHelper.is_valid_type(
                    value=dictionary.applications,
                    type_callable=lambda value:
                        CreateInvoicePaymentApplication.validate(value),
                    is_model_dict=True,
                    is_inner_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return (UnionTypeLookUp.get("CreateMultiInvoicePaymentAmount")
            .validate(dictionary.get("amount")).is_valid) \
            and APIHelper.is_valid_type(
                value=dictionary.get("applications"),
                type_callable=lambda value:
                    CreateInvoicePaymentApplication.validate(value),
                is_model_dict=True,
                is_inner_model_dict=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _details=(
            self.details
            if hasattr(self, "details")
            else None
        )
        _method=(
            self.method
            if hasattr(self, "method")
            else None
        )
        _amount=self.amount
        _received_on=(
            self.received_on
            if hasattr(self, "received_on")
            else None
        )
        _applications=self.applications
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"memo={_memo!r}, "
            f"details={_details!r}, "
            f"method={_method!r}, "
            f"amount={_amount!r}, "
            f"received_on={_received_on!r}, "
            f"applications={_applications!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _details=(
            self.details
            if hasattr(self, "details")
            else None
        )
        _method=(
            self.method
            if hasattr(self, "method")
            else None
        )
        _amount=self.amount
        _received_on=(
            self.received_on
            if hasattr(self, "received_on")
            else None
        )
        _applications=self.applications
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"memo={_memo!s}, "
            f"details={_details!s}, "
            f"method={_method!s}, "
            f"amount={_amount!s}, "
            f"received_on={_received_on!s}, "
            f"applications={_applications!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
