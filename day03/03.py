from dataclasses import dataclass


@dataclass
class Point:
    width: int
    x: int = 0
    y: int = 0


with open('01.txt', 'r') as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

def count_trees(right, down=1):
    y = 0
    trees = 0
    for line in data[::down]:
        if line[y % len(line)] == '#':
            trees += 1
        y += right
    return trees
print(count_trees(3))

print(count_trees(1)*count_trees(3)*count_trees(5)*count_trees(7)*count_trees(1,2))