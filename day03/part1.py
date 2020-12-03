def main():
    with open('map.txt') as f:
        grid = f.read().split('\n')

    n_rows = len(grid)
    n_cols = len(grid[0])
    
    trees = 0
    row, col = 0, 0

    while row < (n_rows-1):
        row += 1
        col += 3
        col = col % n_cols

        if grid[row][col] == '#':
            trees += 1

    print(trees)

    return 0


if __name__ == '__main__':
    main()