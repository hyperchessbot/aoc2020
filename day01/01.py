from itertools import combinations

with open('01.txt', 'r') as f:
    data = list(map(lambda x: int(x), f.readlines()))

for combo in combinations(data, 2):
    if combo[0]+combo[1] == 2020:
        print(combo[0]*combo[1])
        break

for combo in combinations(data, 3):
    if combo[0]+combo[1]+combo[2] == 2020:
        print(combo[0]*combo[1]*combo[2])
        break