import concurrent.futures
import datetime
import math
import random
import statistics
import time

import functools

# from scipy.stats import t todo
import gc

DEV_TO_MEAN_COEFFICIENT = 0.05
CONF = 0.95
DEFAULT_SERIES_LENGTH = 10

WARM_UP_TIMES = 10
WARM_UP_DATA_LENGTH = 1000
WARM_UP_RANDOM_SEED = 7
DEFAULT_WARM_UP_TIMEOUT = datetime.timedelta(minutes=1).total_seconds()
DEFAULT_BENCHMARK_TIMEOUT = datetime.timedelta(minutes=10).total_seconds()
EXECUTOR = concurrent.futures.ThreadPoolExecutor()


def mean_stdev(series):
    """

    :param series: list of measured values. Minimal required length is 2.
    :return: tuple of mean and standard deviation
    """
    mean = statistics.mean(series)
    stdev = statistics.stdev(series, mean)
    return mean, stdev


class CmpCounter:
    def __init__(self):
        self.counter = 0

        def counting_cmp(a, b):
            self.counter += 1
            if a < b:
                return -1
            if a > b:
                return 1
            return 0

        self.key = functools.cmp_to_key(counting_cmp)


def warm_sort_up(sort):
    r = random.Random(WARM_UP_RANDOM_SEED)

    for i in range(WARM_UP_TIMES):
        data = [j for j in range(WARM_UP_DATA_LENGTH)]
        r.shuffle(data)
        cmp_counter = CmpCounter()
        sort(data, key=cmp_counter.key)


def warm_sort_with_timeout(sort, timeout=DEFAULT_WARM_UP_TIMEOUT):
    warm_up_task = EXECUTOR.submit(warm_sort_up, sort)
    try:
        warm_up_task.result(timeout=timeout)
    except concurrent.futures.TimeoutError:
        pass
    except RecursionError:
        pass


def measure_time(func):
    """

    :param func: function without arguments to measure its execution time
    :return: execution time in seconds fraction
    """
    start_time = time.perf_counter()
    func()
    finish_time = time.perf_counter()

    return finish_time - start_time


def benchmark(sort, data: list, benchmark_timeout=DEFAULT_BENCHMARK_TIMEOUT,
              count_cmps=False):
    """

    :param sort: sort function with signature matching list.sort signature
    :param data: data to benchmark sort function on
    :param benchmark_timeout:
    :return: tuple of execution time in seconds(or math.inf if timeout) and
    number of executed comparisons
    """
    if count_cmps:
        cmp_counter = CmpCounter()
        key = cmp_counter.key
    else:
        def key(x):
            return x
    data_copy = data.copy()
    measure_time_task = EXECUTOR.submit(measure_time,
                                        lambda: sort(data_copy,
                                                     key=key))

    gc.collect()

    try:
        execution_time = measure_time_task.result(timeout=benchmark_timeout)
    except concurrent.futures.TimeoutError:
        execution_time = math.inf
    except RecursionError as e:
        execution_time = e
    if count_cmps:
        return execution_time, cmp_counter.counter
    return execution_time


def benchmark_on_kind_of_data(sort, data_generator, lengths):
    """

    :param sort: 
    :param data_generator: function which returns data of given length 
    :param lengths: sequence of lengths to benchmark sort on
    """
    result = []
    print("Test on {0}".format(data_generator.__name__))
    for length in lengths:
        data = data_generator(length)
        print("\tof length {0}".format(length))
        series = []
        for i in range(DEFAULT_SERIES_LENGTH):
            print("\t\t{0}/{1}".format(i + 1, DEFAULT_SERIES_LENGTH))
            time = benchmark(sort, data)
            print("\t\tDone!")
            if time != math.inf and not isinstance(time, RecursionError):
                series.append(time)
            else:
                print("\t\tTIMEOUT OR TOO DEEP RECURSION! SERIES STOPPED")
                result.append((length, time))
                series.clear()
                break
        if len(series) >= 2:
            result.append((length, mean_stdev(series)))
    return result
