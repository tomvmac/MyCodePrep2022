# Problem:
#
# Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph.
# The function should return a list containing the topological-order of the graph.
#
# The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.

# Solution:
# 1. Create num_parents
#    a. Find all parents, num_parents with count of children for each node
# 2. Iterate
#    a. Start with any node with value of 0 in num_parent
#    b. Add to ready collection when item is value 0 in num_parent
#    c. add to order list, mark visited
#    d. look at immediate children, decrement by 1, because just visited parent
# 3. Terminate when ready list is empty
#
# Note:
# Only generate a topological order with NO Cycle

# Time:
# n = # nodes
# e = # edges
# O(n+e)
#
# Space:
# O(n)

def topological_order(graph):
    num_parents = {}
    # Init all items in num_parents
    for node in graph:
        num_parents[node] = 0

    # Count children for each num_parent
    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    ready = [node for node in graph if num_parents[node] == 0]
    order = []
    while ready:
        node = ready.pop()
        order.append(node)
        for child in graph[node]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)

    return order


print(topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
})) # -> ['c', 'a', 'f', 'b', 'd', 'e']