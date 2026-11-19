"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class WalletProductUsageTemplate(object):
    """Implementation of the 'Wallet Product Usage Template' model.

    One wallet template billing through this Wallet Product, joined to the Feature
    and plan/component that assigns it, when there is one.

    Attributes:
        plan_name (str): The name of the product or component the Feature is assigned
            to. `null` when the wallet template has no assigning Feature.
        wallet_template_name (str): The label set in `wallet_behavior.name` on the
            Feature, or the standalone wallet's own `name`.
        unit_name (str): The model property of type str.
        purchase_mechanism (str): A best-effort label for how this wallet is expected
            to be replenished. Currently reports `"Overage"` when the wallet template
            allows a negative balance, and `null` otherwise; there's no persisted
            field yet distinguishing, for example, an intended "Auto top-up" from
            "Purchase more" setup. Treat this as informational, not a stable enum.
        price_point_name (str): The model property of type str.
        currency (str): The model property of type str.
        active (bool): `false` when the assigning Feature is archived.
        feature_template_id (int): The model property of type int.
        feature_template_name (str): The model property of type str.
        price_point_override (bool): `true` when this wallet template is priced at a
            price point other than the Wallet Product's default.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "plan_name": "plan_name",
        "wallet_template_name": "wallet_template_name",
        "unit_name": "unit_name",
        "purchase_mechanism": "purchase_mechanism",
        "price_point_name": "price_point_name",
        "currency": "currency",
        "active": "active",
        "feature_template_id": "feature_template_id",
        "feature_template_name": "feature_template_name",
        "price_point_override": "price_point_override",
    }

    _optionals = [
        "plan_name",
        "wallet_template_name",
        "unit_name",
        "purchase_mechanism",
        "price_point_name",
        "currency",
        "active",
        "feature_template_id",
        "feature_template_name",
        "price_point_override",
    ]

    _nullables = [
        "plan_name",
        "wallet_template_name",
        "purchase_mechanism",
        "price_point_name",
        "feature_template_id",
        "feature_template_name",
    ]

    def __init__(
        self,
        plan_name=APIHelper.SKIP,
        wallet_template_name=APIHelper.SKIP,
        unit_name=APIHelper.SKIP,
        purchase_mechanism=APIHelper.SKIP,
        price_point_name=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        active=APIHelper.SKIP,
        feature_template_id=APIHelper.SKIP,
        feature_template_name=APIHelper.SKIP,
        price_point_override=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletProductUsageTemplate instance."""
        # Initialize members of the class
        if plan_name is not APIHelper.SKIP:
            self.plan_name = plan_name
        if wallet_template_name is not APIHelper.SKIP:
            self.wallet_template_name = wallet_template_name
        if unit_name is not APIHelper.SKIP:
            self.unit_name = unit_name
        if purchase_mechanism is not APIHelper.SKIP:
            self.purchase_mechanism = purchase_mechanism
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if active is not APIHelper.SKIP:
            self.active = active
        if feature_template_id is not APIHelper.SKIP:
            self.feature_template_id = feature_template_id
        if feature_template_name is not APIHelper.SKIP:
            self.feature_template_name = feature_template_name
        if price_point_override is not APIHelper.SKIP:
            self.price_point_override = price_point_override

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
        plan_name =\
            dictionary.get("plan_name")\
            if "plan_name" in dictionary.keys()\
                else APIHelper.SKIP
        wallet_template_name =\
            dictionary.get("wallet_template_name")\
            if "wallet_template_name" in dictionary.keys()\
                else APIHelper.SKIP
        unit_name =\
            dictionary.get("unit_name")\
            if dictionary.get("unit_name")\
                else APIHelper.SKIP
        purchase_mechanism =\
            dictionary.get("purchase_mechanism")\
            if "purchase_mechanism" in dictionary.keys()\
                else APIHelper.SKIP
        price_point_name =\
            dictionary.get("price_point_name")\
            if "price_point_name" in dictionary.keys()\
                else APIHelper.SKIP
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else APIHelper.SKIP
        active =\
            dictionary.get("active")\
            if "active" in dictionary.keys()\
                else APIHelper.SKIP
        feature_template_id =\
            dictionary.get("feature_template_id")\
            if "feature_template_id" in dictionary.keys()\
                else APIHelper.SKIP
        feature_template_name =\
            dictionary.get("feature_template_name")\
            if "feature_template_name" in dictionary.keys()\
                else APIHelper.SKIP
        price_point_override =\
            dictionary.get("price_point_override")\
            if "price_point_override" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(plan_name,
                   wallet_template_name,
                   unit_name,
                   purchase_mechanism,
                   price_point_name,
                   currency,
                   active,
                   feature_template_id,
                   feature_template_name,
                   price_point_override,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _plan_name=(
            self.plan_name
            if hasattr(self, "plan_name")
            else None
        )
        _wallet_template_name=(
            self.wallet_template_name
            if hasattr(self, "wallet_template_name")
            else None
        )
        _unit_name=(
            self.unit_name
            if hasattr(self, "unit_name")
            else None
        )
        _purchase_mechanism=(
            self.purchase_mechanism
            if hasattr(self, "purchase_mechanism")
            else None
        )
        _price_point_name=(
            self.price_point_name
            if hasattr(self, "price_point_name")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _active=(
            self.active
            if hasattr(self, "active")
            else None
        )
        _feature_template_id=(
            self.feature_template_id
            if hasattr(self, "feature_template_id")
            else None
        )
        _feature_template_name=(
            self.feature_template_name
            if hasattr(self, "feature_template_name")
            else None
        )
        _price_point_override=(
            self.price_point_override
            if hasattr(self, "price_point_override")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_name={_plan_name!r}, "
            f"wallet_template_name={_wallet_template_name!r}, "
            f"unit_name={_unit_name!r}, "
            f"purchase_mechanism={_purchase_mechanism!r}, "
            f"price_point_name={_price_point_name!r}, "
            f"currency={_currency!r}, "
            f"active={_active!r}, "
            f"feature_template_id={_feature_template_id!r}, "
            f"feature_template_name={_feature_template_name!r}, "
            f"price_point_override={_price_point_override!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _plan_name=(
            self.plan_name
            if hasattr(self, "plan_name")
            else None
        )
        _wallet_template_name=(
            self.wallet_template_name
            if hasattr(self, "wallet_template_name")
            else None
        )
        _unit_name=(
            self.unit_name
            if hasattr(self, "unit_name")
            else None
        )
        _purchase_mechanism=(
            self.purchase_mechanism
            if hasattr(self, "purchase_mechanism")
            else None
        )
        _price_point_name=(
            self.price_point_name
            if hasattr(self, "price_point_name")
            else None
        )
        _currency=(
            self.currency
            if hasattr(self, "currency")
            else None
        )
        _active=(
            self.active
            if hasattr(self, "active")
            else None
        )
        _feature_template_id=(
            self.feature_template_id
            if hasattr(self, "feature_template_id")
            else None
        )
        _feature_template_name=(
            self.feature_template_name
            if hasattr(self, "feature_template_name")
            else None
        )
        _price_point_override=(
            self.price_point_override
            if hasattr(self, "price_point_override")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_name={_plan_name!s}, "
            f"wallet_template_name={_wallet_template_name!s}, "
            f"unit_name={_unit_name!s}, "
            f"purchase_mechanism={_purchase_mechanism!s}, "
            f"price_point_name={_price_point_name!s}, "
            f"currency={_currency!s}, "
            f"active={_active!s}, "
            f"feature_template_id={_feature_template_id!s}, "
            f"feature_template_name={_feature_template_name!s}, "
            f"price_point_override={_price_point_override!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
