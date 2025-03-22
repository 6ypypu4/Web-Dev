def split_and_join(s):
    words = s.split()
    return '-'.join(words)

if __name__ == '__main__':
    input_string = input()
    print(split_and_join(input_string))

