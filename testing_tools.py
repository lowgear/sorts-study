import statistics
import time
from scipy.stats import t

DEV_TO_MEAN_COEFFICIENT = 0.05
CONF = 0.95


def sort_time(data, sort):
    """
    Measures time of executing given sort funtion on given data.
    :param data: 
    :param sort: 
    :return: time in fractional seconds
    """
    data = data[:]
    start_time = time.perf_counter()
    sort(data)
    finish_time = time.perf_counter()

    return finish_time - start_time


def _mean_and_stdev(series):
    mean = statistics.mean(series)
    stdev = statistics.stdev(series, mean)
    return mean, stdev


def time_stat_on_data(data, sort, min_series_len=2, max_series_len=50):
    """
    Measures sort execution time on the same data given times and returns
    series as a list.
    :param data: 
    :param sort: 
    :param min_series_len: should not be less than 2
    :return: 
    """
    if not isinstance(min_series_len, int):
        raise TypeError("min_series_len can only be int")
    if min_series_len < 2:
        raise ValueError("series can not be shorter than 2")

    # warm up caches I guess
    sort([i for i in range(500, 0, -1)])

    series = [sort_time(data, sort) for i in range(min_series_len)]

    while True:
        mean, stdev = _mean_and_stdev(series)
        if stdev / mean < DEV_TO_MEAN_COEFFICIENT \
                or (max_series_len and len(series) > max_series_len):
            return t.interval(CONF, len(series), mean, stdev / len(series))
        series.append(sort_time(data, sort))
