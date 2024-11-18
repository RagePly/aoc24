def part1(src):
    return sum(map(int, src.splitlines()))

from functools import reduce
from operator import mul

def part2(src):
    return reduce(mul, map(int, src.splitlines()))
