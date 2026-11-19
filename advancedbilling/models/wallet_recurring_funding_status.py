"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class WalletRecurringFundingStatus(object):
    """Implementation of the 'Wallet Recurring Funding Status' enum.

    `active`: refilling normally. `erroring`: the schedule is still due and retrying,
    but the last attempt couldn't be written (see `reason`); correcting the
    underlying entitlement resumes funding on the next run with no action needed on
    the wallet itself. `stopped`: funding has ended for good (see `reason`); units
    already granted stay on the wallet and remain spendable, but no further automatic
    grants will be made.

    Attributes:
        ACTIVE: The enum member of type str.
        ERRORING: The enum member of type str.
        STOPPED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    ACTIVE = "active"

    ERRORING = "erroring"

    STOPPED = "stopped"

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
