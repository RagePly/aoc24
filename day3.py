import re
def part1(src):
    s = 0
    for m in re.findall(r"mul\((\d+),(\d+)\)", src):
        s += int(m[0]) * int(m[1])

    return s

def part2(src):
    is_active = True
    s = 0
    for m in re.findall(r"(mul|do|don\'t)\((?:(\d+),(\d+))?\)", src):
        if m[0] == "do":
            is_active = True
        elif m[0] == "don't":
            is_active = False
        elif m[0] == "mul" and m[1] is not None and m[2] is not None and is_active:
            s += int(m[1]) * int(m[2])

    return s
