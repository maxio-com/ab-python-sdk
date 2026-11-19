"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class WalletRecurringFunding(object):
    """Implementation of the 'Wallet Recurring Funding' model.

    Describes automatic funding of the wallet from a usage-limit entitlement. Set up
    by configuring `wallet_behavior` on the Feature behind that entitlement, not by
    any parameter on the wallet itself. This field is an array as of its first
    release. The array currently holds zero or one element, and is expected to hold
    several once a wallet can be funded by more than one entitlement.

    Attributes:
        id (int): The Advanced Billing id of the recurring funding schedule.
        entitlement_id (int): The usage-limit entitlement this schedule reads its
            allowance and cadence from.
        allowance (str): The entitlement's current allowance, read fresh at request
            time rather than stored on the wallet. Editing the entitlement changes
            this immediately, with no separate sync step. `"0"` means the entitlement
            is configured to grant nothing, a valid, working configuration and not an
            error. `null` when `status` is `stopped`, since there is no longer an
            entitlement to read.
        next_grant_at (datetime): When the next automatic grant is due. Grants are
            applied by a background process shortly after this moment passes, not
            exactly on it, so a wallet read taken in that window still shows the
            pre-grant balance. `null` when `status` is `stopped`, and also `null`
            once the owning subscription has terminated, even while `status` is still
            `active`: at its next due moment the schedule is stopped with reason
            `subscription_terminated`.
        next_grant_on (date): The calendar day `next_grant_at` falls on, resolved in
            the site's time zone. `null` under the same conditions as `next_grant_at`.
        skipped_periods (int): Cumulative count of due moments that passed without a
            grant being made (for example, during an outage). A gap in funding is
            visible here without cross-referencing the ledger.
        status (WalletRecurringFundingStatus): `active`: refilling normally.
            `erroring`: the schedule is still due and retrying, but the last attempt
            couldn't be written (see `reason`); correcting the underlying entitlement
            resumes funding on the next run with no action needed on the wallet
            itself. `stopped`: funding has ended for good (see `reason`); units
            already granted stay on the wallet and remain spendable, but no further
            automatic grants will be made.
        reason (Reason): Set whenever `status` isn't `active`. Accompanying
            `stopped`: `entitlement_missing` (an ordinary product or component change
            removed the entitlement), `wallet_archived` (the wallet was archived),
            `subscription_terminated` (the subscription reached a terminal state;
            funding resumes if the subscription returns to a granting state, for
            example on reactivation, without back-granting the periods it missed),
            `feature_removed` (the subscription no longer has this Feature),
            `wallet_behavior_disabled` (the Feature no longer has `wallet_behavior`
            configured), `superseded_by_replacement` (a later entitlement now funds
            this wallet instead), or `subscription_prepaid` (the subscription
            switched to prepaid, which cannot carry an active wallet). Accompanying
            `erroring`: `allowance_not_representable` (the entitlement's current
            allowance doesn't fit the wallet's amount encoding) or
            `balance_at_capacity` (granting it would push the balance past the
            maximum supported value).
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "entitlement_id": "entitlement_id",
        "allowance": "allowance",
        "next_grant_at": "next_grant_at",
        "next_grant_on": "next_grant_on",
        "skipped_periods": "skipped_periods",
        "status": "status",
        "reason": "reason",
    }

    _optionals = [
        "id",
        "entitlement_id",
        "allowance",
        "next_grant_at",
        "next_grant_on",
        "skipped_periods",
        "status",
        "reason",
    ]

    _nullables = [
        "allowance",
        "next_grant_at",
        "next_grant_on",
        "reason",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        entitlement_id=APIHelper.SKIP,
        allowance=APIHelper.SKIP,
        next_grant_at=APIHelper.SKIP,
        next_grant_on=APIHelper.SKIP,
        skipped_periods=APIHelper.SKIP,
        status=APIHelper.SKIP,
        reason=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletRecurringFunding instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if entitlement_id is not APIHelper.SKIP:
            self.entitlement_id = entitlement_id
        if allowance is not APIHelper.SKIP:
            self.allowance = allowance
        if next_grant_at is not APIHelper.SKIP:
            self.next_grant_at =\
                 APIHelper.apply_datetime_converter(
                next_grant_at, APIHelper.RFC3339DateTime)\
                 if next_grant_at else None
        if next_grant_on is not APIHelper.SKIP:
            self.next_grant_on = next_grant_on
        if skipped_periods is not APIHelper.SKIP:
            self.skipped_periods = skipped_periods
        if status is not APIHelper.SKIP:
            self.status = status
        if reason is not APIHelper.SKIP:
            self.reason = reason

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
        entitlement_id =\
            dictionary.get("entitlement_id")\
            if dictionary.get("entitlement_id")\
                else APIHelper.SKIP
        allowance =\
            dictionary.get("allowance")\
            if "allowance" in dictionary.keys()\
                else APIHelper.SKIP
        if "next_grant_at" in dictionary.keys():
            next_grant_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("next_grant_at")).datetime\
                if dictionary.get("next_grant_at") else None

        else:
            next_grant_at = APIHelper.SKIP
        if "next_grant_on" in dictionary.keys():
            next_grant_on = dateutil.parser.parse(
                dictionary.get("next_grant_on")).date()\
                if dictionary.get("next_grant_on") else None

        else:
            next_grant_on = APIHelper.SKIP
        skipped_periods =\
            dictionary.get("skipped_periods")\
            if dictionary.get("skipped_periods")\
                else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        reason =\
            dictionary.get("reason")\
            if "reason" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   entitlement_id,
                   allowance,
                   next_grant_at,
                   next_grant_on,
                   skipped_periods,
                   status,
                   reason,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _entitlement_id=(
            self.entitlement_id
            if hasattr(self, "entitlement_id")
            else None
        )
        _allowance=(
            self.allowance
            if hasattr(self, "allowance")
            else None
        )
        _next_grant_at=(
            self.next_grant_at
            if hasattr(self, "next_grant_at")
            else None
        )
        _next_grant_on=(
            self.next_grant_on
            if hasattr(self, "next_grant_on")
            else None
        )
        _skipped_periods=(
            self.skipped_periods
            if hasattr(self, "skipped_periods")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"entitlement_id={_entitlement_id!r}, "
            f"allowance={_allowance!r}, "
            f"next_grant_at={_next_grant_at!r}, "
            f"next_grant_on={_next_grant_on!r}, "
            f"skipped_periods={_skipped_periods!r}, "
            f"status={_status!r}, "
            f"reason={_reason!r}, "
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
        _entitlement_id=(
            self.entitlement_id
            if hasattr(self, "entitlement_id")
            else None
        )
        _allowance=(
            self.allowance
            if hasattr(self, "allowance")
            else None
        )
        _next_grant_at=(
            self.next_grant_at
            if hasattr(self, "next_grant_at")
            else None
        )
        _next_grant_on=(
            self.next_grant_on
            if hasattr(self, "next_grant_on")
            else None
        )
        _skipped_periods=(
            self.skipped_periods
            if hasattr(self, "skipped_periods")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"entitlement_id={_entitlement_id!s}, "
            f"allowance={_allowance!s}, "
            f"next_grant_at={_next_grant_at!s}, "
            f"next_grant_on={_next_grant_on!s}, "
            f"skipped_periods={_skipped_periods!s}, "
            f"status={_status!s}, "
            f"reason={_reason!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
