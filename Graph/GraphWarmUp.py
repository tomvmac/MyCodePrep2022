
from collections import deque

def dfs(graph, start):
    stack = [ start]
    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


def dfs_recur(graph, current):
    print(current)
    for neighbor in graph[current]:
        dfs_recur(graph, neighbor)


def bfs(graph, start):
    queue = deque([start])

    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


# Driver Code

# adjacency list
graph = {
    "a" : ["b", "c"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : []
}

dfs(graph, "a")
print("--------------")
dfs_recur(graph, "a")
print("--------------")
bfs(graph, "a")

