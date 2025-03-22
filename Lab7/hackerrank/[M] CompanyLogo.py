s = input()
char_count = {}

for char in s:
    char_count[char] = char_count.get(char, 0) + 1
    
def sort_key(item):
    return (-item[1], item[0])

sorted_chars = sorted(char_count.items(), key=sort_key)

for char, count in sorted_chars[:3]:
    print(f"{char} {count}")
