
# Create Metadata Request

## Structure

`CreateMetadataRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`List[CreateMetadata]`](../../doc/models/create-metadata.md) | Required | - |

## Example

```python
from advancedbilling.models.create_metadata import CreateMetadata
from advancedbilling.models.create_metadata_request import CreateMetadataRequest

create_metadata_request = CreateMetadataRequest(
    metadata=[
        CreateMetadata(
            name='name6',
            value='value8'
        )
    ]
)
```

