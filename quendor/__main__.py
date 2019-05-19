import sys
import logging
import argparse
import textwrap

from quendor.xyzzy import mithican
import quendor.zinterface.fileio as zio

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

    logging_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    parser.add_argument(
        "-v",
        "--verbose",
        dest="log_level",
        default="WARNING",
        choices=logging_levels,
        metavar="",
        help="increase output verbosity; allowed values: "
        + ", ".join(logging_levels)
        + " (default: %(default)s)",
    )

    parser.add_argument(
        "--xyzzy",
        dest="xyzzy",
        default=False,
        action="store_true",
        help="Run Mithican (pre-Quendor)",
    )

    option_set = parser.parse_args(opts)

    options = dict()
    options["story_file"] = option_set.story_file
    options["xyzzy"] = option_set.xyzzy

    logging.basicConfig(
        level=logging.getLevelName(option_set.log_level), format="%(message)s"
    )

    return options


def main():
    print("Quendor Z-Machine Interpreter\n")

    options = process_options(sys.argv[1:])

    story_data = zio.load_story(options["story_file"])
    assert isinstance(story_data, bytes)

    if options["xyzzy"]:
        mithican.execute(story_data)


if __name__ == "__main__":
    main()
