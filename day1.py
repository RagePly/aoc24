def part1(src):
    s = 0
    ns = [list(map(int, l.split())) for l in src.splitlines()]
    l1 = [n1 for n1,n2 in ns] 
    l2 = [n2 for n1,n2 in ns] 

    l1.sort()
    l2.sort()

    for x1, x2 in zip(l1, l2):
        s += abs(x1 - x2)

    return s

def part2(src):
    s = 0
    ns = [list(map(int, l.split())) for l in src.splitlines()]
    l1 = [n1 for n1,n2 in ns] 
    l2 = [n2 for n1,n2 in ns] 

    l2.sort()

    for x1 in l1:
        c = 0
        for x2 in l2:
            if x1 == x2:
                c += 1
        s += c * x1

    return s
