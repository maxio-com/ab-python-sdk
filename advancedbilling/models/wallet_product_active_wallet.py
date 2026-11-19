"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class WalletProductActiveWallet(object):
    """Implementation of the 'Wallet Product Active Wallet' model.

    One active wallet drawing on this Wallet Product.

    Attributes:
        id (int): The Advanced Billing id of the wallet.
        subscription_id (int): The model property of type int.
        company_name (str): The owning customer's organization name, falling back to
            their full name, then to `"Customer #<id>"`. `"Customer"` (with no id)
            when the wallet's subscription has no customer at all.
        purchase_mechanism (str): See the same field on [Wallet Product Usage
            Template]($m/Wallet%20Product%20Usage%20Template). The same caveats apply.
        price_point_name (str): The model property of type str.
        currency (str): The model property of type str.
        active (bool): `false` when the wallet's Feature is archived.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "subscription_id": "subscription_id",
        "company_name": "company_name",
        "purchase_mechanism": "purchase_mechanism",
        "price_point_name": "price_point_name",
        "currency": "currency",
        "active": "active",
    }

    _optionals = [
        "id",
        "subscription_id",
        "company_name",
        "purchase_mechanism",
        "price_point_name",
        "currency",
        "active",
    ]

    _nullables = [
        "purchase_mechanism",
        "price_point_name",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        subscription_id=APIHelper.SKIP,
        company_name=APIHelper.SKIP,
        purchase_mechanism=APIHelper.SKIP,
        price_point_name=APIHelper.SKIP,
        currency=APIHelper.SKIP,
        active=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletProductActiveWallet instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id
        if company_name is not APIHelper.SKIP:
            self.company_name = company_name
        if purchase_mechanism is not APIHelper.SKIP:
            self.purchase_mechanism = purchase_mechanism
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name
        if currency is not APIHelper.SKIP:
            self.currency = currency
        if active is not APIHelper.SKIP:
            self.active = active

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        subscription_id =\
            dictionary.get("subscription_id")\
            if dictionary.get("subscription_id")\
                else APIHelper.SKIP
        company_name =\
            dictionary.get("company_name")\
            if dictionary.get("company_name")\
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

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   subscription_id,
                   company_name,
                   purchase_mechanism,
                   price_point_name,
                   currency,
                   active,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _company_name=(
            self.company_name
            if hasattr(self, "company_name")
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"subscription_id={_subscription_id!r}, "
            f"company_name={_company_name!r}, "
            f"purchase_mechanism={_purchase_mechanism!r}, "
            f"price_point_name={_price_point_name!r}, "
            f"currency={_currency!r}, "
            f"active={_active!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
        _company_name=(
            self.company_name
            if hasattr(self, "company_name")
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
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"subscription_id={_subscription_id!s}, "
            f"company_name={_company_name!s}, "
            f"purchase_mechanism={_purchase_mechanism!s}, "
            f"price_point_name={_price_point_name!s}, "
            f"currency={_currency!s}, "
            f"active={_active!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
