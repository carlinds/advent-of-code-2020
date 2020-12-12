import copy

def main():
    with open('seat_layout.txt') as f:
        initial_grid = [list(line.strip()) for line in f.readlines()]
    n = len(initial_grid)
    m = len(initial_grid[0])

    new_grid = copy.deepcopy(initial_grid)
    grid = []
    while new_grid != grid:
        grid = copy.deepcopy(new_grid)

        for i, row in enumerate(grid):
            for j, seat in enumerate(row):
                occupied = 0
                if seat == '.':
                    continue

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (dx, dy) == (0, 0):
                            continue
                        
                        nx = i + dx
                        ny = j + dy

                        while (nx >= 0) and (nx < n) and (ny >= 0) and (ny < m) and grid[nx][ny] == '.':
                            nx += dx
                            ny += dy

                        if (nx >= 0) and (nx < n) and (ny >= 0) and (ny < m):
                            occupied += grid[nx][ny] == '#'

                if (seat == 'L') and (occupied == 0):
                    new_grid[i][j] = '#'
                
                if (seat == '#') and (occupied >= 5):
                    new_grid[i][j] = 'L'

    tot_occupied_seats = 0
    for row in grid:
        tot_occupied_seats += sum([x == '#' for x in row])

    print(tot_occupied_seats)
    return 0


if __name__ == "__main__":
    main()