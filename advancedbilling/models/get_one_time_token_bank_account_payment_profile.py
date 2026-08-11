"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.bank_account_holder_type import (
    BankAccountHolderType,
)
from advancedbilling.models.bank_account_type import (
    BankAccountType,
)
from advancedbilling.models.bank_account_vault import (
    BankAccountVault,
)


class GetOneTimeTokenBankAccountPaymentProfile(object):
    """Implementation of the 'Get One Time Token Bank Account Payment Profile' model.

    Attributes:
        id (str): The model property of type str.
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        customer_id (str): The model property of type str.
        current_vault (BankAccountVault): The vault that stores the payment profile
            with the provided vault_token. Use `bogus` for testing.
        vault_token (str): The model property of type str.
        billing_address (str): The model property of type str.
        billing_address_2 (str): The model property of type str.
        billing_city (str): The model property of type str.
        billing_country (str): The model property of type str.
        billing_state (str): The model property of type str.
        billing_zip (str): The model property of type str.
        bank_name (str): The model property of type str.
        masked_bank_routing_number (str): The model property of type str.
        masked_bank_account_number (str): The model property of type str.
        bank_account_type (BankAccountType): Defaults to checking
        bank_account_holder_type (BankAccountHolderType): Defaults to personal
        payment_type (str): The model property of type str.
        disabled (bool): The model property of type bool.
        site_gateway_setting_id (int): The model property of type int.
        customer_vault_token (str): The model property of type str.
        gateway_handle (str): The model property of type str.
        verified (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": "first_name",
        "last_name": "last_name",
        "current_vault": "current_vault",
        "vault_token": "vault_token",
        "billing_address": "billing_address",
        "billing_city": "billing_city",
        "billing_country": "billing_country",
        "billing_state": "billing_state",
        "billing_zip": "billing_zip",
        "bank_name": "bank_name",
        "masked_bank_routing_number": "masked_bank_routing_number",
        "masked_bank_account_number": "masked_bank_account_number",
        "bank_account_type": "bank_account_type",
        "bank_account_holder_type": "bank_account_holder_type",
        "payment_type": "payment_type",
        "disabled": "disabled",
        "site_gateway_setting_id": "site_gateway_setting_id",
        "id": "id",
        "customer_id": "customer_id",
        "billing_address_2": "billing_address_2",
        "customer_vault_token": "customer_vault_token",
        "gateway_handle": "gateway_handle",
        "verified": "verified",
    }

    _optionals = [
        "id",
        "customer_id",
        "billing_address_2",
        "customer_vault_token",
        "gateway_handle",
        "verified",
    ]

    _nullables = [
        "id",
        "customer_id",
        "customer_vault_token",
        "gateway_handle",
        "verified",
    ]

    def __init__(
        self,
        first_name=None,
        last_name=None,
        current_vault=None,
        vault_token=None,
        billing_address=None,
        billing_city=None,
        billing_country=None,
        billing_state=None,
        billing_zip=None,
        bank_name=None,
        masked_bank_routing_number=None,
        masked_bank_account_number=None,
        bank_account_type=None,
        bank_account_holder_type=None,
        payment_type=None,
        disabled=None,
        site_gateway_setting_id=None,
        id=APIHelper.SKIP,
        customer_id=APIHelper.SKIP,
        billing_address_2=APIHelper.SKIP,
        customer_vault_token=APIHelper.SKIP,
        gateway_handle=APIHelper.SKIP,
        verified=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a GetOneTimeTokenBankAccountPaymentProfile instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        self.first_name = first_name
        self.last_name = last_name
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
        self.bank_name = bank_name
        self.masked_bank_routing_number = masked_bank_routing_number
        self.masked_bank_account_number = masked_bank_account_number
        self.bank_account_type = bank_account_type
        self.bank_account_holder_type = bank_account_holder_type
        self.payment_type = payment_type
        self.disabled = disabled
        self.site_gateway_setting_id = site_gateway_setting_id
        if customer_vault_token is not APIHelper.SKIP:
            self.customer_vault_token = customer_vault_token
        if gateway_handle is not APIHelper.SKIP:
            self.gateway_handle = gateway_handle
        if verified is not APIHelper.SKIP:
            self.verified = verified

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
        bank_name =\
            dictionary.get("bank_name")\
            if dictionary.get("bank_name")\
                else None
        masked_bank_routing_number =\
            dictionary.get("masked_bank_routing_number")\
            if dictionary.get("masked_bank_routing_number")\
                else None
        masked_bank_account_number =\
            dictionary.get("masked_bank_account_number")\
            if dictionary.get("masked_bank_account_number")\
                else None
        bank_account_type =\
            dictionary.get("bank_account_type")\
            if dictionary.get("bank_account_type")\
                else None
        bank_account_holder_type =\
            dictionary.get("bank_account_holder_type")\
            if dictionary.get("bank_account_holder_type")\
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
        verified =\
            dictionary.get("verified")\
            if "verified" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   current_vault,
                   vault_token,
                   billing_address,
                   billing_city,
                   billing_country,
                   billing_state,
                   billing_zip,
                   bank_name,
                   masked_bank_routing_number,
                   masked_bank_account_number,
                   bank_account_type,
                   bank_account_holder_type,
                   payment_type,
                   disabled,
                   site_gateway_setting_id,
                   id,
                   customer_id,
                   billing_address_2,
                   customer_vault_token,
                   gateway_handle,
                   verified,
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
                    value=dictionary.first_name,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.last_name,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.current_vault,
                    type_callable=lambda value:
                        BankAccountVault.validate(value)) \
                and APIHelper.is_valid_type(
                    value=dictionary.vault_token,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.billing_address,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.billing_city,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.billing_country,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.billing_state,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.billing_zip,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.bank_name,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.masked_bank_routing_number,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.masked_bank_account_number,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.bank_account_type,
                    type_callable=lambda value:
                        BankAccountType.validate(value)) \
                and APIHelper.is_valid_type(
                    value=dictionary.bank_account_holder_type,
                    type_callable=lambda value:
                        BankAccountHolderType.validate(value)) \
                and APIHelper.is_valid_type(
                    value=dictionary.payment_type,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.disabled,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        bool,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.site_gateway_setting_id,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        int,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("first_name"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("last_name"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("current_vault"),
                type_callable=lambda value:
                    BankAccountVault.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("vault_token"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("billing_address"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("billing_city"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("billing_country"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("billing_state"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("billing_zip"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("bank_name"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("masked_bank_routing_number"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("masked_bank_account_number"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("bank_account_type"),
                type_callable=lambda value:
                    BankAccountType.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("bank_account_holder_type"),
                type_callable=lambda value:
                    BankAccountHolderType.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("payment_type"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("disabled"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    bool,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("site_gateway_setting_id"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    int,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _first_name=self.first_name
        _last_name=self.last_name
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
        _bank_name=self.bank_name
        _masked_bank_routing_number=self.masked_bank_routing_number
        _masked_bank_account_number=self.masked_bank_account_number
        _bank_account_type=self.bank_account_type
        _bank_account_holder_type=self.bank_account_holder_type
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
        _verified=(
            self.verified
            if hasattr(self, "verified")
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
            f"billing_address_2={_billing_address_2!r}, "
            f"billing_city={_billing_city!r}, "
            f"billing_country={_billing_country!r}, "
            f"billing_state={_billing_state!r}, "
            f"billing_zip={_billing_zip!r}, "
            f"bank_name={_bank_name!r}, "
            f"masked_bank_routing_number={_masked_bank_routing_number!r}, "
            f"masked_bank_account_number={_masked_bank_account_number!r}, "
            f"bank_account_type={_bank_account_type!r}, "
            f"bank_account_holder_type={_bank_account_holder_type!r}, "
            f"payment_type={_payment_type!r}, "
            f"disabled={_disabled!r}, "
            f"site_gateway_setting_id={_site_gateway_setting_id!r}, "
            f"customer_vault_token={_customer_vault_token!r}, "
            f"gateway_handle={_gateway_handle!r}, "
            f"verified={_verified!r}, "
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
        _bank_name=self.bank_name
        _masked_bank_routing_number=self.masked_bank_routing_number
        _masked_bank_account_number=self.masked_bank_account_number
        _bank_account_type=self.bank_account_type
        _bank_account_holder_type=self.bank_account_holder_type
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
        _verified=(
            self.verified
            if hasattr(self, "verified")
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
            f"billing_address_2={_billing_address_2!s}, "
            f"billing_city={_billing_city!s}, "
            f"billing_country={_billing_country!s}, "
            f"billing_state={_billing_state!s}, "
            f"billing_zip={_billing_zip!s}, "
            f"bank_name={_bank_name!s}, "
            f"masked_bank_routing_number={_masked_bank_routing_number!s}, "
            f"masked_bank_account_number={_masked_bank_account_number!s}, "
            f"bank_account_type={_bank_account_type!s}, "
            f"bank_account_holder_type={_bank_account_holder_type!s}, "
            f"payment_type={_payment_type!s}, "
            f"disabled={_disabled!s}, "
            f"site_gateway_setting_id={_site_gateway_setting_id!s}, "
            f"customer_vault_token={_customer_vault_token!s}, "
            f"gateway_handle={_gateway_handle!s}, "
            f"verified={_verified!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
