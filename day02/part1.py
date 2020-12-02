import re

def main():
    with open("passwords.txt") as f:
        input_list = f.read().split('\n')

    n_valid_passwords = 0    
    for input_str in input_list:

        tmp = input_str.split(':')
        password = tmp[1].strip()

        lower_limit = int(re.search('([0-9]+-)', tmp[0]).group(0).strip('-'))
        upper_limit = int(re.search('(-[0-9]+)', tmp[0]).group(0).strip('-'))
        policy = re.search('([a-z])', tmp[0]).group(0)

        matches = password.count(policy)
        if (matches >= lower_limit) and (matches <= upper_limit):
            n_valid_passwords += 1

    print(n_valid_passwords)
    return 0


if __name__ == "__main__":
    main()
