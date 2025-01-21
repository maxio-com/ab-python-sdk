# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.historic_usage import HistoricUsage
from advancedbilling.models.subscription_component_subscription import SubscriptionComponentSubscription


class SubscriptionComponent(object):

    """Implementation of the 'Subscription Component' model.

    Attributes:
        id (int): The model property of type int.
        name (str): The model property of type str.
        kind (ComponentKind): A handle for the component type
        unit_name (str): The model property of type str.
        enabled (bool): (for on/off components) indicates if the component is
            enabled for the subscription
        unit_balance (int): The model property of type int.
        currency (str): The model property of type str.
        allocated_quantity (int | str | None): For Quantity-based components:
            The current allocation for the component on the given
            subscription. For On/Off components: Use 1 for on. Use 0 for off.
        pricing_scheme (PricingScheme): The model property of type
            PricingScheme.
        component_id (int): The model property of type int.
        component_handle (str): The model property of type str.
        subscription_id (int): The model property of type int.
        recurring (bool): The model property of type bool.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        archived_at (datetime): The model property of type datetime.
        price_point_id (int): The model property of type int.
        price_point_handle (str): The model property of type str.
        price_point_type (PricePointType): The model property of type
            PricePointType.
        price_point_name (str): The model property of type str.
        product_family_id (int): The model property of type int.
        product_family_handle (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        use_site_exchange_rate (bool): The model property of type bool.
        description (str): The model property of type str.
        allow_fractional_quantities (bool): The model property of type bool.
        subscription (SubscriptionComponentSubscription): An optional object,
            will be returned if provided `include=subscription` query param.
        historic_usages (List[HistoricUsage]): The model property of type
            List[HistoricUsage].
        display_on_hosted_page (bool): The model property of type bool.
        interval (int): The numerical interval. i.e. an interval of '30'
            coupled with an interval_unit of day would mean this component
            price point would renew every 30 days. This property is only
            available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component price point, either month or day. This property
            is only available for sites with Multifrequency enabled.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "kind": 'kind',
        "unit_name": 'unit_name',
        "enabled": 'enabled',
        "unit_balance": 'unit_balance',
        "currency": 'currency',
        "allocated_quantity": 'allocated_quantity',
        "pricing_scheme": 'pricing_scheme',
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "subscription_id": 'subscription_id',
        "recurring": 'recurring',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "archived_at": 'archived_at',
        "price_point_id": 'price_point_id',
        "price_point_handle": 'price_point_handle',
        "price_point_type": 'price_point_type',
        "price_point_name": 'price_point_name',
        "product_family_id": 'product_family_id',
        "product_family_handle": 'product_family_handle',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "description": 'description',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "subscription": 'subscription',
        "historic_usages": 'historic_usages',
        "display_on_hosted_page": 'display_on_hosted_page',
        "interval": 'interval',
        "interval_unit": 'interval_unit'
    }

    _optionals = [
        'id',
        'name',
        'kind',
        'unit_name',
        'enabled',
        'unit_balance',
        'currency',
        'allocated_quantity',
        'pricing_scheme',
        'component_id',
        'component_handle',
        'subscription_id',
        'recurring',
        'upgrade_charge',
        'downgrade_credit',
        'archived_at',
        'price_point_id',
        'price_point_handle',
        'price_point_type',
        'price_point_name',
        'product_family_id',
        'product_family_handle',
        'created_at',
        'updated_at',
        'use_site_exchange_rate',
        'description',
        'allow_fractional_quantities',
        'subscription',
        'historic_usages',
        'display_on_hosted_page',
        'interval',
        'interval_unit',
    ]

    _nullables = [
        'pricing_scheme',
        'component_handle',
        'upgrade_charge',
        'downgrade_credit',
        'archived_at',
        'price_point_id',
        'price_point_handle',
        'price_point_type',
        'price_point_name',
        'use_site_exchange_rate',
        'description',
        'interval_unit',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 unit_name=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 unit_balance=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 allocated_quantity=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 subscription_id=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 price_point_handle=APIHelper.SKIP,
                 price_point_type=APIHelper.SKIP,
                 price_point_name=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 product_family_handle=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 subscription=APIHelper.SKIP,
                 historic_usages=APIHelper.SKIP,
                 display_on_hosted_page=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionComponent class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if unit_name is not APIHelper.SKIP:
            self.unit_name = unit_name 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if unit_balance is not APIHelper.SKIP:
            self.unit_balance = unit_balance 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if allocated_quantity is not APIHelper.SKIP:
            self.allocated_quantity = allocated_quantity 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if component_handle is not APIHelper.SKIP:
            self.component_handle = component_handle 
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = APIHelper.apply_datetime_converter(archived_at, APIHelper.RFC3339DateTime) if archived_at else None 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if price_point_handle is not APIHelper.SKIP:
            self.price_point_handle = price_point_handle 
        if price_point_type is not APIHelper.SKIP:
            self.price_point_type = price_point_type 
        if price_point_name is not APIHelper.SKIP:
            self.price_point_name = price_point_name 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if product_family_handle is not APIHelper.SKIP:
            self.product_family_handle = product_family_handle 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if description is not APIHelper.SKIP:
            self.description = description 
        if allow_fractional_quantities is not APIHelper.SKIP:
            self.allow_fractional_quantities = allow_fractional_quantities 
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 
        if historic_usages is not APIHelper.SKIP:
            self.historic_usages = historic_usages 
        if display_on_hosted_page is not APIHelper.SKIP:
            self.display_on_hosted_page = display_on_hosted_page 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        unit_name = dictionary.get("unit_name") if dictionary.get("unit_name") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        unit_balance = dictionary.get("unit_balance") if dictionary.get("unit_balance") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        allocated_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SubscriptionComponentAllocatedQuantity'), dictionary.get('allocated_quantity'), False) if dictionary.get('allocated_quantity') is not None else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if "pricing_scheme" in dictionary.keys() else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if "component_handle" in dictionary.keys() else APIHelper.SKIP
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        if 'archived_at' in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("archived_at")).datetime if dictionary.get("archived_at") else None
        else:
            archived_at = APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if "price_point_id" in dictionary.keys() else APIHelper.SKIP
        price_point_handle = dictionary.get("price_point_handle") if "price_point_handle" in dictionary.keys() else APIHelper.SKIP
        price_point_type = dictionary.get("price_point_type") if "price_point_type" in dictionary.keys() else APIHelper.SKIP
        price_point_name = dictionary.get("price_point_name") if "price_point_name" in dictionary.keys() else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        product_family_handle = dictionary.get("product_family_handle") if dictionary.get("product_family_handle") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        subscription = SubscriptionComponentSubscription.from_dictionary(dictionary.get('subscription')) if 'subscription' in dictionary.keys() else APIHelper.SKIP
        historic_usages = None
        if dictionary.get('historic_usages') is not None:
            historic_usages = [HistoricUsage.from_dictionary(x) for x in dictionary.get('historic_usages')]
        else:
            historic_usages = APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   kind,
                   unit_name,
                   enabled,
                   unit_balance,
                   currency,
                   allocated_quantity,
                   pricing_scheme,
                   component_id,
                   component_handle,
                   subscription_id,
                   recurring,
                   upgrade_charge,
                   downgrade_credit,
                   archived_at,
                   price_point_id,
                   price_point_handle,
                   price_point_type,
                   price_point_name,
                   product_family_id,
                   product_family_handle,
                   created_at,
                   updated_at,
                   use_site_exchange_rate,
                   description,
                   allow_fractional_quantities,
                   subscription,
                   historic_usages,
                   display_on_hosted_page,
                   interval,
                   interval_unit,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'name={self.name!r}, '
                f'kind={self.kind!r}, '
                f'unit_name={self.unit_name!r}, '
                f'enabled={self.enabled!r}, '
                f'unit_balance={self.unit_balance!r}, '
                f'currency={self.currency!r}, '
                f'allocated_quantity={self.allocated_quantity!r}, '
                f'pricing_scheme={self.pricing_scheme!r}, '
                f'component_id={self.component_id!r}, '
                f'component_handle={self.component_handle!r}, '
                f'subscription_id={self.subscription_id!r}, '
                f'recurring={self.recurring!r}, '
                f'upgrade_charge={self.upgrade_charge!r}, '
                f'downgrade_credit={self.downgrade_credit!r}, '
                f'archived_at={self.archived_at!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'price_point_handle={self.price_point_handle!r}, '
                f'price_point_type={self.price_point_type!r}, '
                f'price_point_name={self.price_point_name!r}, '
                f'product_family_id={self.product_family_id!r}, '
                f'product_family_handle={self.product_family_handle!r}, '
                f'created_at={self.created_at!r}, '
                f'updated_at={self.updated_at!r}, '
                f'use_site_exchange_rate={self.use_site_exchange_rate!r}, '
                f'description={self.description!r}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!r}, '
                f'subscription={self.subscription!r}, '
                f'historic_usages={self.historic_usages!r}, '
                f'display_on_hosted_page={self.display_on_hosted_page!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'name={self.name!s}, '
                f'kind={self.kind!s}, '
                f'unit_name={self.unit_name!s}, '
                f'enabled={self.enabled!s}, '
                f'unit_balance={self.unit_balance!s}, '
                f'currency={self.currency!s}, '
                f'allocated_quantity={self.allocated_quantity!s}, '
                f'pricing_scheme={self.pricing_scheme!s}, '
                f'component_id={self.component_id!s}, '
                f'component_handle={self.component_handle!s}, '
                f'subscription_id={self.subscription_id!s}, '
                f'recurring={self.recurring!s}, '
                f'upgrade_charge={self.upgrade_charge!s}, '
                f'downgrade_credit={self.downgrade_credit!s}, '
                f'archived_at={self.archived_at!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'price_point_handle={self.price_point_handle!s}, '
                f'price_point_type={self.price_point_type!s}, '
                f'price_point_name={self.price_point_name!s}, '
                f'product_family_id={self.product_family_id!s}, '
                f'product_family_handle={self.product_family_handle!s}, '
                f'created_at={self.created_at!s}, '
                f'updated_at={self.updated_at!s}, '
                f'use_site_exchange_rate={self.use_site_exchange_rate!s}, '
                f'description={self.description!s}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!s}, '
                f'subscription={self.subscription!s}, '
                f'historic_usages={self.historic_usages!s}, '
                f'display_on_hosted_page={self.display_on_hosted_page!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'additional_properties={self.additional_properties!s})')
