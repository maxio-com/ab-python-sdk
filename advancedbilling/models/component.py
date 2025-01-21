# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_price import ComponentPrice


class Component(object):

    """Implementation of the 'Component' model.

    Attributes:
        id (int): The unique ID assigned to the component by Chargify. This ID
            can be used to fetch the component from the API.
        name (str): The name of the Component, suitable for display on
            statements. i.e. Text Messages.
        handle (str): The component API handle
        pricing_scheme (PricingScheme): The model property of type
            PricingScheme.
        unit_name (str): The name of the unit that the component’s usage is
            measured in. i.e. message
        unit_price (str): The amount the customer will be charged per unit.
            This field is only populated for ‘per_unit’ pricing schemes,
            otherwise it may be null.
        product_family_id (int): The id of the Product Family to which the
            Component belongs
        product_family_name (str): The name of the Product Family to which the
            Component belongs
        price_per_unit_in_cents (int): deprecated - use unit_price instead
        kind (ComponentKind): A handle for the component type
        archived (bool): Boolean flag describing whether a component is
            archived or not.
        taxable (bool): Boolean flag describing whether a component is taxable
            or not.
        description (str): The description of the component.
        default_price_point_id (int): The model property of type int.
        overage_prices (List[ComponentPrice]): Applicable only to prepaid
            usage components. An array of overage price brackets.
        prices (List[ComponentPrice]): An array of price brackets. If the
            component uses the ‘per_unit’ pricing scheme, this array will be
            empty.
        price_point_count (int): Count for the number of price points
            associated with the component
        price_points_url (str): URL that points to the location to read the
            existing price points via GET request
        default_price_point_name (str): The model property of type str.
        tax_code (str): A string representing the tax code related to the
            component type. This is especially important when using the
            Avalara service to tax based on locale. This attribute has a max
            length of 10 characters.
        recurring (bool): The model property of type bool.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        created_at (datetime): Timestamp indicating when this component was
            created
        updated_at (datetime): Timestamp indicating when this component was
            updated
        archived_at (datetime): Timestamp indicating when this component was
            archived
        hide_date_range_on_invoice (bool): (Only available on Relationship
            Invoicing sites) Boolean flag describing if the service date range
            should show for the component on generated invoices.
        allow_fractional_quantities (bool): The model property of type bool.
        item_category (ItemCategory): One of the following: Business Software,
            Consumer Software, Digital Services, Physical Goods, Other
        use_site_exchange_rate (bool): The model property of type bool.
        accounting_code (str): E.g. Internal ID or SKU Number
        event_based_billing_metric_id (int): (Only for Event Based Components)
            This is an ID of a metric attached to the component. This metric
            is used to bill upon collected events.
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
        "id": 'id',
        "name": 'name',
        "handle": 'handle',
        "pricing_scheme": 'pricing_scheme',
        "unit_name": 'unit_name',
        "unit_price": 'unit_price',
        "product_family_id": 'product_family_id',
        "product_family_name": 'product_family_name',
        "price_per_unit_in_cents": 'price_per_unit_in_cents',
        "kind": 'kind',
        "archived": 'archived',
        "taxable": 'taxable',
        "description": 'description',
        "default_price_point_id": 'default_price_point_id',
        "overage_prices": 'overage_prices',
        "prices": 'prices',
        "price_point_count": 'price_point_count',
        "price_points_url": 'price_points_url',
        "default_price_point_name": 'default_price_point_name',
        "tax_code": 'tax_code',
        "recurring": 'recurring',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "archived_at": 'archived_at',
        "hide_date_range_on_invoice": 'hide_date_range_on_invoice',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "item_category": 'item_category',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "accounting_code": 'accounting_code',
        "event_based_billing_metric_id": 'event_based_billing_metric_id',
        "interval": 'interval',
        "interval_unit": 'interval_unit'
    }

    _optionals = [
        'id',
        'name',
        'handle',
        'pricing_scheme',
        'unit_name',
        'unit_price',
        'product_family_id',
        'product_family_name',
        'price_per_unit_in_cents',
        'kind',
        'archived',
        'taxable',
        'description',
        'default_price_point_id',
        'overage_prices',
        'prices',
        'price_point_count',
        'price_points_url',
        'default_price_point_name',
        'tax_code',
        'recurring',
        'upgrade_charge',
        'downgrade_credit',
        'created_at',
        'updated_at',
        'archived_at',
        'hide_date_range_on_invoice',
        'allow_fractional_quantities',
        'item_category',
        'use_site_exchange_rate',
        'accounting_code',
        'event_based_billing_metric_id',
        'interval',
        'interval_unit',
    ]

    _nullables = [
        'handle',
        'pricing_scheme',
        'unit_price',
        'price_per_unit_in_cents',
        'description',
        'default_price_point_id',
        'overage_prices',
        'prices',
        'price_points_url',
        'tax_code',
        'upgrade_charge',
        'downgrade_credit',
        'archived_at',
        'item_category',
        'use_site_exchange_rate',
        'accounting_code',
        'interval_unit',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 unit_name=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 product_family_name=APIHelper.SKIP,
                 price_per_unit_in_cents=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 archived=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 default_price_point_id=APIHelper.SKIP,
                 overage_prices=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 price_point_count=APIHelper.SKIP,
                 price_points_url=APIHelper.SKIP,
                 default_price_point_name=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 hide_date_range_on_invoice=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 item_category=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 accounting_code=APIHelper.SKIP,
                 event_based_billing_metric_id=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Component class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if unit_name is not APIHelper.SKIP:
            self.unit_name = unit_name 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if product_family_name is not APIHelper.SKIP:
            self.product_family_name = product_family_name 
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
        if overage_prices is not APIHelper.SKIP:
            self.overage_prices = overage_prices 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        if price_point_count is not APIHelper.SKIP:
            self.price_point_count = price_point_count 
        if price_points_url is not APIHelper.SKIP:
            self.price_points_url = price_points_url 
        if default_price_point_name is not APIHelper.SKIP:
            self.default_price_point_name = default_price_point_name 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = APIHelper.apply_datetime_converter(archived_at, APIHelper.RFC3339DateTime) if archived_at else None 
        if hide_date_range_on_invoice is not APIHelper.SKIP:
            self.hide_date_range_on_invoice = hide_date_range_on_invoice 
        if allow_fractional_quantities is not APIHelper.SKIP:
            self.allow_fractional_quantities = allow_fractional_quantities 
        if item_category is not APIHelper.SKIP:
            self.item_category = item_category 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code 
        if event_based_billing_metric_id is not APIHelper.SKIP:
            self.event_based_billing_metric_id = event_based_billing_metric_id 
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if "handle" in dictionary.keys() else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if "pricing_scheme" in dictionary.keys() else APIHelper.SKIP
        unit_name = dictionary.get("unit_name") if dictionary.get("unit_name") else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if "unit_price" in dictionary.keys() else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
        price_per_unit_in_cents = dictionary.get("price_per_unit_in_cents") if "price_per_unit_in_cents" in dictionary.keys() else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        archived = dictionary.get("archived") if "archived" in dictionary.keys() else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        default_price_point_id = dictionary.get("default_price_point_id") if "default_price_point_id" in dictionary.keys() else APIHelper.SKIP
        if 'overage_prices' in dictionary.keys():
            overage_prices = [ComponentPrice.from_dictionary(x) for x in dictionary.get('overage_prices')] if dictionary.get('overage_prices') else None
        else:
            overage_prices = APIHelper.SKIP
        if 'prices' in dictionary.keys():
            prices = [ComponentPrice.from_dictionary(x) for x in dictionary.get('prices')] if dictionary.get('prices') else None
        else:
            prices = APIHelper.SKIP
        price_point_count = dictionary.get("price_point_count") if dictionary.get("price_point_count") else APIHelper.SKIP
        price_points_url = dictionary.get("price_points_url") if "price_points_url" in dictionary.keys() else APIHelper.SKIP
        default_price_point_name = dictionary.get("default_price_point_name") if dictionary.get("default_price_point_name") else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if "tax_code" in dictionary.keys() else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        if 'archived_at' in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("archived_at")).datetime if dictionary.get("archived_at") else None
        else:
            archived_at = APIHelper.SKIP
        hide_date_range_on_invoice = dictionary.get("hide_date_range_on_invoice") if "hide_date_range_on_invoice" in dictionary.keys() else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        item_category = dictionary.get("item_category") if "item_category" in dictionary.keys() else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        accounting_code = dictionary.get("accounting_code") if "accounting_code" in dictionary.keys() else APIHelper.SKIP
        event_based_billing_metric_id = dictionary.get("event_based_billing_metric_id") if dictionary.get("event_based_billing_metric_id") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   handle,
                   pricing_scheme,
                   unit_name,
                   unit_price,
                   product_family_id,
                   product_family_name,
                   price_per_unit_in_cents,
                   kind,
                   archived,
                   taxable,
                   description,
                   default_price_point_id,
                   overage_prices,
                   prices,
                   price_point_count,
                   price_points_url,
                   default_price_point_name,
                   tax_code,
                   recurring,
                   upgrade_charge,
                   downgrade_credit,
                   created_at,
                   updated_at,
                   archived_at,
                   hide_date_range_on_invoice,
                   allow_fractional_quantities,
                   item_category,
                   use_site_exchange_rate,
                   accounting_code,
                   event_based_billing_metric_id,
                   interval,
                   interval_unit,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'name={self.name!r}, '
                f'handle={self.handle!r}, '
                f'pricing_scheme={self.pricing_scheme!r}, '
                f'unit_name={self.unit_name!r}, '
                f'unit_price={self.unit_price!r}, '
                f'product_family_id={self.product_family_id!r}, '
                f'product_family_name={self.product_family_name!r}, '
                f'price_per_unit_in_cents={self.price_per_unit_in_cents!r}, '
                f'kind={self.kind!r}, '
                f'archived={self.archived!r}, '
                f'taxable={self.taxable!r}, '
                f'description={self.description!r}, '
                f'default_price_point_id={self.default_price_point_id!r}, '
                f'overage_prices={self.overage_prices!r}, '
                f'prices={self.prices!r}, '
                f'price_point_count={self.price_point_count!r}, '
                f'price_points_url={self.price_points_url!r}, '
                f'default_price_point_name={self.default_price_point_name!r}, '
                f'tax_code={self.tax_code!r}, '
                f'recurring={self.recurring!r}, '
                f'upgrade_charge={self.upgrade_charge!r}, '
                f'downgrade_credit={self.downgrade_credit!r}, '
                f'created_at={self.created_at!r}, '
                f'updated_at={self.updated_at!r}, '
                f'archived_at={self.archived_at!r}, '
                f'hide_date_range_on_invoice={self.hide_date_range_on_invoice!r}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!r}, '
                f'item_category={self.item_category!r}, '
                f'use_site_exchange_rate={self.use_site_exchange_rate!r}, '
                f'accounting_code={self.accounting_code!r}, '
                f'event_based_billing_metric_id={self.event_based_billing_metric_id!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'name={self.name!s}, '
                f'handle={self.handle!s}, '
                f'pricing_scheme={self.pricing_scheme!s}, '
                f'unit_name={self.unit_name!s}, '
                f'unit_price={self.unit_price!s}, '
                f'product_family_id={self.product_family_id!s}, '
                f'product_family_name={self.product_family_name!s}, '
                f'price_per_unit_in_cents={self.price_per_unit_in_cents!s}, '
                f'kind={self.kind!s}, '
                f'archived={self.archived!s}, '
                f'taxable={self.taxable!s}, '
                f'description={self.description!s}, '
                f'default_price_point_id={self.default_price_point_id!s}, '
                f'overage_prices={self.overage_prices!s}, '
                f'prices={self.prices!s}, '
                f'price_point_count={self.price_point_count!s}, '
                f'price_points_url={self.price_points_url!s}, '
                f'default_price_point_name={self.default_price_point_name!s}, '
                f'tax_code={self.tax_code!s}, '
                f'recurring={self.recurring!s}, '
                f'upgrade_charge={self.upgrade_charge!s}, '
                f'downgrade_credit={self.downgrade_credit!s}, '
                f'created_at={self.created_at!s}, '
                f'updated_at={self.updated_at!s}, '
                f'archived_at={self.archived_at!s}, '
                f'hide_date_range_on_invoice={self.hide_date_range_on_invoice!s}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!s}, '
                f'item_category={self.item_category!s}, '
                f'use_site_exchange_rate={self.use_site_exchange_rate!s}, '
                f'accounting_code={self.accounting_code!s}, '
                f'event_based_billing_metric_id={self.event_based_billing_metric_id!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'additional_properties={self.additional_properties!s})')
