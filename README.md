# Quendor

The goal of Quendor is to be an emulator.

The goal behind any emulator is to be able to execute the binary files from some original machine directly. These files are always assembly level instructions. In this case, the machine is the [Z-Machine](https://en.wikipedia.org/wiki/Z-machine) and the files are called story files. These story files are made up of assembly instructions for text adventure games.

A Z-Machine interpreter implementation uses the story file as input to get a serialization of the story state that is encoded as an array of bytes. That series of bytes has to then be decoded. That decoding is a large part of what a tool like Quendor has to do.

## Project Details

Quendor is purely an exercise in coding and learning how to write emulators. What that means is Quendor is unlikely to ever become a reference implementation interpreter. Currently the only true reference implementation that I know of is [Frotz](https://davidgriffith.gitlab.io/frotz/) and that's written in C that is, for me, hard to digest. There are plenty of other interpreters out there that already do a very good job. Notables are [Gargoyle](http://ccxvii.net/gargoyle/), [Lectrote](https://github.com/erkyrath/lectrote), [Bocfel](https://cspiegel.github.io/bocfel/), [Spatterlight] (https://github.com/angstsmurf/spatterlight), and [Fizmo](https://fizmo.spellbreaker.org/).

Quendor will attempt to replace none of them.

Quendor will be written entirely in Python. (And only for Python 3.) This will no doubt have some impacts on the performance of the interpreter. That said, the choice of Python should not compromise my ability to provide an accurate implementation; perhaps merely a performant one.

## Running Quendor

Quendor is designed to run as a module. That means if you have the code distribution, you should be able to do this:

```
python3 -m quendor
```

To test that all is well, from a Python REPL, try the following:

```
import quendor
print(quendor.__version__)
```

In order to use Quendor you have to provide it with a story file. The repository itself comes with an example file that I'm using to build up the interpreter. So to run it you could, for example, do this:

```
python3 -m quendor examples/minizork.z3
```

You can also set a `QUENDOR_PATH` environment variable and keep your story files there. If the variable is provided, Quendor will search the path referenced by it.

I'm learning a lot as I go in terms of how to build this emulator. As such, I suspect my learning implementation and my actual implementation will differ a bit. To help with this, Quendor provides a switch to allow me -- and thus you -- to execute this minimal Quendor. "Minimal" here means an implementation constructed solely for the purposes of making sure the absolute basics work. To run this, just use the `--xyzzy` flag:

```
python3 -m quendor examples/minizork.z3 --xyzzy
```

This will run a version of Quendor I call Mithican. This name actually comes from the [Chronology of Quendor](http://quendor.robinlionheart.com/chronology) which states the following: "The Mithicans, one of the last of the pre-Quendorian tribes, disappear in what most anthropologists term 'a goof-up of the first order'."

Mithican is basically there to showcase how to build up the operations of a Z-Machine emulator without all of the surrounding elements that I suspect will become necessary but also confusing.
