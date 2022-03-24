# Problem:
#
# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land.
# The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

# Solution:
# 1. Iterate through rows and cols
# 2. Check for land
# 3. For land nodes, perform DFS and mark each node as visited
# 4. Count each time DFS is performed.
# 5. Return count


def minimum_island(grid):
    visited = set()
    min_size = float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size


def explore_size(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return 0

    if grid[r][c] == 'W':
        return 0

    pos = (r, c)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += explore_size(grid, r - 1, c, visited)
    size += explore_size(grid, r + 1, c, visited)
    size += explore_size(grid, r, c - 1, visited)
    size += explore_size(grid, r, c + 1, visited)

    return size

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 9

