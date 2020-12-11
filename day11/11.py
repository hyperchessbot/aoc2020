from copy import deepcopy
from functools import cache
from itertools import chain, combinations

with open('01.txt', 'r') as f:
    data = [list(x.strip()) for x in f.readlines()]


@cache
def get_surrounding(x, y):
    y_range = [i for i in [y - 1, y, y + 1] if i >= 0 and i < len(data)]
    x_range = [i for i in [x - 1, x, x + 1] if i >= 0 and i < len(data[y])]
    return list(chain(*[[(i, j) for i in x_range if not (i == x and j == y)] for j in y_range]))


def process_tick(area):
    new = deepcopy(area)
    for y, row in enumerate(area):
        for x, seat in enumerate(row):
            if seat =='.':
                continue
            else:
                occupied = sum([1 for i, j in get_surrounding(x, y) if area[j][i] == '#'])
                if occupied == 0:
                    new[y][x] = '#'
                elif occupied >= 4:
                    new[y][x] = 'L'
    return new, ''.join(chain(*area)) == ''.join(chain(*new))


seating = deepcopy(data)
while True:
    seating, unchanged = process_tick(seating)
    if unchanged:
        break
print('Part 1:', ''.join(chain(*seating)).count('#'))

cardinals = list(chain(*[[(x,y) for x in [-1, 0, 1]if (x,y) != (0,0)] for y in [-1, 0, 1]]))


@cache
def get_surrounding2(x, y):
    line_of_sight = []
    for direction in cardinals:
        next_x = x
        next_y = y
        while True:
            next_x += direction[0]
            next_y += direction[1]
            if 0 <= next_x < len(data[0]) and 0 <= next_y < len(data):
                if data[next_y][next_x] != '.':
                    line_of_sight.append((next_x, next_y))
                    break
            else:
                break
    return line_of_sight

def process_tick2(area):
    new = deepcopy(area)
    for y, row in enumerate(area):
        for x, seat in enumerate(row):
            if seat == '.':
                continue
            else:
                occupied = sum([1 for i, j in get_surrounding2(x, y) if area[j][i] == '#'])
                if occupied == 0:
                    new[y][x] = '#'
                elif occupied >= 5:
                    new[y][x] = 'L'
    return new, ''.join(chain(*area)) == ''.join(chain(*new))

seating = deepcopy(data)
while True:
    seating, unchanged = process_tick2(seating)
    if unchanged:
        break
print('Part 2:', ''.join(chain(*seating)).count('#'))

