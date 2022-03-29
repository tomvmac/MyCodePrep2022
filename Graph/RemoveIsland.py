# Problem:
#
# Given a graph or adjacency list of nodes, remove islands.
#
# Island is defined as any component that does not touch the 4 borders.

# Solution:

# Brute Force:
# 1. Loop through graph
# 2. For each node
#    a. DFS, if one touches the  border, change the whole island to 0s

# Optimized:
# 1. Create a matrix of the same size and init with all False
# 2. Loop through 4 borders
#    a. If 1, mark as True for the position and DFS and mark every position as True
# 2. Loop through interior box
#      a. If the pos in T/F matrix is F, then change to 0

# Super Optimized:
# 1. Loop through 4 borders
#    a. If 1, change to 2 for the position and DFS and mark every position as True
# 2. Loop through interior box
#      a. If val 1, then change to 0
#      b. If val is 2, change to 1

# Optimized:
# 1. Create a matrix of the same size and init with all False
# 2. Loop through 4 borders
#    a. If 1, mark as True for the position and DFS and mark every position as True
# 2. Loop through interior box
#      a. If the pos in T/F matrix is F, then change to 0

def print(grid):
    pass

def removeIslands(grid):
    grid = mark_border_lands(grid)


def mark_border_lands(grid):
    visited = set()
    # Iterate through 4 borders and mark node as 2 when a 1 is found and DFS and mark all connected 1s to 2.

    # top border
    # for row in range(0,0):
    #     for col in range(0, grid[0]) :


    # left border
    # right border
    # bottom border


grid: [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]