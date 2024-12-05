def part1(src):
    m =  {}
    w, h = 0, 0
    for y, line in enumerate(src.splitlines()):
        for x, c in enumerate(line):
            m[x,y] = c
            w = max(x, w)
        h = max(y, h)

    c = 0
    w += 1
    h += 1

    for x in range(w):
        for y in range(h):
            for xd, yd in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                l1 = "".join(m.get((x + xd*i, y + yd*i), ".") for i in range(4))
                l2 = "".join(m.get((x - xd*i, y - yd*i), ".") for i in range(4))
                if l1 == "XMAS":
                    c += 1
                if l2 == "XMAS":
                    c += 1
    return c
