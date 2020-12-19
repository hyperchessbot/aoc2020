import regex as re


def build_rule(rid):
    rule = []
    if '|' in rules[rid]:
        rule.append('(')
        halves = rules[rid].split(' | ')
        if str(rid) in rules[rid].split():
            rule.append(f'?P<g{rid}>')
        for half in halves:
            for i in half.split():
                if rid == int(i):
                    rule.append(f'(?P>g{rid})')
                else:
                    rule.append(build_rule(int(i)))
            rule.append('|')
        rule.pop()
        rule.append(')')
        return ''.join(rule)
    elif '"' in rules[rid]:
        return rules[rid][-2:-1]
    else:
        for i in rules[rid].split():
            rule.append(build_rule(int(i)))
        return ''.join(rule)

rules = []
messages = []
with open('01.txt', 'r') as f:
    while (line := f.readline().strip()) != '':
        rules.append(line)

    while line := f.readline().strip():
        messages.append(line)

rules = {
    int(rid): val for rid, val in [r.split(': ') for r in rules]
}

regex = re.compile(f'^{build_rule(0)}$')
matches = 0
for line in messages:
    if regex.match(line):
        matches += 1
print('Part 1:', matches)



rules = []
messages = []
with open('02.txt', 'r') as f:
    while (line := f.readline().strip()) != '':
        rules.append(line)

    while line := f.readline().strip():
        messages.append(line)
rules = {
    int(rid): val for rid, val in [r.split(': ') for r in rules]
}

regex = re.compile(f'^{build_rule(0)}$')
matches = 0
for line in messages:
    if regex.match(line):
        matches += 1
print('Part 2:', matches)
