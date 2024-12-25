from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby, permutations
from re import findall
from heapq import *
from math import log10, ceil
from functools import cache, reduce

def lmap(f,it): return list(map(f, iter(it)))
def ints(it): return lmap(int, it)
def tmap(tf,it): return list(tuple(f(x) for f in iter(tf)) for x in iter(it))
def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

DELTAXY = [(1,0),(-1,0),(0,1),(0,-1)]

def part1(src):
    blocks = src.split("\n\n")
    keys = []
    locks = []
    for b in blocks:
        ls = b.splitlines()
        rows = [-1 for _ in range(len(ls[0]))]
        
        for l in ls:
            for i,x in enumerate(l):
                if x == "#":
                    rows[i] += 1

        if all(x == "#" for x in ls[0]):
            locks.append(rows)
        else:
            keys.append(rows)

        h = len(ls) - 2
    s = 0
    for k,l in product(keys, locks):
        if all(kh + lh <= h for kh,lh in zip(k,l)):
            s += 1

    return s

def part2(src):
    pass

