#A
def evens(a,  b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)


#B
def reminder(a, b, c, d):
    for num in range(a, b + 1):
        if num % d == c:
            print(num)
#C
def full_squares(a, b):
    for num in range(a, b + 1):
        sqrt = int(num ** 0.5)
        if sqrt * sqrt == num:
            print(num)

#D
def repet(x, d):
    count = 0
    for digit in str(x):
        if digit == str(d):
            count += 1
    print(count)
    #можно с конца дробить /10

#E
def sum_of_digits(x):
    total = 0
    for digit in str(x):
        total += int(digit)
    print(total)
    
#F
def reverse_number(x):
    reversed_num = ''
    for digit in str(x):
        reversed_num = digit + reversed_num
    print(int(reversed_num))


#G
def smallest_divisor(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return i
    return x

#H 
def all_divisors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

#I
def print_all_divisors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

#J
def sum_of_100_numbers():
    total = 0
    for _ in range(100):
        num = int(input())
        total += num
    print(total)

#K 
def sum_of_n_numbers(n):
    total = 0
    for _ in range(n):
        num = int(input())
        total += num
    print(total)

#L
def binary_to_decimal(binary):
    decimal = 0
    powered_two = 1  
    for digit in reversed(str(binary)):
        decimal += int(digit) * powered_two
        powered_two *= 2  
    print(decimal)

#M
def count_zeros(n):
    count = 0
    for _ in range(n):
        num = int(input())
        if num == 0:
            count += 1
    print(count)



