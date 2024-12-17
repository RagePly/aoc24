
from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby
from re import findall
from heapq import *
from math import log10, ceil

def ints(it): return list(map(int, iter(it)))

def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

def part1(src):
    reg,prog = src.split("\n\n")
    regs = ints(findall(r"(\d+)", reg))
    program = ints(prog.split(": ")[1].split(","))
    
    ip = 0

    def get_combo(val):
        match val:
            case 0 | 1 | 2 | 3:
                return val
            case val if val < 7:
                return regs[val - 4]
            case _:
                raise Exception("invalid combo")

    out = []
    try:
        while True:
            op, val = program[ip:ip+2]
            ip += 2
            
            match op:
                case 0:
                    combo = 2**get_combo(val)
                    regs[0] = regs[0] // combo
                case 1:
                    regs[1] = regs[1] ^ val
                case 2:
                    regs[1] = get_combo(val) % 8
                case 3:
                    if regs[0] != 0:
                        ip = val
                case 4:
                    regs[1] = regs[1] ^ regs[2]
                case 5:
                    out.append(get_combo(val) % 8)         
                case 6:
                    combo = 2**get_combo(val)
                    regs[1] = regs[0] // combo
                case 7:
                    combo = 2**get_combo(val)
                    regs[2] = regs[0] // combo
    except:
        return ",".join(map(str,out))

def part2(src):
    reg,prog = src.split("\n\n")
    regs_og = ints(findall(r"(\d+)", reg))
    program = ints(prog.split(": ")[1].split(","))

    a = [0]
    for p in reversed(program):
        new_a = []
        succ = False
        for aa in a:
            for t in range(8):
                at = (aa << 3) | t
                b = t ^ 1
                c = at >> b
                b = b ^ c
                b = b ^ 6
                if b % 8 == p:
                    new_a.append(at)
                    succ = True
        assert succ
        a = new_a

    return min(a)

