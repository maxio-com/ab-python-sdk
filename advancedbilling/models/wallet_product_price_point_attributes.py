"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.price_1 import Price1


class WalletProductPricePointAttributes(object):
    """Implementation of the 'Wallet Product Price Point Attributes' model.

    A price point to create for the Wallet Product, in the same call that creates or
    updates it.

    Attributes:
        name (str): The price point's name. Required. Omitting it fails validation
            with a message that reads `Name: cannot be blank.`, not naming the price
            point.
        handle (str): The model property of type str.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme. See
            [Product
            Components](https://help.chargify.com/products/product-components.html)
            for an overview of pricing schemes.
        unit_price (str): Required when `pricing_scheme` is `per_unit`.
        tax_included (bool): The model property of type bool.
        interval (int): Requires Multifrequency to be enabled on the site.
        interval_unit (IntervalUnit): The model property of type IntervalUnit.
        use_site_exchange_rate (bool): The model property of type bool.
        prices (List[Price1]): Required for every `pricing_scheme` other than
            `per_unit`.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "handle": "handle",
        "pricing_scheme": "pricing_scheme",
        "unit_price": "unit_price",
        "tax_included": "tax_included",
        "interval": "interval",
        "interval_unit": "interval_unit",
        "use_site_exchange_rate": "use_site_exchange_rate",
        "prices": "prices",
    }

    _optionals = [
        "handle",
        "pricing_scheme",
        "unit_price",
        "tax_included",
        "interval",
        "interval_unit",
        "use_site_exchange_rate",
        "prices",
    ]

    _nullables = [
        "unit_price",
    ]

    def __init__(
        self,
        name=None,
        handle=APIHelper.SKIP,
        pricing_scheme=APIHelper.SKIP,
        unit_price=APIHelper.SKIP,
        tax_included=APIHelper.SKIP,
        interval=APIHelper.SKIP,
        interval_unit=APIHelper.SKIP,
        use_site_exchange_rate=APIHelper.SKIP,
        prices=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletProductPricePointAttributes instance."""
        # Initialize members of the class
        self.name = name
        if handle is not APIHelper.SKIP:
            self.handle = handle
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price
        if tax_included is not APIHelper.SKIP:
            self.tax_included = tax_included
        if interval is not APIHelper.SKIP:
            self.interval = interval
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate
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
                else None
        handle =\
            dictionary.get("handle")\
            if dictionary.get("handle")\
                else APIHelper.SKIP
        pricing_scheme =\
            dictionary.get("pricing_scheme")\
            if dictionary.get("pricing_scheme")\
                else APIHelper.SKIP
        unit_price =\
            dictionary.get("unit_price")\
            if "unit_price" in dictionary.keys()\
                else APIHelper.SKIP
        tax_included =\
            dictionary.get("tax_included")\
            if "tax_included" in dictionary.keys()\
                else APIHelper.SKIP
        interval =\
            dictionary.get("interval")\
            if dictionary.get("interval")\
                else APIHelper.SKIP
        interval_unit =\
            dictionary.get("interval_unit")\
            if dictionary.get("interval_unit")\
                else APIHelper.SKIP
        use_site_exchange_rate =\
            dictionary.get("use_site_exchange_rate")\
            if "use_site_exchange_rate" in dictionary.keys()\
                else APIHelper.SKIP
        prices = None
        if dictionary.get("prices") is not None:
            prices = [
                Price1.from_dictionary(x)
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
                   unit_price,
                   tax_included,
                   interval,
                   interval_unit,
                   use_site_exchange_rate,
                   prices,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=self.name
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
        _unit_price=(
            self.unit_price
            if hasattr(self, "unit_price")
            else None
        )
        _tax_included=(
            self.tax_included
            if hasattr(self, "tax_included")
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
        _use_site_exchange_rate=(
            self.use_site_exchange_rate
            if hasattr(self, "use_site_exchange_rate")
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
            f"unit_price={_unit_price!r}, "
            f"tax_included={_tax_included!r}, "
            f"interval={_interval!r}, "
            f"interval_unit={_interval_unit!r}, "
            f"use_site_exchange_rate={_use_site_exchange_rate!r}, "
            f"prices={_prices!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=self.name
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
        _unit_price=(
            self.unit_price
            if hasattr(self, "unit_price")
            else None
        )
        _tax_included=(
            self.tax_included
            if hasattr(self, "tax_included")
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
        _use_site_exchange_rate=(
            self.use_site_exchange_rate
            if hasattr(self, "use_site_exchange_rate")
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
            f"unit_price={_unit_price!s}, "
            f"tax_included={_tax_included!s}, "
            f"interval={_interval!s}, "
            f"interval_unit={_interval_unit!s}, "
            f"use_site_exchange_rate={_use_site_exchange_rate!s}, "
            f"prices={_prices!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
