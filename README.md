# req-update

[![PyPI](https://img.shields.io/pypi/v/req-update)](https://pypi.org/project/req-update/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/req-update)
![PyPI - License](https://img.shields.io/pypi/l/req-update)

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/req-update/status.svg)](https://drone.albertyw.com/albertyw/req-update)
[![Dependency Status](https://pyup.io/repos/github/albertyw/req-update/shield.svg)](https://pyup.io/repos/github/albertyw/req-update/)
[![Code Climate](https://codeclimate.com/github/albertyw/req-update/badges/gpa.svg)](https://codeclimate.com/github/albertyw/req-update)
[![Test Coverage](https://codeclimate.com/github/albertyw/req-update/badges/coverage.svg)](https://codeclimate.com/github/albertyw/req-update/coverage)

`req-update` is a CLI tool to automatically update python, go, node, and git submodule dependencies.

## Usage

`req-update` requires no command line arguments.  Running `req-update` will
create a branch `dep-update`, check for outdated packages, and commit a
series of commits to update packages.

```
$ req_update
usage: req_update.py [-h] [-p] [-i] [-d] [-v] [--version]

Update python, go, node, and git submodule dependencies for your project with git integration

https://github.com/albertyw/req-update

optional arguments:
  -h, --help     show this help message and exit
  -p, --push     Push commits individually to remote origin
  -d, --dryrun   Dry run
  -v, --verbose  Verbose output
  --version      show program's version number and exit
```

## Features

 - Update python dependencies in `requirements*.txt` pip.
 - Update go dependencies in `go.mod` and `go.sum` with go modules.
 - Update node dependencies in `package-lock.json` with npm.
 - Update git submodules in `.gitmodules` with git.
 - Integrates with git, creating a branch with one commit per updated dependency
 - No third party dependencies beyond python 3 standard library
 - Automatic detection of python, go, node, and git dependencies; no CLI arguments required

## Comparisons

 - `req-upgrader` - `req-update` integrates with git
