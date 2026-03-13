"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class GetOneTimeTokenPaymentProfile(object):
    """Implementation of the 'Get One Time Token Payment Profile' model.

    Attributes:
        id (str): The model property of type str.
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        masked_card_number (str): The model property of type str.
        card_type (CardType): The type of card used.
        expiration_month (float): The model property of type float.
        expiration_year (float): The model property of type float.
        customer_id (str): The model property of type str.
        current_vault (CreditCardVault): The vault that stores the payment profile
            with the provided `vault_token`. Use `bogus` for testing.
        vault_token (str): The model property of type str.
        billing_address (str): The model property of type str.
        billing_address_2 (str): The model property of type str.
        billing_city (str): The model property of type str.
        billing_country (str): The model property of type str.
        billing_state (str): The model property of type str.
        billing_zip (str): The model property of type str.
        payment_type (str): The model property of type str.
        disabled (bool): The model property of type bool.
        site_gateway_setting_id (int): The model property of type int.
        customer_vault_token (str): The model property of type str.
        gateway_handle (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": "first_name",
        "last_name": "last_name",
        "masked_card_number": "masked_card_number",
        "card_type": "card_type",
        "expiration_month": "expiration_month",
        "expiration_year": "expiration_year",
        "current_vault": "current_vault",
        "vault_token": "vault_token",
        "billing_address": "billing_address",
        "billing_city": "billing_city",
        "billing_country": "billing_country",
        "billing_state": "billing_state",
        "billing_zip": "billing_zip",
        "payment_type": "payment_type",
        "disabled": "disabled",
        "site_gateway_setting_id": "site_gateway_setting_id",
        "id": "id",
        "customer_id": "customer_id",
        "billing_address_2": "billing_address_2",
        "customer_vault_token": "customer_vault_token",
        "gateway_handle": "gateway_handle",
    }

    _optionals = [
        "id",
        "customer_id",
        "billing_address_2",
        "customer_vault_token",
        "gateway_handle",
    ]

    _nullables = [
        "id",
        "customer_id",
        "customer_vault_token",
        "gateway_handle",
    ]

    def __init__(
        self,
        first_name=None,
        last_name=None,
        masked_card_number=None,
        card_type=None,
        expiration_month=None,
        expiration_year=None,
        current_vault=None,
        vault_token=None,
        billing_address=None,
        billing_city=None,
        billing_country=None,
        billing_state=None,
        billing_zip=None,
        payment_type=None,
        disabled=None,
        site_gateway_setting_id=None,
        id=APIHelper.SKIP,
        customer_id=APIHelper.SKIP,
        billing_address_2=APIHelper.SKIP,
        customer_vault_token=APIHelper.SKIP,
        gateway_handle=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a GetOneTimeTokenPaymentProfile instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.masked_card_number = masked_card_number
        self.card_type = card_type
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id
        self.current_vault = current_vault
        self.vault_token = vault_token
        self.billing_address = billing_address
        if billing_address_2 is not APIHelper.SKIP:
            self.billing_address_2 = billing_address_2
        self.billing_city = billing_city
        self.billing_country = billing_country
        self.billing_state = billing_state
        self.billing_zip = billing_zip
        self.payment_type = payment_type
        self.disabled = disabled
        self.site_gateway_setting_id = site_gateway_setting_id
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle

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
        first_name =\
            dictionary.get("first_name")\
            if dictionary.get("first_name")\
                else None
        last_name =\
            dictionary.get("last_name")\
            if dictionary.get("last_name")\
                else None
        masked_card_number =\
            dictionary.get("masked_card_number")\
            if dictionary.get("masked_card_number")\
                else None
        card_type =\
            dictionary.get("card_type")\
            if dictionary.get("card_type")\
                else None
        expiration_month =\
            dictionary.get("expiration_month")\
            if dictionary.get("expiration_month")\
                else None
        expiration_year =\
            dictionary.get("expiration_year")\
            if dictionary.get("expiration_year")\
                else None
        current_vault =\
            dictionary.get("current_vault")\
            if dictionary.get("current_vault")\
                else None
        vault_token =\
            dictionary.get("vault_token")\
            if dictionary.get("vault_token")\
                else None
        billing_address =\
            dictionary.get("billing_address")\
            if dictionary.get("billing_address")\
                else None
        billing_city =\
            dictionary.get("billing_city")\
            if dictionary.get("billing_city")\
                else None
        billing_country =\
            dictionary.get("billing_country")\
            if dictionary.get("billing_country")\
                else None
        billing_state =\
            dictionary.get("billing_state")\
            if dictionary.get("billing_state")\
                else None
        billing_zip =\
            dictionary.get("billing_zip")\
            if dictionary.get("billing_zip")\
                else None
        payment_type =\
            dictionary.get("payment_type")\
            if dictionary.get("payment_type")\
                else None
        disabled =\
            dictionary.get("disabled")\
            if "disabled" in dictionary.keys()\
                else None
        site_gateway_setting_id =\
            dictionary.get("site_gateway_setting_id")\
            if dictionary.get("site_gateway_setting_id")\
                else None
        id =\
            dictionary.get("id")\
            if "id" in dictionary.keys()\
                else APIHelper.SKIP
        customer_id =\
            dictionary.get("customer_id")\
            if "customer_id" in dictionary.keys()\
                else APIHelper.SKIP
        billing_address_2 =\
            dictionary.get("billing_address_2")\
            if dictionary.get("billing_address_2")\
                else APIHelper.SKIP
        customer_vault_token =\
            dictionary.get("customer_vault_token")\
            if "customer_vault_token" in dictionary.keys()\
                else APIHelper.SKIP
        gateway_handle =\
            dictionary.get("gateway_handle")\
            if "gateway_handle" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   masked_card_number,
                   card_type,
                   expiration_month,
                   expiration_year,
                   current_vault,
                   vault_token,
                   billing_address,
                   billing_city,
                   billing_country,
                   billing_state,
                   billing_zip,
                   payment_type,
                   disabled,
                   site_gateway_setting_id,
                   id,
                   customer_id,
                   billing_address_2,
                   customer_vault_token,
                   gateway_handle,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _first_name=self.first_name
        _last_name=self.last_name
        _masked_card_number=self.masked_card_number
        _card_type=self.card_type
        _expiration_month=self.expiration_month
        _expiration_year=self.expiration_year
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _current_vault=self.current_vault
        _vault_token=self.vault_token
        _billing_address=self.billing_address
        _billing_address_2=(
            self.billing_address_2
            if hasattr(self, "billing_address_2")
            else None
        )
        _billing_city=self.billing_city
        _billing_country=self.billing_country
        _billing_state=self.billing_state
        _billing_zip=self.billing_zip
        _payment_type=self.payment_type
        _disabled=self.disabled
        _site_gateway_setting_id=self.site_gateway_setting_id
        _customer_vault_token=(
            self.customer_vault_token
            if hasattr(self, "customer_vault_token")
            else None
        )
        _gateway_handle=(
            self.gateway_handle
            if hasattr(self, "gateway_handle")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"first_name={_first_name!r}, "
            f"last_name={_last_name!r}, "
            f"masked_card_number={_masked_card_number!r}, "
            f"card_type={_card_type!r}, "
            f"expiration_month={_expiration_month!r}, "
            f"expiration_year={_expiration_year!r}, "
            f"customer_id={_customer_id!r}, "
            f"current_vault={_current_vault!r}, "
            f"vault_token={_vault_token!r}, "
            f"billing_address={_billing_address!r}, "
            f"billing_address_2={_billing_address_2!r}, "
            f"billing_city={_billing_city!r}, "
            f"billing_country={_billing_country!r}, "
            f"billing_state={_billing_state!r}, "
            f"billing_zip={_billing_zip!r}, "
            f"payment_type={_payment_type!r}, "
            f"disabled={_disabled!r}, "
            f"site_gateway_setting_id={_site_gateway_setting_id!r}, "
            f"customer_vault_token={_customer_vault_token!r}, "
            f"gateway_handle={_gateway_handle!r}, "
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
        _first_name=self.first_name
        _last_name=self.last_name
        _masked_card_number=self.masked_card_number
        _card_type=self.card_type
        _expiration_month=self.expiration_month
        _expiration_year=self.expiration_year
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _current_vault=self.current_vault
        _vault_token=self.vault_token
        _billing_address=self.billing_address
        _billing_address_2=(
            self.billing_address_2
            if hasattr(self, "billing_address_2")
            else None
        )
        _billing_city=self.billing_city
        _billing_country=self.billing_country
        _billing_state=self.billing_state
        _billing_zip=self.billing_zip
        _payment_type=self.payment_type
        _disabled=self.disabled
        _site_gateway_setting_id=self.site_gateway_setting_id
        _customer_vault_token=(
            self.customer_vault_token
            if hasattr(self, "customer_vault_token")
            else None
        )
        _gateway_handle=(
            self.gateway_handle
            if hasattr(self, "gateway_handle")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"first_name={_first_name!s}, "
            f"last_name={_last_name!s}, "
            f"masked_card_number={_masked_card_number!s}, "
            f"card_type={_card_type!s}, "
            f"expiration_month={_expiration_month!s}, "
            f"expiration_year={_expiration_year!s}, "
            f"customer_id={_customer_id!s}, "
            f"current_vault={_current_vault!s}, "
            f"vault_token={_vault_token!s}, "
            f"billing_address={_billing_address!s}, "
            f"billing_address_2={_billing_address_2!s}, "
            f"billing_city={_billing_city!s}, "
            f"billing_country={_billing_country!s}, "
            f"billing_state={_billing_state!s}, "
            f"billing_zip={_billing_zip!s}, "
            f"payment_type={_payment_type!s}, "
            f"disabled={_disabled!s}, "
            f"site_gateway_setting_id={_site_gateway_setting_id!s}, "
            f"customer_vault_token={_customer_vault_token!s}, "
            f"gateway_handle={_gateway_handle!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
