import re
from pathlib import Path
from pprint import pp

from aoc24.support import get_input


def solution1(left: list[int], right: list[int]) -> int:
    return sum([abs(l - r) for l, r in zip(left, right)])


def solution2(left: list[int], right: list[int]) -> int:
    score = 0
    for lval in left:
        score += lval * sum([1 for rval in right if rval == lval])
    return score


def line2intpair(line: str) -> tuple[int, int]:
    return tuple(map(int, re.findall(r"\d+", line)))


def main() -> tuple[int, int]:
    lines: list[tuple[int, int]] = get_input(
        Path(__file__).parent / "input01.txt", line_parser=line2intpair
    )

    left, right = [], []
    for line in lines:
        left.append(line[0])
        right.append(line[1])

    return solution1(sorted(left), sorted(right)), solution2(
        sorted(left), sorted(right)
    )


if __name__ == "__main__":
    sol1, sol2 = main()
    pp(f"Solution 1: {sol1}")
    pp(f"Solution 2: {sol2}")
