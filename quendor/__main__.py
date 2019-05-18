import sys
import argparse
import textwrap

from quendor.zinterface.fileio import (
    locate_story_file,
    load_story_file,
    load_story_data,
)

if sys.version_info < (3, 0):
    sys.stderr.write("Quendor requires Python 3.\n")
    sys.exit(1)


def process_options(opts):
    op_usage = None

    if len(sys.argv) < 3:
        if sys.argv[0].endswith("__main__.py"):
            op_usage = "-m quendor"
        else:
            op_usage = sys.argv[0]

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Options:",
        usage=textwrap.dedent(
            f"""
            The general format is:

                python3 {op_usage}
            """
        ),
        epilog=textwrap.dedent(
            """
            Enjoy your visit to Quendor!
            """
        ),
    )

    parser.add_argument("story_file", help="z-code story file to load")

    option_set = parser.parse_args(opts)

    options = dict()
    options["story_file"] = option_set.story_file

    return options


def main():
    print("Quendor Z-Machine Interpreter\n")

    options = process_options(sys.argv[1:])

    story_file = locate_story_file(options["story_file"])
    story_file = load_story_file(story_file)
    load_story_data(story_file)


if __name__ == "__main__":
    main()
