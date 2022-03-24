# Problem:
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst).
# The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.


# Solution:
# 1. DFS
# 2. return true if dest node is found

def has_path(graph, src, dest):
  current = src
  if current == dest:
    return True

  for neighbor in graph[current]:
    if has_path(graph, neighbor, dest) == True:
      return True

  return False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True