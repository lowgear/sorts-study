from sorts.sort_common import sort_preparation
from sorts.insertion_sort import _sort


def _generate_d(length):
    while length != 0:
        length //= 2
        yield length


def shell_sort(lst, key=None, reverse=False):
    key, less = sort_preparation(lst, key, reverse)

    for d in _generate_d(len(lst)):
        _sort(lst, d, key, less)