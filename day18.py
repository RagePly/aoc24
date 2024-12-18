from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    w = 71
    g = [[False for _ in range(w)] for _ in range(w)]
    f = 1024

    for i, l in enumerate(src.splitlines()):
        if i >= f: break
        x,y = ints(l.split(","))

        g[y][x] = True

    s = [(0, 0, 0)]
    v = set()

    # print("\n".join("".join("#" if x else "." for x in ys) for ys in g))
    while s:
        
        d,x,y = heappop(s)

        if (x,y) in v:
            continue
        v.add((x,y))
        
        if (x,y) == (w-1,w-1):
            return d

        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy

            if 0 <= nx < w and 0 <= ny < w and not g[ny][nx]:
                heappush(s, (d+1,nx,ny))

def part2(src):
    w = 71
    g = [[False for _ in range(w)] for _ in range(w)]
    f = 1024

    ls = src.splitlines()
    for i, l in enumerate(ls):
        if i >= f: break
        x,y = ints(l.split(","))

        g[y][x] = True

    for l in ls[f:]:
        x,y = ints(l.split(","))
        g[y][x] = True

        s = [(0, 0, 0)]
        v = set()

        while s:
            
            d,x,y = heappop(s)

            if (x,y) in v:
                continue
            v.add((x,y))
            
            if (x,y) == (w-1,w-1):
                break

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy

                if 0 <= nx < w and 0 <= ny < w and not g[ny][nx]:
                    heappush(s, (d+1,nx,ny))
        else:
            return l

