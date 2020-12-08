data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
data = data.split('\n')

# with open('01.txt', 'r') as f:
#     data = f.readlines()

idx = 0
visited = set()
accumulator = 0
while idx not in visited:
    visited.add(idx)
    inst, val = data[idx].split()
    if inst == 'nop':
        pass
    elif inst == 'acc':
        accumulator += int(val)
    elif inst == 'jmp':
        idx += int(val)
        continue
    idx += 1
print("Part 1:", accumulator)