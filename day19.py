from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    designs,trials = src.split("\n\n")
    des = designs.split(", ")
    s = 0 
    for trial in trials.splitlines():
        avail = [trial]
        v = set()
        while avail:
            a = avail.pop()
            found = False
            for d in des:
                if a.startswith(d):
                    na = a[len(d):]
                    if len(na) == 0:
                        found = True
                        break
                    if not na in v:
                        v.add(na)
                        avail.append(na)
            if found:
                s += 1
                break
    return s 

from functools import cache

def part2(src):
    designs,trials = src.split("\n\n")
    des = designs.split(", ")
    @cache
    def count_designs(a):
        nonlocal des
        
        s = 0
        for d in des:
            if a.startswith(d):
                na = a[len(d):]
                if len(na) == 0:
                    s += 1
                else:
                    s += count_designs(na)
        return s

    s = 0 
    for trial in trials.splitlines():
        s += count_designs(trial) 
    return s 

