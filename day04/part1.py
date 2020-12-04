def main():
    with open('passports.txt') as f:
        passports = f.read().split('\n\n')

    passports = map(convert_passport, passports)

    valid_passports = 0
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        if all([field in passport for field in expected_fields]):
            valid_passports += 1

    print(valid_passports)
    return 0


def convert_passport(passport):
    return {field.split(':')[0] : field.split(':')[1] for field in passport.split()}


if __name__ == "__main__":
    main()