from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *

def ints(it): return list(map(int, iter(it)))

def part1(src):
    m = [ints(r) for r in src.splitlines()]
    stack = [(x, y, [(x, y)]) for y in range(len(m)) for x in range(len(m[0])) if m[y][x] == 0]
    ps = [] 
    while stack:
        x, y, p = stack.pop()
        h = m[y][x]

        if h == 9:
            ps.append(p)

        for (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(m) and 0 <= nx < len(m[0]) and (nx, ny) not in p and m[ny][nx] == h + 1:
                stack.append((nx, ny, p + [(nx, ny)]))

    scs = defaultdict(set)
    for p in ps:
        s,e  = p[0], p[-1]
        scs[s].add((s,e))
          
    return sum(map(len, scs.values()))

def part2(src):
    m = [ints(r) for r in src.splitlines()]
    stack = [(x, y, [(x, y)]) for y in range(len(m)) for x in range(len(m[0])) if m[y][x] == 0]
    ps = [] 
    while stack:
        x, y, p = stack.pop()
        h = m[y][x]

        if h == 9:
            ps.append(p)

        for (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(m) and 0 <= nx < len(m[0]) and (nx, ny) not in p and m[ny][nx] == h + 1:
                stack.append((nx, ny, p + [(nx, ny)]))

    scs = defaultdict(int)
    for p in ps:
        e2e  = p[0], p[-1]
        scs[e2e] += 1
          
    return sum(scs.values())
