# Problem:
#
# Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments.
# Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B)
# means that course A must be taken before course B.
# The function should return a boolean indicating whether or not it is possible to complete all courses.

# Solution:
# 1. Convert prereqs (edge list) to an adjacency list
# 2. If there is a cycle, then you cannot complete all courses to be cyclic pre-reqs

def prereqs_possible(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    visiting = set()
    visited = set()

    for node in range(0, num_courses):
        if has_cycle(graph, node, visiting, visited):
            return False

    return True


def has_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)

    return False


def build_graph(num_courses, prereqs):
    graph = {}

    for i in range(0, num_courses):
        graph[i] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


numCourses = 5
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]

print(prereqs_possible(numCourses, prereqs) )# -> True