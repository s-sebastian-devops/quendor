import sys
import argparse
import textwrap

if sys.version_info < (3, 0):
    sys.stderr.write("Quendor requires Python 3.\n")
    sys.exit(1)


def process_options(opts):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Options:",
        usage=textwrap.dedent(
            """
            The general format is:

                python3 -m quendor
            """
        ),
        epilog=textwrap.dedent(
            """
            Enjoy your visit to Quendor!
            """
        ),
    )

    parser.parse_args(opts)


def main():
    print("Quendor Z-Machine Interpreter\n")

    process_options(sys.argv[1:])


if __name__ == "__main__":
    main()
