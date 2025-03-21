#A
def bigger( a,  b):
    if a > b:
        return a
    return  b

#B
def leap_year( a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return "YES"
    return "NO"
#C
def testing_system(a, b):
    if a == 1:
        if b == 1:
            print("YES")
        else:
            print("NO")
    else:
        if b != 1:
            print("YES")
        else:
            print("NO")

#D
def sign(a):
    if a > 0:
        print(1)
    elif a < 0:
        print(-1)
    else:
        print(0)

#E
def bigger2(a, b):
    if a > b:
        return 1
    elif b > a:
        return 2
    else:
        return 0