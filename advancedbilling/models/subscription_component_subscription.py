# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionComponentSubscription(object):

    """Implementation of the 'Subscription Component Subscription' model.

    An optional object, will be returned if provided `include=subscription`
    query param.

    Attributes:
        state (SubscriptionState): The state of a subscription. * **Live
            States**     * `active` - A normal, active subscription. It is not
            in a trial and is paid and up to date.     * `assessing` - An
            internal (transient) state that indicates a subscription is in the
            middle of periodic assessment. Do not base any access decisions in
            your app on this state, as it may not always be exposed.     *
            `pending` - An internal (transient) state that indicates a
            subscription is in the creation process. Do not base any access
            decisions in your app on this state, as it may not always be
            exposed.     * `trialing` - A subscription in trialing state has a
            valid trial subscription. This type of subscription may transition
            to active once payment is received when the trial has ended.
            Otherwise, it may go to a Problem or End of Life state.     *
            `paused` - An internal state that indicates that your account with
            Advanced Billing is in arrears. * **Problem States**     *
            `past_due` - Indicates that the most recent payment has failed,
            and payment is past due for this subscription. If you have enabled
            our automated dunning, this subscription will be in the dunning
            process (additional status and callbacks from the dunning process
            will be available in the future). If you are handling dunning and
            payment updates yourself, you will want to use this state to
            initiate a payment update from your customers.     *
            `soft_failure` - Indicates that normal assessment/processing of
            the subscription has failed for a reason that cannot be fixed by
            the Customer. For example, a Soft Fail may result from a timeout
            at the gateway or incorrect credentials on your part. The
            subscriptions should be retried automatically. An interface is
            being built for you to review problems resulting from these events
            to take manual action when needed.     * `unpaid` - Indicates an
            unpaid subscription. A subscription is marked unpaid if the retry
            period expires and you have configured your
            [Dunning](https://maxio.zendesk.com/hc/en-us/articles/2428707658356
            5-Dunning-Overview) settings to have a Final Action of `mark the
            subscription unpaid`. * **End of Life States**     * `canceled` -
            Indicates a canceled subscription. This may happen at your request
            (via the API or the web interface) or due to the expiration of the
            [Dunning](https://maxio.zendesk.com/hc/en-us/articles/2428707658356
            5-Dunning-Overview) process without payment. See the
            [Reactivation](https://maxio.zendesk.com/hc/en-us/articles/24252109
            503629-Reactivating-and-Resuming) documentation for info on how to
            restart a canceled subscription.     While a subscription is
            canceled, its period will not advance, it will not accrue any new
            charges, and Advanced Billing will not attempt to collect the
            overdue balance.     * `expired` - Indicates a subscription that
            has expired due to running its normal life cycle. Some products
            may be configured to have an expiration period. An expired
            subscription then is one that stayed active until it fulfilled its
            full period.     * `failed_to_create` - Indicates that signup has
            failed. (You may see this state in a signup_failure webhook.)    
            * `on_hold` - Indicates that a subscription’s billing has been
            temporarily stopped. While it is expected that the subscription
            will resume and return to active status, this is still treated as
            an “End of Life” state because the customer is not paying for
            services during this time.     * `suspended` - Indicates that a
            prepaid subscription has used up all their prepayment balance. If
            a prepayment is applied, it will return to an active state.     *
            `trial_ended` - A subscription in a trial_ended state is a
            subscription that completed a no-obligation trial and did not have
            a card on file at the expiration of the trial period. See [Product
            Pricing – No Obligation
            Trials](https://maxio.zendesk.com/hc/en-us/articles/24261076617869-
            Product-Editing) for more details.  See [Subscription
            States](https://maxio.zendesk.com/hc/en-us/articles/24252119027853-
            Subscription-States) for more info about subscription states and
            state transitions.
        updated_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "state": 'state',
        "updated_at": 'updated_at'
    }

    _optionals = [
        'state',
        'updated_at',
    ]

    def __init__(self,
                 state=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionComponentSubscription class"""

        # Initialize members of the class
        if state is not APIHelper.SKIP:
            self.state = state 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

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
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(state,
                   updated_at,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

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
        return (f'{self.__class__.__name__}('
                f'state={self.state!r}, '
                f'updated_at={self.updated_at!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'state={self.state!s}, '
                f'updated_at={self.updated_at!s}, '
                f'additional_properties={self.additional_properties!s})')
