import copy

def main():
    with open('seat_layout.txt') as f:
        initial_grid = [list(line.strip()) for line in f.readlines()]
    n_rows = len(initial_grid)
    n_cols = len(initial_grid[0])

    # Add "empty" border around the seat layout
    initial_grid.insert(0, list('L'*n_cols))
    initial_grid.insert(n_rows + 1, list('L'*n_cols))
    for row in initial_grid:
        row.insert(0, 'L')
        row.insert(n_cols + 1, 'L')

    new_grid = copy.deepcopy(initial_grid)
    grid = []
    while new_grid != grid:
        grid = copy.deepcopy(new_grid)
        for i in range(1, n_rows + 1):
            for j in range(1, n_cols + 1):
                seat = grid[i][j]
                adjacent_seats = [
                    grid[i-1][j-1],
                    grid[i-1][j],
                    grid[i-1][j+1],
                    grid[i][j-1],
                    grid[i][j+1],
                    grid[i+1][j-1],
                    grid[i+1][j],
                    grid[i+1][j+1]]
                    
                occupied_seats = sum([x == '#' for x in adjacent_seats])

                if (seat == 'L') and (occupied_seats == 0):
                    new_grid[i][j] = '#'
                
                if (seat == '#') and (occupied_seats >= 4):
                    new_grid[i][j] = 'L'

    tot_occupied_seats = 0
    for row in grid[1:-1]:
        tot_occupied_seats += sum([x == '#' for x in row[1:-1]])

    print(tot_occupied_seats)
    return 0


if __name__ == "__main__":
    main()