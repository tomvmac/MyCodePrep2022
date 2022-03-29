# Problem:
#
# Write a function, string_search, that takes in a grid of letters and a string as arguments.
# The function should return a boolean indicating whether or not the string can be found
# in the grid as a path by connecting horizontal or vertical positions. The path can begin at any position,
# but you cannot reuse a position more than once in the path.
#
# You can assume that all letters are lowercase and alphabetic.
#
# Solution:
# 1. Given a grid of rows and cols, iterate through the grid matching each val against first letter of string
# 2. Once matched, perform DFS
# 3. If DFS matches entire string, then return True, otherwise continue until end of grid


def string_search(grid, s):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if dfs(grid, r, c, s, set()):
                return True
    return False


def dfs(grid, r, c, s, visited):
    if s == '':
        return True

    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    pos = (r, c)
    if pos in visited:
        return False
    visited.add(pos)

    if not row_inbounds or not col_inbounds:
        return False

    # match current character against start of search string
    char = grid[r][c]
    if char != s[0]:
        return False

    suffix = s[1:]

    # grid[r][c] = '*'

    result = dfs(grid, r + 1, c, suffix) or dfs(grid, r - 1, c, suffix) or dfs(grid, r, c + 1, suffix) or dfs(grid, r,
                                                                                                              c - 1,
                                                                                                              suffix)
    # grid[r][c] = char
    return result



grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'hello') # -> True