"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ProductFamily(object):
    """Implementation of the 'Product Family' model.

    Attributes:
        id (int): The model property of type int.
        name (str): The model property of type str.
        handle (str): The model property of type str.
        accounting_code (str): The model property of type str.
        description (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        archived_at (datetime): Timestamp indicating when this product family was
            archived. `null` if the product family is not archived.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "name": "name",
        "handle": "handle",
        "accounting_code": "accounting_code",
        "description": "description",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "archived_at": "archived_at",
    }

    _optionals = [
        "id",
        "name",
        "handle",
        "accounting_code",
        "description",
        "created_at",
        "updated_at",
        "archived_at",
    ]

    _nullables = [
        "accounting_code",
        "description",
        "archived_at",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        handle=APIHelper.SKIP,
        accounting_code=APIHelper.SKIP,
        description=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        updated_at=APIHelper.SKIP,
        archived_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ProductFamily instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if handle is not APIHelper.SKIP:
            self.handle = handle
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code
        if description is not APIHelper.SKIP:
            self.description = description
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
        if archived_at is not APIHelper.SKIP:
            self.archived_at =\
                 APIHelper.apply_datetime_converter(
                archived_at, APIHelper.RFC3339DateTime)\
                 if archived_at else None

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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        handle =\
            dictionary.get("handle")\
            if dictionary.get("handle")\
                else APIHelper.SKIP
        accounting_code =\
            dictionary.get("accounting_code")\
            if "accounting_code" in dictionary.keys()\
                else APIHelper.SKIP
        description =\
            dictionary.get("description")\
            if "description" in dictionary.keys()\
                else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_at")).datetime\
            if dictionary.get("updated_at") else APIHelper.SKIP
        if "archived_at" in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("archived_at")).datetime\
                if dictionary.get("archived_at") else None

        else:
            archived_at = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   name,
                   handle,
                   accounting_code,
                   description,
                   created_at,
                   updated_at,
                   archived_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _accounting_code=(
            self.accounting_code
            if hasattr(self, "accounting_code")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
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
        _archived_at=(
            self.archived_at
            if hasattr(self, "archived_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"name={_name!r}, "
            f"handle={_handle!r}, "
            f"accounting_code={_accounting_code!r}, "
            f"description={_description!r}, "
            f"created_at={_created_at!r}, "
            f"updated_at={_updated_at!r}, "
            f"archived_at={_archived_at!r}, "
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _handle=(
            self.handle
            if hasattr(self, "handle")
            else None
        )
        _accounting_code=(
            self.accounting_code
            if hasattr(self, "accounting_code")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
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
        _archived_at=(
            self.archived_at
            if hasattr(self, "archived_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"name={_name!s}, "
            f"handle={_handle!s}, "
            f"accounting_code={_accounting_code!s}, "
            f"description={_description!s}, "
            f"created_at={_created_at!s}, "
            f"updated_at={_updated_at!s}, "
            f"archived_at={_archived_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
