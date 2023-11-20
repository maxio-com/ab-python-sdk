# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.prepaid_component_price_point import PrepaidComponentPricePoint
from advancedbilling.models.price import Price


class PrepaidUsageComponent(object):

    """Implementation of the 'Prepaid Usage Component' model.

    TODO: type model description here.

    Attributes:
        name (str): A name for this component that is suitable for showing
            customers and displaying on billing statements, ie. "Minutes".
        unit_name (str): The name of the unit of measurement for the
            component. It should be singular since it will be automatically
            pluralized when necessary. i.e. “message”, which may then be shown
            as “5 messages” on a subscription’s component line-item
        description (str): A description for the component that will be
            displayed to the user on the hosted signup page.
        handle (str): A unique identifier for your use that can be used to
            retrieve this component is subsequent requests.  Must start with a
            letter or number and may only contain lowercase letters, numbers,
            or the characters '.', ':', '-', or '_'.
        taxable (bool): Boolean flag describing whether a component is taxable
            or not.
        pricing_scheme (PricingScheme | None): The identifier for the pricing
            scheme. See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): (Not required for ‘per_unit’ pricing schemes)
            One or more price brackets. See [Price Bracket
            Rules](https://chargify.zendesk.com/hc/en-us/articles/4407755865883
            #general-price-bracket-rules) for an overview of how price
            brackets work for different pricing schemes.
        upgrade_charge (str): TODO: type description here.
        downgrade_credit (str): TODO: type description here.
        price_points (List[PrepaidComponentPricePoint]): TODO: type
            description here.
        unit_price (str | float | None): The amount the customer will be
            charged per unit when the pricing scheme is “per_unit”. For On/Off
            Components, this is the amount that the customer will be charged
            when they turn the component on for the subscription. The price
            can contain up to 8 decimal places. i.e. 1.00 or 0.0012 or
            0.00000065
        tax_code (str): A string representing the tax code related to the
            component type. This is especially important when using the
            Avalara service to tax based on locale. This attribute has a max
            length of 10 characters.
        hide_date_range_on_invoice (bool): (Only available on Relationship
            Invoicing sites) Boolean flag describing if the service date range
            should show for the component on generated invoices.
        price_in_cents (str): deprecated May 2011 - use unit_price instead
        overage_pricing (OveragePricing): TODO: type description here.
        rollover_prepaid_remainder (bool): Boolean which controls whether or
            not remaining units should be rolled over to the next period
        renew_prepaid_allocation (bool): Boolean which controls whether or not
            the allocated quantity should be renewed at the beginning of each
            period
        expiration_interval (float): (only for prepaid usage components where
            rollover_prepaid_remainder is true) The number of
            `expiration_interval_unit`s after which rollover amounts should
            expire
        expiration_interval_unit (IntervalUnit | None): TODO: type description
            here.
        display_on_hosted_page (bool): TODO: type description here.
        allow_fractional_quantities (bool): TODO: type description here.
        public_signup_page_ids (List[int]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "unit_name": 'unit_name',
        "description": 'description',
        "handle": 'handle',
        "taxable": 'taxable',
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "price_points": 'price_points',
        "unit_price": 'unit_price',
        "tax_code": 'tax_code',
        "hide_date_range_on_invoice": 'hide_date_range_on_invoice',
        "price_in_cents": 'price_in_cents',
        "overage_pricing": 'overage_pricing',
        "rollover_prepaid_remainder": 'rollover_prepaid_remainder',
        "renew_prepaid_allocation": 'renew_prepaid_allocation',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit',
        "display_on_hosted_page": 'display_on_hosted_page',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "public_signup_page_ids": 'public_signup_page_ids'
    }

    _optionals = [
        'name',
        'unit_name',
        'description',
        'handle',
        'taxable',
        'pricing_scheme',
        'prices',
        'upgrade_charge',
        'downgrade_credit',
        'price_points',
        'unit_price',
        'tax_code',
        'hide_date_range_on_invoice',
        'price_in_cents',
        'overage_pricing',
        'rollover_prepaid_remainder',
        'renew_prepaid_allocation',
        'expiration_interval',
        'expiration_interval_unit',
        'display_on_hosted_page',
        'allow_fractional_quantities',
        'public_signup_page_ids',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 unit_name=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 price_points=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 hide_date_range_on_invoice=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP,
                 overage_pricing=APIHelper.SKIP,
                 rollover_prepaid_remainder=APIHelper.SKIP,
                 renew_prepaid_allocation=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 display_on_hosted_page=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 public_signup_page_ids=APIHelper.SKIP):
        """Constructor for the PrepaidUsageComponent class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if unit_name is not APIHelper.SKIP:
            self.unit_name = unit_name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if price_points is not APIHelper.SKIP:
            self.price_points = price_points 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if hide_date_range_on_invoice is not APIHelper.SKIP:
            self.hide_date_range_on_invoice = hide_date_range_on_invoice 
        if price_in_cents is not APIHelper.SKIP:
            self.price_in_cents = price_in_cents 
        if overage_pricing is not APIHelper.SKIP:
            self.overage_pricing = overage_pricing 
        if rollover_prepaid_remainder is not APIHelper.SKIP:
            self.rollover_prepaid_remainder = rollover_prepaid_remainder 
        if renew_prepaid_allocation is not APIHelper.SKIP:
            self.renew_prepaid_allocation = renew_prepaid_allocation 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 
        if display_on_hosted_page is not APIHelper.SKIP:
            self.display_on_hosted_page = display_on_hosted_page 
        if allow_fractional_quantities is not APIHelper.SKIP:
            self.allow_fractional_quantities = allow_fractional_quantities 
        if public_signup_page_ids is not APIHelper.SKIP:
            self.public_signup_page_ids = public_signup_page_ids 

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        unit_name = dictionary.get("unit_name") if dictionary.get("unit_name") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        pricing_scheme = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PrepaidUsageComponentPricingScheme'), dictionary.get('pricing_scheme'), False) if dictionary.get('pricing_scheme') is not None else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if dictionary.get("upgrade_charge") else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if dictionary.get("downgrade_credit") else APIHelper.SKIP
        price_points = None
        if dictionary.get('price_points') is not None:
            price_points = [PrepaidComponentPricePoint.from_dictionary(x) for x in dictionary.get('price_points')]
        else:
            price_points = APIHelper.SKIP
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PrepaidUsageComponentUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        hide_date_range_on_invoice = dictionary.get("hide_date_range_on_invoice") if "hide_date_range_on_invoice" in dictionary.keys() else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        overage_pricing = OveragePricing.from_dictionary(dictionary.get('overage_pricing')) if 'overage_pricing' in dictionary.keys() else APIHelper.SKIP
        rollover_prepaid_remainder = dictionary.get("rollover_prepaid_remainder") if "rollover_prepaid_remainder" in dictionary.keys() else APIHelper.SKIP
        renew_prepaid_allocation = dictionary.get("renew_prepaid_allocation") if "renew_prepaid_allocation" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if dictionary.get("expiration_interval") else APIHelper.SKIP
        expiration_interval_unit = APIHelper.deserialize_union_type(UnionTypeLookUp.get('PrepaidUsageComponentExpirationIntervalUnit'), dictionary.get('expiration_interval_unit'), False) if dictionary.get('expiration_interval_unit') is not None else APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        public_signup_page_ids = dictionary.get("public_signup_page_ids") if dictionary.get("public_signup_page_ids") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   unit_name,
                   description,
                   handle,
                   taxable,
                   pricing_scheme,
                   prices,
                   upgrade_charge,
                   downgrade_credit,
                   price_points,
                   unit_price,
                   tax_code,
                   hide_date_range_on_invoice,
                   price_in_cents,
                   overage_pricing,
                   rollover_prepaid_remainder,
                   renew_prepaid_allocation,
                   expiration_interval,
                   expiration_interval_unit,
                   display_on_hosted_page,
                   allow_fractional_quantities,
                   public_signup_page_ids)

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
