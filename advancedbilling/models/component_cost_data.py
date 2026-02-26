"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_cost_data_rate_tier import (
    ComponentCostDataRateTier,
)


class ComponentCostData(object):
    """Implementation of the 'Component Cost Data' model.

    Attributes:
        component_code_id (int): The model property of type int.
        price_point_id (int): The model property of type int.
        product_id (int): The model property of type int.
        quantity (str): The model property of type str.
        amount (str): The model property of type str.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme. See
            [Product
            Components](https://help.chargify.com/products/product-components.html)
            for an overview of pricing schemes.
        tiers (List[ComponentCostDataRateTier]): The model property of type
            List[ComponentCostDataRateTier].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_code_id": "component_code_id",
        "price_point_id": "price_point_id",
        "product_id": "product_id",
        "quantity": "quantity",
        "amount": "amount",
        "pricing_scheme": "pricing_scheme",
        "tiers": "tiers",
    }

    _optionals = [
        "component_code_id",
        "price_point_id",
        "product_id",
        "quantity",
        "amount",
        "pricing_scheme",
        "tiers",
    ]

    _nullables = [
        "component_code_id",
    ]

    def __init__(
        self,
        component_code_id=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        product_id=APIHelper.SKIP,
        quantity=APIHelper.SKIP,
        amount=APIHelper.SKIP,
        pricing_scheme=APIHelper.SKIP,
        tiers=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ComponentCostData instance."""
        # Initialize members of the class
        if component_code_id is not APIHelper.SKIP:
            self.component_code_id = component_code_id
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity
        if amount is not APIHelper.SKIP:
            self.amount = amount
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme
        if tiers is not APIHelper.SKIP:
            self.tiers = tiers

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
        component_code_id =\
            dictionary.get("component_code_id")\
            if "component_code_id" in dictionary.keys()\
                else APIHelper.SKIP
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else APIHelper.SKIP
        product_id =\
            dictionary.get("product_id")\
            if dictionary.get("product_id")\
                else APIHelper.SKIP
        quantity =\
            dictionary.get("quantity")\
            if dictionary.get("quantity")\
                else APIHelper.SKIP
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else APIHelper.SKIP
        pricing_scheme =\
            dictionary.get("pricing_scheme")\
            if dictionary.get("pricing_scheme")\
                else APIHelper.SKIP
        tiers = None
        if dictionary.get("tiers") is not None:
            tiers = [
                ComponentCostDataRateTier.from_dictionary(x)
                    for x in dictionary.get("tiers")
            ]
        else:
            tiers = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(component_code_id,
                   price_point_id,
                   product_id,
                   quantity,
                   amount,
                   pricing_scheme,
                   tiers,
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
        _component_code_id=(
            self.component_code_id
            if hasattr(self, "component_code_id")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _product_id=(
            self.product_id
            if hasattr(self, "product_id")
            else None
        )
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _pricing_scheme=(
            self.pricing_scheme
            if hasattr(self, "pricing_scheme")
            else None
        )
        _tiers=(
            self.tiers
            if hasattr(self, "tiers")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"component_code_id={_component_code_id!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"product_id={_product_id!r}, "
            f"quantity={_quantity!r}, "
            f"amount={_amount!r}, "
            f"pricing_scheme={_pricing_scheme!r}, "
            f"tiers={_tiers!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _component_code_id=(
            self.component_code_id
            if hasattr(self, "component_code_id")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _product_id=(
            self.product_id
            if hasattr(self, "product_id")
            else None
        )
        _quantity=(
            self.quantity
            if hasattr(self, "quantity")
            else None
        )
        _amount=(
            self.amount
            if hasattr(self, "amount")
            else None
        )
        _pricing_scheme=(
            self.pricing_scheme
            if hasattr(self, "pricing_scheme")
            else None
        )
        _tiers=(
            self.tiers
            if hasattr(self, "tiers")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"component_code_id={_component_code_id!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"product_id={_product_id!s}, "
            f"quantity={_quantity!s}, "
            f"amount={_amount!s}, "
            f"pricing_scheme={_pricing_scheme!s}, "
            f"tiers={_tiers!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
