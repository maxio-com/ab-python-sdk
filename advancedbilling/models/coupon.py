# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.coupon_restriction import CouponRestriction


class Coupon(object):

    """Implementation of the 'Coupon' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (str): TODO: type description here.
        code (str): TODO: type description here.
        description (str): TODO: type description here.
        amount (float): TODO: type description here.
        amount_in_cents (int): TODO: type description here.
        product_family_id (int): TODO: type description here.
        product_family_name (str): TODO: type description here.
        start_date (str): TODO: type description here.
        end_date (str): TODO: type description here.
        percentage (float): TODO: type description here.
        recurring (bool): TODO: type description here.
        recurring_scheme (RecurringScheme): TODO: type description here.
        duration_period_count (int): TODO: type description here.
        duration_interval (int): TODO: type description here.
        duration_interval_unit (str): TODO: type description here.
        duration_interval_span (str): TODO: type description here.
        allow_negative_balance (bool): TODO: type description here.
        archived_at (str): TODO: type description here.
        conversion_limit (str): TODO: type description here.
        stackable (bool): TODO: type description here.
        compounding_strategy (CompoundingStrategy | None): TODO: type
            description here.
        use_site_exchange_rate (bool): TODO: type description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.
        discount_type (DiscountType): TODO: type description here.
        exclude_mid_period_allocations (bool): TODO: type description here.
        apply_on_cancel_at_end_of_period (bool): TODO: type description here.
        coupon_restrictions (List[CouponRestriction]): TODO: type description
            here.

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
        "coupon_restrictions": 'coupon_restrictions'
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
        'coupon_restrictions',
    ]

    _nullables = [
        'amount',
        'amount_in_cents',
        'end_date',
        'percentage',
        'duration_period_count',
        'duration_interval',
        'duration_interval_unit',
        'archived_at',
        'conversion_limit',
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
                 coupon_restrictions=APIHelper.SKIP):
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
            self.start_date = start_date 
        if end_date is not APIHelper.SKIP:
            self.end_date = end_date 
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
            self.archived_at = archived_at 
        if conversion_limit is not APIHelper.SKIP:
            self.conversion_limit = conversion_limit 
        if stackable is not APIHelper.SKIP:
            self.stackable = stackable 
        if compounding_strategy is not APIHelper.SKIP:
            self.compounding_strategy = compounding_strategy 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if discount_type is not APIHelper.SKIP:
            self.discount_type = discount_type 
        if exclude_mid_period_allocations is not APIHelper.SKIP:
            self.exclude_mid_period_allocations = exclude_mid_period_allocations 
        if apply_on_cancel_at_end_of_period is not APIHelper.SKIP:
            self.apply_on_cancel_at_end_of_period = apply_on_cancel_at_end_of_period 
        if coupon_restrictions is not APIHelper.SKIP:
            self.coupon_restrictions = coupon_restrictions 

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if "amount_in_cents" in dictionary.keys() else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
        start_date = dictionary.get("start_date") if dictionary.get("start_date") else APIHelper.SKIP
        end_date = dictionary.get("end_date") if "end_date" in dictionary.keys() else APIHelper.SKIP
        percentage = dictionary.get("percentage") if "percentage" in dictionary.keys() else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        recurring_scheme = dictionary.get("recurring_scheme") if dictionary.get("recurring_scheme") else APIHelper.SKIP
        duration_period_count = dictionary.get("duration_period_count") if "duration_period_count" in dictionary.keys() else APIHelper.SKIP
        duration_interval = dictionary.get("duration_interval") if "duration_interval" in dictionary.keys() else APIHelper.SKIP
        duration_interval_unit = dictionary.get("duration_interval_unit") if "duration_interval_unit" in dictionary.keys() else APIHelper.SKIP
        duration_interval_span = dictionary.get("duration_interval_span") if dictionary.get("duration_interval_span") else APIHelper.SKIP
        allow_negative_balance = dictionary.get("allow_negative_balance") if "allow_negative_balance" in dictionary.keys() else APIHelper.SKIP
        archived_at = dictionary.get("archived_at") if "archived_at" in dictionary.keys() else APIHelper.SKIP
        conversion_limit = dictionary.get("conversion_limit") if "conversion_limit" in dictionary.keys() else APIHelper.SKIP
        stackable = dictionary.get("stackable") if "stackable" in dictionary.keys() else APIHelper.SKIP
        compounding_strategy = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CouponCompoundingStrategy'), dictionary.get('compounding_strategy'), False) if dictionary.get('compounding_strategy') is not None else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        discount_type = dictionary.get("discount_type") if dictionary.get("discount_type") else APIHelper.SKIP
        exclude_mid_period_allocations = dictionary.get("exclude_mid_period_allocations") if "exclude_mid_period_allocations" in dictionary.keys() else APIHelper.SKIP
        apply_on_cancel_at_end_of_period = dictionary.get("apply_on_cancel_at_end_of_period") if "apply_on_cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        coupon_restrictions = None
        if dictionary.get('coupon_restrictions') is not None:
            coupon_restrictions = [CouponRestriction.from_dictionary(x) for x in dictionary.get('coupon_restrictions')]
        else:
            coupon_restrictions = APIHelper.SKIP
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
                   coupon_restrictions)
