
from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil
from functools import cache

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    walls = []
    W,H = 0,0
    start,end = None, None
    for y, line in enumerate(src.splitlines()):
        wallr = []
        for x, c in enumerate(line):
            if c == "#": wallr.append(True)
            else: wallr.append(False)

            if c == "S": start = x,y
            elif c == "E": end = x,y

            W = max(x+1,W)
            H = max(y+1,H)
        walls.append(wallr)

    def mh(x,y): return abs(end[0] - x) + abs(end[1] - y)

    cached_map = dict() 
    stack = [(0,end)]
    v = set()

    while stack:
        d, (x,y) = heappop(stack)

        if (x,y) in cached_map:
            continue
        cached_map[(x,y)] = d
        
        if (x,y) == start:
            continue
        
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            
            if not walls[ny][nx]:
                heappush(stack, (d+1,(nx,ny)))

    stack = [(0, start, None)]
    v = set()
    
    cheat_wins = []
    while stack:
        d, (x,y), cheat = heappop(stack)

        if (x,y) == end:
            count = 0
            vc = set()
            for cheat, cheat_d in cheat_wins:
                if cheat in vc: continue
                vc.add(cheat)
                saved = d - cheat_d
                if saved >= 100:
                    count += 1

            return count
        
        if (x,y,cheat) in v:
            continue
        v.add((x,y,cheat))

        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy

            if 0 <= nx < W and 0 <= ny < H:
                if walls[ny][nx]:
                    if cheat is None:
                         ncheat = (nx,ny)
                         heappush(stack, (d+1,(nx,ny),ncheat))
                else: 
                    if cheat is not None:
                        assert (nx,ny) in cached_map
                        cheat_wins.append(((cheat, (nx,ny)), d + 1 + cached_map[(nx,ny)]))
                    else:
                        heappush(stack, (d+1,(nx,ny),cheat))

def part2(src):
    walls = []
    W,H = 0,0
    start,end = None, None
    for y, line in enumerate(src.splitlines()):
        wallr = []
        for x, c in enumerate(line):
            if c == "#": wallr.append(True)
            else: wallr.append(False)

            if c == "S": start = x,y
            elif c == "E": end = x,y

            W = max(x+1,W)
            H = max(y+1,H)
        walls.append(wallr)

    cached_map = dict() 
    stack = [(0,end)]
    v = set()
    full_distance = 0
    def mh(p1,p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    while stack:
        d, (x,y) = heappop(stack)

        if (x,y) in cached_map:
            continue
        cached_map[(x,y)] = d

        if (x,y) == start:
            full_distance = d
            break
        
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            
            if not walls[ny][nx]:
                heappush(stack, (d+1,(nx,ny)))
    
    count = 0
    target_save = 100
    for target, rd in cached_map.items():
        max_save = full_distance - rd - mh(target, start)
        if max_save < target_save:
            continue

        stack = [(0,start)]
        v = set()

        while stack:
            d, (x,y) = heappop(stack)
             
            if (x,y) in v: continue
            else: v.add((x,y))

            cheat_distance = mh((x,y), target)
            if cheat_distance <= 20:
                saving = full_distance - rd - cheat_distance - d
                if saving < target_save: break
                else: count += 1

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                
                if not walls[ny][nx]:
                    heappush(stack, (d+1,(nx,ny)))
    return count 
