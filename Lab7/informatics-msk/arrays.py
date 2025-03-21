#A
def even_indexes():
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(0, N, 2):
        print(numbers[i])

#B
def even_numbers():
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i % 2 == 0:
            print(i)
#C
def count_positive_numbers():
    numbers = list(map(int, input().split()))
    counter = 0
    for i in numbers:
        if i > 0:
            counter += 1
    print(counter)

#D
def print_greater_than_previous():
    numbers = list(map(int, input().split()))
    for i in range(1, len(numbers)):
        if numbers[i-1] < numbers[i]:
            print(numbers[i])

#E
def find_adjacent_same_sign():
    numbers = list(map(int, input().split()))
    for i in range(0, len(numbers) -1):
        if (numbers[i] > 0 and numbers[i+1] > 0) or (numbers[i] < 0 and numbers[i+1] < 0):
            print(numbers[i], numbers[i+1])
            return

#F
def count_local_maxima():
    numbers = list(map(int, input().split()))
    counter = 0
    for i in range(1, len(numbers) - 1):
        if(numbers[i-1] < numbers[i] and numbers[i] > numbers[i+1]):
            counter += 1
    print(counter)

#G
def find_max_position():
    numbers = list(map(int, input().split()))
    max = 0
    max_pos = 0
    for i in range(0, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
            max_pos = i
    print(max_pos)
