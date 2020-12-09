from itertools import combinations

with open('01.txt', 'r') as f:
    data = f.readlines()

orignal = data.copy()
window = []
for _ in range(25):
    window.append(int(data.pop(0).strip()))

for num in data:
    num = int(num.strip())
    if num in set([sum(x) for x in combinations(window, 2)]):
        window.pop(0)
        window.append(num)
    else:
        target = num
        break
print('Part 1:', num)

def zippy(dat):
    i = 1
    while i < len(dat):
        zipper = [dat]
        for x in range(i):
            zipper.append(dat[x+1:])
        yield zip(*zipper)
        i += 1

z = zippy([int(x.strip()) for x in orignal])
for batch in z:
    for nums in batch:
        if target == sum(nums):
            print('Part 2:', min(nums)+max(nums))