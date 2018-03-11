import unittest
import random
from sorts.bubble_sort import sort as bubble_sort
from sorts.heap_sort import sort as heap_sort
from sorts.hoare_sort import sort as hoare_sort
from sorts.merge_sort import sort as merge_sort
from sorts.shell_sort import sort as shell_sort
from sorts.insertion_sort import sort as insertion_sort

LENGTH_LIMIT = 200
RECURSION_TEST_LENGTH = 1_000_000


def uniform_data(length: int, x=7):
    return [x for i in range(length)]


def increasing_unique_data(length: int):
    return list(range(length))


def decreasing_unique_data(length: int):
    return list(range(length, 0, -1))


def random_data(length: int, seed=1):
    r = random.Random(seed)
    return [r.randint(0, length) for i in range(length)]


def random_unique_data(length: int, seed=1):
    r = random.Random(seed)
    data = increasing_unique_data(length)
    r.shuffle(data)
    return data


ALL_DATA_KINDS = [uniform_data,
                  increasing_unique_data,
                  decreasing_unique_data,
                  random_data,
                  random_unique_data]


def test_sort(self, sort, data: list):
    sorted_by_std_sort = data.copy()

    sort(data)
    list.sort(sorted_by_std_sort)

    self.assertEqual(data, sorted_by_std_sort)


def test_with_data_generator(self, sort, data):
    for length in range(LENGTH_LIMIT):
        with self.subTest():
            test_sort(self, sort, data(length))


class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.sort = bubble_sort

    def test_on_uniform(self):
        test_with_data_generator(self, self.sort, uniform_data)

    def test_on_increasing(self):
        test_with_data_generator(self, self.sort, increasing_unique_data)

    def test_on_decreasing(self):
        test_with_data_generator(self, self.sort, decreasing_unique_data)

    def test_on_random(self):
        test_with_data_generator(self, self.sort, random_data)

    def test_on_random_unique(self):
        test_with_data_generator(self, self.sort, random_unique_data)


class InsertionSortTest(unittest.TestCase):
    def setUp(self):
        self.sort = insertion_sort

    def test_on_uniform(self):
        test_with_data_generator(self, self.sort, uniform_data)

    def test_on_increasing(self):
        test_with_data_generator(self, self.sort, increasing_unique_data)

    def test_on_decreasing(self):
        test_with_data_generator(self, self.sort, decreasing_unique_data)

    def test_on_random(self):
        test_with_data_generator(self, self.sort, random_data)

    def test_on_random_unique(self):
        test_with_data_generator(self, self.sort, random_unique_data)


class ShellTest(unittest.TestCase):
    def setUp(self):
        self.sort = shell_sort

    def test_on_uniform(self):
        test_with_data_generator(self, self.sort, uniform_data)

    def test_on_increasing(self):
        test_with_data_generator(self, self.sort, increasing_unique_data)

    def test_on_decreasing(self):
        test_with_data_generator(self, self.sort, decreasing_unique_data)

    def test_on_random(self):
        test_with_data_generator(self, self.sort, random_data)

    def test_on_random_unique(self):
        test_with_data_generator(self, self.sort, random_unique_data)

    def test_sort_doesnt_fall_with_recursion_error(self):
        for data in ALL_DATA_KINDS:
            with self.subTest(data.__name__):
                self.sort(data(100_000))


class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.sort = merge_sort

    def test_on_uniform(self):
        test_with_data_generator(self, self.sort, uniform_data)

    def test_on_increasing(self):
        test_with_data_generator(self, self.sort, increasing_unique_data)

    def test_on_decreasing(self):
        test_with_data_generator(self, self.sort, decreasing_unique_data)

    def test_on_random(self):
        test_with_data_generator(self, self.sort, random_data)

    def test_on_random_unique(self):
        test_with_data_generator(self, self.sort, random_unique_data)

    def test_sort_doesnt_fall_with_recursion_error(self):
        for data in ALL_DATA_KINDS:
            with self.subTest(data.__name__):
                self.sort(data(RECURSION_TEST_LENGTH))


class HoareSortTest(unittest.TestCase):
    def setUp(self):
        self.sort = hoare_sort

    def test_on_uniform(self):
        test_with_data_generator(self, self.sort, uniform_data)

    def test_on_increasing(self):
        test_with_data_generator(self, self.sort, increasing_unique_data)

    def test_on_decreasing(self):
        test_with_data_generator(self, self.sort, decreasing_unique_data)

    def test_on_random(self):
        test_with_data_generator(self, self.sort, random_data)

    def test_on_random_unique(self):
        test_with_data_generator(self, self.sort, random_unique_data)

    def test_sort_doesnt_fall_with_recursion_error(self):
        for data in [uniform_data(RECURSION_TEST_LENGTH),
                     random_data(RECURSION_TEST_LENGTH),
                     random_unique_data(RECURSION_TEST_LENGTH)]:
            with self.subTest(data.__name__):
                self.sort(data)


class HeapSortTest(unittest.TestCase):
    def setUp(self):
        self.sort = heap_sort

    def test_on_uniform(self):
        test_with_data_generator(self, self.sort, uniform_data)

    def test_on_increasing(self):
        test_with_data_generator(self, self.sort, increasing_unique_data)

    def test_on_decreasing(self):
        test_with_data_generator(self, self.sort, decreasing_unique_data)

    def test_on_random(self):
        test_with_data_generator(self, self.sort, random_data)

    def test_on_random_unique(self):
        test_with_data_generator(self, self.sort, random_unique_data)

    def test_sort_doesnt_fall_with_recursion_error(self):
        for data in ALL_DATA_KINDS:
            with self.subTest(data.__name__):
                self.sort(data(300_000))


if __name__ == '__main__':
    unittest.main()
