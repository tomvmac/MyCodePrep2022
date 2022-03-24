# Problem:
# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
# The function should return the number of connected components within the graph.

# Solution:
# 1. Iterate through adjacency list
# 2. Perform DFS or BFS starting with that node, keep track of all visited nodes, only proceed with DFS if node is not visited
# 3. Once DFS or BFS is done, increment count


def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore_graph(graph, node, visited):
            count += 1

    return count


def explore_graph(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore_graph(graph, neighbor, visited)

    return True






print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 2