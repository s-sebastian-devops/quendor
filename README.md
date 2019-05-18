# Quendor

The goal of Quendor is to be an emulator.

The goal behind any emulator is to be able to execute the binary files from some original machine directly. These files are always assembly level instructions. In this case, the machine is the [Z-Machine](https://en.wikipedia.org/wiki/Z-machine) and the files are called story files. These story files are made up of assembly instructions for text adventure games.

A Z-Machine interpreter implementation uses the story file as input to get a serialization of the story state that is encoded as an array of bytes. That series of bytes has to then be decoded. That decoding is a large part of what a tool like Quendor has to do.

## Project Details

Quendor is purely an exercise in coding and learning how to write emulators. What that means is Quendor is unlikely to ever become a reference implementation interpreter. Currently the only true reference implementation that I know of is [Frotz](https://davidgriffith.gitlab.io/frotz/) and that's written in C that is, for me, hard to digest. There are plenty of other interpreters out there that already do a very good job. Notables are [Gargoyle](http://ccxvii.net/gargoyle/), [Lectrote](https://github.com/erkyrath/lectrote), [Bocfel](https://cspiegel.github.io/bocfel/), [Spatterlight] (https://github.com/angstsmurf/spatterlight), and [Fizmo](https://fizmo.spellbreaker.org/).

Quendor will attempt to replace none of them.

Quendor will be written entirely in Python. (And only for Python 3.) This will no doubt have some impacts on the performance of the interpreter. That said, the choice of Python should not compromise my ability to provide an accurate implementation; perhaps merely a performant one.
