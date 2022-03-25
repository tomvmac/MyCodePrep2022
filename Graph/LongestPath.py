# Problem:
#
# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph.
# The function should return the length of the longest path within the graph.
# A path may start and end at any two nodes.
# The length of a path is considered the number of edges in the path, not the number of nodes.

# Solution:
# 1. Iterate through adjacency list, Find terminal node(s), mark with distance of 0
# 2. DFS, fill out the distance dictionary
# 3. Increment distance, favor large side if there are multiple edges connected to the same origin


def longest_path(graph):
    distance = {}

    # locate and mark all terminal nodes
    for node in graph:
        if len(graph[node] == 0):
            distance[node] = 0


    for node in graph:
        traverse_distance(graph, node, distance)

    return max(distance.values())

# DFS
def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    max_length = 0
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distance)
        max_length = max(attempt, max_length)

    # add 1 to the max_length to get edges from node
    distance[node] = 1 + max_length

    return distance[node]