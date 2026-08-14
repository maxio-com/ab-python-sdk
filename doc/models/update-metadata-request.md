
# Update Metadata Request

## Structure

`UpdateMetadataRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`UpdateMetadata`](../../doc/models/update-metadata.md) | Optional | - |

## Example

```python
from advancedbilling.models.update_metadata import UpdateMetadata
from advancedbilling.models.update_metadata_request import UpdateMetadataRequest

update_metadata_request = UpdateMetadataRequest(
    metadata=UpdateMetadata(
        current_name='current_name0',
        name='name6',
        value='value8'
    )
)
```

