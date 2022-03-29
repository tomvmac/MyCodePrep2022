# Problem:
#
# Write a function, _breaking_boundaries, that takes in 5 arguments:
# a number of rows (m), a number of columns (n), a number of moves (k), a starting row (r), and a starting column (c).
# Say you were situated in a grid with dimensions m * n. If you had to start at position (r,c),
# in how many different ways could you move out of bounds if you could take at most k moves.
#
# A single move is moving one space up, down, left, or right. During a path you may revisit a position.

# Notes:
# m: rows
# n: columns
# k: moves
# r: starting row
# c: starting col

# Solution:
# 1. Track k, r, c as we move up, down, left, right, decrement k
# 2. Check for out of bounds when r == m or c ==n, assign 1, count
# 3. When k is 0, assign 0
# 4. Include dynamic programming and memo on (k, r, c)
#
# Complexity:
#
# Time: O(mnk)
# Space: O(mnk)

def breaking_boundaries(m, n, k, r, c):
    return _breaking_boundaries(m, n, k, r, c, {})

def _breaking_boundaries(m, n, k, r, c, memo):
    key = (k, r, c)

    if key in memo:
        return memo[key]

    row_inbounds = 0 <= r < m
    col_inbounds = 0 <= c < n

    # base cases
    # count out of bounds
    if not row_inbounds or not col_inbounds:
        return 1

    # when k is 0, no more moves
    if k == 0:
        return 0

    total_count = 0
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for move in moves:
        move_row, move_col = move
        # Get number of ways to get out of bounds from current position
        total_count += _breaking_boundaries(m, n, k-1, r+move_row, c+move_col, memo)
        memo[key] = total_count

    return total_count

print(breaking_boundaries(3, 4, 2, 0, 0)) # -> 4