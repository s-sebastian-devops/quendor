import sys


def eprint(*args, **kwargs):
    print("error: ", *args, file=sys.stderr, **kwargs)
    sys.exit(1)
