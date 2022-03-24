# Problem:
#
# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B).
# The function should return the length of the shortest path between A and B.
# Consider the length as the number of edges in the path, not the number of nodes.
# If there is no path between A and B, then return -1.


# Solution:
# 1. BFS
# 2. Store the distance along with the queue item where queue will have (node, distance)

from collections import deque

def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == node_B:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'y', 'x')) # -> 1
