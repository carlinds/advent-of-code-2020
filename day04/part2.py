import re

def main():
    with open('passports.txt') as f:
        passports = f.read().split('\n\n')

    passports = map(convert_passport, passports)

    valid_passports = 0
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        valid_fields = []
        for field in expected_fields:
            valid_fields.append(check_valid_field(field, passport))

        if all(valid_fields):
            valid_passports += 1

    print(valid_passports)
    return 0


def convert_passport(passport):
    return {field.split(':')[0] : field.split(':')[1] for field in passport.split()}


def check_valid_field(field, passport):
    if field in passport:
        value = passport[field]
        if field == 'byr':
            valid = (int(value)>=1920 and int(value)<=2002)

        if field == 'iyr':
            valid = (int(value)>=2010 and int(value)<=2020)

        if field == 'eyr':
            valid = (int(value)>=2020 and int(value)<=2030)

        if field == 'hgt':
            if value.endswith('cm'):
                value = int(value.strip('cm'))
                valid = (value>=150 and value<=193)

            elif value.endswith('in'):
                value = int(value.strip('in'))
                valid = (value>=59 and value<=76)

            else:
                valid = False

        if field == 'hcl':
            valid = bool(re.match('(#[a-f0-9]{6}$)', value))

        if field == 'ecl':
            valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if field == 'pid':
            valid = bool(re.match('([0-9]{9}$)', value))

    else:
        valid = False

    return valid


if __name__ == "__main__":
    main()