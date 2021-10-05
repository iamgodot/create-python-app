from {{cookiecutter.project_slug}} import dict_substract


class TestDictUtils():
    '''Test dict related functions.
    '''
    def test_substract(self):
        dict1 = {'a': 11, 'b': 0}
        dict2 = {'b': 0}

        assert dict_substract(dict1, dict2) == {'a': 11}
