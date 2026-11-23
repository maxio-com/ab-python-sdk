"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class WalletProduct1(object):
    """Implementation of the 'WalletProduct1' model.

    Attributes:
        name (str): The model property of type str.
        description (str): The model property of type str.
        taxable (bool): The model property of type bool.
        tax_code (str): The model property of type str.
        accounting_code (str): The model property of type str.
        item_category (ItemCategory): One of the following: Business Software,
            Consumer Software, Digital Services, Physical Goods, Other
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "description": "description",
        "taxable": "taxable",
        "tax_code": "tax_code",
        "accounting_code": "accounting_code",
        "item_category": "item_category",
    }

    _optionals = [
        "name",
        "description",
        "taxable",
        "tax_code",
        "accounting_code",
        "item_category",
    ]

    _nullables = [
        "description",
        "tax_code",
        "accounting_code",
        "item_category",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        taxable=APIHelper.SKIP,
        tax_code=APIHelper.SKIP,
        accounting_code=APIHelper.SKIP,
        item_category=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a WalletProduct1 instance."""
        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code
        if item_category is not APIHelper.SKIP:
            self.item_category = item_category

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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        description =\
            dictionary.get("description")\
            if "description" in dictionary.keys()\
                else APIHelper.SKIP
        taxable =\
            dictionary.get("taxable")\
            if "taxable" in dictionary.keys()\
                else APIHelper.SKIP
        tax_code =\
            dictionary.get("tax_code")\
            if "tax_code" in dictionary.keys()\
                else APIHelper.SKIP
        accounting_code =\
            dictionary.get("accounting_code")\
            if "accounting_code" in dictionary.keys()\
                else APIHelper.SKIP
        item_category =\
            dictionary.get("item_category")\
            if "item_category" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(name,
                   description,
                   taxable,
                   tax_code,
                   accounting_code,
                   item_category,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
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
        _taxable=(
            self.taxable
            if hasattr(self, "taxable")
            else None
        )
        _tax_code=(
            self.tax_code
            if hasattr(self, "tax_code")
            else None
        )
        _accounting_code=(
            self.accounting_code
            if hasattr(self, "accounting_code")
            else None
        )
        _item_category=(
            self.item_category
            if hasattr(self, "item_category")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}, "
            f"description={_description!r}, "
            f"taxable={_taxable!r}, "
            f"tax_code={_tax_code!r}, "
            f"accounting_code={_accounting_code!r}, "
            f"item_category={_item_category!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
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
        _taxable=(
            self.taxable
            if hasattr(self, "taxable")
            else None
        )
        _tax_code=(
            self.tax_code
            if hasattr(self, "tax_code")
            else None
        )
        _accounting_code=(
            self.accounting_code
            if hasattr(self, "accounting_code")
            else None
        )
        _item_category=(
            self.item_category
            if hasattr(self, "item_category")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}, "
            f"description={_description!s}, "
            f"taxable={_taxable!s}, "
            f"tax_code={_tax_code!s}, "
            f"accounting_code={_accounting_code!s}, "
            f"item_category={_item_category!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
