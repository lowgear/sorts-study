from sorts.sort_common import sort_preparation
from sorts.insertion_sort import _sort


def _generate_d(length):
    while length != 0:
        length //= 2
        yield length


def sort(lst, key=None, reverse=False):
    key, less = sort_preparation(lst, key, reverse)

    for d in _generate_d(len(lst)):
        _sort(lst, d, key, less)


# this is reasonable because it such case there would not be any swaps at all
# and only O(n log n) comparisons
def best_case_data(length: int):
    return [i for i in range(length)]


# that is pure suggestion. In cases when length is power of 2 complexity is
# more or less analyzable but otherwise is to difficult. As far as I know there
# is no complete analysis for Shell sort
def worst_case_data(length: int):
    return [i for i in range(length, -1, -1)]
