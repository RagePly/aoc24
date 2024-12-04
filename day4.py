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
    for y in range(h):
        line = "".join(m[x, y] for x in range(w))
        c += line.count("XMAS")
        c += line.count("SAMX")
    for x in range(w):
        line = "".join(m[x, y] for y in range(h))
        c += line.count("XMAS")
        c += line.count("SAMX")

    for x in range(w):
        for y in range(h):
            if not (x in [0, w-1] or y in [0, h-1]):
                continue
            line = []
            xp, yp = x, y
            while xp < w and yp < h:
                line.append(m[xp,yp])
                xp += 1
                yp += 1
            if not line: continue
            line = "".join(line)
            c += line.count("XMAS")
            c += line.count("SAMX")

            line = []
            xp, yp = x, y
            while 0 <= xp and yp < h:
                line.append(m[xp,yp])
                xp -= 1
                yp += 1
            if not line: continue
            line = "".join(line)
            c += line.count("XMAS")
            c += line.count("SAMX")


    return c
            

def part2(src):
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
            if x in [0, w-1] or y in [0, h-1]:
                continue
            
            l1 = "".join([m[x-1, y-1], m[x,y], m[x+1, y+1]])
            l2 = "".join([m[x-1, y+1], m[x,y], m[x+1, y-1]])

            if l1 in ["MAS", "SAM"] and l2 in ["MAS", "SAM"]:
                c += 1
    return c 

