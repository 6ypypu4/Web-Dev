def wrap_text(string, width):
    wrapped_lines = []
    for i in range(0, len(string), width):
        wrapped_lines.append(string[i:i+width])
    return '\n'.join(wrapped_lines)

if __name__ == '__main__':
    string = input()
    width = int(input())
    print(wrap_text(string, width))

