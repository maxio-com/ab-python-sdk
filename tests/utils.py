def assert_properties(obj, properties: dict) -> None:
    for key, value in properties.items():
        actual_val = getattr(obj, key, None)
        assert actual_val == value, f"Value of key: `{key}` is {actual_val} but expected {value}"
