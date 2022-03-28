# Problem:
#
# Write a function, count_paths, that takes in a grid as an argument. In the grid, 'X' represents walls and 'O' represents open spaces.
# You may only move down or to the right and cannot pass through walls.
# The function should return the number of ways possible to travel from the top-left corner of the grid to the bottom-right corner.


# Solution:
# 1. Start from root or left most position, move right and move down
# 2. Check for inbounds and wall
# 3. Check for reaching end of the grid position
# 4. Count the path or edges from bottom where it is 1, bubble up to root
#
# Time:
# r = rows
# c = cols
#
# O(2 ^ (r+c)) - brute force
# O(r * c) - memoize


def count_paths(grid):
    return _count_paths(grid, 0, 0, {})


def _count_paths(grid, r, c, memo):
    pos = (r, c)
    if pos in memo:
        return memo[pos]

    # Check for inbounds and wall
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0

    # check that we have reached the end position
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    right_count = _count_paths(grid, r, c + 1, memo)
    down_count = _count_paths(grid, r + 1, c, memo)
    memo[pos] =  down_count + right_count

    return memo[pos]


grid = [
  ["O", "O"],
  ["O", "O"],
]

print(count_paths(grid)) # -> 2