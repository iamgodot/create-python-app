from {{cookiecutter.project_slug}} import dict_subtract


class TestDictUtils:
    """Test dict related functions."""

    def test_subtract(self):
        dict1 = {"a": 11, "b": 0}
        dict2 = {"b": 0}

        assert dict_subtract(dict1, dict2) == {"a": 11}
