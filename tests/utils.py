def assert_properties(obj, properties: dict) -> None:
    for key, value in properties.items():
        if isinstance(value, dict):
            assert_properties(getattr(obj, key, None), value)
            continue

        actual_val = getattr(obj, key, None)
        assert actual_val == value, f"Value of key: `{key}` is {actual_val} but expected {value}"
