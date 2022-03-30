# Problem:
#
# Given a matrix, return a list of river sizes.  A river is a node that has a value of 1.

# Solution:
# 1. Iterate through the grid
# 2. if a node has a value of 1, then DFS and count

def river_sizes(grid):
    visited = set()
    river_sizes = []
    # Iterate through rows and columns
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                river_size = explore_river(grid, row, col, visited)
                if river_size > 0:
                    river_sizes.append(river_size)

    return river_sizes

def explore_river(grid, row, col, visited):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return 0

    if grid[row][col] == 0:
        return 0

    pos = (row, col)
    if pos in visited:
        return 0

    visited.add(pos)
    size = 1
    size += explore_river(grid, row - 1, col, visited)
    size += explore_river(grid, row + 1, col, visited)
    size += explore_river(grid, row, col - 1, visited)
    size += explore_river(grid, row, col + 1, visited)

    return size

grid = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

print(river_sizes(grid))