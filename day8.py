from collections import defaultdict
def part1(src):
    g = defaultdict(list)
    w, h = 0, 0
    for y, r in enumerate(src.splitlines()):
        for x, c in enumerate(r):
            w = max(x + 1, w)
            h = max(y + 1, h)
            if c != ".":
                g[c].append((x, y)) 

    inmap = lambda x, y: 0 <= x < w and 0 <= y < h
    locs = set() 
    for k in g.keys():
        for i, p1 in enumerate(g[k][:-1]):
            for p2 in g[k][i+1:]:
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]

                p3 = p1[0] - dx, p1[1] - dy
                p4 = p2[0] + dx, p2[1] + dy

                if inmap(*p3):
                    locs.add(p3)
                if inmap(*p4):
                    locs.add(p4)
    return len(locs)

def part2(src):
    g = defaultdict(list)
    w, h = 0, 0
    for y, r in enumerate(src.splitlines()):
        for x, c in enumerate(r):
            w = max(x + 1, w)
            h = max(y + 1, h)
            if c != ".":
                g[c].append((x, y)) 

    inmap = lambda x, y: 0 <= x < w and 0 <= y < h
    locs = set() 
    for k in g.keys():
        for i, p1 in enumerate(g[k][:-1]):
            for p2 in g[k][i+1:]:
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]

                j = 1
                f = True

                locs.add(p1)
                locs.add(p2)
                while f:
                    f = False
                    p3 = p1[0] - j*dx, p1[1] - j*dy
                    p4 = p2[0] + j*dx, p2[1] + j*dy

                    if inmap(*p3):
                        locs.add(p3)
                        f = True

                    if inmap(*p4):
                        locs.add(p4)
                        f = True

                    j += 1
    return len(locs)

