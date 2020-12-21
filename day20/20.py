import math
from dataclasses import dataclass
from functools import reduce
from itertools import product, permutations, chain
from typing import NamedTuple, List, Tuple, Set


class Borders(NamedTuple):
    north: str
    east: str
    south: str
    west: str

    def show(self):
        print(self.north)
        for line in zip(self.west[1:-1], self.east[1:-1]):
            print(line[0], ' '*(len(self.north)-4) , line[1])
        print(self.south)


@dataclass(unsafe_hash=True)
class Tile:
    id: int
    orig_north: str
    orig_east: str
    orig_south: str
    orig_west: str
    perms: Tuple[Borders]

    def __init__(self, data):
        data = data.strip().split('\n')
        self.id = int(data.pop(0).split()[1][:-1])
        self.orig_north = data[0]
        self.orig_south = data[-1]
        self.orig_east = ''.join([x[-1] for x in data])
        self.orig_west = ''.join([x[0] for x in data])
        self.perms_build = [
            Borders(self.orig_north, self.orig_east, self.orig_south, self.orig_west),
            Borders(self.orig_west[::-1], self.orig_north, self.orig_east[::-1], self.orig_south),
            Borders(self.orig_south[::-1], self.orig_west[::-1], self.orig_north[::-1], self.orig_east[::-1]),
            Borders(self.orig_east, self.orig_south[::-1], self.orig_west, self.orig_north[::-1]),
        ]
        for border in list(self.perms_build):
            self.perms_build.extend([
                Borders(border.south, border.east[::-1], border.north, border.west[::-1]),
                Borders(border.north[::-1], border.west, border.south[::-1], border.east),
                Borders(border.south[::-1], border.west[::-1], border.north[::-1], border.east[::-1])
            ])
        self.perms = tuple(self.perms_build)
        self.data = data

    @property
    def borders(self):
        return {
            self.orig_north, self.orig_north[::-1],
            self.orig_east, self.orig_east[::-1],
            self.orig_south, self.orig_south[::-1],
            self.orig_west, self.orig_west[::-1]
        }

tiles = []
with open('02.txt', 'r') as f:
    raw_data = f.read()
    tiles_raw = raw_data.split('\n\n')
    for tile_raw in tiles_raw:
        tiles.append(Tile(tile_raw))

size = math.sqrt(len(tiles))
print(int(size))
if size == 3:
    state = [['', '', ''] for _ in range(3)]

tile_map = {}
for tile in tiles:
    tile_map[tile] = []
    for other_tile in tiles:
        if tile == other_tile:
            continue
        elif tile.borders & other_tile.borders:
            tile_map[tile].append(other_tile)

total = [k.id for k,v in  tile_map.items() if len(v) == 2]
# for k, v in tile_map.items():
#     print(k.id, [x.id for x in v])
print('Part 1:', reduce(lambda a, b: a*b, total))

