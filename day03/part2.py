def main():
    with open('map.txt') as f:
        grid = f.read().split('\n')

    # Slopes with (right, down)
    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]

    trees = 1
    for slope in slopes:
        trees *= traverse_slope(slope[0], slope[1], grid)

    print(trees)
    return 0


def traverse_slope(right, down, grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    trees = 0
    row, col = 0, 0

    while row < (n_rows-1):
        row += down
        col += right
        col = col % n_cols

        if grid[row][col] == '#':
            trees += 1

    return trees

if __name__ == '__main__':
    main()