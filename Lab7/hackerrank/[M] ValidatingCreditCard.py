import re

n = int(input())
for _ in range(n):
    card = input().strip()

    if not re.match(r'^[456]', card):
        print('Invalid')
        continue

    digits = re.sub(r'\D', '', card)
    if len(digits) != 16:
        print('Invalid')
        continue

    if not re.match(r'^[0-9-]+$', card):
        print('Invalid')
        continue

    if '-' in card:
        if not re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card):
            print('Invalid')
            continue

    if re.search(r'(\d)\1{3,}', digits):
        print('Invalid')
        continue

    print('Valid')
