"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class SaleRepItemMrr(object):
    """Implementation of the 'Sale Rep Item Mrr' model.

    Attributes:
        mrr (str): The model property of type str.
        usage (str): The model property of type str.
        recurring (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mrr": "mrr",
        "usage": "usage",
        "recurring": "recurring",
    }

    _optionals = [
        "mrr",
        "usage",
        "recurring",
    ]

    def __init__(
        self,
        mrr=APIHelper.SKIP,
        usage=APIHelper.SKIP,
        recurring=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SaleRepItemMrr instance."""
        # Initialize members of the class
        if mrr is not APIHelper.SKIP:
            self.mrr = mrr
        if usage is not APIHelper.SKIP:
            self.usage = usage
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring

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
        mrr =\
            dictionary.get("mrr")\
            if dictionary.get("mrr")\
                else APIHelper.SKIP
        usage =\
            dictionary.get("usage")\
            if dictionary.get("usage")\
                else APIHelper.SKIP
        recurring =\
            dictionary.get("recurring")\
            if dictionary.get("recurring")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(mrr,
                   usage,
                   recurring,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _mrr=(
            self.mrr
            if hasattr(self, "mrr")
            else None
        )
        _usage=(
            self.usage
            if hasattr(self, "usage")
            else None
        )
        _recurring=(
            self.recurring
            if hasattr(self, "recurring")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mrr={_mrr!r}, "
            f"usage={_usage!r}, "
            f"recurring={_recurring!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _mrr=(
            self.mrr
            if hasattr(self, "mrr")
            else None
        )
        _usage=(
            self.usage
            if hasattr(self, "usage")
            else None
        )
        _recurring=(
            self.recurring
            if hasattr(self, "recurring")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mrr={_mrr!s}, "
            f"usage={_usage!s}, "
            f"recurring={_recurring!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
