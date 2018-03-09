import math


class Measurement:
    def __init__(self, sort_name, data_kind, points):
        self.points = points
        self.data_kind = data_kind
        self.sort_name = sort_name


def serialize_stat_point(point):
    if point[1] == math.inf:
        return str(point[0]) + ' ' + str(point[1])
    if isinstance(point[1], RecursionError) or point[1] == math.inf:
        return str(point[0]) + ' ' + RecursionError.__name__
    return str(point[0]) + ' ' + str(point[1][0]) + ' ' + str(point[1][1])


def get_machine_stats(f):
    return ""  # todo


def load_point(f):
    return tuple(float(i) for i in f.readline().split())


def load_series(f):
    sort_name = f.readline().replace("\n", "")
    data_kind = f.readline().replace("\n", "")
    points_number = int(f.readline())
    points = [load_point(f) for i in range(points_number)]
    return Measurement(sort_name, data_kind, points)


class Results:
    def __init__(self, machine_stats, measurements):
        self.measurements = measurements
        self.machine_stats = machine_stats


def load_results(file):
    with open(file, "r", encoding="ascii") as f:
        machine_stats = get_machine_stats(f)
        results = list()
        while True:
            try:
                results.append(load_series(f))
            except EOFError:
                break
            except ValueError:
                break
    return Results(machine_stats, results)


def serialize_result(data_kind, series, sort_module):
    return "\n".join([sort_module.__name__,
                      data_kind.__name__,
                      str(len(series)),
                      '\n'.join(
                          (serialize_stat_point(point)
                           for point in series))]) + "\n"


def current_machine_stats_str():
    return ""  # todo