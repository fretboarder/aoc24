import re
from pathlib import Path
from pprint import pp
from xmlrpc.client import Boolean

from aoc24.support import get_input


def is_monotonic(nums: list[int]) -> Boolean:
    increasing = decreasing = True
    min_diff = 1
    max_diff = 3

    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i - 1])
        if diff < min_diff or diff > max_diff:
            return False
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing


def can_become_monotonic(nums: list[int]) -> Boolean:
    for i in range(len(nums)):
        temp_list = nums[:i] + nums[i + 1 :]
        if is_monotonic(temp_list):
            return True
    return False


def solution1(lines: list[list[int]]) -> int:
    return sum([1 for line in lines if is_monotonic(line)])


def solution2(lines: list[list[int]]) -> int:
    unsafe = [line for line in lines if not is_monotonic(line)]
    safe = sum([1 for line in unsafe if can_become_monotonic(line)])
    return len(lines) - len(unsafe) + safe


def line2ints(line: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", line)))


def main() -> tuple[int, int]:
    lines: list[list[int]] = get_input(
        Path(__file__).parent / "input01.txt", line_parser=line2ints
    )

    return solution1(lines), solution2(lines)


if __name__ == "__main__":
    sol1, sol2 = main()
    pp(f"Solution 1: {sol1}")
    pp(f"Solution 2: {sol2}")
