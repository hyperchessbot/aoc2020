from functools import cache

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

index = {x: [y for y in data if y > x and y-x <= 3] for x in data}


@cache
def search(num, endpoint):
    total = 0
    for n in index[num]:
        if n == endpoint:
            total += 1
        else:
            total += search(n, endpoint)
    return total


print('Part 2:', search(0, max(data)))
