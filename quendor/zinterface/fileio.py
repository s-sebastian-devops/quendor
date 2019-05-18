import os
import sys

from io import BufferedReader
from quendor.utilities.messages import eprint


def load_story(story_file: str) -> bytes:
    """
    Loads a story file that is passed in from the user at the command line.
    """

    story_file = locate_story_file(story_file)
    story_file = load_story_file(story_file)
    story_data = load_story_data(story_file)

    return story_data


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

    eprint(f"\nUnable to find the story file: {story_file}\n")

    sys.exit()


def load_story_file(story_file: str) -> BufferedReader:
    """
    This function will load the passed in story file by opening it as a binary
    file.
    """

    try:
        file = open(story_file, "rb")
    except IOError:
        eprint(f"\nUnable to open the story file: {story_file}\n")

    assert isinstance(file, BufferedReader)

    return file


def load_story_data(story_file: BufferedReader) -> bytes:
    """
    This function will read the data from a binary story file as a series of
    bytes.
    """

    story_file.seek(0)
    story_data = story_file.read()

    return story_data
