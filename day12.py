from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    m = [[c for c in r] for r in src.splitlines()]

    v = set()
    i = 0
    ss = 0
    for x, y in [(x,y) for y in range(len(m)) for x in range(len(m[y]))]:
        if (x,y) in v: continue 
        cc = m[y][x]
        s = [(x, y)]
        ii = i
        i += 1
        a = 0
        p = 0

        while s:
            x, y = s.pop()
            c = m[y][x]
            if (x,y) in v: continue
            if c != cc: continue

            ps = 0
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                    cn = m[ny][nx]

                    if cn != cc:
                        ps += 1
                    else:
                        s.append((nx, ny))
                else:
                    ps += 1

            v.add((x,y))
            a += 1
            p += ps

        ss += a * p
    return ss

def part2(src):
    m = [[c for c in r] for r in src.splitlines()]

    v = set()
    i = 0
    ss = 0
    for x, y in [(x,y) for y in range(len(m)) for x in range(len(m[y]))]:
        if (x,y) in v: continue 
        cc = m[y][x]
        s = [(x, y)]
        ii = i
        i += 1
        a = 0
        vp = defaultdict(list)
        hp = defaultdict(list)
        while s:
            x, y = s.pop()
            c = m[y][x]
            if (x,y) in v: continue
            if c != cc: continue

            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                    cn = m[ny][nx]

                    if cn != cc:
                        if abs(dx) == 1:
                            vp[(dx, nx)].append(ny)
                        if abs(dy) == 1:
                            hp[(dy, ny)].append(nx)
                    else:
                        s.append((nx, ny))
                else:
                    if abs(dx) == 1:
                        vp[(dx, nx)].append(ny)
                    if abs(dy) == 1:
                        hp[(dy, ny)].append(nx)


            v.add((x,y))
            a += 1

        p = 0
        for (_, x), yn in vp.items():
            py = None
            for y in sorted(yn):
                if py is None or y != py + 1:
                    p += 1
                py = y
        for (_, y), xn in vp.items():
            px = None
            for x in sorted(xn):
                if px is None or x != px + 1:
                    p += 1
                px = x

        ss += a * p
    return ss

