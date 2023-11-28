# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_price_point_item import ComponentPricePointItem
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme


class QuantityBasedComponent(object):

    """Implementation of the 'Quantity Based Component' model.

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
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): (Not required for ‘per_unit’ pricing schemes)
            One or more price brackets. See [Price Bracket
            Rules](https://chargify.zendesk.com/hc/en-us/articles/4407755865883
            #price-bracket-rules) for an overview of how price brackets work
            for different pricing schemes.
        upgrade_charge (str): TODO: type description here.
        downgrade_credit (str): TODO: type description here.
        price_points (List[ComponentPricePointItem]): TODO: type description
            here.
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
        recurring (bool): TODO: type description here.
        display_on_hosted_page (bool): TODO: type description here.
        allow_fractional_quantities (bool): TODO: type description here.
        public_signup_page_ids (List[int]): TODO: type description here.

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
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "price_points": 'price_points',
        "unit_price": 'unit_price',
        "tax_code": 'tax_code',
        "hide_date_range_on_invoice": 'hide_date_range_on_invoice',
        "price_in_cents": 'price_in_cents',
        "recurring": 'recurring',
        "display_on_hosted_page": 'display_on_hosted_page',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "public_signup_page_ids": 'public_signup_page_ids'
    }

    _optionals = [
        'description',
        'handle',
        'taxable',
        'prices',
        'upgrade_charge',
        'downgrade_credit',
        'price_points',
        'unit_price',
        'tax_code',
        'hide_date_range_on_invoice',
        'price_in_cents',
        'recurring',
        'display_on_hosted_page',
        'allow_fractional_quantities',
        'public_signup_page_ids',
    ]

    def __init__(self,
                 name=None,
                 unit_name=None,
                 pricing_scheme=None,
                 description=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 price_points=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 hide_date_range_on_invoice=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 display_on_hosted_page=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 public_signup_page_ids=APIHelper.SKIP):
        """Constructor for the QuantityBasedComponent class"""

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
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
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
        upgrade_charge = dictionary.get("upgrade_charge") if dictionary.get("upgrade_charge") else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if dictionary.get("downgrade_credit") else APIHelper.SKIP
        price_points = None
        if dictionary.get('price_points') is not None:
            price_points = [ComponentPricePointItem.from_dictionary(x) for x in dictionary.get('price_points')]
        else:
            price_points = APIHelper.SKIP
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('QuantityBasedComponentUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        hide_date_range_on_invoice = dictionary.get("hide_date_range_on_invoice") if "hide_date_range_on_invoice" in dictionary.keys() else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        public_signup_page_ids = dictionary.get("public_signup_page_ids") if dictionary.get("public_signup_page_ids") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   unit_name,
                   pricing_scheme,
                   description,
                   handle,
                   taxable,
                   prices,
                   upgrade_charge,
                   downgrade_credit,
                   price_points,
                   unit_price,
                   tax_code,
                   hide_date_range_on_invoice,
                   price_in_cents,
                   recurring,
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
            return APIHelper.is_valid_type(value=dictionary.name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.unit_name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.pricing_scheme, type_callable=lambda value: PricingScheme.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('unit_name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('pricing_scheme'), type_callable=lambda value: PricingScheme.validate(value))
