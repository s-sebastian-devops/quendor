import os
import sys


def locate_story_file(story_file: str) -> str:
    """
    This function makes sure that the passed in story file can be found. The
    current directory where Quendor is executing will be searched as will any
    directories that are stored in a QUENDOR_PATH environment variable.
    """

    paths = [os.curdir]
    paths.extend(os.path.expandvars("$QUENDOR_PATH").split(":"))

    for path in paths:
        found = os.path.isfile(os.path.join(path, story_file))

        if found:
            return os.path.join(path, story_file)

    print(f"\nUnable to find the story file: {story_file}\n")

    sys.exit()
