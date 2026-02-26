"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ListSubscriptionComponentsFilter(object):
    """Implementation of the 'List Subscription Components Filter' model.

    Attributes:
        currencies (List[str]): Allows fetching components allocation with matching
            currency based on provided values. Use in query
            `filter[currencies]=EUR,USD`.
        use_site_exchange_rate (bool): Allows fetching components allocation with
            matching use_site_exchange_rate based on provided value. Use in query
            `filter[use_site_exchange_rate]=true`.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currencies": "currencies",
        "use_site_exchange_rate": "use_site_exchange_rate",
    }

    _optionals = [
        "currencies",
        "use_site_exchange_rate",
    ]

    def __init__(
        self,
        currencies=APIHelper.SKIP,
        use_site_exchange_rate=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ListSubscriptionComponentsFilter instance."""
        # Initialize members of the class
        if currencies is not APIHelper.SKIP:
            self.currencies = currencies
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate

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
        currencies =\
            dictionary.get("currencies")\
            if dictionary.get("currencies")\
                else APIHelper.SKIP
        use_site_exchange_rate =\
            dictionary.get("use_site_exchange_rate")\
            if "use_site_exchange_rate" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(currencies,
                   use_site_exchange_rate,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _currencies=(
            self.currencies
            if hasattr(self, "currencies")
            else None
        )
        _use_site_exchange_rate=(
            self.use_site_exchange_rate
            if hasattr(self, "use_site_exchange_rate")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currencies={_currencies!r}, "
            f"use_site_exchange_rate={_use_site_exchange_rate!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _currencies=(
            self.currencies
            if hasattr(self, "currencies")
            else None
        )
        _use_site_exchange_rate=(
            self.use_site_exchange_rate
            if hasattr(self, "use_site_exchange_rate")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"currencies={_currencies!s}, "
            f"use_site_exchange_rate={_use_site_exchange_rate!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
