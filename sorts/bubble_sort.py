from sorts.sort_common import sort_preparation


def sort(lst, key=None, reverse=False):
    key, less = sort_preparation(lst, key, reverse)

    flag = True
    while flag:
        flag = False
        for i in range(len(lst) - 1):
            if less(key(lst[i + 1]), key(lst[i])):
                flag = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def best_case_data(length: int):
    return [i for i in range(length)]


def worst_case_data(length: int):
    return [i for i in range(length, -1, -1)]
