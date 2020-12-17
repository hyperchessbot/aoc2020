from functools import cache
from itertools import  product
from typing import NamedTuple, Set

with open('01.txt', 'r') as f:
    data = f.readlines()


class Cube(NamedTuple):
    x: int
    y: int
    z: int
    w: int

    @property
    @cache
    def neighbours(self):
        all_cubes = set([Cube(*c) for c in
                         product(range(self.x - 1, self.x + 2), range(self.y - 1, self.y + 2),
                                 range(self.z - 1, self.z + 2), range(self.w - 1, self.w + 2))])
        all_cubes.remove(self)
        return all_cubes


class Universe:
    cubes: Set[Cube] = set()
    next_cubes: Set[Cube] = set()

    @property
    def x_range(self):
        allx = [c.x for c in self.cubes]
        return min(allx) - 1, max(allx) + 2

    @property
    def y_range(self):
        ally = [c.y for c in self.cubes]
        return min(ally) - 1, max(ally) + 2

    @property
    def z_range(self):
        allz = [c.z for c in self.cubes]
        return min(allz) - 1, max(allz) + 2

    @property
    def w_range(self):
        allw = [c.w for c in self.cubes]
        return min(allw) - 1, max(allw) + 2

    def search_area(self):
        return (Cube(*c) for c in
                product(range(*self.x_range), range(*self.y_range), range(*self.z_range), range(*self.w_range)))

    def simulate(self):
        self.next_cubes = set()
        for cube in self.search_area():
            if cube in self.cubes and 2 <= len(cube.neighbours & self.cubes) <= 3:
                self.next_cubes.add(cube)
            elif cube not  in self.cubes and len(cube.neighbours & self.cubes) == 3:
                self.next_cubes.add(cube)
        self.cubes = self.next_cubes


uni = Universe()

for y, row, in enumerate(data):
    for x, col in enumerate(row.strip()):
        if col == '#':
            uni.cubes.add(Cube(x, y, 0, 0))

for t in range(6):
    uni.simulate()

print("Part 2:", len(uni.cubes))