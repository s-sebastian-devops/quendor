import sys
import argparse
import textwrap

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

    parser.parse_args(opts)


def main():
    print("Quendor Z-Machine Interpreter\n")

    process_options(sys.argv[1:])


if __name__ == "__main__":
    main()
