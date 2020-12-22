import math
from dataclasses import dataclass
from functools import reduce
from itertools import product, permutations, chain
from typing import NamedTuple, List, Tuple, Set
import numpy as np


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

    def __init__(self, data):
        data = data.strip().split('\n')
        self.id = int(data.pop(0).split()[1][:-1])
        self.orig_north = data[0]
        self.orig_south = data[-1]
        self.orig_east = ''.join([x[-1] for x in data])
        self.orig_west = ''.join([x[0] for x in data])
        self.data = [x.replace('.', '0') for x in data]
        self.data = [list(map(int, x.replace('#', '1'))) for x in self.data]
        print(self.data)
        self.array = np.array(self.data)

    @property
    def borders(self):
        return {
            self.orig_north, self.orig_north[::-1],
            self.orig_east, self.orig_east[::-1],
            self.orig_south, self.orig_south[::-1],
            self.orig_west, self.orig_west[::-1]
        }

tiles = []
with open('01.txt', 'r') as f:
    raw_data = f.read()
    tiles_raw = raw_data.split('\n\n')
    for tile_raw in tiles_raw:
        tiles.append(Tile(tile_raw))

size = int(math.sqrt(len(tiles)))

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

map = []



