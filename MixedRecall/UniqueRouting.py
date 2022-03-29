# Problem:
#
# Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples where each tuple represents a direct road
# that connects a pair of cities. The function should return a boolean indicating whether or not there exists a unique route for
# every pair of cities. A route is a sequence of roads that does not visit a city more than once.
#
# Cities will be numbered 0 to n - 1.
#
# You can assume that all roads are two-way roads. This means if there is a road between A and B,
# then you can use that road to go from A to B or go from B to A.

# Notes:

# For example, given these roads:
#
# 0 --- 1
# | \
# |  \
# |   \
# 2    3
#
# There is a unique route for between every pair of cities.
# So the answer is True.
#
#
# For example, given these roads:
#
# 0 --- 1
# | \
# |  \
# |   \
# 2 -- 3
#
# There are two routes that can be used to travel from city 1 to city 2:
# - first route:  1, 0, 2
# - second route: 1, 0, 3, 2
# The answer is False, because routes should be unique.


# Solution:
# 1. Convert edge list to adjacency list
# 2. Iterate through adjacency list
# 3. DFS, track visited
#    a. if visited second time, return False
#    b. if DFS finishes and not match roads, then False too


def rare_routing(n, roads):
    graph = make_graph(n, roads)
    visited = set()
    valid = validate(graph, 0, visited, None)

    # check that it is valid and we have visited all nodes
    return valid and len(visited) == n


def validate(graph, node, visited, last_node):
    # All visited nodes are considered False, because we're searching for unique paths
    if node in visited:
        return False

    visited.add(node)
    for neighbor in graph[node]:
        # keep track of last node to preven from duplicate travel back to last node
        if neighbor != last_node and not validate(graph, neighbor, visited, node):
            return False

    return True


def make_graph(n, roads):
    graph = {}

    for city in range(n):
        graph[city] = []

    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)

    return graph

print(rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
])) # -> True