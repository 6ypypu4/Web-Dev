def make_bricks(small, big, goal):
    max_big = min(big, goal // 5)
    remaining = goal - max_big * 5
    return small >= remaining

def lone_sum(a, b, c):
    if(a == b):
        if(b == c):
            return 0
        return c
    if(a == c):
        return b
    if(b == c):
        return a
    return a+b+c

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

def no_teen_sum(a, b, c):
    def fix_teen(n):
        if 13 <= n <= 19 and n not in (15, 16):
            return 0
        return n
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def round_sum(a, b, c):
    def round10(num):
        remainder = num % 10
        if remainder >= 5:
           return num + (10 - remainder)
        return num - remainder
    return round10(a) + round10(b) + round10(c)

def close_far(a, b, c):
    if abs(b - a) <= 1:
        return abs(c - a) >= 2 and abs(c - b) >= 2
    if abs(c - a) <= 1:
        return abs(b - a) >= 2 and abs(b - c) >= 2
    return False

def make_chocolate(small, big, goal):
    max_big = min(big, goal // 5)
    remaining = goal - max_big * 5
    if remaining <= small:
        return remaining
    return -1


