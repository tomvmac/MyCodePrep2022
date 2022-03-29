# Problem:
#
# Oh-no! You forgot the number combination that unlocks your safe.
# Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that
# can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that
# indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).
#
# The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one
# working combination and that a digit can occur zero or one time in the answer.
#
# Write a function, safe_cracking, that takes in a list of hints as an argument and determines
# the combination that will unlock the safe. The function should return a string representing
# the combination.

# Solution:
# Combo pairs are like node to node relationships in a graph
# 1. Build graph or adjacency list from edge list
# 2. Use topical order,
#    # a. Create num_parents
# #       a. Find all parents, num_parents with count of children for each node
#      b. Iterate
#         i. Start with any node with value of 0 in num_parent
#        ii. Add to ready collection when item is value 0 in num_parent
#        iii. add to order list, mark visited
#         iv. look at immediate children, decrement by 1, because just visited parent
#      c. Terminate when ready list is empty

# Complexity:
# e = # hints
# Time: O(e)
# Space: O(e)

def safe_cracking(hints):
    graph = build_graph(hints)
    return topological_order(graph)


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
    return graph


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


print(safe_cracking([
  (3, 1),
  (4, 7),
  (5, 9),
  (4, 3),
  (7, 3),
  (3, 5),
  (9, 1),
])) # -> '473591'
