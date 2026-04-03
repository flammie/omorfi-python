# omorfi-python

Omorfi python was originally designed as a python runtime for
[omorfi](https://flammie.github.io/omorfi). It is meant for easier way to use
finite-state automata and related tooling than hand-crafting pipelines with
low-level command-line tools. Many functionalities are related to me
implementing a specific NLP application and writing an academic paper out of it
with (semi-)automated testing and evaluation.

## Dependencies

* pyhfst
* omorfi

## Installation

Pip can be used to install the library and the command-line stuff:

```console
$ pip install omorfi
```

If you are in a system that cannot use pip directly, consider creating a virtual
environment (probably as instructed in the error message).

Pipx can be used to install command-line stuffs and the library:

```console
$ pipx install git+https://github.com/flammie/omorfi-python
```

To get omorfi language models, you can fetch a package of binaries from the
[omorfi releases](https://github.com/flammie/omorfi/releases) or clone the
github repo and build your own:

```console
$ git clone https://github.com/flammie/omorfi
$ cd omorfi
$ ./autogen.sh
$ ./configure
$ make
$ sudo make install
```

The command line above is just a reminder, read through the [README in
omorfi repo](https://github.com/flammie/omorfi/#README) for further
instructions.

## Usage

There are several command-line programs for using omorfi for various NLP tasks.
...
...
