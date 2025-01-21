# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class CouponPayload(object):

    """Implementation of the 'Coupon Payload' model.

    Attributes:
        name (str): Required when creating a new coupon. This name is not
            displayed to customers and is limited to 255 characters.
        code (str): Required when creating a new coupon. The code is limited
            to 255 characters. May contain uppercase alphanumeric characters
            and these special characters (which allow for email addresses to
            be used): “%”, “@”, “+”, “-”, “_”, and “.”
        description (str): Required when creating a new coupon. A description
            of the coupon that can be displayed to customers in transactions
            and on statements. The description is limited to 255 characters.
        percentage (str | float | None): Required when creating a new
            percentage coupon. Can't be used together with amount_in_cents.
            Percentage discount
        amount_in_cents (int): Required when creating a new flat amount
            coupon. Can't be used together with percentage. Flat USD discount
        allow_negative_balance (bool): If set to true, discount is not limited
            (credits will carry forward to next billing). Can't be used
            together with restrictions.
        recurring (bool): The model property of type bool.
        end_date (date): After the end of the given day, this coupon code will
            be invalid for new signups. Recurring discounts started before
            this date will continue to recur even after this date.
        product_family_id (str): The model property of type str.
        stackable (bool): A stackable coupon can be combined with other
            coupons on a Subscription.
        compounding_strategy (CompoundingStrategy): Applicable only to
            stackable coupons. For `compound`, Percentage-based discounts will
            be calculated against the remaining price, after prior discounts
            have been calculated. For `full-price`, Percentage-based discounts
            will always be calculated against the original item price, before
            other discounts are applied.
        exclude_mid_period_allocations (bool): The model property of type bool.
        apply_on_cancel_at_end_of_period (bool): The model property of type
            bool.
        apply_on_subscription_expiration (bool): The model property of type
            bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "code": 'code',
        "description": 'description',
        "percentage": 'percentage',
        "amount_in_cents": 'amount_in_cents',
        "allow_negative_balance": 'allow_negative_balance',
        "recurring": 'recurring',
        "end_date": 'end_date',
        "product_family_id": 'product_family_id',
        "stackable": 'stackable',
        "compounding_strategy": 'compounding_strategy',
        "exclude_mid_period_allocations": 'exclude_mid_period_allocations',
        "apply_on_cancel_at_end_of_period": 'apply_on_cancel_at_end_of_period',
        "apply_on_subscription_expiration": 'apply_on_subscription_expiration'
    }

    _optionals = [
        'name',
        'code',
        'description',
        'percentage',
        'amount_in_cents',
        'allow_negative_balance',
        'recurring',
        'end_date',
        'product_family_id',
        'stackable',
        'compounding_strategy',
        'exclude_mid_period_allocations',
        'apply_on_cancel_at_end_of_period',
        'apply_on_subscription_expiration',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 allow_negative_balance=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 stackable=APIHelper.SKIP,
                 compounding_strategy=APIHelper.SKIP,
                 exclude_mid_period_allocations=APIHelper.SKIP,
                 apply_on_cancel_at_end_of_period=APIHelper.SKIP,
                 apply_on_subscription_expiration=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CouponPayload class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if allow_negative_balance is not APIHelper.SKIP:
            self.allow_negative_balance = allow_negative_balance 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if end_date is not APIHelper.SKIP:
            self.end_date = end_date 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if stackable is not APIHelper.SKIP:
            self.stackable = stackable 
        if compounding_strategy is not APIHelper.SKIP:
            self.compounding_strategy = compounding_strategy 
        if exclude_mid_period_allocations is not APIHelper.SKIP:
            self.exclude_mid_period_allocations = exclude_mid_period_allocations 
        if apply_on_cancel_at_end_of_period is not APIHelper.SKIP:
            self.apply_on_cancel_at_end_of_period = apply_on_cancel_at_end_of_period 
        if apply_on_subscription_expiration is not APIHelper.SKIP:
            self.apply_on_subscription_expiration = apply_on_subscription_expiration 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        percentage = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CouponPayloadPercentage'), dictionary.get('percentage'), False) if dictionary.get('percentage') is not None else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        allow_negative_balance = dictionary.get("allow_negative_balance") if "allow_negative_balance" in dictionary.keys() else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        end_date = dateutil.parser.parse(dictionary.get('end_date')).date() if dictionary.get('end_date') else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        stackable = dictionary.get("stackable") if "stackable" in dictionary.keys() else APIHelper.SKIP
        compounding_strategy = dictionary.get("compounding_strategy") if dictionary.get("compounding_strategy") else APIHelper.SKIP
        exclude_mid_period_allocations = dictionary.get("exclude_mid_period_allocations") if "exclude_mid_period_allocations" in dictionary.keys() else APIHelper.SKIP
        apply_on_cancel_at_end_of_period = dictionary.get("apply_on_cancel_at_end_of_period") if "apply_on_cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        apply_on_subscription_expiration = dictionary.get("apply_on_subscription_expiration") if "apply_on_subscription_expiration" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   code,
                   description,
                   percentage,
                   amount_in_cents,
                   allow_negative_balance,
                   recurring,
                   end_date,
                   product_family_id,
                   stackable,
                   compounding_strategy,
                   exclude_mid_period_allocations,
                   apply_on_cancel_at_end_of_period,
                   apply_on_subscription_expiration,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'code={self.code!r}, '
                f'description={self.description!r}, '
                f'percentage={self.percentage!r}, '
                f'amount_in_cents={self.amount_in_cents!r}, '
                f'allow_negative_balance={self.allow_negative_balance!r}, '
                f'recurring={self.recurring!r}, '
                f'end_date={self.end_date!r}, '
                f'product_family_id={self.product_family_id!r}, '
                f'stackable={self.stackable!r}, '
                f'compounding_strategy={self.compounding_strategy!r}, '
                f'exclude_mid_period_allocations={self.exclude_mid_period_allocations!r}, '
                f'apply_on_cancel_at_end_of_period={self.apply_on_cancel_at_end_of_period!r}, '
                f'apply_on_subscription_expiration={self.apply_on_subscription_expiration!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'code={self.code!s}, '
                f'description={self.description!s}, '
                f'percentage={self.percentage!s}, '
                f'amount_in_cents={self.amount_in_cents!s}, '
                f'allow_negative_balance={self.allow_negative_balance!s}, '
                f'recurring={self.recurring!s}, '
                f'end_date={self.end_date!s}, '
                f'product_family_id={self.product_family_id!s}, '
                f'stackable={self.stackable!s}, '
                f'compounding_strategy={self.compounding_strategy!s}, '
                f'exclude_mid_period_allocations={self.exclude_mid_period_allocations!s}, '
                f'apply_on_cancel_at_end_of_period={self.apply_on_cancel_at_end_of_period!s}, '
                f'apply_on_subscription_expiration={self.apply_on_subscription_expiration!s}, '
                f'additional_properties={self.additional_properties!s})')
