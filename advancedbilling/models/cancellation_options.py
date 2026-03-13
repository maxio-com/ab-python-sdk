"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class CancellationOptions(object):
    """Implementation of the 'Cancellation Options' model.

    Attributes:
        cancellation_message (str): An indication as to why the subscription is being
            canceled. For your internal use.
        reason_code (str): The reason code associated with the cancellation. Use the
            [List Reason Codes]($e/Reason%20Codes/listReasonCodes) endpoint to
            retrieve the reason codes associated with your site.
        cancel_at_end_of_period (bool): When true, the subscription is cancelled at
            the current period end instead of immediately. To use this option, the
            Schedule Subscription Cancellation feature must be enabled on your site.
        scheduled_cancellation_at (datetime): Schedules the cancellation on the
            provided date. This is option is not applicable for prepaid
            subscriptions. To use this option, the Schedule Subscription Cancellation
            feature must be enabled on your site.
        refund_prepayment_account_balance (bool): Applies to prepaid subscriptions.
            When true, which is the default, the remaining prepaid balance is
            refunded as part of cancellation processing. When false, prepaid balance
            is not refunded as part of cancellation processing. To use this option,
            the Schedule Subscription Cancellation feature must be enabled on your
            site.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cancellation_message": "cancellation_message",
        "reason_code": "reason_code",
        "cancel_at_end_of_period": "cancel_at_end_of_period",
        "scheduled_cancellation_at": "scheduled_cancellation_at",
        "refund_prepayment_account_balance": "refund_prepayment_account_balance",
    }

    _optionals = [
        "cancellation_message",
        "reason_code",
        "cancel_at_end_of_period",
        "scheduled_cancellation_at",
        "refund_prepayment_account_balance",
    ]

    _nullables = [
        "scheduled_cancellation_at",
    ]

    def __init__(
        self,
        cancellation_message=APIHelper.SKIP,
        reason_code=APIHelper.SKIP,
        cancel_at_end_of_period=APIHelper.SKIP,
        scheduled_cancellation_at=APIHelper.SKIP,
        refund_prepayment_account_balance=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CancellationOptions instance."""
        # Initialize members of the class
        if cancellation_message is not APIHelper.SKIP:
            self.cancellation_message = cancellation_message
        if reason_code is not APIHelper.SKIP:
            self.reason_code = reason_code
        if cancel_at_end_of_period is not APIHelper.SKIP:
            self.cancel_at_end_of_period = cancel_at_end_of_period
        if scheduled_cancellation_at is not APIHelper.SKIP:
            self.scheduled_cancellation_at =\
                 APIHelper.apply_datetime_converter(
                scheduled_cancellation_at, APIHelper.RFC3339DateTime)\
                 if scheduled_cancellation_at else None
        if refund_prepayment_account_balance is not APIHelper.SKIP:
            self.refund_prepayment_account_balance =\
                 refund_prepayment_account_balance

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
        cancellation_message =\
            dictionary.get("cancellation_message")\
            if dictionary.get("cancellation_message")\
                else APIHelper.SKIP
        reason_code =\
            dictionary.get("reason_code")\
            if dictionary.get("reason_code")\
                else APIHelper.SKIP
        cancel_at_end_of_period =\
            dictionary.get("cancel_at_end_of_period")\
            if "cancel_at_end_of_period" in dictionary.keys()\
                else APIHelper.SKIP
        if "scheduled_cancellation_at" in dictionary.keys():
            scheduled_cancellation_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("scheduled_cancellation_at")).datetime\
                if dictionary.get("scheduled_cancellation_at") else None

        else:
            scheduled_cancellation_at = APIHelper.SKIP
        refund_prepayment_account_balance =\
            dictionary.get("refund_prepayment_account_balance")\
            if "refund_prepayment_account_balance" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(cancellation_message,
                   reason_code,
                   cancel_at_end_of_period,
                   scheduled_cancellation_at,
                   refund_prepayment_account_balance,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _cancellation_message=(
            self.cancellation_message
            if hasattr(self, "cancellation_message")
            else None
        )
        _reason_code=(
            self.reason_code
            if hasattr(self, "reason_code")
            else None
        )
        _cancel_at_end_of_period=(
            self.cancel_at_end_of_period
            if hasattr(self, "cancel_at_end_of_period")
            else None
        )
        _scheduled_cancellation_at=(
            self.scheduled_cancellation_at
            if hasattr(self, "scheduled_cancellation_at")
            else None
        )
        _refund_prepayment_account_balance=(
            self.refund_prepayment_account_balance
            if hasattr(self, "refund_prepayment_account_balance")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cancellation_message={_cancellation_message!r}, "
            f"reason_code={_reason_code!r}, "
            f"cancel_at_end_of_period={_cancel_at_end_of_period!r}, "
            f"scheduled_cancellation_at={_scheduled_cancellation_at!r}, "
            f"refund_prepayment_account_balance={_refund_prepayment_account_balance!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _cancellation_message=(
            self.cancellation_message
            if hasattr(self, "cancellation_message")
            else None
        )
        _reason_code=(
            self.reason_code
            if hasattr(self, "reason_code")
            else None
        )
        _cancel_at_end_of_period=(
            self.cancel_at_end_of_period
            if hasattr(self, "cancel_at_end_of_period")
            else None
        )
        _scheduled_cancellation_at=(
            self.scheduled_cancellation_at
            if hasattr(self, "scheduled_cancellation_at")
            else None
        )
        _refund_prepayment_account_balance=(
            self.refund_prepayment_account_balance
            if hasattr(self, "refund_prepayment_account_balance")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"cancellation_message={_cancellation_message!s}, "
            f"reason_code={_reason_code!s}, "
            f"cancel_at_end_of_period={_cancel_at_end_of_period!s}, "
            f"scheduled_cancellation_at={_scheduled_cancellation_at!s}, "
            f"refund_prepayment_account_balance={_refund_prepayment_account_balance!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
