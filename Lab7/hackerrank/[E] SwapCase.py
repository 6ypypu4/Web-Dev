def swap_case(s):
    swapped = []
    for char in s:
        if char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)
    return ''.join(swapped)

if __name__ == '__main__':
    input_string = input()
    print(swap_case(input_string))

