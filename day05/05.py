trans = str.maketrans('FBLR', '0101')

with open('01.txt', 'r') as f:
    data = f.readlines()
highest = 0
for seat in data:
    seat = seat.translate(trans)
    row = eval(f'0b{seat[:7]}')
    col = eval(f'0b{seat[7:]}')
    sid = (row*8) + col
    if sid > highest:
        highest = sid
print('Part 1:', highest)
seat_ids = set()
for seat in data:
    seat = seat.translate(trans)
    row = eval(f'0b{seat[:7]}')
    col = eval(f'0b{seat[7:]}')
    sid = (row*8) + col
    seat_ids.add(sid)
print('Part 2:', set(range(min(seat_ids), max(seat_ids))) - seat_ids)
