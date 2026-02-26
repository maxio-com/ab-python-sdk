"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.payment_type import (
    PaymentType,
)


class ApplePayPaymentProfile(object):
    """Implementation of the 'ApplePay Payment Profile' model.

    Attributes:
        id (int): The Chargify-assigned ID of the Apple Pay payment profile.
        first_name (str): The first name of the Apple Pay account holder
        last_name (str): The last name of the Apple Pay account holder
        customer_id (int): The Chargify-assigned id for the customer record to which
            the Apple Pay account belongs
        current_vault (ApplePayVault): The vault that stores the payment profile with
            the provided vault_token.
        vault_token (str): The “token” provided by your vault storage for an already
            stored payment profile
        billing_address (str): The current billing street address for the Apple Pay
            account
        billing_city (str): The current billing address city for the Apple Pay account
        billing_state (str): The current billing address state for the Apple Pay
            account
        billing_zip (str): The current billing address zip code for the Apple Pay
            account
        billing_country (str): The current billing address country for the Apple Pay
            account
        customer_vault_token (str): The model property of type str.
        billing_address_2 (str): The current billing street address, second line, for
            the Apple Pay account
        payment_type (PaymentType): The model property of type PaymentType.
        site_gateway_setting_id (int): The model property of type int.
        gateway_handle (str): The model property of type str.
        created_at (datetime): A timestamp indicating when this payment profile was
            created
        updated_at (datetime): A timestamp indicating when this payment profile was
            last updated
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": "payment_type",
        "id": "id",
        "first_name": "first_name",
        "last_name": "last_name",
        "customer_id": "customer_id",
        "current_vault": "current_vault",
        "vault_token": "vault_token",
        "billing_address": "billing_address",
        "billing_city": "billing_city",
        "billing_state": "billing_state",
        "billing_zip": "billing_zip",
        "billing_country": "billing_country",
        "customer_vault_token": "customer_vault_token",
        "billing_address_2": "billing_address_2",
        "site_gateway_setting_id": "site_gateway_setting_id",
        "gateway_handle": "gateway_handle",
        "created_at": "created_at",
        "updated_at": "updated_at",
    }

    _optionals = [
        "id",
        "first_name",
        "last_name",
        "customer_id",
        "current_vault",
        "vault_token",
        "billing_address",
        "billing_city",
        "billing_state",
        "billing_zip",
        "billing_country",
        "customer_vault_token",
        "billing_address_2",
        "site_gateway_setting_id",
        "gateway_handle",
        "created_at",
        "updated_at",
    ]

    _nullables = [
        "billing_address",
        "billing_city",
        "billing_state",
        "billing_zip",
        "billing_country",
        "customer_vault_token",
        "billing_address_2",
        "site_gateway_setting_id",
        "gateway_handle",
    ]

    def __init__(
        self,
        payment_type="apple_pay",
        id=APIHelper.SKIP,
        first_name=APIHelper.SKIP,
        last_name=APIHelper.SKIP,
        customer_id=APIHelper.SKIP,
        current_vault=APIHelper.SKIP,
        vault_token=APIHelper.SKIP,
        billing_address=APIHelper.SKIP,
        billing_city=APIHelper.SKIP,
        billing_state=APIHelper.SKIP,
        billing_zip=APIHelper.SKIP,
        billing_country=APIHelper.SKIP,
        customer_vault_token=APIHelper.SKIP,
        billing_address_2=APIHelper.SKIP,
        site_gateway_setting_id=APIHelper.SKIP,
        gateway_handle=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        updated_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ApplePayPaymentProfile instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id
        if current_vault is not APIHelper.SKIP:
            self.current_vault = current_vault
        if vault_token is not APIHelper.SKIP:
            self.vault_token = vault_token
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address
        if billing_city is not APIHelper.SKIP:
            self.billing_city = billing_city
        if billing_state is not APIHelper.SKIP:
            self.billing_state = billing_state
        if billing_zip is not APIHelper.SKIP:
            self.billing_zip = billing_zip
        if billing_country is not APIHelper.SKIP:
            self.billing_country = billing_country
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token
        if billing_address_2 is not APIHelper.SKIP:
            self.billing_address_2 = billing_address_2
        self.payment_type = payment_type
        if site_gateway_setting_id is not APIHelper.SKIP:
            self.site_gateway_setting_id = site_gateway_setting_id
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None
        if updated_at is not APIHelper.SKIP:
            self.updated_at =\
                 APIHelper.apply_datetime_converter(
                updated_at, APIHelper.RFC3339DateTime)\
                 if updated_at else None

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
        payment_type =\
            dictionary.get("payment_type")\
            if dictionary.get("payment_type")\
                else "apple_pay"
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        first_name =\
            dictionary.get("first_name")\
            if dictionary.get("first_name")\
                else APIHelper.SKIP
        last_name =\
            dictionary.get("last_name")\
            if dictionary.get("last_name")\
                else APIHelper.SKIP
        customer_id =\
            dictionary.get("customer_id")\
            if dictionary.get("customer_id")\
                else APIHelper.SKIP
        current_vault =\
            dictionary.get("current_vault")\
            if dictionary.get("current_vault")\
                else APIHelper.SKIP
        vault_token =\
            dictionary.get("vault_token")\
            if dictionary.get("vault_token")\
                else APIHelper.SKIP
        billing_address =\
            dictionary.get("billing_address")\
            if "billing_address" in dictionary.keys()\
                else APIHelper.SKIP
        billing_city =\
            dictionary.get("billing_city")\
            if "billing_city" in dictionary.keys()\
                else APIHelper.SKIP
        billing_state =\
            dictionary.get("billing_state")\
            if "billing_state" in dictionary.keys()\
                else APIHelper.SKIP
        billing_zip =\
            dictionary.get("billing_zip")\
            if "billing_zip" in dictionary.keys()\
                else APIHelper.SKIP
        billing_country =\
            dictionary.get("billing_country")\
            if "billing_country" in dictionary.keys()\
                else APIHelper.SKIP
        customer_vault_token =\
            dictionary.get("customer_vault_token")\
            if "customer_vault_token" in dictionary.keys()\
                else APIHelper.SKIP
        billing_address_2 =\
            dictionary.get("billing_address_2")\
            if "billing_address_2" in dictionary.keys()\
                else APIHelper.SKIP
        site_gateway_setting_id =\
            dictionary.get("site_gateway_setting_id")\
            if "site_gateway_setting_id" in dictionary.keys()\
                else APIHelper.SKIP
        gateway_handle =\
            dictionary.get("gateway_handle")\
            if "gateway_handle" in dictionary.keys()\
                else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_at")).datetime\
            if dictionary.get("updated_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(payment_type,
                   id,
                   first_name,
                   last_name,
                   customer_id,
                   current_vault,
                   vault_token,
                   billing_address,
                   billing_city,
                   billing_state,
                   billing_zip,
                   billing_country,
                   customer_vault_token,
                   billing_address_2,
                   site_gateway_setting_id,
                   gateway_handle,
                   created_at,
                   updated_at,
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
                    value=dictionary.payment_type,
                    type_callable=lambda value:
                        PaymentType.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("payment_type"),
                type_callable=lambda value:
                    PaymentType.validate(value))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _first_name=(
            self.first_name
            if hasattr(self, "first_name")
            else None
        )
        _last_name=(
            self.last_name
            if hasattr(self, "last_name")
            else None
        )
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _current_vault=(
            self.current_vault
            if hasattr(self, "current_vault")
            else None
        )
        _vault_token=(
            self.vault_token
            if hasattr(self, "vault_token")
            else None
        )
        _billing_address=(
            self.billing_address
            if hasattr(self, "billing_address")
            else None
        )
        _billing_city=(
            self.billing_city
            if hasattr(self, "billing_city")
            else None
        )
        _billing_state=(
            self.billing_state
            if hasattr(self, "billing_state")
            else None
        )
        _billing_zip=(
            self.billing_zip
            if hasattr(self, "billing_zip")
            else None
        )
        _billing_country=(
            self.billing_country
            if hasattr(self, "billing_country")
            else None
        )
        _customer_vault_token=(
            self.customer_vault_token
            if hasattr(self, "customer_vault_token")
            else None
        )
        _billing_address_2=(
            self.billing_address_2
            if hasattr(self, "billing_address_2")
            else None
        )
        _payment_type=self.payment_type
        _site_gateway_setting_id=(
            self.site_gateway_setting_id
            if hasattr(self, "site_gateway_setting_id")
            else None
        )
        _gateway_handle=(
            self.gateway_handle
            if hasattr(self, "gateway_handle")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"first_name={_first_name!r}, "
            f"last_name={_last_name!r}, "
            f"customer_id={_customer_id!r}, "
            f"current_vault={_current_vault!r}, "
            f"vault_token={_vault_token!r}, "
            f"billing_address={_billing_address!r}, "
            f"billing_city={_billing_city!r}, "
            f"billing_state={_billing_state!r}, "
            f"billing_zip={_billing_zip!r}, "
            f"billing_country={_billing_country!r}, "
            f"customer_vault_token={_customer_vault_token!r}, "
            f"billing_address_2={_billing_address_2!r}, "
            f"payment_type={_payment_type!r}, "
            f"site_gateway_setting_id={_site_gateway_setting_id!r}, "
            f"gateway_handle={_gateway_handle!r}, "
            f"created_at={_created_at!r}, "
            f"updated_at={_updated_at!r}, "
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
        _first_name=(
            self.first_name
            if hasattr(self, "first_name")
            else None
        )
        _last_name=(
            self.last_name
            if hasattr(self, "last_name")
            else None
        )
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _current_vault=(
            self.current_vault
            if hasattr(self, "current_vault")
            else None
        )
        _vault_token=(
            self.vault_token
            if hasattr(self, "vault_token")
            else None
        )
        _billing_address=(
            self.billing_address
            if hasattr(self, "billing_address")
            else None
        )
        _billing_city=(
            self.billing_city
            if hasattr(self, "billing_city")
            else None
        )
        _billing_state=(
            self.billing_state
            if hasattr(self, "billing_state")
            else None
        )
        _billing_zip=(
            self.billing_zip
            if hasattr(self, "billing_zip")
            else None
        )
        _billing_country=(
            self.billing_country
            if hasattr(self, "billing_country")
            else None
        )
        _customer_vault_token=(
            self.customer_vault_token
            if hasattr(self, "customer_vault_token")
            else None
        )
        _billing_address_2=(
            self.billing_address_2
            if hasattr(self, "billing_address_2")
            else None
        )
        _payment_type=self.payment_type
        _site_gateway_setting_id=(
            self.site_gateway_setting_id
            if hasattr(self, "site_gateway_setting_id")
            else None
        )
        _gateway_handle=(
            self.gateway_handle
            if hasattr(self, "gateway_handle")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"first_name={_first_name!s}, "
            f"last_name={_last_name!s}, "
            f"customer_id={_customer_id!s}, "
            f"current_vault={_current_vault!s}, "
            f"vault_token={_vault_token!s}, "
            f"billing_address={_billing_address!s}, "
            f"billing_city={_billing_city!s}, "
            f"billing_state={_billing_state!s}, "
            f"billing_zip={_billing_zip!s}, "
            f"billing_country={_billing_country!s}, "
            f"customer_vault_token={_customer_vault_token!s}, "
            f"billing_address_2={_billing_address_2!s}, "
            f"payment_type={_payment_type!s}, "
            f"site_gateway_setting_id={_site_gateway_setting_id!s}, "
            f"gateway_handle={_gateway_handle!s}, "
            f"created_at={_created_at!s}, "
            f"updated_at={_updated_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
