# Problem:
#
# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column.
# In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots.
# The function should return a number representing the length of the shortest path from the starting position to a carrot.
# You may move up, down, left, or right, but cannot pass through walls (X).
# If there is no possible path to a carrot, then return -1.

# Solution:
# 1. Iterate through rows/cols
# 2. BFS
# 3. Queue should track row, col, distance
# 4. Track visited and skip walls (W)
# 5. return smallest size

from collections import deque


def closest_carrot(grid, starting_row, starting_col):
    visited = set([(starting_row, starting_col)])
    queue = deque([(starting_row, starting_col, 0)])
    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == 'C':
            return distance

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            pos = (neighbor_row, neighbor_col)
            row_inbounds = 0 <= neighbor_row < len(grid)
            col_inbounds = 0 <= neighbor_col < len(grid[0])
            if row_inbounds and col_inbounds and pos not in visited and grid[row][col] != 'X':
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))

    return -1


grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 0, 0)) # -> 5