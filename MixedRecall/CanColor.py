# Problem:
#
# Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph.
# The function should return a boolean indicating whether or not it is possible to color nodes of the graph
# using two colors in such a way that adjacent nodes are always different colors.

# Notes:
# - Neighbor should be different color
# - Use DFS and Island hopping logic
# - When travel to a node that is visited and different color than expected, then return false

# Solution:
# 1. Iterate through adjacency list
# 2. For each component, DFS
#    a. track alternating color
#    b. return False if expected color is not there, otherwise return True


# Traverse through all components
def can_color(graph):
    coloring = {}
    for node in graph:
        if node not in coloring:
            if not valid(graph, node, coloring, False):
                return False

    return True

# Traverse within one component
def valid(graph, node, coloring, current_color):
    if node in coloring:
        return current_color == coloring[node]

    coloring[node] = current_color

    for neighbor in graph[node]:
        if not valid(graph, neighbor, coloring, not current_color):
            return False

    return True


print(can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
})) # -> True

print(can_color({
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
})) # -> False