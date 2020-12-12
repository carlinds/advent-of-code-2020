def main():
    with open('instructions.txt') as f:
        instructions = [ (line[0], int(line[1:].strip())) for line in f.readlines() ]

    directions = ['N', 'E', 'S', 'W']
    direction_map = {'N': (0, 1),
                     'E': (1, 0),
                     'S': (0, -1),
                     'W': (-1, 0)}

    x, y = 0, 0
    di = 1

    for action, value in instructions:
        dx, dy = 0, 0
        move = 0

        if action == 'F':
            dx, dy = direction_map[directions[di]]
            move = value

        elif action == 'R':
            di += int(value / 90)

        elif action == 'L':
            di -= int(value / 90)

        else:
            dx, dy = direction_map[action]
            move = value

        x += dx * move
        y += dy * move
        di %= len(directions)

    print(abs(x) + abs(y))
    return 0


if __name__ == "__main__":
    main()