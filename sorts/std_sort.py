sort = list.sort


# todo
# in presumption that std sort is smart enough to check if data is sorted
def best_case_data(length: int):
    return [i for i in range(length)]


# todo better worst case
def worst_case_data(length: int):
    return [i for i in range(length, -1, -1)]
