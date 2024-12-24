
from collections import defaultdict, Counter, deque
from itertools import combinations, product, groupby, permutations
from re import findall
from heapq import *
from math import log10, ceil
from functools import cache, reduce

def lmap(f,it): return list(map(f, iter(it)))
def ints(it): return lmap(int, it)
def tmap(tf,it): return list(tuple(f(x) for f in iter(tf)) for x in iter(it))
def digits(n): return len(str(n)) # about 5% faster than doing a log10 approach for digits < 1e6

DELTAXY = [(1,0),(-1,0),(0,1),(0,-1)]

def part1(src):
    sval, cons = src.split("\n\n")
    gv = {g0: int(v) for g0,v in map(lambda s: s.split(": "), sval.splitlines()) }
    g = {}
    gs = set(gv.keys())
    for l in cons.splitlines():
        g1, op, g2, _, gout = l.split()
        gs |= {g1, g2, gout}
        g[gout] = (g1, op, g2) 
    
    @cache
    def rfind(s):
        if s not in g:
            return gv[s]
        x,o,y = g[s]

        match o:
            case "XOR": return rfind(x) ^ rfind(y)
            case "OR": return rfind(x) | rfind(y)
            case "AND": return rfind(x) & rfind(y)
            case _: assert False

    r = []
    for gz in gs:
        if gz.startswith("z"):
            r.append((gz[1:], rfind(gz)))

    r.sort(key=lambda p: p[0], reverse=True)
    print(r)
    return eval("0b" + "".join(str(p[1]) for p in r))

def part2(src):
    # import graphviz as gv
    sval, cons = src.split("\n\n")
    g = {}
    gs = set()

    #f = gv.Graph(engine="dot")
    for l in cons.splitlines():
        g1, op, g2, _, gout = l.split()
        # f.node(gout, label=f"{gout}({op})")
        # f.edge(g1, gout)
        # f.edge(g2, gout)

        gs |= {g1, g2, gout}
        g[gout] = (g1, op, g2) 
    # f.view()

    # The graph should be VERY regular, output all discrepencies. The graph has the
    # following structure:
    # z00 = x00 ^ y00, z45 = out_45, otherwise
    #   zi = out_i ^ (xi ^ yi)
    #              ^
    #       allways an XOR
    #          
    # where out_1 = x00 & y00 and
    #   out_(i+1) = (out_i & (xi ^ yi)) | (xi & yi)
    #                                   ^
    #                     only time an OR *should* be used

    for gor, v in g.items():
        if gor.startswith("z") and gor != "z45" and v[1] != "XOR": print(gor, v)
        match v:
            case (gl, "OR", gr):
                match g[gl], g[gr]:
                    case ((gll, "AND", glr), (grl, "AND", grr)): pass
                    case _: print(gor, v)
    
    # Use these values to find the parts to swap :)
    nodes = sorted("xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx".split(","))
    return ",".join(nodes)

