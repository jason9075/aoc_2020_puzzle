import re

FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    passports = []
    passport_fields = {}

    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        if line == "":
            passports.append(passport_fields.copy())
            passport_fields.clear()
            continue

        fields = line.split(" ")

        for field in fields:
            passport_fields[field.split(":")[0]] = field.split(":")[1]

    passports.append(passport_fields.copy())  # last record

    valid_count = 0
    for passport in passports:
        if len(passport) == 8:
            valid_count += 1
        elif len(passport) == 7 and 'cid' not in passport.keys():
            valid_count += 1

    print(valid_count)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    passports = []
    passport_fields = {}

    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        if line == "":
            passports.append(passport_fields.copy())
            passport_fields.clear()
            continue

        fields = line.split(" ")

        for field in fields:
            passport_fields[field.split(":")[0]] = field.split(":")[1]

    passports.append(passport_fields.copy())  # last record

    valid_count = 0
    for passport in passports:
        if len(passport) < 7:
            continue
        if len(passport) == 7 and 'cid' in passport.keys():
            continue

        byr = int(passport['byr'])
        if not (1920 <= byr <= 2002):
            continue

        iyr = int(passport['iyr'])
        if not (2010 <= iyr <= 2020):
            continue

        eyr = int(passport['eyr'])
        if not (2020 <= eyr <= 2030):
            continue

        hgt = passport['hgt']
        hgt_type = hgt[-2:]
        if hgt_type == 'cm':
            hgt_value = int(hgt[:-2])
            if not (150 <= hgt_value <= 193):
                continue
        elif hgt_type == 'in':
            hgt_value = int(hgt[:-2])
            if not (59 <= hgt_value <= 76):
                continue
        else:
            continue

        hcl = passport['hcl']
        if re.match(r"#[a-f0-9]{6}$", hcl) is None:
            continue

        ecl = passport['ecl']
        if re.match(r"(amb|blu|brn|gry|grn|hzl|oth)$", ecl) is None:
            continue

        pid = passport['pid']
        if re.match(r"[0-9]{9}$", pid) is None:
            continue

        valid_count += 1

    print(valid_count)


if __name__ == '__main__':
    # p1()
    p2()
