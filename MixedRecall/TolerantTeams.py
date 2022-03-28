# Problem:
#
# Write a function, tolerant_teams, that takes in a list of rivalries as an argument.
# A rivalry is a pair of people who should not be placed on the same team.
# The function should return a boolean indicating whether or not it is possible to separate people into two teams,
# without rivals being on the same team. The two teams formed do not have to be the same size.

# Notes:
# - bipartite graph, it is a graph where adjacent nodes have alternating attribute values


# # Solution:
# 1. Convert list of tuples to adjacency list
# 2. Iterate through adjacency list for all components, tracking visited
# 3. For each component, DFS through nodes tracking alternating color and if not possible, return False

def tolerant_teams(rivalries):
    graph = build_graph(rivalries)

    coloring = {}
    for node in graph:
        if node not in coloring and not is_bipartite(graph, node, coloring, False):
            return False

    return True


def is_bipartite(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color
    coloring[node] = current_color

    # DFS
    for neighbor in graph[node]:
        if not is_bipartite(graph, neighbor, coloring, not current_color):
            return False

    return True

# Build adjacency list from edge for undirected graph
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

print(tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
])) # -> True