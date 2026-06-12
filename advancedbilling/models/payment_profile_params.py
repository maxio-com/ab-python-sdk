"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class PaymentProfileParams(object):
    """Implementation of the 'PaymentProfileParams' model.

    PCI-safe cardholder fields only. Full card numbers, CVV, and billing address are
    never included.

    Attributes:
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        card_type (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": "first_name",
        "last_name": "last_name",
        "card_type": "card_type",
    }

    _optionals = [
        "first_name",
        "last_name",
        "card_type",
    ]

    def __init__(
        self,
        first_name=APIHelper.SKIP,
        last_name=APIHelper.SKIP,
        card_type=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a PaymentProfileParams instance."""
        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name
        if card_type is not APIHelper.SKIP:
            self.card_type = card_type

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
        first_name =\
            dictionary.get("first_name")\
            if dictionary.get("first_name")\
                else APIHelper.SKIP
        last_name =\
            dictionary.get("last_name")\
            if dictionary.get("last_name")\
                else APIHelper.SKIP
        card_type =\
            dictionary.get("card_type")\
            if dictionary.get("card_type")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   card_type,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _first_name=(
            self.first_name
            if hasattr(self, "first_name")
            else None
        )
        _last_name=(
            self.last_name
            if hasattr(self, "last_name")
            else None
        )
        _card_type=(
            self.card_type
            if hasattr(self, "card_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"first_name={_first_name!r}, "
            f"last_name={_last_name!r}, "
            f"card_type={_card_type!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _first_name=(
            self.first_name
            if hasattr(self, "first_name")
            else None
        )
        _last_name=(
            self.last_name
            if hasattr(self, "last_name")
            else None
        )
        _card_type=(
            self.card_type
            if hasattr(self, "card_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"first_name={_first_name!s}, "
            f"last_name={_last_name!s}, "
            f"card_type={_card_type!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
