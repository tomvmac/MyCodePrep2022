# Problem:
#
# Write a function, largest_component, that takes in the adjacency list of an undirected graph.
# The function should return the size of the largest connected component in the graph.


# Solution:
# 1. Iterate through adjacency list
# 2. Perform DFS or BFS starting with that node, keep track of all visited nodes, only proceed with DFS if node is not visited
# 3. Count component size, maintain maxComponentSize


def largest_component(graph):
    visited = set()
    maxComponentSize = 0

    for node in graph:
        size = count_graph_size(graph, node, visited)
        maxComponentSize = max(size, maxComponentSize)


    return maxComponentSize


def count_graph_size(graph, current, visited):
    if current in visited:
        return 0

    size = 1
    visited.add(current)

    for neighbor in graph[current]:
        size += count_graph_size(graph, neighbor, visited)

    return size

print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6