from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby, permutations
from re import findall
from heapq import *
from math import log10, ceil
from functools import cache

def lmap(f,it): return list(map(f, iter(it)))
def ints(it): return lmap(int, it)
def tmap(tf,it): return list(tuple(f(x) for f in iter(tf)) for x in iter(it))
def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

DELTAXY = [(1,0),(-1,0),(0,1),(0,-1)]

def shortest_keypad(inp):
    kp = [["7","8","9"],
          ["4","5","6"],
          ["1","2","3"],
          [None,"0","A"]]

    def coord(i):
        for y,kl in enumerate(kp):
            for x,c in enumerate(kl):
                if c == i:
                    return (x,y)
        assert False, i

    start = (2,3)
    mv = [[]]
    for i in inp:
        goal = coord(i)
        dx,dy = goal[0]-start[0],goal[1]-start[1]


        mvdx = "<" * -dx if dx < 0 else ">" * dx
        mvdy = "^" * -dy if dy < 0 else "v" * dy

        nmv = []
        for m in mv:
            if kp[start[1]+dy][start[0]] is not None:
                nmv.append(m + [mvdy, mvdx,"A"])
            if kp[start[1]][start[0]+dx] is not None:
                nmv.append(m + [mvdx, mvdy,"A"])
        mv = nmv
        start = goal
    return set("".join(m) for m in mv)

@cache
def shortest_dpad(inp):
    kp = [[None, "^", "A"],
          ["<",  "v", ">"]]

    def coord(i):
        for y,kl in enumerate(kp):
            for x,c in enumerate(kl):
                if c == i:
                    return (x,y)
        assert False, i

    start = (2, 0)
    mv = [[]]
    for i in inp:
        goal = coord(i)
        dx,dy = goal[0]-start[0],goal[1]-start[1]

        mvdx = "<" * -dx if dx < 0 else ">" * dx
        mvdy = "^" * -dy if dy < 0 else "v" * dy

        # alld = set("".join(p) for p in permutations("".join([mvdx, mvdy])))

        nmv = []
        for m in mv:
            # for ddd in alld:
            #     nmv.append(m + [ddd + "A"])
            if kp[start[1]+dy][start[0]] is not None:
                nmv.append(m + [mvdy, mvdx,"A"])
            if kp[start[1]][start[0]+dx] is not None:
                nmv.append(m + [mvdx, mvdy,"A"])
        mv = nmv
        start = goal
    return set("".join(m) for m in mv)

def get_dpad(inp):
    mv = [""]
    assert inp[-1] == "A" and inp[0] != "A"
    for chk in inp[:-1].split("A"):
        nmv = []
        for p in shortest_dpad(chk + "A"):
            for m in mv:
                nmv.append(m + p)
        mv = nmv
    return set(mv)

from functools import reduce

def part1(src):
    s = 0
    for mvs in src.splitlines():
        kpad = shortest_keypad(mvs)
        dpad1 = reduce(lambda x,y: x | y, (get_dpad(k) for k in kpad))
        dpad2 = list(reduce(lambda x,y: x | y, (get_dpad(k) for k in dpad1)))
        dpad2.sort(key=len)
        s += int(mvs[:-1]) * len(dpad2[0])
    return s

@cache
def get_dpad_r(inp, depth):
    if depth == 0:
        return min(map(len, get_dpad(inp)))
    else:
        s = 0
        for chk in inp[:-1].split("A"):
            ms = None
            for path in get_dpad(chk + "A"):
                ss = 0
                for subchk in path[:-1].split("A"):
                    if not subchk:
                        ss += 1
                    else:
                        ss += get_dpad_r(subchk + "A", depth - 1)
                ms = ss if ms is None else min(ss, ms)
            s += ms
        return s

def part2(src):
    s = 0
    for mvs in src.splitlines():
        path = shortest_keypad(mvs)
        ml = None
        for p in path:
            l = get_dpad_r(p, 25 - 1)
            ml = l if ml is None else min(l, ml)
        s += int(mvs[:-1]) * ml

    return s
