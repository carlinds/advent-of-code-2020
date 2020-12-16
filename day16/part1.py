def main():
    with open('ticketdata.txt') as f:
        a = f.read().split('\n\n')
    rules = a[0].split('\n')
    #my_ticket = a[1].split('\n')[1].strip().split(',')
    scanned_tickets = [row.strip().split(',') for row in a[2].split('\n')[1:]]

    valid_ranges = []
    for rule in rules:
        _, ranges = rule.split(': ')
        lower_range, upper_range = ranges.split(' or ')
        lower_range = lower_range.split('-')
        upper_range = upper_range.split('-')

        valid_ranges.append(lower_range)
        valid_ranges.append(upper_range)
    
    error_rate = 0
    for ticket in scanned_tickets:
        for number in ticket:
            number = int(number)
            valid_number = False
            for r in valid_ranges:
                l = int(r[0])
                u = int(r[1])

                if (l <= number <= u):
                    valid_number = True
                    break
            
            if not valid_number:
                error_rate += number

    print(error_rate)

    return 0

if __name__ == "__main__":
    main()