from copy import deepcopy


def dict_subtract(dict1, dict2):
    '''subtract dict2 from dict1 and return dict1.
    Args:
        dict1: supposed to be the minuend.
        dict2: supposed to be the subtrahend.
    Returns:
        difference dict from the subtraction.
    '''

    if isinstance(dict1, dict) and isinstance(dict2, dict):
        dict_diff = deepcopy(dict1)

        for k, v in dict2.items():
            if dict_diff.get(k) == v:
                del dict_diff[k]

        return dict_diff
    else:
        raise ValueError('Only do subtraction between two dicts!')
