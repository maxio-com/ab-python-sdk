"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class ProformaInvoiceTaxSourceType(object):
    """Implementation of the 'Proforma Invoice Tax Source Type' enum.

    The source of the tax. `Tax` is a tax configured in Advanced Billing. The other
    values identify the tax service that calculated the tax.

    Attributes:
        TAX: The enum member of type str.
        AVALARA: The enum member of type str.
        ANROK: The enum member of type str.
        TAXJAR: The enum member of type str.
        NUMERAL: The enum member of type str.
        SPHERE: The enum member of type str.
        TAXWIRE: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    _all_values = ["Tax", "Avalara", "Anrok", "TaxJar", "Numeral", "Sphere", "Taxwire"]
    TAX = "Tax"

    AVALARA = "Avalara"

    ANROK = "Anrok"

    TAXJAR = "TaxJar"

    NUMERAL = "Numeral"

    SPHERE = "Sphere"

    TAXWIRE = "Taxwire"

    @classmethod
    def validate(cls, value):
        """Validate value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
