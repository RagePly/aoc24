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
    g = defaultdict(list)

    for l in src.splitlines():
        n1,n2 = l.split("-")
        g[n1].append(n2)
        g[n2].append(n1)

    conns = defaultdict(set)
    nodes = list(g.keys())

    for n in nodes:
        stack = list(g[n])

        while stack:
            nn = stack.pop()

            if nn == n or nn in conns[n]:
                continue

            conns[n].add(nn)
            conns[nn].add(n)

            stack += list(g[nn])

    tripples = set()
    for n1,ns in g.items():
        for n2,n3 in combinations(list(ns), 2):
            if n2 in g[n3]:
                tripples.add(tuple(sorted([n1,n2,n3])))
    s = 0
    for t in tripples:
        if any(tt.startswith("t") for tt in t):
            s += 1

    return s


def part2(src):
    g = defaultdict(list)

    for l in src.splitlines():
        n1,n2 = l.split("-")
        g[n1].append(n2)
        g[n2].append(n1)

    best = None
    for n,ns in g.items():
        og = set(ns) | set((n,))
        trials = [og]

        for nn in ns:
            c = set(g[nn]) | set((nn,))
            ntrials = []
            for t in trials:
                if (nc := c & t) and nc:
                    ntrials.append(nc)
                ntrials.append(t - set((nn,)))
            trials = ntrials
        for t in trials:
            if best is None or len(t) > len(best):
                best = t

    return ",".join(sorted(best))

