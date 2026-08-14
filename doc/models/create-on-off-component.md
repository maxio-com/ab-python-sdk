
# Create On Off Component

## Structure

`CreateOnOffComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `on_off_component` | [`OnOffComponent`](../../doc/models/on-off-component.md) | Required | - |

## Example

```python
from advancedbilling.models.create_on_off_component import CreateOnOffComponent
from advancedbilling.models.credit_type import CreditType
from advancedbilling.models.on_off_component import OnOffComponent

create_on_off_component = CreateOnOffComponent(
    on_off_component=OnOffComponent(
        name='name6',
        unit_price='String5',
        description='description6',
        handle='handle2',
        taxable=False,
        upgrade_charge=CreditType.FULL,
        downgrade_credit=CreditType.FULL
    )
)
```

