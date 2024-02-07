def assert_properties(obj, properties: dict) -> None:
    for key, value in properties.items():
        if isinstance(value, dict):
            assert_properties(getattr(obj, key, None), value)
            continue

        if isinstance(value, list):
            assert len(getattr(obj, key)) == len(value)

            for i, item in enumerate(value):
                if isinstance(item, dict):
                    assert_properties(getattr(obj, key)[i], item)
                    continue

                assert getattr(obj, key)[i] == item

            continue

        actual_val = getattr(obj, key, None)
        assert actual_val == value, f"Value of key: `{key}` is {actual_val} but expected {value}"
