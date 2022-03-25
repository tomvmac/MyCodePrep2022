# Problem:
#
# Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph.
# The function should return a boolean indicating whether or not the graph contains a cycle.

# Solution:
# 1. Use white-grey-black algorithm where:\
#     a. white (unexplored)
#     b. grey (visiting)
#     c. black (visited)
# 2. Iterate through adjacency list
# 3. if a node that is already marked as visiting is visited again, then there is a cycle


def has_cycle(graph):
    visiting = set()
    visited = set()

    for node in graph:
        if cycle_detect(graph, node, visiting, visited) == True:
            return True

def cycle_detect(graph, node, visiting, visited):

    if node in visited:
        return False

    if node in visiting:
        # has cycle
        return True

    visiting.add(node)

    # DFS
    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited) == True:
            return True

    visiting.remove(node)
    visited.add(node)


    return False

print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True
