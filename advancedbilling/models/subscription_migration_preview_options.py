# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.proration import Proration


class SubscriptionMigrationPreviewOptions(object):

    """Implementation of the 'Subscription Migration Preview Options' model.

    Attributes:
        product_id (int): The ID of the target Product. Either a product_id or
            product_handle must be present. A Subscription can be migrated to
            another product for both the current Product Family and another
            Product Family. Note: Going to another Product Family, components
            will not be migrated as well.
        product_price_point_id (int): The ID of the specified product's price
            point. This can be passed to migrate to a non-default price point.
        include_trial (bool): Whether to include the trial period configured
            for the product price point when starting a new billing period.
            Note that if preserve_period is set, then include_trial will be
            ignored.
        include_initial_charge (bool): If `true` is sent initial charges will
            be assessed.
        include_coupons (bool): If `true` is sent, any coupons associated with
            the subscription will be applied to the migration. If `false` is
            sent, coupons will not be applied. Note: When migrating to a new
            product family, the coupon cannot migrate.
        preserve_period (bool): If `false` is sent, the subscription's billing
            period will be reset to today and the full price of the new
            product will be charged. If `true` is sent, the billing period
            will not change and a prorated charge will be issued for the new
            product.
        product_handle (str): The handle of the target Product. Either a
            product_id or product_handle must be present. A Subscription can
            be migrated to another product for both the current Product Family
            and another Product Family. Note: Going to another Product Family,
            components will not be migrated as well.
        product_price_point_handle (str): The ID or handle of the specified
            product's price point. This can be passed to migrate to a
            non-default price point.
        proration (Proration): The model property of type Proration.
        proration_date (datetime): The date that the proration is calculated
            from for the preview
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_id": 'product_id',
        "product_price_point_id": 'product_price_point_id',
        "include_trial": 'include_trial',
        "include_initial_charge": 'include_initial_charge',
        "include_coupons": 'include_coupons',
        "preserve_period": 'preserve_period',
        "product_handle": 'product_handle',
        "product_price_point_handle": 'product_price_point_handle',
        "proration": 'proration',
        "proration_date": 'proration_date'
    }

    _optionals = [
        'product_id',
        'product_price_point_id',
        'include_trial',
        'include_initial_charge',
        'include_coupons',
        'preserve_period',
        'product_handle',
        'product_price_point_handle',
        'proration',
        'proration_date',
    ]

    def __init__(self,
                 product_id=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 include_trial=False,
                 include_initial_charge=False,
                 include_coupons=True,
                 preserve_period=False,
                 product_handle=APIHelper.SKIP,
                 product_price_point_handle=APIHelper.SKIP,
                 proration=APIHelper.SKIP,
                 proration_date=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionMigrationPreviewOptions class"""

        # Initialize members of the class
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        self.include_trial = include_trial 
        self.include_initial_charge = include_initial_charge 
        self.include_coupons = include_coupons 
        self.preserve_period = preserve_period 
        if product_handle is not APIHelper.SKIP:
            self.product_handle = product_handle 
        if product_price_point_handle is not APIHelper.SKIP:
            self.product_price_point_handle = product_price_point_handle 
        if proration is not APIHelper.SKIP:
            self.proration = proration 
        if proration_date is not APIHelper.SKIP:
            self.proration_date = APIHelper.apply_datetime_converter(proration_date, APIHelper.RFC3339DateTime) if proration_date else None 

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
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        include_trial = dictionary.get("include_trial") if dictionary.get("include_trial") else False
        include_initial_charge = dictionary.get("include_initial_charge") if dictionary.get("include_initial_charge") else False
        include_coupons = dictionary.get("include_coupons") if dictionary.get("include_coupons") else True
        preserve_period = dictionary.get("preserve_period") if dictionary.get("preserve_period") else False
        product_handle = dictionary.get("product_handle") if dictionary.get("product_handle") else APIHelper.SKIP
        product_price_point_handle = dictionary.get("product_price_point_handle") if dictionary.get("product_price_point_handle") else APIHelper.SKIP
        proration = Proration.from_dictionary(dictionary.get('proration')) if 'proration' in dictionary.keys() else APIHelper.SKIP
        proration_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("proration_date")).datetime if dictionary.get("proration_date") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(product_id,
                   product_price_point_id,
                   include_trial,
                   include_initial_charge,
                   include_coupons,
                   preserve_period,
                   product_handle,
                   product_price_point_handle,
                   proration,
                   proration_date,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!r}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!r}, '
                f'include_trial={(self.include_trial if hasattr(self, "include_trial") else None)!r}, '
                f'include_initial_charge={(self.include_initial_charge if hasattr(self, "include_initial_charge") else None)!r}, '
                f'include_coupons={(self.include_coupons if hasattr(self, "include_coupons") else None)!r}, '
                f'preserve_period={(self.preserve_period if hasattr(self, "preserve_period") else None)!r}, '
                f'product_handle={(self.product_handle if hasattr(self, "product_handle") else None)!r}, '
                f'product_price_point_handle={(self.product_price_point_handle if hasattr(self, "product_price_point_handle") else None)!r}, '
                f'proration={(self.proration if hasattr(self, "proration") else None)!r}, '
                f'proration_date={(self.proration_date if hasattr(self, "proration_date") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!s}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!s}, '
                f'include_trial={(self.include_trial if hasattr(self, "include_trial") else None)!s}, '
                f'include_initial_charge={(self.include_initial_charge if hasattr(self, "include_initial_charge") else None)!s}, '
                f'include_coupons={(self.include_coupons if hasattr(self, "include_coupons") else None)!s}, '
                f'preserve_period={(self.preserve_period if hasattr(self, "preserve_period") else None)!s}, '
                f'product_handle={(self.product_handle if hasattr(self, "product_handle") else None)!s}, '
                f'product_price_point_handle={(self.product_price_point_handle if hasattr(self, "product_price_point_handle") else None)!s}, '
                f'proration={(self.proration if hasattr(self, "proration") else None)!s}, '
                f'proration_date={(self.proration_date if hasattr(self, "proration_date") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
