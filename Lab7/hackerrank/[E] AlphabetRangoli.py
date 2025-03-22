def print_rangoli(size):
    import string
    letters = string.ascii_lowercase[:size]
    
    for i in range(size-1, -size, -1):
        abs_i = abs(i)
        middle = '-'.join(letters[size-1:abs_i:-1] + letters[abs_i:size])
        print(middle.center(4*size-3, '-'))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
