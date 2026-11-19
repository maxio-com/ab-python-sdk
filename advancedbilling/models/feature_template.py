"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class FeatureTemplate(object):
    """Implementation of the 'Feature Template' model.

    A feature that can be granted to subscribers, defined once at the site level and
    then attached to products or components.

    Attributes:
        id (int): The Advanced Billing id of the feature template.
        key (str): A unique, lowercase, underscore-separated identifier for the
            feature. Immutable once set.
        name (str): The display name of the feature.
        description (str): The model property of type str.
        kind (FeatureKind): The behavior of a feature: - `access_right`: a boolean
            entitlement. A subscriber either has access or does not. - `usage_limit`:
            a quantified allowance measured over a recurring period (for example,
            "10,000 API calls per month"). - `service_right`: a free-form value
            (text, boolean, or number) that isn't a simple access flag or a metered
            limit.
        unit (str): The unit the feature is measured in (for example, `requests` or
            `GB`). Required when `kind` is `usage_limit`.
        value_type (FeatureValueType): The data type of a feature's value. For
            `access_right` features this is always `boolean`, and for `usage_limit`
            features this is always `numeric`. For `service_right` features, you
            choose the value type explicitly.
        default_value (str): A default value used to pre-populate new feature catalog
            items created from this template.
        default_periodicity_interval (int): For `usage_limit` features, the default
            periodicity interval used to pre-populate new feature catalog items.
            Always `null` for other kinds.
        default_periodicity_unit (EntitlementPeriodicityUnit): For `usage_limit`
            features, the default periodicity unit used to pre-populate new feature
            catalog items. Always `null` for other kinds.
        archived_at (datetime): The date and time the feature template was archived,
            or `null` if it is active.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        products_count (int): The number of **components** this feature template is
            currently attached to via an active feature catalog item. Despite the
            name, this counts components, not products. In the Advanced Billing UI,
            components are labeled "Products."
        plans_count (int): The number of **products** this feature template is
            currently attached to via an active feature catalog item. Despite the
            name, this counts products, not plans. In the Advanced Billing UI,
            products are labeled "Plans."
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "key": "key",
        "name": "name",
        "description": "description",
        "kind": "kind",
        "unit": "unit",
        "value_type": "value_type",
        "default_value": "default_value",
        "default_periodicity_interval": "default_periodicity_interval",
        "default_periodicity_unit": "default_periodicity_unit",
        "archived_at": "archived_at",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "products_count": "products_count",
        "plans_count": "plans_count",
    }

    _optionals = [
        "id",
        "key",
        "name",
        "description",
        "kind",
        "unit",
        "value_type",
        "default_value",
        "default_periodicity_interval",
        "default_periodicity_unit",
        "archived_at",
        "created_at",
        "updated_at",
        "products_count",
        "plans_count",
    ]

    _nullables = [
        "description",
        "unit",
        "default_value",
        "default_periodicity_interval",
        "default_periodicity_unit",
        "archived_at",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        key=APIHelper.SKIP,
        name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        kind=APIHelper.SKIP,
        unit=APIHelper.SKIP,
        value_type=APIHelper.SKIP,
        default_value=APIHelper.SKIP,
        default_periodicity_interval=APIHelper.SKIP,
        default_periodicity_unit=APIHelper.SKIP,
        archived_at=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        updated_at=APIHelper.SKIP,
        products_count=APIHelper.SKIP,
        plans_count=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a FeatureTemplate instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if key is not APIHelper.SKIP:
            self.key = key
        if name is not APIHelper.SKIP:
            self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
        if kind is not APIHelper.SKIP:
            self.kind = kind
        if unit is not APIHelper.SKIP:
            self.unit = unit
        if value_type is not APIHelper.SKIP:
            self.value_type = value_type
        if default_value is not APIHelper.SKIP:
            self.default_value = default_value
        if default_periodicity_interval is not APIHelper.SKIP:
            self.default_periodicity_interval = default_periodicity_interval
        if default_periodicity_unit is not APIHelper.SKIP:
            self.default_periodicity_unit = default_periodicity_unit
        if archived_at is not APIHelper.SKIP:
            self.archived_at =\
                 APIHelper.apply_datetime_converter(
                archived_at, APIHelper.RFC3339DateTime)\
                 if archived_at else None
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None
        if updated_at is not APIHelper.SKIP:
            self.updated_at =\
                 APIHelper.apply_datetime_converter(
                updated_at, APIHelper.RFC3339DateTime)\
                 if updated_at else None
        if products_count is not APIHelper.SKIP:
            self.products_count = products_count
        if plans_count is not APIHelper.SKIP:
            self.plans_count = plans_count

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        key =\
            dictionary.get("key")\
            if dictionary.get("key")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        description =\
            dictionary.get("description")\
            if "description" in dictionary.keys()\
                else APIHelper.SKIP
        kind =\
            dictionary.get("kind")\
            if dictionary.get("kind")\
                else APIHelper.SKIP
        unit =\
            dictionary.get("unit")\
            if "unit" in dictionary.keys()\
                else APIHelper.SKIP
        value_type =\
            dictionary.get("value_type")\
            if dictionary.get("value_type")\
                else APIHelper.SKIP
        default_value =\
            dictionary.get("default_value")\
            if "default_value" in dictionary.keys()\
                else APIHelper.SKIP
        default_periodicity_interval =\
            dictionary.get("default_periodicity_interval")\
            if "default_periodicity_interval" in dictionary.keys()\
                else APIHelper.SKIP
        default_periodicity_unit =\
            dictionary.get("default_periodicity_unit")\
            if "default_periodicity_unit" in dictionary.keys()\
                else APIHelper.SKIP
        if "archived_at" in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("archived_at")).datetime\
                if dictionary.get("archived_at") else None

        else:
            archived_at = APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_at")).datetime\
            if dictionary.get("updated_at") else APIHelper.SKIP
        products_count =\
            dictionary.get("products_count")\
            if dictionary.get("products_count")\
                else APIHelper.SKIP
        plans_count =\
            dictionary.get("plans_count")\
            if dictionary.get("plans_count")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   key,
                   name,
                   description,
                   kind,
                   unit,
                   value_type,
                   default_value,
                   default_periodicity_interval,
                   default_periodicity_unit,
                   archived_at,
                   created_at,
                   updated_at,
                   products_count,
                   plans_count,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _key=(
            self.key
            if hasattr(self, "key")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _kind=(
            self.kind
            if hasattr(self, "kind")
            else None
        )
        _unit=(
            self.unit
            if hasattr(self, "unit")
            else None
        )
        _value_type=(
            self.value_type
            if hasattr(self, "value_type")
            else None
        )
        _default_value=(
            self.default_value
            if hasattr(self, "default_value")
            else None
        )
        _default_periodicity_interval=(
            self.default_periodicity_interval
            if hasattr(self, "default_periodicity_interval")
            else None
        )
        _default_periodicity_unit=(
            self.default_periodicity_unit
            if hasattr(self, "default_periodicity_unit")
            else None
        )
        _archived_at=(
            self.archived_at
            if hasattr(self, "archived_at")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _products_count=(
            self.products_count
            if hasattr(self, "products_count")
            else None
        )
        _plans_count=(
            self.plans_count
            if hasattr(self, "plans_count")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"key={_key!r}, "
            f"name={_name!r}, "
            f"description={_description!r}, "
            f"kind={_kind!r}, "
            f"unit={_unit!r}, "
            f"value_type={_value_type!r}, "
            f"default_value={_default_value!r}, "
            f"default_periodicity_interval={_default_periodicity_interval!r}, "
            f"default_periodicity_unit={_default_periodicity_unit!r}, "
            f"archived_at={_archived_at!r}, "
            f"created_at={_created_at!r}, "
            f"updated_at={_updated_at!r}, "
            f"products_count={_products_count!r}, "
            f"plans_count={_plans_count!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _key=(
            self.key
            if hasattr(self, "key")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _kind=(
            self.kind
            if hasattr(self, "kind")
            else None
        )
        _unit=(
            self.unit
            if hasattr(self, "unit")
            else None
        )
        _value_type=(
            self.value_type
            if hasattr(self, "value_type")
            else None
        )
        _default_value=(
            self.default_value
            if hasattr(self, "default_value")
            else None
        )
        _default_periodicity_interval=(
            self.default_periodicity_interval
            if hasattr(self, "default_periodicity_interval")
            else None
        )
        _default_periodicity_unit=(
            self.default_periodicity_unit
            if hasattr(self, "default_periodicity_unit")
            else None
        )
        _archived_at=(
            self.archived_at
            if hasattr(self, "archived_at")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _products_count=(
            self.products_count
            if hasattr(self, "products_count")
            else None
        )
        _plans_count=(
            self.plans_count
            if hasattr(self, "plans_count")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"key={_key!s}, "
            f"name={_name!s}, "
            f"description={_description!s}, "
            f"kind={_kind!s}, "
            f"unit={_unit!s}, "
            f"value_type={_value_type!s}, "
            f"default_value={_default_value!s}, "
            f"default_periodicity_interval={_default_periodicity_interval!s}, "
            f"default_periodicity_unit={_default_periodicity_unit!s}, "
            f"archived_at={_archived_at!s}, "
            f"created_at={_created_at!s}, "
            f"updated_at={_updated_at!s}, "
            f"products_count={_products_count!s}, "
            f"plans_count={_plans_count!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
