import study_tools
import argparse
from pathlib import Path


def main():
    description = 'Utility to study sort functions efficiency.'
    parser = argparse.ArgumentParser(prog='sort_study',
                                     description=description)
    subparsers = parser.add_subparsers(help='commands', dest='command')

    generate_parser = subparsers.add_parser('generate')
    generate_parser.add_argument('max_length', type=int)
    generate_parser.add_argument('folder', type=Path)

    run_test_parser = subparsers.add_parser('run')
    run_test_parser.add_argument('folder', type=Path)

    args = parser.parse_args()

    if args.command == 'generate':
        study_tools.gen_usual_random_tests(args.folder, args.max_length)
    elif args.command == 'run':
        study_tools.test_all_sorts(args.folder)


if __name__ == '__main__':
    main()
