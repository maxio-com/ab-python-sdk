# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.coupon_currency import CouponCurrency
from advancedbilling.models.coupon_restriction import CouponRestriction


class Coupon(object):

    """Implementation of the 'Coupon' model.

    Attributes:
        id (int): The model property of type int.
        name (str): The model property of type str.
        code (str): The model property of type str.
        description (str): The model property of type str.
        amount (float): The model property of type float.
        amount_in_cents (int): The model property of type int.
        product_family_id (int): The model property of type int.
        product_family_name (str): The model property of type str.
        start_date (datetime): The model property of type datetime.
        end_date (datetime): After the given time, this coupon code will be
            invalid for new signups. Recurring discounts started before this
            date will continue to recur even after this date.
        percentage (str): The model property of type str.
        recurring (bool): The model property of type bool.
        recurring_scheme (RecurringScheme): The model property of type
            RecurringScheme.
        duration_period_count (int): The model property of type int.
        duration_interval (int): The model property of type int.
        duration_interval_unit (str): The model property of type str.
        duration_interval_span (str): The model property of type str.
        allow_negative_balance (bool): If set to true, discount is not limited
            (credits will carry forward to next billing).
        archived_at (datetime): The model property of type datetime.
        conversion_limit (str): The model property of type str.
        stackable (bool): A stackable coupon can be combined with other
            coupons on a Subscription.
        compounding_strategy (CompoundingStrategy): Applicable only to
            stackable coupons. For `compound`, Percentage-based discounts will
            be calculated against the remaining price, after prior discounts
            have been calculated. For `full-price`, Percentage-based discounts
            will always be calculated against the original item price, before
            other discounts are applied.
        use_site_exchange_rate (bool): The model property of type bool.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        discount_type (DiscountType): The model property of type DiscountType.
        exclude_mid_period_allocations (bool): The model property of type bool.
        apply_on_cancel_at_end_of_period (bool): The model property of type
            bool.
        apply_on_subscription_expiration (bool): The model property of type
            bool.
        coupon_restrictions (List[CouponRestriction]): The model property of
            type List[CouponRestriction].
        currency_prices (List[CouponCurrency]): Returned in read, find, and
            list endpoints if the query parameter is provided.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "code": 'code',
        "description": 'description',
        "amount": 'amount',
        "amount_in_cents": 'amount_in_cents',
        "product_family_id": 'product_family_id',
        "product_family_name": 'product_family_name',
        "start_date": 'start_date',
        "end_date": 'end_date',
        "percentage": 'percentage',
        "recurring": 'recurring',
        "recurring_scheme": 'recurring_scheme',
        "duration_period_count": 'duration_period_count',
        "duration_interval": 'duration_interval',
        "duration_interval_unit": 'duration_interval_unit',
        "duration_interval_span": 'duration_interval_span',
        "allow_negative_balance": 'allow_negative_balance',
        "archived_at": 'archived_at',
        "conversion_limit": 'conversion_limit',
        "stackable": 'stackable',
        "compounding_strategy": 'compounding_strategy',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "discount_type": 'discount_type',
        "exclude_mid_period_allocations": 'exclude_mid_period_allocations',
        "apply_on_cancel_at_end_of_period": 'apply_on_cancel_at_end_of_period',
        "apply_on_subscription_expiration": 'apply_on_subscription_expiration',
        "coupon_restrictions": 'coupon_restrictions',
        "currency_prices": 'currency_prices'
    }

    _optionals = [
        'id',
        'name',
        'code',
        'description',
        'amount',
        'amount_in_cents',
        'product_family_id',
        'product_family_name',
        'start_date',
        'end_date',
        'percentage',
        'recurring',
        'recurring_scheme',
        'duration_period_count',
        'duration_interval',
        'duration_interval_unit',
        'duration_interval_span',
        'allow_negative_balance',
        'archived_at',
        'conversion_limit',
        'stackable',
        'compounding_strategy',
        'use_site_exchange_rate',
        'created_at',
        'updated_at',
        'discount_type',
        'exclude_mid_period_allocations',
        'apply_on_cancel_at_end_of_period',
        'apply_on_subscription_expiration',
        'coupon_restrictions',
        'currency_prices',
    ]

    _nullables = [
        'amount',
        'amount_in_cents',
        'product_family_name',
        'end_date',
        'percentage',
        'duration_period_count',
        'duration_interval',
        'duration_interval_unit',
        'duration_interval_span',
        'archived_at',
        'conversion_limit',
        'compounding_strategy',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 product_family_name=APIHelper.SKIP,
                 start_date=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 recurring_scheme=APIHelper.SKIP,
                 duration_period_count=APIHelper.SKIP,
                 duration_interval=APIHelper.SKIP,
                 duration_interval_unit=APIHelper.SKIP,
                 duration_interval_span=APIHelper.SKIP,
                 allow_negative_balance=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 conversion_limit=APIHelper.SKIP,
                 stackable=APIHelper.SKIP,
                 compounding_strategy=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 discount_type=APIHelper.SKIP,
                 exclude_mid_period_allocations=APIHelper.SKIP,
                 apply_on_cancel_at_end_of_period=APIHelper.SKIP,
                 apply_on_subscription_expiration=APIHelper.SKIP,
                 coupon_restrictions=APIHelper.SKIP,
                 currency_prices=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Coupon class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if product_family_name is not APIHelper.SKIP:
            self.product_family_name = product_family_name 
        if start_date is not APIHelper.SKIP:
            self.start_date = APIHelper.apply_datetime_converter(start_date, APIHelper.RFC3339DateTime) if start_date else None 
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.apply_datetime_converter(end_date, APIHelper.RFC3339DateTime) if end_date else None 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if recurring_scheme is not APIHelper.SKIP:
            self.recurring_scheme = recurring_scheme 
        if duration_period_count is not APIHelper.SKIP:
            self.duration_period_count = duration_period_count 
        if duration_interval is not APIHelper.SKIP:
            self.duration_interval = duration_interval 
        if duration_interval_unit is not APIHelper.SKIP:
            self.duration_interval_unit = duration_interval_unit 
        if duration_interval_span is not APIHelper.SKIP:
            self.duration_interval_span = duration_interval_span 
        if allow_negative_balance is not APIHelper.SKIP:
            self.allow_negative_balance = allow_negative_balance 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = APIHelper.apply_datetime_converter(archived_at, APIHelper.RFC3339DateTime) if archived_at else None 
        if conversion_limit is not APIHelper.SKIP:
            self.conversion_limit = conversion_limit 
        if stackable is not APIHelper.SKIP:
            self.stackable = stackable 
        if compounding_strategy is not APIHelper.SKIP:
            self.compounding_strategy = compounding_strategy 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if discount_type is not APIHelper.SKIP:
            self.discount_type = discount_type 
        if exclude_mid_period_allocations is not APIHelper.SKIP:
            self.exclude_mid_period_allocations = exclude_mid_period_allocations 
        if apply_on_cancel_at_end_of_period is not APIHelper.SKIP:
            self.apply_on_cancel_at_end_of_period = apply_on_cancel_at_end_of_period 
        if apply_on_subscription_expiration is not APIHelper.SKIP:
            self.apply_on_subscription_expiration = apply_on_subscription_expiration 
        if coupon_restrictions is not APIHelper.SKIP:
            self.coupon_restrictions = coupon_restrictions 
        if currency_prices is not APIHelper.SKIP:
            self.currency_prices = currency_prices 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if "amount_in_cents" in dictionary.keys() else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if "product_family_name" in dictionary.keys() else APIHelper.SKIP
        start_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_date")).datetime if dictionary.get("start_date") else APIHelper.SKIP
        if 'end_date' in dictionary.keys():
            end_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_date")).datetime if dictionary.get("end_date") else None
        else:
            end_date = APIHelper.SKIP
        percentage = dictionary.get("percentage") if "percentage" in dictionary.keys() else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        recurring_scheme = dictionary.get("recurring_scheme") if dictionary.get("recurring_scheme") else APIHelper.SKIP
        duration_period_count = dictionary.get("duration_period_count") if "duration_period_count" in dictionary.keys() else APIHelper.SKIP
        duration_interval = dictionary.get("duration_interval") if "duration_interval" in dictionary.keys() else APIHelper.SKIP
        duration_interval_unit = dictionary.get("duration_interval_unit") if "duration_interval_unit" in dictionary.keys() else APIHelper.SKIP
        duration_interval_span = dictionary.get("duration_interval_span") if "duration_interval_span" in dictionary.keys() else APIHelper.SKIP
        allow_negative_balance = dictionary.get("allow_negative_balance") if "allow_negative_balance" in dictionary.keys() else APIHelper.SKIP
        if 'archived_at' in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("archived_at")).datetime if dictionary.get("archived_at") else None
        else:
            archived_at = APIHelper.SKIP
        conversion_limit = dictionary.get("conversion_limit") if "conversion_limit" in dictionary.keys() else APIHelper.SKIP
        stackable = dictionary.get("stackable") if "stackable" in dictionary.keys() else APIHelper.SKIP
        compounding_strategy = dictionary.get("compounding_strategy") if "compounding_strategy" in dictionary.keys() else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        discount_type = dictionary.get("discount_type") if dictionary.get("discount_type") else APIHelper.SKIP
        exclude_mid_period_allocations = dictionary.get("exclude_mid_period_allocations") if "exclude_mid_period_allocations" in dictionary.keys() else APIHelper.SKIP
        apply_on_cancel_at_end_of_period = dictionary.get("apply_on_cancel_at_end_of_period") if "apply_on_cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        apply_on_subscription_expiration = dictionary.get("apply_on_subscription_expiration") if "apply_on_subscription_expiration" in dictionary.keys() else APIHelper.SKIP
        coupon_restrictions = None
        if dictionary.get('coupon_restrictions') is not None:
            coupon_restrictions = [CouponRestriction.from_dictionary(x) for x in dictionary.get('coupon_restrictions')]
        else:
            coupon_restrictions = APIHelper.SKIP
        currency_prices = None
        if dictionary.get('currency_prices') is not None:
            currency_prices = [CouponCurrency.from_dictionary(x) for x in dictionary.get('currency_prices')]
        else:
            currency_prices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   code,
                   description,
                   amount,
                   amount_in_cents,
                   product_family_id,
                   product_family_name,
                   start_date,
                   end_date,
                   percentage,
                   recurring,
                   recurring_scheme,
                   duration_period_count,
                   duration_interval,
                   duration_interval_unit,
                   duration_interval_span,
                   allow_negative_balance,
                   archived_at,
                   conversion_limit,
                   stackable,
                   compounding_strategy,
                   use_site_exchange_rate,
                   created_at,
                   updated_at,
                   discount_type,
                   exclude_mid_period_allocations,
                   apply_on_cancel_at_end_of_period,
                   apply_on_subscription_expiration,
                   coupon_restrictions,
                   currency_prices,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'product_family_id={(self.product_family_id if hasattr(self, "product_family_id") else None)!r}, '
                f'product_family_name={(self.product_family_name if hasattr(self, "product_family_name") else None)!r}, '
                f'start_date={(self.start_date if hasattr(self, "start_date") else None)!r}, '
                f'end_date={(self.end_date if hasattr(self, "end_date") else None)!r}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!r}, '
                f'recurring={(self.recurring if hasattr(self, "recurring") else None)!r}, '
                f'recurring_scheme={(self.recurring_scheme if hasattr(self, "recurring_scheme") else None)!r}, '
                f'duration_period_count={(self.duration_period_count if hasattr(self, "duration_period_count") else None)!r}, '
                f'duration_interval={(self.duration_interval if hasattr(self, "duration_interval") else None)!r}, '
                f'duration_interval_unit={(self.duration_interval_unit if hasattr(self, "duration_interval_unit") else None)!r}, '
                f'duration_interval_span={(self.duration_interval_span if hasattr(self, "duration_interval_span") else None)!r}, '
                f'allow_negative_balance={(self.allow_negative_balance if hasattr(self, "allow_negative_balance") else None)!r}, '
                f'archived_at={(self.archived_at if hasattr(self, "archived_at") else None)!r}, '
                f'conversion_limit={(self.conversion_limit if hasattr(self, "conversion_limit") else None)!r}, '
                f'stackable={(self.stackable if hasattr(self, "stackable") else None)!r}, '
                f'compounding_strategy={(self.compounding_strategy if hasattr(self, "compounding_strategy") else None)!r}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'discount_type={(self.discount_type if hasattr(self, "discount_type") else None)!r}, '
                f'exclude_mid_period_allocations={(self.exclude_mid_period_allocations if hasattr(self, "exclude_mid_period_allocations") else None)!r}, '
                f'apply_on_cancel_at_end_of_period={(self.apply_on_cancel_at_end_of_period if hasattr(self, "apply_on_cancel_at_end_of_period") else None)!r}, '
                f'apply_on_subscription_expiration={(self.apply_on_subscription_expiration if hasattr(self, "apply_on_subscription_expiration") else None)!r}, '
                f'coupon_restrictions={(self.coupon_restrictions if hasattr(self, "coupon_restrictions") else None)!r}, '
                f'currency_prices={(self.currency_prices if hasattr(self, "currency_prices") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'product_family_id={(self.product_family_id if hasattr(self, "product_family_id") else None)!s}, '
                f'product_family_name={(self.product_family_name if hasattr(self, "product_family_name") else None)!s}, '
                f'start_date={(self.start_date if hasattr(self, "start_date") else None)!s}, '
                f'end_date={(self.end_date if hasattr(self, "end_date") else None)!s}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!s}, '
                f'recurring={(self.recurring if hasattr(self, "recurring") else None)!s}, '
                f'recurring_scheme={(self.recurring_scheme if hasattr(self, "recurring_scheme") else None)!s}, '
                f'duration_period_count={(self.duration_period_count if hasattr(self, "duration_period_count") else None)!s}, '
                f'duration_interval={(self.duration_interval if hasattr(self, "duration_interval") else None)!s}, '
                f'duration_interval_unit={(self.duration_interval_unit if hasattr(self, "duration_interval_unit") else None)!s}, '
                f'duration_interval_span={(self.duration_interval_span if hasattr(self, "duration_interval_span") else None)!s}, '
                f'allow_negative_balance={(self.allow_negative_balance if hasattr(self, "allow_negative_balance") else None)!s}, '
                f'archived_at={(self.archived_at if hasattr(self, "archived_at") else None)!s}, '
                f'conversion_limit={(self.conversion_limit if hasattr(self, "conversion_limit") else None)!s}, '
                f'stackable={(self.stackable if hasattr(self, "stackable") else None)!s}, '
                f'compounding_strategy={(self.compounding_strategy if hasattr(self, "compounding_strategy") else None)!s}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'discount_type={(self.discount_type if hasattr(self, "discount_type") else None)!s}, '
                f'exclude_mid_period_allocations={(self.exclude_mid_period_allocations if hasattr(self, "exclude_mid_period_allocations") else None)!s}, '
                f'apply_on_cancel_at_end_of_period={(self.apply_on_cancel_at_end_of_period if hasattr(self, "apply_on_cancel_at_end_of_period") else None)!s}, '
                f'apply_on_subscription_expiration={(self.apply_on_subscription_expiration if hasattr(self, "apply_on_subscription_expiration") else None)!s}, '
                f'coupon_restrictions={(self.coupon_restrictions if hasattr(self, "coupon_restrictions") else None)!s}, '
                f'currency_prices={(self.currency_prices if hasattr(self, "currency_prices") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
