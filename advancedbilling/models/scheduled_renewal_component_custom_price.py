"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import (
    PricingScheme,
)


class ScheduledRenewalComponentCustomPrice(object):
    """Implementation of the 'Scheduled Renewal Component Custom Price' model.

    Custom pricing for a component within a scheduled renewal.

    Attributes:
        tax_included (bool): Whether or not the price point includes tax
        pricing_scheme (PricingScheme): Omit for On/Off components
        prices (List[Price]): On/off components only need one price bracket starting
            at 1.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": "pricing_scheme",
        "prices": "prices",
        "tax_included": "tax_included",
    }

    _optionals = [
        "tax_included",
    ]

    def __init__(
        self,
        pricing_scheme=None,
        prices=None,
        tax_included=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ScheduledRenewalComponentCustomPrice instance."""
        # Initialize members of the class
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included
        self.pricing_scheme = pricing_scheme
        self.prices = prices

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
        pricing_scheme =\
            dictionary.get("pricing_scheme")\
            if dictionary.get("pricing_scheme")\
                else None
        prices = None
        if dictionary.get("prices") is not None:
            prices = [
                Price.from_dictionary(x)
                    for x in dictionary.get("prices")
            ]
        tax_included =\
            dictionary.get("tax_included")\
            if "tax_included" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(pricing_scheme,
                   prices,
                   tax_included,
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
                    value=dictionary.pricing_scheme,
                    type_callable=lambda value:
                        PricingScheme.validate(value)) \
                and APIHelper.is_valid_type(
                    value=dictionary.prices,
                    type_callable=lambda value:
                        Price.validate(value),
                    is_model_dict=True,
                    is_inner_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("pricing_scheme"),
                type_callable=lambda value:
                    PricingScheme.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("prices"),
                type_callable=lambda value:
                    Price.validate(value),
                is_model_dict=True,
                is_inner_model_dict=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _tax_included=(
            self.tax_included
            if hasattr(self, "tax_included")
            else None
        )
        _pricing_scheme=self.pricing_scheme
        _prices=self.prices
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"tax_included={_tax_included!r}, "
            f"pricing_scheme={_pricing_scheme!r}, "
            f"prices={_prices!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _tax_included=(
            self.tax_included
            if hasattr(self, "tax_included")
            else None
        )
        _pricing_scheme=self.pricing_scheme
        _prices=self.prices
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"tax_included={_tax_included!s}, "
            f"pricing_scheme={_pricing_scheme!s}, "
            f"prices={_prices!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
