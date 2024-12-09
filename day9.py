from collections import defaultdict, Counter, deque
from itertools import combinations, product
from re import findall
from heapq import *

def part1(src):
    ns = list(map(int, src.strip()))
    fs = deque()
    em = deque()
    for i in range(len(ns)):
        if i % 2 == 0:
            fs.append((i // 2, ns[i]))
        else:
            em.append(ns[i])

    (fl, cl), (fr, cr) = fs.popleft(), fs.pop()
    e = None
    s = 0
    i = 0
    while True:
        if e is not None and e > 0:
            if cr <= 0:
                fr, cr = fs.pop()
            s += i * fr
            cr -= 1
            e -= 1
            i += 1
        elif e is not None:
            e = None
        else:
            if cl <= 0:
                e = em.popleft()
                if fs:
                    fl, cl = fs.popleft()
                    continue
                else:
                    for _ in range(cr):
                        s += i * fr
                        i += 1
                    break

            else:
                s += i * fl
                cl -= 1
                i += 1

    return s

def part2(src):
    ns = list(map(int, src.strip()))
    fs = []
    for i in range(len(ns)):
        fs.append((i // 2, ns[i], i % 2 == 0, False))

    i = len(fs) - 1
    while i > 0:
        if not fs[i][2] or fs[i][3]:
            i -= 1
            continue
        for ii in range(i):
            if not fs[ii][2] and fs[ii][1] >= fs[i][1]:
                dff = fs[ii][1] - fs[i][1]
                fs[ii] = (fs[i][0], fs[i][1], fs[i][2], True)
                fs[i] = (fs[i][0], fs[i][1], False, True)
                if dff > 0:
                    fs.insert(ii+1, (fs[i][0], dff, False, False))
                    i += 2
                break

        i -= 1 
    s = 0
    i = 0
    for fi, fs, is_file, _ in fs:
        if is_file:
            for ii in range(i, i + fs):
                s += ii * fi
        i += fs

    return s
