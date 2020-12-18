with open('01.txt', 'r') as f:
    data = f.readlines()


def simple_calc(cmd):
    result = cmd.pop(0)
    while cmd:
        op, nn, *cmd = cmd
        result = eval(f'{result} {op} {nn}')
    return result


def advanced_calc(cmd):
    while '+' in cmd:
        ind = cmd.index('+')
        res = int(cmd[ind - 1]) + int(cmd[ind + 1])
        cmd = cmd[:ind - 1] + [res] + cmd[ind + 2:]
    return simple_calc(cmd)


def get_parent(math_data: str, calc_func):
    while '(' in math_data:
        first_open = math_data.index('(')
        first_close = math_data.index(')')
        if first_close < first_open:
            first_close = math_data[first_open:].index(')') + first_open
        try:
            second_open = math_data[first_open + 1:].index('(') + first_open + 1
        except ValueError:
            second_open = first_close + 1
        if first_close < second_open:
            new = calc_func(math_data[first_open + 1:first_close].split())
            math_data = math_data[:first_open] + str(new) + math_data[first_close + 1:]
        else:
            new = get_parent(math_data[second_open:], calc_func)
            math_data = math_data[:second_open] + str(new)
    return math_data


total = 0
for line in data:
    total += simple_calc(get_parent(line.strip(), simple_calc).split())
print('Part 1:', total)

total = 0
for line in data:
    total += advanced_calc(get_parent(line.strip(), advanced_calc).split())
print('Part 2:', total)
