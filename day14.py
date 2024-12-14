
from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil
import time

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    h, w =  103, 101 
    m = defaultdict(set)
    
    for i, line in enumerate(src.splitlines()):
        x,y,dx,dy = map(int, findall(r"p=([\-\d]+),([\-\d]+) v=([\-\d]+),([\-\d]+)", line)[0])

        m[x,y].add((i, dx, dy))

    
    for _ in range(100):
        nm = defaultdict(set)
        for (x,y),rs in m.items():
            for i, dx, dy in rs:
                nx = (x + dx) % w
                ny = (y + dy) % h

                nm[nx,ny].add((i, dx, dy))
        m = nm

    p = 1
    for qx,qy in [(0, 0), (w//2+1,0), (0, h//2+1), (w//2+1, h//2+1)]:
        s = 0
        for x in range(qx, qx + w//2):
            for y in range(qy, qy + h//2):
                s += len(m.get((x,y), set()))

        assert s > 0
        p *= s
    
    return p
                
def part2(src):
    return "uncomment this line and stop the code when the tree apppears"
    h, w =  103, 101 
    m = defaultdict(set)
    
    for i, line in enumerate(src.splitlines()):
        x,y,dx,dy = map(int, findall(r"p=([\-\d]+),([\-\d]+) v=([\-\d]+),([\-\d]+)", line)[0])

        m[x,y].add((i, dx, dy))

    
    c = 0
    while True:
        nm = defaultdict(set)
        for (x,y),rs in m.items():
            for i, dx, dy in rs:
                nx = (x + dx) % w
                ny = (y + dy) % h

                nm[nx,ny].add((i, dx, dy))
        m = nm

        s = list(f"\x1b[2J{c + 1}\n")
        for y in range(h):
            for x in range(w):
                s.append("#" if (x,y) in nm else " ")
            s.append("\n")

        if (c - 62) % 103 == 0:
            print("".join(s))
            try: time.sleep(0.5)
            except KeyboardInterrupt: return c + 1
        c += 1
