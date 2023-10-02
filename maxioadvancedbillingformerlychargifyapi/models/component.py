# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper
from maxioadvancedbillingformerlychargifyapi.models.component_price import ComponentPrice


class Component(object):

    """Implementation of the 'Component' model.

    TODO: type model description here.

    Attributes:
        id (int): The unique ID assigned to the component by Chargify. This ID
            can be used to fetch the component from the API.
        name (str): The name of the Component, suitable for display on
            statements. i.e. Text Messages.
        pricing_scheme (str): The handle for the pricing scheme. Available
            options: per_unit, volume, tiered, stairstep. See [Price Bracket
            Rules](https://chargify.zendesk.com/hc/en-us/articles/4407755865883
            #price-bracket-rules) for an overview of pricing schemes.
        unit_name (str): The name of the unit that the component’s usage is
            measured in. i.e. message
        unit_price (str): The amount the customer will be charged per unit.
            This field is only populated for ‘per_unit’ pricing schemes,
            otherwise it may be null.
        product_family_id (int): The id of the Product Family to which the
            Component belongs
        price_per_unit_in_cents (int): deprecated - use unit_price instead
        kind (ComponentKindEnum): A handle for the component type
        archived (bool): Boolean flag describing whether a component is
            archived or not.
        taxable (bool): Boolean flag describing whether a component is taxable
            or not.
        description (str): The description of the component.
        default_price_point_id (int): TODO: type description here.
        price_point_count (int): Count for the number of price points
            associated with the component
        price_points_url (str): URL that points to the location to read the
            existing price points via GET request
        tax_code (str): A string representing the tax code related to the
            component type. This is especially important when using the
            Avalara service to tax based on locale. This attribute has a max
            length of 10 characters.
        recurring (bool): TODO: type description here.
        upgrade_charge (str): TODO: type description here.
        downgrade_credit (str): TODO: type description here.
        created_at (str): TODO: type description here.
        prices (List[ComponentPrice]): An array of price brackets. If the
            component uses the ‘per_unit’ pricing scheme, this array will be
            empty.
        default_price_point_name (str): TODO: type description here.
        product_family_name (str): TODO: type description here.
        hide_date_range_on_invoice (bool): (Only available on Relationship
            Invoicing sites) Boolean flag describing if the service date range
            should show for the component on generated invoices.
        event_based_billing_metric_id (int): (Only for Event Based Components)
            This is an ID of a metric attached to the component. This metric
            is used to bill upon collected events.
        item_category (ItemCategoryEnum): One of the following: Business
            Software, Consumer Software, Digital Services, Physical Goods,
            Other
        allow_fractional_quantities (bool): TODO: type description here.
        use_site_exchange_rate (bool): TODO: type description here.
        accounting_code (str): E.g. Internal ID or SKU Number

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "pricing_scheme": 'pricing_scheme',
        "unit_name": 'unit_name',
        "unit_price": 'unit_price',
        "product_family_id": 'product_family_id',
        "price_per_unit_in_cents": 'price_per_unit_in_cents',
        "kind": 'kind',
        "archived": 'archived',
        "taxable": 'taxable',
        "description": 'description',
        "default_price_point_id": 'default_price_point_id',
        "price_point_count": 'price_point_count',
        "price_points_url": 'price_points_url',
        "tax_code": 'tax_code',
        "recurring": 'recurring',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "created_at": 'created_at',
        "prices": 'prices',
        "default_price_point_name": 'default_price_point_name',
        "product_family_name": 'product_family_name',
        "hide_date_range_on_invoice": 'hide_date_range_on_invoice',
        "event_based_billing_metric_id": 'event_based_billing_metric_id',
        "item_category": 'item_category',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "accounting_code": 'accounting_code'
    }

    _optionals = [
        'id',
        'name',
        'pricing_scheme',
        'unit_name',
        'unit_price',
        'product_family_id',
        'price_per_unit_in_cents',
        'kind',
        'archived',
        'taxable',
        'description',
        'default_price_point_id',
        'price_point_count',
        'price_points_url',
        'tax_code',
        'recurring',
        'upgrade_charge',
        'downgrade_credit',
        'created_at',
        'prices',
        'default_price_point_name',
        'product_family_name',
        'hide_date_range_on_invoice',
        'event_based_billing_metric_id',
        'item_category',
        'allow_fractional_quantities',
        'use_site_exchange_rate',
        'accounting_code',
    ]

    _nullables = [
        'pricing_scheme',
        'unit_price',
        'price_per_unit_in_cents',
        'description',
        'tax_code',
        'upgrade_charge',
        'downgrade_credit',
        'prices',
        'use_site_exchange_rate',
        'accounting_code',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 unit_name=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 price_per_unit_in_cents=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 archived=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 default_price_point_id=APIHelper.SKIP,
                 price_point_count=APIHelper.SKIP,
                 price_points_url=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 default_price_point_name=APIHelper.SKIP,
                 product_family_name=APIHelper.SKIP,
                 hide_date_range_on_invoice=APIHelper.SKIP,
                 event_based_billing_metric_id=APIHelper.SKIP,
                 item_category=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 accounting_code=APIHelper.SKIP):
        """Constructor for the Component class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if unit_name is not APIHelper.SKIP:
            self.unit_name = unit_name 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if price_per_unit_in_cents is not APIHelper.SKIP:
            self.price_per_unit_in_cents = price_per_unit_in_cents 
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if archived is not APIHelper.SKIP:
            self.archived = archived 
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable 
        if description is not APIHelper.SKIP:
            self.description = description 
        if default_price_point_id is not APIHelper.SKIP:
            self.default_price_point_id = default_price_point_id 
        if price_point_count is not APIHelper.SKIP:
            self.price_point_count = price_point_count 
        if price_points_url is not APIHelper.SKIP:
            self.price_points_url = price_points_url 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        if default_price_point_name is not APIHelper.SKIP:
            self.default_price_point_name = default_price_point_name 
        if product_family_name is not APIHelper.SKIP:
            self.product_family_name = product_family_name 
        if hide_date_range_on_invoice is not APIHelper.SKIP:
            self.hide_date_range_on_invoice = hide_date_range_on_invoice 
        if event_based_billing_metric_id is not APIHelper.SKIP:
            self.event_based_billing_metric_id = event_based_billing_metric_id 
        if item_category is not APIHelper.SKIP:
            self.item_category = item_category 
        if allow_fractional_quantities is not APIHelper.SKIP:
            self.allow_fractional_quantities = allow_fractional_quantities 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code 

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
        pricing_scheme = dictionary.get("pricing_scheme") if "pricing_scheme" in dictionary.keys() else APIHelper.SKIP
        unit_name = dictionary.get("unit_name") if dictionary.get("unit_name") else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if "unit_price" in dictionary.keys() else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        price_per_unit_in_cents = dictionary.get("price_per_unit_in_cents") if "price_per_unit_in_cents" in dictionary.keys() else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        archived = dictionary.get("archived") if "archived" in dictionary.keys() else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        default_price_point_id = dictionary.get("default_price_point_id") if dictionary.get("default_price_point_id") else APIHelper.SKIP
        price_point_count = dictionary.get("price_point_count") if dictionary.get("price_point_count") else APIHelper.SKIP
        price_points_url = dictionary.get("price_points_url") if dictionary.get("price_points_url") else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if "tax_code" in dictionary.keys() else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        if 'prices' in dictionary.keys():
            prices = [ComponentPrice.from_dictionary(x) for x in dictionary.get('prices')] if dictionary.get('prices') else None
        else:
            prices = APIHelper.SKIP
        default_price_point_name = dictionary.get("default_price_point_name") if dictionary.get("default_price_point_name") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
        hide_date_range_on_invoice = dictionary.get("hide_date_range_on_invoice") if "hide_date_range_on_invoice" in dictionary.keys() else APIHelper.SKIP
        event_based_billing_metric_id = dictionary.get("event_based_billing_metric_id") if dictionary.get("event_based_billing_metric_id") else APIHelper.SKIP
        item_category = dictionary.get("item_category") if dictionary.get("item_category") else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        accounting_code = dictionary.get("accounting_code") if "accounting_code" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   pricing_scheme,
                   unit_name,
                   unit_price,
                   product_family_id,
                   price_per_unit_in_cents,
                   kind,
                   archived,
                   taxable,
                   description,
                   default_price_point_id,
                   price_point_count,
                   price_points_url,
                   tax_code,
                   recurring,
                   upgrade_charge,
                   downgrade_credit,
                   created_at,
                   prices,
                   default_price_point_name,
                   product_family_name,
                   hide_date_range_on_invoice,
                   event_based_billing_metric_id,
                   item_category,
                   allow_fractional_quantities,
                   use_site_exchange_rate,
                   accounting_code)