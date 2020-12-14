import re
with open('01.txt', 'r') as f:
    data = list(map(str.strip, f.readlines()))

mem_re = re.compile(r'mem\[(?P<mem>\d+)\] = (?P<val>\d+)')
mask = []
memory = {}
for line in data:
    if line.startswith('mask'):
        mask = [(x, y) for x, y in zip(line.split(' = ')[1], range(36)) if x.isdigit()]
    elif match := mem_re.match(line):
        val = list(f'{int(match.group("val")):036b}')
        for v, i in mask:
            val[i] = v
        memory[match.group('mem')] = int(''.join(val), 2)
print('Part 1:', sum(memory.values()))

mask = []
memory = {}
for line in data:
    if line.startswith('mask'):
        mask = [(x, y) for x, y in zip(line.split(' = ')[1], range(36)) if x == '1']
        f_mask = [y for x, y in zip(line.split(' = ')[1], range(36)) if x == 'X']
        template = f'{{0:0{len(f_mask)}b}}'
        masks = [list(zip(template.format(x), f_mask)) for x in range(2**len(f_mask))]
    elif match := mem_re.match(line):
        val = list(f'{int(match.group("mem")):036b}')
        for v, i in mask:
            val[i] = v
        for m in masks:
            for v, i in m:
                val[i] = v
            memory[int(''.join(val), 2)] = int(match.group('val'))

print('Part 2:', sum(memory.values()))