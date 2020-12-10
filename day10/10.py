from collections import deque

with open('01.txt', 'r') as f:
    data = [int(x.strip()) for x in f.readlines()]
data.append(0)
data.sort()
data.append(max(data)+3)
ones = 0
threes = 0
for low, high in zip(data, data[1:]):
    if high - low == 3:
        threes += 1
    elif high - low == 1:
        ones += 1
print('Part 1:', ones*threes)

index = {x: [y for y in data if y>x and y-x <= 3] for x in data}

results = {}


def search(num, endpoint):
    total = 0
    queue = deque([num])
    while queue:
        current = queue.popleft()
        for n in index[current]:
            if n == endpoint:
                total += 1
            elif n in results:
                total += results[n]
            else:
                queue.append(n)
    return total


for i in sorted(data, reverse=True)[1:]:
    results[i] = search(i, max(data))

print('Part 2:', results[0])
