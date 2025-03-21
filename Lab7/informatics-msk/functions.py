#A
def find_min_of_four(a, b, c, d):
    min_num = a
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c
    if d < min_num:
        min_num = d
    print(min_num)

#B
def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    print(result)
#C
def xor(x, y):
    return (x + y) % 2
