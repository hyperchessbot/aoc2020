from collections import Counter

with open('01.txt', 'r') as f:
    data = f.readlines()
valid = 0
valid_2 = 0
for line in data:
    # 4-8 v: bqvvxmvtvhfvv
    rule, pwd = line.split(':')
    pwd = pwd.strip()
    count = Counter(pwd)
    numbers, letter = rule.split()
    min_c, max_c = map(int, numbers.split('-'))
    if min_c <= count[letter] <= max_c:
        valid+=1
    if pwd[min_c-1] == letter or pwd[max_c-1] == letter:
        if pwd[min_c-1] != pwd[max_c-1]:
            valid_2 += 1
print(f"Part 1: {valid}")
print(f"Part 2: {valid_2}")

