"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class WalletPurchase(object):
    """Implementation of the 'Wallet Purchase' model.

    A completed unit purchase.

    Attributes:
        id (int): The id of the grant this purchase created. When the wallet was
            overdrawn by at least the purchased quantity, the units repay the debt
            and the grant is still created, with `remaining` of `0` and `original`
            equal to the purchased quantity.
        price_point_id (int): The price point the purchase was priced at.
        invoice_uid (str): The uid of the invoice created to collect payment for this
            purchase.
        quantity (str): The number of units purchased, as a decimal string.
        expires_at (datetime): When the purchased units expire, following the funding
            entitlement's grant expiration policy. `null` when the wallet has no
            funding entitlement or its entitlements disagree on an expiration policy.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "price_point_id": "price_point_id",
        "invoice_uid": "invoice_uid",
        "quantity": "quantity",
        "expires_at": "expires_at",
    }

    _nullables = [
        "expires_at",
    ]

    def __init__(
        self,
        id=None,
        price_point_id=None,
        invoice_uid=None,
        quantity=None,
        expires_at=None,
        additional_properties=None):
        """Initialize a WalletPurchase instance."""
        # Initialize members of the class
        self.id = id
        self.price_point_id = price_point_id
        self.invoice_uid = invoice_uid
        self.quantity = quantity
        self.expires_at =\
             APIHelper.apply_datetime_converter(
            expires_at, APIHelper.RFC3339DateTime)\
             if expires_at else None

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
                else None
        price_point_id =\
            dictionary.get("price_point_id")\
            if dictionary.get("price_point_id")\
                else None
        invoice_uid =\
            dictionary.get("invoice_uid")\
            if dictionary.get("invoice_uid")\
                else None
        quantity =\
            dictionary.get("quantity")\
            if dictionary.get("quantity")\
                else None
        expires_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("expires_at")).datetime\
            if dictionary.get("expires_at") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   price_point_id,
                   invoice_uid,
                   quantity,
                   expires_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=self.id
        _price_point_id=self.price_point_id
        _invoice_uid=self.invoice_uid
        _quantity=self.quantity
        _expires_at=self.expires_at
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"invoice_uid={_invoice_uid!r}, "
            f"quantity={_quantity!r}, "
            f"expires_at={_expires_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=self.id
        _price_point_id=self.price_point_id
        _invoice_uid=self.invoice_uid
        _quantity=self.quantity
        _expires_at=self.expires_at
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"invoice_uid={_invoice_uid!s}, "
            f"quantity={_quantity!s}, "
            f"expires_at={_expires_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
