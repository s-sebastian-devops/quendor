import sys

if sys.version_info < (3, 0):
    sys.stderr.write("Quendor requires Python 3.\n")
    sys.exit(1)


def main():
    print("Welcome to Quendor!")


if __name__ == "__main__":
    main()
