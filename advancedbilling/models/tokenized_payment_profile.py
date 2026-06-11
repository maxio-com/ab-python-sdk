"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class TokenizedPaymentProfile(object):
    """Implementation of the 'Tokenized Payment Profile' model.

    Attributes:
        id (int): The model property of type int.
        vault_token (str): The model property of type str.
        gateway_handle (str): The model property of type str.
        customer_vault_token (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "vault_token": "vault_token",
        "gateway_handle": "gateway_handle",
        "customer_vault_token": "customer_vault_token",
    }

    _optionals = [
        "vault_token",
        "gateway_handle",
        "customer_vault_token",
    ]

    _nullables = [
        "gateway_handle",
        "customer_vault_token",
    ]

    def __init__(
        self,
        id=None,
        vault_token=APIHelper.SKIP,
        gateway_handle=APIHelper.SKIP,
        customer_vault_token=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenizedPaymentProfile instance."""
        # Initialize members of the class
        self.id = id
        if vault_token is not APIHelper.SKIP:
            self.vault_token = vault_token
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else None
        vault_token =\
            dictionary.get("vault_token")\
            if dictionary.get("vault_token")\
                else APIHelper.SKIP
        gateway_handle =\
            dictionary.get("gateway_handle")\
            if "gateway_handle" in dictionary.keys()\
                else APIHelper.SKIP
        customer_vault_token =\
            dictionary.get("customer_vault_token")\
            if "customer_vault_token" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   vault_token,
                   gateway_handle,
                   customer_vault_token,
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
                    value=dictionary.id,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        int,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("id"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    int,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=self.id
        _vault_token=(
            self.vault_token
            if hasattr(self, "vault_token")
            else None
        )
        _gateway_handle=(
            self.gateway_handle
            if hasattr(self, "gateway_handle")
            else None
        )
        _customer_vault_token=(
            self.customer_vault_token
            if hasattr(self, "customer_vault_token")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"vault_token={_vault_token!r}, "
            f"gateway_handle={_gateway_handle!r}, "
            f"customer_vault_token={_customer_vault_token!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=self.id
        _vault_token=(
            self.vault_token
            if hasattr(self, "vault_token")
            else None
        )
        _gateway_handle=(
            self.gateway_handle
            if hasattr(self, "gateway_handle")
            else None
        )
        _customer_vault_token=(
            self.customer_vault_token
            if hasattr(self, "customer_vault_token")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"vault_token={_vault_token!s}, "
            f"gateway_handle={_gateway_handle!s}, "
            f"customer_vault_token={_customer_vault_token!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
