def part1(src):
    s = 0
    for line in src.splitlines():
        nums = list(map(int, line.split()))
            
        d = None
        for n1, n2 in zip(nums[:-1], nums[1:]):
            if n1 < n2 and (d is None or not d):
                d = False
                if n2 - n1 > 3:
                    break
            elif n1 > n2 and (d is None or d):
                d = True
                if n1 - n2 > 3:
                    break
            else:
                break
        else:
            s += 1

    return s 

def check(nums):
    d = None
    for n1, n2 in zip(nums[:-1], nums[1:]):
        if n1 < n2 and (d is None or not d):
            d = False
            if n2 - n1 > 3:
                return False
        elif n1 > n2 and (d is None or d):
            d = True
            if n1 - n2 > 3:
                return False
        else:
            return False
    return True

def part2(src):
    s = 0
    for line in src.splitlines():
        nums = list(map(int, line.split()))
            
        if check(nums):
            s += 1
            continue

        for ir in range(len(nums)):
            numst = [x for i, x in enumerate(nums) if i != ir]
            if check(numst):
                s += 1
                break
    return s 
