# Advent Of Code 2024


[![pytest](https://github.com/fretboarder/aoc24/actions/workflows/unittest.yml/badge.svg)](https://github.com/fretboarder/aoc24/actions/workflows/unittest.yml)
[![ruff](https://github.com/fretboarder/aoc24/actions/workflows/ruff.yml/badge.svg)](https://github.com/fretboarder/aoc24/actions/workflows/ruff.yml)
[![mypy](https://github.com/fretboarder/aoc24/actions/workflows/mypy.yml/badge.svg)](https://github.com/fretboarder/aoc24/actions/workflows/mypy.yml)
[![Release Creation](https://github.com/fretboarder/aoc24/actions/workflows/releaseplease.yml/badge.svg)](https://github.com/fretboarder/aoc24/actions/workflows/releaseplease.yml)

---

## Preparations

```
$ git clone ...
$ cd aoc24
$ poetry install
```

## Running the CLI

```
$ aoc
Usage: aoc [OPTIONS] COMMAND [ARGS]...

  CLI arguments and options.

Options:
  --help  Show this message and exit.

Commands:
  day        Execute and print solutions for a day.
  solutions  Execute and print solutions for all days available.
  version    Print application version.
```

## Examples

```
$ aoc day 1
Solution 1: ...
Solution 2: ...
```

```
$ aoc solutions
========== DAY 01 ==========
  Solution 1: ...
  Solution 2: ...
========== DAY 02 ==========
  ...
```

## Legal Notice

For copyright reasons, input data stored in this repo is encrypted by a random
private encryption key only known by the author of this repository.