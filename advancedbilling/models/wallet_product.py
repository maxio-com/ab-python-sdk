"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.wallet_product_price_point_attributes import (
    WalletProductPricePointAttributes,
)


class WalletProduct(object):
    """Implementation of the 'WalletProduct' model.

    Attributes:
        name (str): The model property of type str.
        unit_name (str): The name of the unit the Wallet Product's usage is measured
            in, for example `tokens`.
        handle (str): The model property of type str.
        description (str): The model property of type str.
        taxable (bool): The model property of type bool.
        tax_code (str): The model property of type str.
        accounting_code (str): The model property of type str.
        item_category (ItemCategory): One of the following: Business Software,
            Consumer Software, Digital Services, Physical Goods, Other
        price_point (WalletProductPricePointAttributes): Creates one price point for
            the Wallet Product in the same call. Ignored if `price_points` is also
            sent.
        price_points (List[WalletProductPricePointAttributes]): Creates several price
            points for the Wallet Product in the same call, winning over
            `price_point` if both are sent. The first price point created becomes the
            Wallet Product's default. The whole call is one transaction: if any price
            point in the array fails validation, nothing is created, including the
            Wallet Product itself.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "unit_name": "unit_name",
        "handle": "handle",
        "description": "description",
        "taxable": "taxable",
        "tax_code": "tax_code",
        "accounting_code": "accounting_code",
        "item_category": "item_category",
        "price_point": "price_point",
        "price_points": "price_points",
    }

    _optionals = [
        "handle",
        "description",
        "taxable",
        "tax_code",
        "accounting_code",
        "item_category",
        "price_point",
        "price_points",
    ]

    _nullables = [
        "description",
        "tax_code",
        "accounting_code",
        "item_category",
    ]

    def __init__(
        self,
        name=None,
        unit_name=None,
        handle=APIHelper.SKIP,
        description=APIHelper.SKIP,
        taxable=APIHelper.SKIP,
        tax_code=APIHelper.SKIP,
        accounting_code=APIHelper.SKIP,
        item_category=APIHelper.SKIP,
        price_point=APIHelper.SKIP,
        price_points=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletProduct instance."""
        # Initialize members of the class
        self.name = name
        self.unit_name = unit_name
        if handle is not APIHelper.SKIP:
            self.handle = handle
        if description is not APIHelper.SKIP:
            self.description = description
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code
        if item_category is not APIHelper.SKIP:
            self.item_category = item_category
        if price_point is not APIHelper.SKIP:
            self.price_point = price_point
        if price_points is not APIHelper.SKIP:
            self.price_points = price_points

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
        unit_name =\
            dictionary.get("unit_name")\
            if dictionary.get("unit_name")\
                else None
        handle =\
            dictionary.get("handle")\
            if dictionary.get("handle")\
                else APIHelper.SKIP
        description =\
            dictionary.get("description")\
            if "description" in dictionary.keys()\
                else APIHelper.SKIP
        taxable =\
            dictionary.get("taxable")\
            if "taxable" in dictionary.keys()\
                else APIHelper.SKIP
        tax_code =\
            dictionary.get("tax_code")\
            if "tax_code" in dictionary.keys()\
                else APIHelper.SKIP
        accounting_code =\
            dictionary.get("accounting_code")\
            if "accounting_code" in dictionary.keys()\
                else APIHelper.SKIP
        item_category =\
            dictionary.get("item_category")\
            if "item_category" in dictionary.keys()\
                else APIHelper.SKIP
        price_point =\
            WalletProductPricePointAttributes.from_dictionary(
                dictionary.get("price_point"))\
                if "price_point" in dictionary.keys()\
                else APIHelper.SKIP
        price_points = None
        if dictionary.get("price_points") is not None:
            price_points = [
                WalletProductPricePointAttributes.from_dictionary(x)
                    for x in dictionary.get("price_points")
            ]
        else:
            price_points = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(name,
                   unit_name,
                   handle,
                   description,
                   taxable,
                   tax_code,
                   accounting_code,
                   item_category,
                   price_point,
                   price_points,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=self.name
        _unit_name=self.unit_name
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _taxable=(
            self.taxable
            if hasattr(self, "taxable")
            else None
        )
        _tax_code=(
            self.tax_code
            if hasattr(self, "tax_code")
            else None
        )
        _accounting_code=(
            self.accounting_code
            if hasattr(self, "accounting_code")
            else None
        )
        _item_category=(
            self.item_category
            if hasattr(self, "item_category")
            else None
        )
        _price_point=(
            self.price_point
            if hasattr(self, "price_point")
            else None
        )
        _price_points=(
            self.price_points
            if hasattr(self, "price_points")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}, "
            f"unit_name={_unit_name!r}, "
            f"handle={_handle!r}, "
            f"description={_description!r}, "
            f"taxable={_taxable!r}, "
            f"tax_code={_tax_code!r}, "
            f"accounting_code={_accounting_code!r}, "
            f"item_category={_item_category!r}, "
            f"price_point={_price_point!r}, "
            f"price_points={_price_points!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=self.name
        _unit_name=self.unit_name
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _taxable=(
            self.taxable
            if hasattr(self, "taxable")
            else None
        )
        _tax_code=(
            self.tax_code
            if hasattr(self, "tax_code")
            else None
        )
        _accounting_code=(
            self.accounting_code
            if hasattr(self, "accounting_code")
            else None
        )
        _item_category=(
            self.item_category
            if hasattr(self, "item_category")
            else None
        )
        _price_point=(
            self.price_point
            if hasattr(self, "price_point")
            else None
        )
        _price_points=(
            self.price_points
            if hasattr(self, "price_points")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}, "
            f"unit_name={_unit_name!s}, "
            f"handle={_handle!s}, "
            f"description={_description!s}, "
            f"taxable={_taxable!s}, "
            f"tax_code={_tax_code!s}, "
            f"accounting_code={_accounting_code!s}, "
            f"item_category={_item_category!s}, "
            f"price_point={_price_point!s}, "
            f"price_points={_price_points!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
