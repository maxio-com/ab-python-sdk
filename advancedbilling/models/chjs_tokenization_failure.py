"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payment_profile_params import (
    PaymentProfileParams,
)


class ChjsTokenizationFailure(object):
    """Implementation of the 'Chjs Tokenization Failure' model.

    Attributes:
        errors (str): The model property of type str.
        payment_profile_params (PaymentProfileParams): PCI-safe cardholder fields
            only. Full card numbers, CVV, and billing address are never included.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "errors": "errors",
        "payment_profile_params": "payment_profile_params",
    }

    _optionals = [
        "payment_profile_params",
    ]

    def __init__(
        self,
        errors=None,
        payment_profile_params=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChjsTokenizationFailure instance."""
        # Initialize members of the class
        self.errors = errors
        if payment_profile_params is not APIHelper.SKIP:
            self.payment_profile_params = payment_profile_params

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
        errors =\
            dictionary.get("errors")\
            if dictionary.get("errors")\
                else None
        payment_profile_params =\
            PaymentProfileParams.from_dictionary(
                dictionary.get("payment_profile_params"))\
                if "payment_profile_params" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(errors,
                   payment_profile_params,
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
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                    value=dictionary.errors,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("errors"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _errors=self.errors
        _payment_profile_params=(
            self.payment_profile_params
            if hasattr(self, "payment_profile_params")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"errors={_errors!r}, "
            f"payment_profile_params={_payment_profile_params!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _errors=self.errors
        _payment_profile_params=(
            self.payment_profile_params
            if hasattr(self, "payment_profile_params")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"errors={_errors!s}, "
            f"payment_profile_params={_payment_profile_params!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
