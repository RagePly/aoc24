from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    w,h = 0,0
    wall = []
    start,end = None,None
    for y,l in enumerate(src.splitlines()):
        r = []
        for x,c in enumerate(l):
            r.append(c == "#")
            if c == "E":
                end = x,y
            if c == "S":
                start = x,y
        wall.append(r)
    v = set() 
    stack = [(0, *start, 0)]
    while stack:
        s, x, y, d = heappop(stack)

        if (x,y) in v: continue
        else: v.add((x,y))

        if (x,y) == end:
            return s

        for i in range(4):
            dx,dy = [(1,0), (0,1), (-1,0), (0,-1)][i]
            if i == d and not wall[y+dy][x+dx]:
                heappush(stack, (s + 1, x+dx, y+dy, i))
            elif not wall[y+dy][x+dx]:
                heappush(stack, (s + 1001, x+dx, y+dy, i))

def part2(src):
    w,h = 0,0
    wall = []
    start,end = None,None
    for y,l in enumerate(src.splitlines()):
        r = []
        for x,c in enumerate(l):
            r.append(c == "#")
            if c == "E":
                end = x,y
            if c == "S":
                start = x,y
        wall.append(r)

    vp = set()
    ms = None
    stack_start = [((0, *start, 0, [start]), set())]
    vs = set([start])
    while stack_start:
        start,v = stack_start.pop()
        stack = [start]
        while stack:
            s, x, y, d, p = heappop(stack)

            if ms is not None and s > ms: break

            if (x,y) in v: continue
            else: v.add((x,y))

            if (x,y) == end:
                ms = s
                vp |= set(p)
                break
                
            for i in range(4):
                dx,dy = [(1,0), (0,1), (-1,0), (0,-1)][i]
                if i == d and not wall[y+dy][x+dx]:
                    heappush(stack, (s + 1, x+dx, y+dy, i, p + [(x+dx,y+dy)]))
                elif not wall[y+dy][x+dx]:
                    if not (x,y) in vs:
                        stack_start.append(((s, x, y, d, list(p)), set(p) - set([(x,y)])))
                        vs.add((x,y))
                    heappush(stack, (s + 1001, x+dx, y+dy, i, p + [(x+dx,y+dy)]))
    return len(vp)
