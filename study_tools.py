from testing_tools import time_stat_on_data
import data_tools
import os, shutil

from sorts.bubble_sort import bubble_sort
from sorts.heap_sort import heap_sort
from sorts.hoare_sort import hoare_sort
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.shell_sort import shell_sort


TEST_LIST_FILE_NAME = 'sorttest.testlist'
RESULTS_DIR_NAME = 'sorttest.results'
TEST_EXTENSION = '.sorttest'
RESULT_EXTENSION = TEST_EXTENSION + '.result'
ALL_SORTS = [list.sort, heap_sort, hoare_sort, merge_sort,
             shell_sort, insertion_sort, bubble_sort]


class StopStudy(RuntimeError):
    pass


def study_sort(sort, tests):
    results = []
    for test in tests:
        results.append(time_stat_on_data(test, sort, min_series_len=5))
    return results


def _gen_sizes(max_length):
    # for i in range(10, min(100, max_length)):
    #     yield i
    for i in range(100, min(1000, max_length), 3):
        yield i
    size = 1000
    while size <= max_length:
        yield size
        size *= 2
    if size > max_length:
        yield max_length


def _names_path(folder):
    return os.path.join(folder, TEST_LIST_FILE_NAME)


def _prepare_dir(folder):
    if os.path.isfile(folder):
        raise ValueError("given path is file")
    if not os.path.isdir(folder):
        os.makedirs(folder)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Couldn\'t delete element:\n', e)


def generate_random_tests(folder, sizes):
    _prepare_dir(folder)
    
    names = []
    for size in sizes:
        file_name = str(size) + TEST_EXTENSION
        names.append(file_name)
        data = data_tools.generate_random_int_list(size)
        data_tools.save_data(data, os.path.join(folder, file_name))

    with open(_names_path(folder), 'w', encoding='utf-8') as f:
        f.write('\n'.join(names))


def gen_usual_random_tests(folder, max_length):
    generate_random_tests(folder, _gen_sizes(max_length))


def load_names_from_dir(folder):
    with open(_names_path(folder), 'r', encoding='utf-8') as f:
        res = f.readlines()
    return [s[:-1] if s[-1] == '\n' else s for s in res if s != '']


def load_tests_from_dir_by_one(folder):
    for name in load_names_from_dir(folder):
        yield data_tools.load_data(os.path.join(folder, name))


def test_sort_on_row_of_tests(sort, folder):
    results_dir_path = os.path.join(folder, RESULTS_DIR_NAME)
    if not os.path.isdir(results_dir_path):
        os.makedirs(results_dir_path)

    result_path = os.path.join(results_dir_path, sort.__name__ + RESULT_EXTENSION)
    with open(result_path, 'w', encoding='utf-8'):
        pass
    for data in load_tests_from_dir_by_one(folder):
        size = len(data)
        result = time_stat_on_data(data, sort)
        with open(result_path, 'a', encoding='utf-8') as f:
            f.write(' '.join(str(i) for i in [size, *result]) + '\n')


def test_all_sorts(folder):
    for sort in ALL_SORTS:
        test_sort_on_row_of_tests(sort, folder)


def load_results(file):
    if os.path.split(file)[1][-len(RESULT_EXTENSION):] != RESULT_EXTENSION:
        raise ValueError('{0} "extension" expected.'.format(RESULT_EXTENSION))
    with open(file, 'r', encoding='utf-8') as f:
        results = f.readlines()
    results = [s.split() for s in results]
    conf_intervals = []
    for i in results:
        conf_intervals.append(int(i[0]))
        conf_intervals.append(float(i[1]))
        conf_intervals.append(float(i[2]))
    return conf_intervals