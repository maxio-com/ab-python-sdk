# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_price_point_item import ComponentPricePointItem
from advancedbilling.models.price import Price


class MeteredComponent(object):

    """Implementation of the 'Metered Component' model.

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
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): (Not required for ‘per_unit’ pricing schemes)
            One or more price brackets. See [Price Bracket
            Rules](https://maxio.zendesk.com/hc/en-us/articles/24261149166733-C
            omponent-Pricing-Schemes#price-bracket-rules) for an overview of
            how price brackets work for different pricing schemes.
        price_points (List[ComponentPricePointItem]): The model property of
            type List[ComponentPricePointItem].
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
        display_on_hosted_page (bool): The model property of type bool.
        allow_fractional_quantities (bool): The model property of type bool.
        public_signup_page_ids (List[int]): The model property of type
            List[int].
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component's
            default price point would renew every 30 days. This property is
            only available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component's default price point, either month or day.
            This property is only available for sites with Multifrequency
            enabled.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "unit_name": 'unit_name',
        "pricing_scheme": 'pricing_scheme',
        "description": 'description',
        "handle": 'handle',
        "taxable": 'taxable',
        "prices": 'prices',
        "price_points": 'price_points',
        "unit_price": 'unit_price',
        "tax_code": 'tax_code',
        "hide_date_range_on_invoice": 'hide_date_range_on_invoice',
        "display_on_hosted_page": 'display_on_hosted_page',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "public_signup_page_ids": 'public_signup_page_ids',
        "interval": 'interval',
        "interval_unit": 'interval_unit'
    }

    _optionals = [
        'description',
        'handle',
        'taxable',
        'prices',
        'price_points',
        'unit_price',
        'tax_code',
        'hide_date_range_on_invoice',
        'display_on_hosted_page',
        'allow_fractional_quantities',
        'public_signup_page_ids',
        'interval',
        'interval_unit',
    ]

    _nullables = [
        'interval_unit',
    ]

    def __init__(self,
                 name=None,
                 unit_name=None,
                 pricing_scheme=None,
                 description=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 price_points=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 hide_date_range_on_invoice=APIHelper.SKIP,
                 display_on_hosted_page=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 public_signup_page_ids=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the MeteredComponent class"""

        # Initialize members of the class
        self.name = name 
        self.unit_name = unit_name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable 
        self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        if price_points is not APIHelper.SKIP:
            self.price_points = price_points 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if hide_date_range_on_invoice is not APIHelper.SKIP:
            self.hide_date_range_on_invoice = hide_date_range_on_invoice 
        if display_on_hosted_page is not APIHelper.SKIP:
            self.display_on_hosted_page = display_on_hosted_page 
        if allow_fractional_quantities is not APIHelper.SKIP:
            self.allow_fractional_quantities = allow_fractional_quantities 
        if public_signup_page_ids is not APIHelper.SKIP:
            self.public_signup_page_ids = public_signup_page_ids 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        unit_name = dictionary.get("unit_name") if dictionary.get("unit_name") else None
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else None
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        price_points = None
        if dictionary.get('price_points') is not None:
            price_points = [ComponentPricePointItem.from_dictionary(x) for x in dictionary.get('price_points')]
        else:
            price_points = APIHelper.SKIP
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('MeteredComponentUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        hide_date_range_on_invoice = dictionary.get("hide_date_range_on_invoice") if "hide_date_range_on_invoice" in dictionary.keys() else APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        public_signup_page_ids = dictionary.get("public_signup_page_ids") if dictionary.get("public_signup_page_ids") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   unit_name,
                   pricing_scheme,
                   description,
                   handle,
                   taxable,
                   prices,
                   price_points,
                   unit_price,
                   tax_code,
                   hide_date_range_on_invoice,
                   display_on_hosted_page,
                   allow_fractional_quantities,
                   public_signup_page_ids,
                   interval,
                   interval_unit,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'unit_name={self.unit_name!r}, '
                f'description={self.description!r}, '
                f'handle={self.handle!r}, '
                f'taxable={self.taxable!r}, '
                f'pricing_scheme={self.pricing_scheme!r}, '
                f'prices={self.prices!r}, '
                f'price_points={self.price_points!r}, '
                f'unit_price={self.unit_price!r}, '
                f'tax_code={self.tax_code!r}, '
                f'hide_date_range_on_invoice={self.hide_date_range_on_invoice!r}, '
                f'display_on_hosted_page={self.display_on_hosted_page!r}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!r}, '
                f'public_signup_page_ids={self.public_signup_page_ids!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'unit_name={self.unit_name!s}, '
                f'description={self.description!s}, '
                f'handle={self.handle!s}, '
                f'taxable={self.taxable!s}, '
                f'pricing_scheme={self.pricing_scheme!s}, '
                f'prices={self.prices!s}, '
                f'price_points={self.price_points!s}, '
                f'unit_price={self.unit_price!s}, '
                f'tax_code={self.tax_code!s}, '
                f'hide_date_range_on_invoice={self.hide_date_range_on_invoice!s}, '
                f'display_on_hosted_page={self.display_on_hosted_page!s}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!s}, '
                f'public_signup_page_ids={self.public_signup_page_ids!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'additional_properties={self.additional_properties!s})')
