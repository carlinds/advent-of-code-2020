import collections
import re

def parse_rules_to_dict(rules):
    d = collections.defaultdict(list)
    for line in rules.split('\n'):
        [rule_id, rule_content] = line.split(': ')
        d[rule_id] = rule_content.strip().split()

    return d


def main():
    with open('messages.txt') as f:
        [rules, messages] = f.read().split('\n\n')

    d = parse_rules_to_dict(rules)

    def expand_sub_rules(rule_id):
        sub_rules = d[rule_id]

        regex = '('
        for rule in sub_rules:
            if rule in {'"a"', '"b"'}:
                regex += rule[1]

            elif rule == '|':
                regex += '|'

            else:
                regex += expand_sub_rules(rule)

        regex += ')'
        return regex

    regex = expand_sub_rules('0')

    c = 0
    for message in messages.split():
        match = re.fullmatch(regex, message.strip(), flags=0)
        if match:
            c += 1

    print(c)

    return 0


if __name__ == "__main__":
    main()