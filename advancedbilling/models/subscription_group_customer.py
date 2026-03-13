"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupCustomer(object):
    """Implementation of the 'Subscription Group Customer' model.

    Attributes:
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        organization (str): The model property of type str.
        email (str): The model property of type str.
        reference (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": "first_name",
        "last_name": "last_name",
        "organization": "organization",
        "email": "email",
        "reference": "reference",
    }

    _optionals = [
        "first_name",
        "last_name",
        "organization",
        "email",
        "reference",
    ]

    def __init__(
        self,
        first_name=APIHelper.SKIP,
        last_name=APIHelper.SKIP,
        organization=APIHelper.SKIP,
        email=APIHelper.SKIP,
        reference=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionGroupCustomer instance."""
        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name
        if organization is not APIHelper.SKIP:
            self.organization = organization
        if email is not APIHelper.SKIP:
            self.email = email
        if reference is not APIHelper.SKIP:
            self.reference = reference

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
        organization =\
            dictionary.get("organization")\
            if dictionary.get("organization")\
                else APIHelper.SKIP
        email =\
            dictionary.get("email")\
            if dictionary.get("email")\
                else APIHelper.SKIP
        reference =\
            dictionary.get("reference")\
            if dictionary.get("reference")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   organization,
                   email,
                   reference,
                   additional_properties)

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
        _organization=(
            self.organization
            if hasattr(self, "organization")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _reference=(
            self.reference
            if hasattr(self, "reference")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"first_name={_first_name!r}, "
            f"last_name={_last_name!r}, "
            f"organization={_organization!r}, "
            f"email={_email!r}, "
            f"reference={_reference!r}, "
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
        _organization=(
            self.organization
            if hasattr(self, "organization")
            else None
        )
        _email=(
            self.email
            if hasattr(self, "email")
            else None
        )
        _reference=(
            self.reference
            if hasattr(self, "reference")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"first_name={_first_name!s}, "
            f"last_name={_last_name!s}, "
            f"organization={_organization!s}, "
            f"email={_email!s}, "
            f"reference={_reference!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
