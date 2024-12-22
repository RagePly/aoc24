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

def gensecret(sec,c):
    for _ in range(c):
        n = sec*64
        sec = sec ^ n
        sec %= 16777216
        n = sec // 32
        sec = sec ^ n
        sec %= 16777216 
        n = sec * 2048
        sec = sec ^ n
        sec %= 16777216 
    return sec

def part1(src):
    s = 0
    for n in src.splitlines():
        s += gensecret(int(n), 2000)
    return s

def gensecrets(sec,c):
    arr = [(sec, sec % 10, None)]
    for _ in range(c):
        n = sec*64
        sec = sec ^ n
        sec %= 16777216
        n = sec // 32
        sec = sec ^ n
        sec %= 16777216 
        n = sec * 2048
        sec = sec ^ n
        sec %= 16777216 
        p = sec % 10
        arr.append((sec, p, p - arr[-1][1]))
    return arr

def part2(src):
    s = 0
    secs = lmap(lambda n: gensecrets(int(n), 2000), src.splitlines())
    chains = defaultdict(int)

    for s in secs:
        v = set()
        for i in range(0, len(s) - 4):
            p1,p2,p3,p4 = s[i:i+4]
            chs = (p1[2],p2[2],p3[2],p4[2])
            if chs not in v:
                chains[chs] += p4[1]
            v.add(chs)

    return max(chains.values())
