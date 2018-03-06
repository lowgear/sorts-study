import unittest
import random
from sorts.bubble_sort import bubble_sort
from sorts.heap_sort import heap_sort
from sorts.hoare_sort import hoare_sort
from sorts.merge_sort import merge_sort
from sorts.shell_sort import shell_sort
from sorts.insertion_sort import insertion_sort

size = 0


def test_sort_random_unique(self, sort):
    original_data = [i for i in range(size)]
    r = random.Random(1)
    r.shuffle(original_data)

    data_copy = original_data[:]

    sort(original_data)
    data_copy.sort()

    self.assertEqual(original_data, data_copy)


def test_sort_random_repeatable(self, sort):
    r = random.Random(1)
    original_data = []
    for i in range(size):
        original_data.append(r.randint(0, size // 3))

    data_copy = original_data[:]

    sort(original_data)
    data_copy.sort()

    self.assertEqual(original_data, data_copy)


def test_sort_uniform(self, sort):
    original_data = []
    for i in range(size):
        original_data.append(15)

    data_copy = original_data[:]

    sort(original_data)
    data_copy.sort()

    self.assertEqual(original_data, data_copy)


def test_sort(self, sort):
    for i in range(100):
        global size
        size = i
        test_sort_random_unique(self, sort)
        test_sort_random_repeatable(self, sort)
        test_sort_uniform(self, sort)


class TestSortsCorrectness(unittest.TestCase):
    # @unittest.skip
    def test_bubble_sort(self):
        test_sort(self, bubble_sort)

    # @unittest.skip
    def test_hoare_sort(self):
        test_sort(self, hoare_sort)

    # @unittest.skip
    def test_heap_sort(self):
        test_sort(self, heap_sort)

    def test_merge_sort(self):
        test_sort(self, merge_sort)

    def test_shell_sort(self):
        test_sort(self, shell_sort)

    def test_insertion_sort(self):
        test_sort(self, insertion_sort)


if __name__ == '__main__':
    unittest.main()
