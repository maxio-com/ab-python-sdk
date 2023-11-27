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


class EBBComponent(object):

    """Implementation of the 'EBB Component' model.

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
            Rules](https://help.chargify.com/products/product-components.html#g
            eneral-price-bracket-rules) for an overview of how price brackets
            work for different pricing schemes.
        upgrade_charge (str): TODO: type description here.
        downgrade_credit (str): TODO: type description here.
        price_points (List[ComponentPricePointItem]): TODO: type description
            here.
        unit_price (str | float | None): The amount the customer will be
            charged per unit when the pricing scheme is “per_unit”. The price
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
        event_based_billing_metric_id (int): The ID of an event based billing
            metric that will be attached to this component.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "unit_name": 'unit_name',
        "pricing_scheme": 'pricing_scheme',
        "event_based_billing_metric_id": 'event_based_billing_metric_id',
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
        "price_in_cents": 'price_in_cents'
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
    ]

    def __init__(self,
                 name=None,
                 unit_name=None,
                 pricing_scheme=None,
                 event_based_billing_metric_id=None,
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
                 price_in_cents=APIHelper.SKIP):
        """Constructor for the EBBComponent class"""

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
        self.event_based_billing_metric_id = event_based_billing_metric_id 

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
        event_based_billing_metric_id = dictionary.get("event_based_billing_metric_id") if dictionary.get("event_based_billing_metric_id") else None
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
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('EBBComponentUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        hide_date_range_on_invoice = dictionary.get("hide_date_range_on_invoice") if "hide_date_range_on_invoice" in dictionary.keys() else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   unit_name,
                   pricing_scheme,
                   event_based_billing_metric_id,
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
                   price_in_cents)

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
                and APIHelper.is_valid_type(value=dictionary.pricing_scheme, type_callable=lambda value: PricingScheme.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.event_based_billing_metric_id, type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('unit_name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('pricing_scheme'), type_callable=lambda value: PricingScheme.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('event_based_billing_metric_id'), type_callable=lambda value: isinstance(value, int))
