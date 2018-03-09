from sorts.sort_common import sort_preparation


class _Heapifier:
    def __init__(self, key, cmp):
        self.key = key
        self.less = cmp

    def heapify(self, lst):
        for i in range((len(lst) - 1) // 2, -1, -1):
            self.sift_down(lst, i, len(lst))

    def delete_max(self, lst, length):
        lst[0], lst[length - 1] = lst[length - 1], lst[0]
        self.sift_down(lst, 0, length - 1)

    def sift_down(self, lst, i, length):
        while True:
            left = i * 2 + 1
            right = left + 1
            if right < length:
                if self.less(self.key(lst[right]), self.key(lst[left])):
                    son = left
                else:
                    son = right
            elif left < length:
                son = left
            else:
                return
            if self.less(self.key(lst[i]), self.key(lst[son])):
                lst[i], lst[son] = lst[son], lst[i]
                i = son
            else:
                return


def sort(lst, key=None, reverse=False):
    key, cmp = sort_preparation(lst, key, reverse)

    h = _Heapifier(key, cmp)
    h.heapify(lst)
    for i in range(len(lst)):
        h.delete_max(lst, len(lst) - i)


def best_case_data(length: int):
    return [0 for i in range(length)]


def worst_case_data(length: int):
    return [i for i in range(length)]