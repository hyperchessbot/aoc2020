with open('01.txt', 'r') as f:
    data = f.read().split('\n\n')

total = 0
for group in data:
    group = group.replace('\n', '')
    total += len(set(group))
print("Part 1:", total)

total = 0
for group in data:
    members = [set(x) for x in group.split()]
    total += len(set.intersection(*members))
print("Part 2:", total)

