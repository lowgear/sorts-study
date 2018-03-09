import random


DEFAULT_SEED = 7
r = random.Random(DEFAULT_SEED)


def _less(x, y):
    return x < y


def _greater(x, y):
    return y > x


def sort_preparation(lst, key=None, reverse=False):
    if not isinstance(lst, list):
        raise TypeError("a list is required (got type {0})".format(type(lst)))
    if not isinstance(reverse, bool):
        raise TypeError("a bool is required (got type {0})".format(type(lst)))

    if key is None:
        def key(v):
            return v
    if reverse:
        return key, _greater
    return key, _less


random_data_cache = dict()


def random_data(length: int):
    if length not in random_data_cache.keys():
        random_data_cache[length] = \
            [r.randint(0, length) for i in range(length)]
    return random_data_cache[length]
