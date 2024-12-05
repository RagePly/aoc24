from collections import defaultdict
def part1(src):
    ordering, order = src.split('\n\n')

    rules = defaultdict(set)

    for r in ordering.splitlines():
        f,s = map(int, r.split("|"))
        rules[s].add(f)

    s = 0
    for os in order.splitlines():
        v = set()
        os = list(map(int, os.split(",")))
        osl = set(os)
        for o in os:
            if (j := rules[o] & osl):
                if not (j <= v):
                    break
            v.add(o)
        else:
            s += os[len(os) // 2]

    return s

from functools import cmp_to_key
def part2(src):
    ordering, order = src.split('\n\n')

    rules = defaultdict(set)

    for r in ordering.splitlines():
        f,s = map(int, r.split("|"))
        rules[s].add(f)

    key = cmp_to_key(lambda a, b: -1 if a in rules[b] else 1 if b in rules[a] else 0)

    s = 0
    for os in order.splitlines():
        os = list(map(int, os.split(",")))
        oss = sorted(os, key=key)
        
        if oss != os:
            s+= oss[len(oss) // 2]

    return s


