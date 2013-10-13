"""
The main console script for the Python solutions to the Codejam problems
"""
import sys
import inspect
import pkgutil
import importlib
import argparse
import codejam
from codejam.codejambase import CodeJamBase


def run_func(args):
    """
    Runs the specified Codejam problem if it exists
    """
    try:
        proj_mod = importlib.import_module('codejam.%s.runner' % args.problem)

        def valid_class(obj):
            """Simple predicate function used to inspect the module"""
            return inspect.isclass(obj) \
                and proj_mod.__name__ == obj.__module__ \
                and issubclass(obj, CodeJamBase)

        class_list = inspect.getmembers(proj_mod, valid_class)
        if len(class_list) != 1:
            print 'The chosen solution %s is invalid:' % args.problem, \
                  'It contains %d CodeJamBase classes' % len(class_list)
            return 2

        print 'Running the \'%s\' Codejam solution:' % args.problem
        if args.output_file != sys.stdout:
            print 'Solution output written to \'%s\'' % args.output_file.name
        # the class we want in the first entry in the list and 2nd in the tuple
        solver = class_list[0][1](args.input_file, args.output_file)
        return solver.solve()
    except ImportError:
        print 'No Codejam problem named \'%s\'' % args.problem
        return 2


def list_func(_):
    """
    Lists all available Codejam solutions
    """

    print 'Listing all available Codejam solutions:'

    for _, modname, _ in pkgutil.iter_modules(codejam.__path__):
        try:
            importlib.import_module('codejam.%s.runner' % modname)
            print modname
        except ImportError:
            pass
        #print "Found submodule %s (is a package: %s)" % (modname, ispkg)


def parse_cmdline():
    """
    Parses the commandline args for the codejam problem
    """
    parser = argparse.ArgumentParser(
        description='Command line runner for Google Codejam solutions'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s ' + codejam.__version__
    )

    subparsers = parser.add_subparsers(title='subcommands')
    parser_run = subparsers.add_parser(
        'run',
        description='Comand for running a specific Codejam solutions',
        help='runs a specific Codejam solution',
    )

    parser_run.add_argument(
        'problem',
        metavar='PROBLEM_NAME',
        help='the name of the Codejam problem to run'
    )

    parser_run.add_argument(
        'input_file',
        metavar='INPUT_FILE',
        type=argparse.FileType('r'),
        help='input file for the Codejam problem'
    )

    parser_run.add_argument(
        'output_file',
        metavar='OUTPUT_FILE',
        nargs='?',
        type=argparse.FileType('w'),
        default=sys.stdout,
        help='optional output file for the Codejam problem'
    )

    parser_run.set_defaults(func=run_func)

    parser_list = subparsers.add_parser(
        'list',
        description='Comand for listing available Codejam solutions',
        help='lists available Codejam solution'
    )

    parser_list.set_defaults(func=list_func)

    return parser.parse_args()


def main():
    """
    Main function: parses the args and calls the proper codejam problem
    """
    try:
        args = parse_cmdline()
        return args.func(args)
        #for line in args.input_file:
        #    args.output_file.write(line)
    except KeyboardInterrupt:
        return 1


if __name__ == '__main__':
    main()
