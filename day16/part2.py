import itertools
import collections

def parse_input(text_file):
    with open(text_file) as f:
        text_input = f.read().split('\n\n')
    
    fields = parse_fields(text_input[0].split('\n'))
    my_ticket = text_input[1].split('\n')[1].strip().split(',')
    scanned_tickets = [row.strip().split(',') for row in text_input[2].split('\n')[1:]]

    return fields, my_ticket, scanned_tickets


def parse_fields(lines):
    fields = {}
    for line in lines:
        name, ranges = line.split(': ')
        lower_range, upper_range = ranges.split(' or ')
        lower_range = lower_range.split('-')
        upper_range = upper_range.split('-')

        tot_range = (list(range(int(lower_range[0]), int(lower_range[-1]) + 1)) + 
            list(range(int(upper_range[0]), int(upper_range[-1]) + 1)))

        fields[name] = tot_range
    return fields


def get_valid_tickets(scanned_tickets, fields):
    valid_ranges = list(itertools.chain(*fields.values()))  
    valid_tickets = []
    for ticket in scanned_tickets:
        valid = True
        for number in ticket:
            if int(number) not in valid_ranges:
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    return valid_tickets


def conclude_positions(possible_positions):
    for i in possible_positions:
        if (len(possible_positions[i]) == 1):
            for j in possible_positions:
                if (i != j) and (possible_positions[i][0] in possible_positions[j]):
                    possible_positions[j].remove(possible_positions[i][0])
                    conclude_positions(possible_positions)


def find_possible_positions(fields, valid_tickets):
    possible_positions = collections.defaultdict(list)
    for i in range(len(fields)):
        numbers = [int(t[i]) for t in valid_tickets]

        for name in fields:
            in_range = True
            for n in numbers:
                if n not in fields[name]:
                    in_range = False
                    break
            
            if in_range:
                possible_positions[name].append(i)

    return possible_positions


def main():
    fields, my_ticket, scanned_tickets = parse_input('ticketdata.txt')
    
    valid_tickets = get_valid_tickets(scanned_tickets, fields)

    possible_positions = find_possible_positions(fields, valid_tickets)

    conclude_positions(possible_positions)

    s = 1
    for name in possible_positions:
        if 'departure' in name:
            pos = possible_positions[name][0]
            s *= int(my_ticket[pos])

    print(s)


    return 0

if __name__ == "__main__":
    main()