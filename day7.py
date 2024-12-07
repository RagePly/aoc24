from heapq import *
def part1(src):
    s = 0
    for line in src.splitlines():
        m, ns = line.split(": ")
        m = int(m)
        ns = list(map(int, ns.split(" ")))
        fn = ns[0]
        stack = [(m, len(ns) - 1)]

        while stack:
            mc, i = heappop(stack)
            n = ns[i]
            if i == 0:
                if n == mc:
                    s += m
                    break
                continue
            if (mcn := mc - n) >= fn:
                heappush(stack, (mcn, i - 1))
            if mc % n == 0:
                heappush(stack, (mc // n, i - 1))
    return s

def part2(src):
    s = 0
    for line in src.splitlines():
        m, ns = line.split(": ")
        m = int(m)
        ns = list(map(int, ns.split(" ")))
        fn = ns[0]
        stack = [(m, len(ns) - 1)]

        while stack:
            mc, i = heappop(stack)
            n = ns[i]
            if i == 0:
                if n == mc:
                    s += m
                    break
                continue
            mcs = str(mc)
            nstr = str(n)
            if mcs != nstr and mcs.endswith(nstr):
                heappush(stack, (int(mcs[:len(mcs) - len(nstr)]), i - 1))
            if (mcn := mc - n) >= fn:
                heappush(stack, (mcn, i - 1))
            if mc % n == 0 and (mcn := mc // n) >= fn:
                heappush(stack, (mc // n, i - 1))
    return s
