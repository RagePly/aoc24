def part1(src):
    g = set()
    p = None
    w, h = 0, 0
    for y, r in enumerate(src.splitlines()):
        for x, c in enumerate(r):
            if c == "#":
                g.add((x,y))
            elif c == "^":
                p = x,y
            w = max(x, w)
            h = max(y, h)
    
    w += 1
    h += 1
    nd = {(1,0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
    dx, dy = 0, -1
    x, y = p
    s = set()
    while 0 <= x < w and 0 <= y < h:
        s.add((x, y))
        if (x + dx, y + dy) in g:
            dx, dy = nd[(dx, dy)]

        x += dx
        y += dy
    return len(s)

            

def part2(src):
    g = set()
    p = None
    w, h = 0, 0
    for y, r in enumerate(src.splitlines()):
        for x, c in enumerate(r):
            if c == "#":
                g.add((x,y))
            elif c == "^":
                p = x,y
            w = max(x, w)
            h = max(y, h)
    
    w += 1
    h += 1
    nd = {(1,0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
    dx, dy = 0, -1
    x, y = p
    c = set()
    from collections import defaultdict
    vv = set()
    
    while 0 <= x < w and 0 <= y < h:
        if (x + dx, y + dy) in g:
            dx, dy = nd[dx, dy]
        else:
            vv.add((x,y))
            x += dx
            y += dy

        if (x+dx, y+dy) not in vv and 0 <= (x + dx) < w and 0 <= (y + dy) < h:
            v = defaultdict(set)
            v[x,y].add((dx, dy))
            xt, yt = nd[dx, dy]
            xp, yp = x, y

            while 0 <= xp < w and 0 <= yp < h:
                v[xp, yp].add((xt, yt))
                if (xp + xt, yp + yt) in g or (xp + xt, yp + yt) == (x+dx, y+dy):
                    xt, yt = nd[xt, yt]
                else:
                    xp += xt
                    yp += yt

                if (xt, yt) in v[xp, yp]:
                    c.add((x + dx, y + dy))
                    break



    return len(c)
