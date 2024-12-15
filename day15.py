from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    ws = set()
    bx = set()
    player = None
    world, moves = src.split("\n\n")
    w,h = 0,0
    for y, l in enumerate(world.splitlines()):
        for x,c in enumerate(l):
            if c == "@":
                player = x,y
            if c == "#":
                ws.add((x,y))
            if c == "O":
                bx.add((x,y))

            w = max(w, x+1)
            h = max(h, y+1)
    
    x,y = player
    for m in [m for l in moves.splitlines() for m in l]:
        dx,dy = {">":(1,0),"<":(-1,0),"^":(0,-1),"v":(0,1)}[m]
        nx,ny = x+dx,y+dy
        mv = dict()
        moved = False
        
        while True:
            if (nx,ny) in ws:
                break

            if (nx,ny) in bx:
                mv[nx,ny] = (nx+dx,ny+dy)
                nx += dx
                ny += dy
            else:
                moved = True
                break     
         
        if moved:
            for old in mv.keys():
                bx.remove(old)
            for new in mv.values():
                bx.add(new)

            x += dx
            y += dy

    s = 0
    for x,y in bx:
        s += 100 * y + x
    
    return s

def part2(src):
    ws = set()
    bx = set()
    player = None
    world, moves = src.split("\n\n")
    w,h = 0,0
    for y, l in enumerate(world.splitlines()):
        for x,c in enumerate(l):
            if c == "@":
                player = 2*x,y
            if c == "#":
                ws.add((2*x,y))
            if c == "O":
                bx.add((2*x,y))

            w = max(w, 2*x+1)
            h = max(h, y+1)
    
    x,y = player

    def can_move(x,y,m,is_box):
        mv = []
        if not is_box:
            checks = {">": [(x+1,y)],
                      "<": [(x-2,y)],
                      "v": [(x, y+1), (x-1,y+1)],
                      "^": [(x, y-1), (x-1,y-1)]}[m]
        else:
            checks = {">": [(x+2,y)],
                      "<": [(x-2,y)],
                      "v": [(x, y+1), (x-1,y+1), (x+1,y+1)],
                      "^": [(x, y-1), (x-1,y-1), (x+1,y-1)]}[m]

        for nx,ny in checks:
            if (nx,ny) in ws:
                return None
            if (nx,ny) in bx:
                if (mvs := can_move(nx,ny,m,True)) is not None:
                    mv += mvs
                else:
                    return None
        return mv + [(x,y)] if is_box else mv

    for m in [m for l in moves.splitlines() for m in l]:
        dx,dy = {">":(1,0),"<":(-1,0),"^":(0,-1),"v":(0,1)}[m]
        mv = can_move(x,y,m,False)
        if mv is not None:
            for box in mv:
                if box in bx: bx.remove(box)
            for nx,ny in mv:
                bx.add((nx+dx, ny+dy))
            x += dx
            y += dy
    s = 0
    for x,y in bx:
        s += 100 * y + x
    
    return s
