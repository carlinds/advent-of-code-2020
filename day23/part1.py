TEST_INPUT = '389125467'
PUZZLE_INPUT = '364297581'

def main():
    cups = [int(c) for c in PUZZLE_INPUT] 


    for i in range(100):
        print('-- move {} --'.format(i+1))
        print('cups: ', cups)
        cur = cups[0]
        pick_up = cups[1:4]
        print('pick up: ', pick_up)

        dest = cur - 1

        while (dest in pick_up) or (dest < min(cups)):
            dest -= 1
            if dest < min(cups):
                dest = max(cups)

        print('destination: ', dest)

        cups.pop(0)
        cups.append(cur)

        for j, c in enumerate(pick_up):
            cups.remove(c)
            cups.insert(cups.index(dest) + j + 1, c)

        print('')

    print('-- final --')
    print('cups: ', cups)
    return 0


if __name__ == "__main__":
    main()