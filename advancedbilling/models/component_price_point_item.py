"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.price import Price


class ComponentPricePointItem(object):
    """Implementation of the 'Component Price Point Item' model.

    Attributes:
        name (str): The model property of type str.
        handle (str): The model property of type str.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme. See
            [Product
            Components](https://help.chargify.com/products/product-components.html)
            for an overview of pricing schemes.
        interval (int): The numerical interval. i.e. an interval of ‘30’ coupled with
            an interval_unit of day would mean this component price point would renew
            every 30 days. This property is only available for sites with
            Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit for
            this component price point, either month or day. This property is only
            available for sites with Multifrequency enabled.
        prices (List[Price]): The model property of type List[Price].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "handle": "handle",
        "pricing_scheme": "pricing_scheme",
        "interval": "interval",
        "interval_unit": "interval_unit",
        "prices": "prices",
    }

    _optionals = [
        "name",
        "handle",
        "pricing_scheme",
        "interval",
        "interval_unit",
        "prices",
    ]

    _nullables = [
        "interval_unit",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        handle=APIHelper.SKIP,
        pricing_scheme=APIHelper.SKIP,
        interval=APIHelper.SKIP,
        interval_unit=APIHelper.SKIP,
        prices=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ComponentPricePointItem instance."""
        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if handle is not APIHelper.SKIP:
            self.handle = handle
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme
        if interval is not APIHelper.SKIP:
            self.interval = interval
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit
        if prices is not APIHelper.SKIP:
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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        handle =\
            dictionary.get("handle")\
            if dictionary.get("handle")\
                else APIHelper.SKIP
        pricing_scheme =\
            dictionary.get("pricing_scheme")\
            if dictionary.get("pricing_scheme")\
                else APIHelper.SKIP
        interval =\
            dictionary.get("interval")\
            if dictionary.get("interval")\
                else APIHelper.SKIP
        interval_unit =\
            dictionary.get("interval_unit")\
            if "interval_unit" in dictionary.keys()\
                else APIHelper.SKIP
        prices = None
        if dictionary.get("prices") is not None:
            prices = [
                Price.from_dictionary(x)
                    for x in dictionary.get("prices")
            ]
        else:
            prices = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(name,
                   handle,
                   pricing_scheme,
                   interval,
                   interval_unit,
                   prices,
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _pricing_scheme=(
            self.pricing_scheme
            if hasattr(self, "pricing_scheme")
            else None
        )
        _interval=(
            self.interval
            if hasattr(self, "interval")
            else None
        )
        _interval_unit=(
            self.interval_unit
            if hasattr(self, "interval_unit")
            else None
        )
        _prices=(
            self.prices
            if hasattr(self, "prices")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}, "
            f"handle={_handle!r}, "
            f"pricing_scheme={_pricing_scheme!r}, "
            f"interval={_interval!r}, "
            f"interval_unit={_interval_unit!r}, "
            f"prices={_prices!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _pricing_scheme=(
            self.pricing_scheme
            if hasattr(self, "pricing_scheme")
            else None
        )
        _interval=(
            self.interval
            if hasattr(self, "interval")
            else None
        )
        _interval_unit=(
            self.interval_unit
            if hasattr(self, "interval_unit")
            else None
        )
        _prices=(
            self.prices
            if hasattr(self, "prices")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}, "
            f"handle={_handle!s}, "
            f"pricing_scheme={_pricing_scheme!s}, "
            f"interval={_interval!s}, "
            f"interval_unit={_interval_unit!s}, "
            f"prices={_prices!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
