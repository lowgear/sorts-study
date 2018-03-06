from sorts.sort_common import sort_preparation


def _sort(lst, d, key, less):
    for t in range(d):
        for i in range(t, len(lst), d):
            while i >= d and less(key(lst[i]), key(lst[i - d])):
                lst[i], lst[i - d] = lst[i - d], lst[i]
                i -= d


def insertion_sort(lst, key=None, reverse=False):
    key, less = sort_preparation(lst, key, reverse)

    _sort(lst, 1, key, less)