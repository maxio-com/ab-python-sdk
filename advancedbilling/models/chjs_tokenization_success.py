"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.tokenized_payment_profile import (
    TokenizedPaymentProfile,
)


class ChjsTokenizationSuccess(object):
    """Implementation of the 'Chjs Tokenization Success' model.

    Attributes:
        payment_profile (TokenizedPaymentProfile): The model property of type
            TokenizedPaymentProfile.
        gateway_customer_id (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_profile": "payment_profile",
        "gateway_customer_id": "gateway_customer_id",
    }

    _optionals = [
        "gateway_customer_id",
    ]

    _nullables = [
        "gateway_customer_id",
    ]

    def __init__(
        self,
        payment_profile=None,
        gateway_customer_id=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChjsTokenizationSuccess instance."""
        # Initialize members of the class
        self.payment_profile = payment_profile
        if gateway_customer_id is not APIHelper.SKIP:
            self.gateway_customer_id = gateway_customer_id

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
        payment_profile =\
            TokenizedPaymentProfile.from_dictionary(
                dictionary.get("payment_profile"))\
                if dictionary.get("payment_profile") else None
        gateway_customer_id =\
            dictionary.get("gateway_customer_id")\
            if "gateway_customer_id" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(payment_profile,
                   gateway_customer_id,
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
                    value=dictionary.payment_profile,
                    type_callable=lambda value:
                        TokenizedPaymentProfile.validate(value),
                    is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("payment_profile"),
                type_callable=lambda value:
                    TokenizedPaymentProfile.validate(value),
                is_model_dict=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _payment_profile=self.payment_profile
        _gateway_customer_id=(
            self.gateway_customer_id
            if hasattr(self, "gateway_customer_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_profile={_payment_profile!r}, "
            f"gateway_customer_id={_gateway_customer_id!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _payment_profile=self.payment_profile
        _gateway_customer_id=(
            self.gateway_customer_id
            if hasattr(self, "gateway_customer_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"payment_profile={_payment_profile!s}, "
            f"gateway_customer_id={_gateway_customer_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
