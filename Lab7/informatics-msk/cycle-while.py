#A
def squares_up_to_n(N):
    i = 1
    while i*i <= N:
        print(i*i)
        i += 1

#B
def smallest_divisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1
#C
def powers_of_two(N):
    power = 1
    while power <= N:
        print(power)
        power *= 2

#D
def is_power_of_two(N):
    if N <= 0:
        return "NO"
    while N > 1:
        if N % 2 != 0:
            return "NO"
        N = N // 2
    return "YES"

#E
def double_log(x):
    k = 0
    power = 1
    while power < x:
        power *= 2
        k += 1
    print(k)
