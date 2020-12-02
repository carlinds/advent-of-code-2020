import re

def main():
    with open("passwords.txt") as f:
        input_list = f.read().split('\n')

    n_valid_passwords = 0    
    for input_str in input_list:

        tmp = input_str.split(':')
        password = tmp[1].strip()

        first_pos = int(re.search('([0-9]+-)', tmp[0]).group(0).strip('-'))
        second_pos = int(re.search('(-[0-9]+)', tmp[0]).group(0).strip('-'))
        policy = re.search('([a-z])', tmp[0]).group(0)

        position_matches = (password[first_pos - 1] == policy) + (password[second_pos - 1] == policy)
        if position_matches == 1:
            n_valid_passwords += 1

    print(n_valid_passwords)
    return 0


if __name__ == "__main__":
    main()
