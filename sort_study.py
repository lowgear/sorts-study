import argparse
import sorts.sort_common
from serialization import load_results, serialize_result, \
    current_machine_stats_str
from sorts import std_sort, heap_sort, hoare_sort, merge_sort, shell_sort, \
    insertion_sort, bubble_sort
from pathlib import Path
from testing_tools import benchmark_on_kind_of_data, warm_sort_with_timeout
from visualisation import visualize

ALL_SORTS = [std_sort, heap_sort, hoare_sort, merge_sort, shell_sort,
             insertion_sort, bubble_sort]

DEFAULT_DATA_LENGTHS = list(range(10, 100, 20)) + \
                       list(range(1000, 10000, 2000)) + \
                       list(range(10000, 100000, 20000))


def handle_study(args):
    with open(args.file, 'w', encoding="ascii") as file:
        file.write(current_machine_stats_str())

    for sort_module in args.sort_modules:
        data_kinds = []
        if args.worst_case:
            data_kinds.append(sort_module.worst_case_data)
        if args.best_case:
            data_kinds.append(sort_module.best_case_data)
        if args.random_case:
            data_kinds.append(sorts.sort_common.random_data)

        warm_sort_with_timeout(sort_module.sort)

        for data_kind in data_kinds:
            series = benchmark_on_kind_of_data(sort_module.sort,
                                               data_kind,
                                               DEFAULT_DATA_LENGTHS)
            with open(args.file, 'a', encoding="ascii") as file:
                serialization = serialize_result(data_kind, series,
                                                 sort_module)
                file.write(serialization)


def handle_visualize(args):
    results = load_results(args.file)  # todo
    visualize(results, args)


def main():
    parser = prepare_parser()
    args = parser.parse_args()
    args.func(args)


def prepare_parser():
    description = 'Utility to study sort functions efficiency.'
    parser = argparse.ArgumentParser(prog='sort_study',
                                     description=description)
    subparsers = parser.add_subparsers(title="subcommands")

    prepare_parser_study_command(subparsers)

    prepare_parser_visualize_command(subparsers)
    return parser


def prepare_parser_visualize_command(subparsers):
    visualize = subparsers.add_parser('visualize')
    visualize.add_argument('file', type=Path)
    visualize.set_defaults(func=handle_visualize)

    visualize.add_argument("--bubble", dest="sort_modules",
                           action="append_const", const=bubble_sort)
    visualize.add_argument("--heap", dest="sort_modules",
                           action="append_const", const=heap_sort)
    visualize.add_argument("--hoare", dest="sort_modules",
                           action="append_const", const=hoare_sort)
    visualize.add_argument("--insertion", dest="sort_modules",
                           action="append_const", const=insertion_sort)
    visualize.add_argument("--merge", dest="sort_modules",
                           action="append_const", const=merge_sort)
    visualize.add_argument("--shell", dest="sort_modules",
                           action="append_const", const=shell_sort)
    visualize.add_argument("--std", dest="sort_modules",
                           action="append_const", const=std_sort)

    visualize.add_argument("-b", "--best_case", action="store_true")
    visualize.add_argument("-w", "--worst_case", action="store_true")
    visualize.add_argument("-r", "--random_case", action="store_true")


def prepare_parser_study_command(subparsers):
    study_parser = subparsers.add_parser('study')
    study_parser.set_defaults(func=handle_study)

    study_parser.add_argument("--bubble", dest="sort_modules",
                              action="append_const", const=bubble_sort)
    study_parser.add_argument("--heap", dest="sort_modules",
                              action="append_const", const=heap_sort)
    study_parser.add_argument("--hoare", dest="sort_modules",
                              action="append_const", const=hoare_sort)
    study_parser.add_argument("--insertion", dest="sort_modules",
                              action="append_const", const=insertion_sort)
    study_parser.add_argument("--merge", dest="sort_modules",
                              action="append_const", const=merge_sort)
    study_parser.add_argument("--shell", dest="sort_modules",
                              action="append_const", const=shell_sort)
    study_parser.add_argument("--std", dest="sort_modules",
                              action="append_const", const=std_sort)

    study_parser.add_argument("-b", "--best_case", action="store_true")
    study_parser.add_argument("-w", "--worst_case", action="store_true")
    study_parser.add_argument("-r", "--random_case", action="store_true")

    study_parser.add_argument('file', type=Path)


if __name__ == '__main__':
    main()
