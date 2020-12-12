def main():
    with open('instructions.txt') as f:
        instructions = [ (line[0], int(line[1:].strip())) for line in f.readlines() ]

    direction_map = {'N': (0, 1),
                     'E': (1, 0),
                     'S': (0, -1),
                     'W': (-1, 0)}

    x, y = 0, 0
    wx, wy = 10, 1

    for action, value in instructions:

        if action == 'F':
            dx, dy = wx, wy
            x += dx * value
            y += dy * value

        elif action == 'R':
            for _ in range(int(value/90)):
                temp = (wx, wy)
                wx = temp[1]
                wy = -temp[0]

        elif action == 'L':
            for _ in range(int(value/90)):
                temp = (wx, wy)
                wx = -temp[1]
                wy = temp[0]

        else:
            dx, dy = direction_map[action]
            wx += dx * value
            wy += dy * value

    print(abs(x) + abs(y))
    return 0


if __name__ == "__main__":
    main()