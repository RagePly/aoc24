from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

"""
    g = n * X + m * Y

    gx = n * xx + m * yx => n = (gx - m * yx) // xx

    gy = xy * (gx - m * yx) // xx + m * yy

    gy = xy * gx // xx  - xy * m * yx // xx + m * yy

    gy = xy * gx // xx + m * (yy - xy * yx // xx) <-- NOTE: This is where I messed

    m = (gy - xy * gx / xx) / (yy - xy * yx / xx)

"""

def part1(src):
    m = lambda X, Y, G: (X[1] * G[0] / X[0] - G[1]) / (X[1] * Y[0] / X[0] + Y[1])
    n = lambda X, Y, G: (G[0] - m(X, Y, G) * Y[0]) / X[0]
    s = 0

    for parts in src.split("\n\n"):
        a,b,g = parts.splitlines()
        
        ax, ay = tuple(map(int, findall(r"Button A: X\+(\d+), Y\+(\d+)", a)[0]))
        bx, by = tuple(map(int, findall(r"Button B: X\+(\d+), Y\+(\d+)", b)[0]))
        gx, gy = tuple(map(int, findall(r"Prize: X=(\d+), Y=(\d+)", g)[0]))
        
        q = [(0, 0, 0)] 
        v = set()
        while q:
            c, x, y = heappop(q)

            if (c, x, y) in v:
                continue

            v.add((c, x, y))
            
            if x == gx and y == gy:
                s += c

            for nc, nx, ny in [(3, x + ax, y + ay), (1, x + bx, y + by)]:
                if nx <= gx and ny <= gy:
                    heappush(q, (c + nc, nx, ny))
         
    return s



def solve(A, B, G):
    xx, xy = A
    yx, yy = B
    gx, gy = G

    m = (gy - xy * gx / xx) / (yy - xy * yx / xx)
    n = (gx - m * yx) / xx    
    
    n = round(n)
    m = round(m)

    gx_t = xx * n + yx * m
    gy_t = xy * n + yy * m

    if gx_t == gx and gy_t == gy:
        return 3 * n + 1 * m

def part2(src):
    m = lambda X, Y, G: (X[1] * G[0] / X[0] - G[1]) / (X[1] * Y[0] / X[0] + Y[1])
    n = lambda X, Y, G: (G[0] - m(X, Y, G) * Y[0]) / X[0]
    s = 0

    for parts in src.split("\n\n"):
        a,b,g = parts.splitlines()
        
        A = tuple(map(int, findall(r"Button A: X\+(\d+), Y\+(\d+)", a)[0]))
        B = tuple(map(int, findall(r"Button B: X\+(\d+), Y\+(\d+)", b)[0]))
        G = tuple(map(int, findall(r"Prize: X=(\d+), Y=(\d+)", g)[0]))
        G = (G[0] + 10000000000000, G[1] + 10000000000000)

        if (sol := solve(A, B, G)) is not None:
            s += sol

    return s

