from sorts.sort_common import sort_preparation


class _MergeSorter:
    def __init__(self, key, cmp):
        self.key = key
        self.less = cmp

    def sort(self, lst1, lst2, left, right, invert):
        if left + 1 == right:
            if invert:
                lst2[left] = lst1[left]
            return

        middle = (left + right) // 2
        self.sort(lst1, lst2, left, middle, not invert)
        self.sort(lst1, lst2, middle, right, not invert)

        if invert % 2 == 1:
            source = lst1
            dist = lst2
        else:
            source = lst2
            dist = lst1
        self._merge(source, dist, left, middle, right)

    def _merge(self, source, dist, left, middle, right):
        i = left
        j = middle
        while i < middle and j < right:
            if self.less(self.key(source[j]), self.key(source[i])):
                dist[-middle + i + j] = source[j]
                j += 1
            else:
                dist[-middle + i + j] = source[i]
                i += 1
        if i == middle:
            remain = (j, right)
        else:
            remain = (i, middle)
        for i in range(*remain):
            dist[right - remain[1] + i] = source[i]


def sort(lst, key=None, reverse=False):
    key, cmp = sort_preparation(lst, key, reverse)
    if len(lst) == 0:
        return

    buffer = [None for i in range(len(lst))]
    # depth = int(math.ceil(math.log2(len(lst))))
    _MergeSorter(key, cmp).sort(lst, buffer, 0, len(lst), False)


def best_case_data(length: int):
    return [i for i in range(length)]


def _worst_order(ordered_elements):
    if len(ordered_elements) == 0:
        return []
    return _worst_order([ordered_elements[::2]]) + \
        _worst_order([ordered_elements[1::2]])


def worst_case_data(length: int):
    return _worst_order([i for i in range(length)])
