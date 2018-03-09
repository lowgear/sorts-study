from sorts.sort_common import sort_preparation


def _sort(lst, d, key, cmp):
    for t in range(d):
        for i in range(t, len(lst), d):
            while i >= d and cmp(key(lst[i]), key(lst[i - d])):
                lst[i], lst[i - d] = lst[i - d], lst[i]
                i -= d


def sort(lst, key=None, reverse=False):
    key, cmp = sort_preparation(lst, key, reverse)

    _sort(lst, 1, key, cmp)


def best_case_data(length: int):
    return [i for i in range(length)]


def worst_case_data(length: int):
    return [i for i in range(length, -1, -1)]
