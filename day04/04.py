from itertools import chain
import re

with open('01.txt', 'r') as f:
    data = f.read().split('\n\n')
# data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in""".split('\n\n')
valid_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
haircolour = re.compile(r'#[a-f0-9]{6}')
valid = 0
for passport in data:
    fields = set(map(lambda x: x[0:3], passport.split()))
    if not (valid_fields - fields):
        valid += 1
print('Part 1:', valid)
valid = 0
for passport in data:
    fields = {x[0:3]: x[4:] for x in passport.split()}
    if not (valid_fields - set(fields.keys())):
        if not (1920 <= int(fields['byr']) <= 2002):
            continue
        if not (2010 <= int(fields['iyr']) <= 2020):
            continue
        if not (2020 <= int(fields['eyr']) <= 2030):
            continue
        hgt_m = fields['hgt'][-2:]
        hgt = int(fields['hgt'][:-2])
        if hgt_m not in ['in', 'cm']:
            continue
        if hgt_m == 'cm':
            if not (150 <= hgt <= 193):
                continue
        if hgt_m == 'in':
            if not (59 <= hgt <= 76):
                continue
        if not haircolour.match(fields['hcl']):
            continue

        if not fields['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            continue
        if not ((len(fields['pid']) == 9) and fields['pid'].isdecimal()):
            continue
        valid += 1
    else:
        pass
print('Part 2:', valid)