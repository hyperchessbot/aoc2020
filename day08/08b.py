from typing import Iterable

data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6"""
data = data.split('\n')


def code(code_input: Iterable[str]):
    code_input = tuple(code_input)
    for i in range(len(code_input)):
        if code_input[i].startswith('nop') or code_input[i].startswith('jmp'):
            yield code_input[:i] + (code_input[i].replace('nop', 'jmp') if 'nop' in code_input[i] else code_input[i].replace('jmp', 'nop'),) + \
                  code_input[i + 1:]


with open('01.txt', 'r') as f:
    data = f.readlines()

code_gen = code(data)

def process(data):
    idx = 0
    visited = set()
    accumulator = 0
    while True:
        if idx in visited:
            return False, accumulator
        visited.add(idx)
        try:
            inst, val = data[idx].split()
        except IndexError:
            return True, accumulator
        if inst == 'nop':
            pass
        elif inst == 'acc':
            accumulator += int(val)
        elif inst == 'jmp':
            idx += int(val)
            continue
        idx += 1

while True:
    try:
        passed, acc = process(next(code_gen))
        if passed:
            break
    except StopIteration:
        break
print('Part 2:', acc)