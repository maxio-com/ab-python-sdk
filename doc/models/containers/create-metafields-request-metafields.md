
# Create Metafields Request Metafields

## Data Type

`CreateMetafield | List[CreateMetafield]`

## Cases

| Type |
|  --- |
| [`CreateMetafield`](../../../doc/models/create-metafield.md) |
| [`List[CreateMetafield]`](../../../doc/models/create-metafield.md) |

## CreateMetafield

### Initialization Code

#### Example

```python
value = CreateMetafield(
    name='my_field',
    scope=MetafieldScope(
        csv=IncludeOption.EXCLUDE,
        invoices=IncludeOption.EXCLUDE,
        statements=IncludeOption.EXCLUDE,
        portal=IncludeOption.EXCLUDE,
        public_show=IncludeOption.EXCLUDE,
        public_edit=IncludeOption.EXCLUDE
    ),
    input_type=MetafieldInput.TEXT,
    enum=[
        'string'
    ]
)
```

## List[CreateMetafield]

### Initialization Code

#### Example

```python
value = [
    CreateMetafield()
]
```

