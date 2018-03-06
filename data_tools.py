import random


def generate_random_int_list(length, unique_elements_num=None, seed=None):
    """ 
    :param length: length of list to generate 
    :param unique_elements_num: any if zero given
    :param seed: set same seed to get same result
    :return: result list
    """
    if not isinstance(length, int):
        raise TypeError("length should be integer")
    if not isinstance(unique_elements_num, int)\
            and unique_elements_num is not None:
        raise TypeError("unique_elements_num should be integer")
    if length < 0:
        raise ValueError("length can not be negative")
    if unique_elements_num:
        if unique_elements_num > length:
            raise ValueError("unique_elements_num element can not exceed length")
        if unique_elements_num < 0:
            raise ValueError("unique_elements_num should can not be negative")

    r = random.Random(seed)
    if unique_elements_num is None:
        a = -(10 ** 6)
        b = 10 ** 6
        return [r.randint(a, b) for i in range(length)]

    result = [i for i in range(unique_elements_num)]
    remain = length - unique_elements_num
    result += [r.randint(0, unique_elements_num - 1) for i in range(remain)]
    return result


def save_data(data, path):
    if not isinstance(data, list):
        raise TypeError("list expected")
    with open(path, 'w', encoding='ascii') as f:
        f.write('\n'.join(str(i) for i in data))
        # for i in data:
        #     f.write(str(i) + '\n')


def load_data(path):
    with open(path, 'r', encoding='ascii') as f:
        res = []
        while True:
            s = f.readline()
            if s == '':
                return res
            res.append(int(s))

