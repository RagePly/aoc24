from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def part1(src):
    stones = {i: 1 for i in ints(src.split())}

    for _ in range(25):
        new_stones = defaultdict(int)

        for k, v in stones.items():
            if k == 0:
                new_stones[1] += v
            elif (e := ceil(log10(k + 0.5))) != 0 and e % 2 == 0:
                new_stones[k % 10**(e // 2)] += v
                new_stones[k // 10**(e // 2)] += v
            else:
                new_stones[2024 * k] += v

        stones = new_stones
    return sum(v for v in stones.values())

def part2(src):
    stones = {i: 1 for i in ints(src.split())}

    for _ in range(75):
        new_stones = defaultdict(int)

        for k, v in stones.items():
            if k == 0:
                new_stones[1] += v
            elif (e := ceil(log10(k + 0.5))) != 0 and e % 2 == 0:
                new_stones[k % 10**(e // 2)] += v
                new_stones[k // 10**(e // 2)] += v
            else:
                new_stones[2024 * k] += v

        stones = new_stones
    return sum(v for v in stones.values())
