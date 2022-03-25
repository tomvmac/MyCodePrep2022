# Problem:
#
# Write a function, semesters_required, that takes in a number of courses (n)
# and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1.
# A single prerequisite of (A, B) means that course A must be taken before course B.
# Return the minimum number of semesters required to complete all n courses.
#
# There is no limit on how many courses you can take in a single semester,
# as long the prerequisites of a course are satisfied before taking it.
#
# Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester.
# You must take A in some semester before B.
#
# You can assume that it is possible to eventually complete all courses.

# Solution:
#
# This is pretty much similar to the longest path probelm

# 1. prereq list is like edge list, need to convert to adjacency list
# 2. it is possible to eventually take all courses, equals to graph is acyclic
# 3. Count the longest paths of nodes will be all classes
# 4. Find terminal nodes, mark as 1, because that's a minimum  one semester
# 5. DFS, for each node not visited, carry over the distance increment by one


def semesters_required(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    distance = {}
    for course in range(num_courses):
        if len(graph[course]) == 0:
            distance[course] = 1

    for course in range(num_courses):
        traverse_distance(graph, course, distance)

    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    max_distance = 0
    for neighbor in graph[node]:
        neighbor_distance = traverse_distance(graph, neighbor, distance)
        if neighbor_distance > max_distance:
            max_distance = neighbor_distance

    distance[node] = 1 + max_distance
    return distance[node]


def build_graph(num_courses, prereqs):
    graph = {}

    for course in range(num_courses):
        graph[course] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


num_courses = 7
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]

print(semesters_required(num_courses, prereqs)) # -> 5