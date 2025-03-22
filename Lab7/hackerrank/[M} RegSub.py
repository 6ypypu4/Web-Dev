n = int(input())
text = [input().strip() for _ in range(n)]

for i in range(len(text)):
    text[i] = text[i].replace(' && ', ' and ')
    text[i] = text[i].replace(' || ', ' or ')

print('\n'.join(text))
