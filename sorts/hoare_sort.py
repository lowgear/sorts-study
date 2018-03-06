from sorts.sort_common import sort_preparation
from random import randint


class _HoareSorter:
    def __init__(self, key, cmp):
        self.key = key
        self.less = cmp

    def _partition(self, lst, left, right):
        pivot_key = self.key(lst[randint(left, right)])
        # pivot_key = self.key(lst[left])
        low, high = left, right
        while True:
            while self.less(self.key(lst[low]), pivot_key):
                low += 1
            while low <= high \
                    and not self.less(self.key(lst[high]), pivot_key):
                high -= 1

            if low < high:
                lst[low], lst[high] = lst[high], lst[low]
            else:
                break
        res_low = high

        high = right

        while True:
            while low <= right and self.key(lst[low]) == pivot_key:
                low += 1
            while self.less(pivot_key, self.key(lst[high])):
                high -= 1

            if low < high:
                lst[low], lst[high] = lst[high], lst[low]
            else:
                break

        return res_low, low

    def sort(self, lst, left, right):
        if left >= right:
            return
        low, high = self._partition(lst, left, right)
        self.sort(lst, left, low)
        self.sort(lst, high, right)


def hoare_sort(lst, key=None, reverse=False):
    key, cmp = sort_preparation(lst, key, reverse)
    _HoareSorter(key, cmp).sort(lst, 0, len(lst) - 1)
